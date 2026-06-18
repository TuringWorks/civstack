/*
  Lamina parametric torso, v0.1

  Units: millimeters.
  Modes:
    "assembly" — preview the stacked torso ribs.
    "layer"    — export one selected rib as 2D DXF.
    "layout"   — arrange all ribs in a rough 2D inspection grid.

  This is a proportion and fabrication starting point, not a structural model.
  Decorative ribs must not carry actuator or joint loads.
*/

$fn = 80;

mode = "assembly";        // [assembly, layer, layout]
layer_index = 12;         // selected layer in layer mode
layer_count = 34;
body_height = 510;
material_thickness = 6.0;
layer_gap = 9.0;
ring_width = 24.0;
rod_diameter = 6.4;       // clearance for nominal M6; tune with coupon
kerf_compensation = 0.0;  // positive enlarges exterior and holes together
layout_columns = 5;
layout_pitch_x = 430;
layout_pitch_y = 330;

// The torso is built as a smooth hull through anatomical control masses.
module outer_body() {
    hull() {
        translate([0, 0, 35])  scale([1.00, 0.72, 0.48]) sphere(r = 125);
        translate([0, 0, 145]) scale([0.82, 0.58, 0.62]) sphere(r = 135);
        translate([0, 0, 300]) scale([1.12, 0.66, 0.72]) sphere(r = 155);
        translate([0, 0, 445]) scale([0.46, 0.42, 0.46]) sphere(r = 105);
    }

    // Shoulder masses keep the upper silhouette intentionally sculptural.
    hull() {
        translate([-165, 0, 345]) scale([0.75, 0.62, 0.55]) sphere(r = 78);
        translate([ 165, 0, 345]) scale([0.75, 0.62, 0.55]) sphere(r = 78);
        translate([0, 0, 325]) scale([1.05, 0.64, 0.65]) sphere(r = 145);
    }
}

function layer_z(i) = 5 + i * (body_height - 10) / (layer_count - 1);

module raw_profile(z) {
    projection(cut = true)
        translate([0, 0, -z])
            outer_body();
}

module registration_holes() {
    for (x = [-72, 72], y = [-38, 38])
        translate([x, y]) circle(d = rod_diameter);
}

module rib_2d(i) {
    z = layer_z(i);
    difference() {
        offset(delta = kerf_compensation)
            raw_profile(z);
        offset(delta = -ring_width)
            raw_profile(z);
        // Registration holes are kept near the structural spine.
        // Verify that each hole remains inside the rib at extreme layers.
        offset(delta = kerf_compensation)
            registration_holes();
    }
}

module assembly() {
    color([0.68, 0.42, 0.20])
        for (i = [0 : layer_count - 1])
            translate([0, 0, i * (material_thickness + layer_gap)])
                linear_extrude(height = material_thickness)
                    rib_2d(i);
}

module layout() {
    for (i = [0 : layer_count - 1]) {
        col = i % layout_columns;
        row = floor(i / layout_columns);
        translate([col * layout_pitch_x, -row * layout_pitch_y])
            rib_2d(i);
    }
}

if (mode == "assembly") {
    assembly();
} else if (mode == "layer") {
    rib_2d(layer_index);
} else if (mode == "layout") {
    layout();
} else {
    assert(false, str("Unknown mode: ", mode));
}

