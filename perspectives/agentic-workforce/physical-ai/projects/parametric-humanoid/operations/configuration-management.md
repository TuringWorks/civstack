# Configuration management

## Identification

Use `Lamina-<assembly>-<major>.<minor>` for released assemblies and tag every test
record with CAD revision, firmware commit, controller parameters, BOM revision and
material lot. Generated files are outputs; their generator scripts are authoritative.

## Change classes

- **A — safety/structure:** E-stop, contactor, hard stops, load path, shaft, bearing,
  tendon termination or control limits. Requires hazard review and regression tests.
- **B — interface/performance:** actuator, encoder, geometry, mass, network or power.
  Requires affected analysis and verification updates.
- **C — cosmetic/documentary:** shell contour, finish or clarification with no
  interface change. Requires inspection and link/validator pass.

## Release checklist

1. Run project, URDF and FreeCAD validators.
2. Freeze BOM and parameter files; archive generated DXFs/STEP/FCStd.
3. Record open hazards and failed or unexecuted verification rows.
4. Sign design, safety and test reviews separately.
5. Label physical parts so mixed revisions cannot enter one assembly unnoticed.

Never edit a generated DXF or STEP as the only copy of a change. Modify the source,
regenerate, and increment the revision.

