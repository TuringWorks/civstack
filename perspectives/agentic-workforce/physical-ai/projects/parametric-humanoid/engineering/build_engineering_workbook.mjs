import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const here = path.dirname(new URL(import.meta.url).pathname);
const project = path.dirname(here);
const out = path.join(here, "Lamina-Engineering-Baseline-v06.xlsx");
const previewDir = path.join(here, "workbook-previews");
await fs.mkdir(previewDir, { recursive: true });

const sources = [
  ["Mass Budget", path.join(here, "mass-budget.csv")],
  ["Joint Loads", path.join(here, "joint-load-budget.csv")],
  ["Power Budget", path.join(here, "power-budget.csv")],
  ["Cost Budget", path.join(here, "cost-budget.csv")],
  ["Hazards", path.join(project, "safety", "hazard-register.csv")],
  ["Verification", path.join(project, "verification", "verification-matrix.csv")],
];

const wb = Workbook.create();
const dashboard = wb.worksheets.add("Dashboard");

for (const [sheetName, filePath] of sources) {
  const csvText = await fs.readFile(filePath, "utf8");
  const imported = await Workbook.fromCSV(csvText, { sheetName });
  const srcSheet = imported.worksheets.getItem(sheetName);
  const values = srcSheet.getUsedRange().values;
  const sheet = wb.worksheets.add(sheetName);
  sheet.getRangeByIndexes(0, 0, values.length, values[0].length).values = values;
}

const gates = wb.worksheets.add("Hardware Gates");
gates.getRange("A1:E12").values = [
  ["Gate", "Evidence required", "Decision unlocked", "Status", "Owner"],
  ["G1", "Plywood/kerf/fit coupon", "Release corrected J1 cutting files", "OPEN", "Structures"],
  ["G2", "Five termination specimens per method", "Select tendon termination and derating", "OPEN", "Transmission"],
  ["G3", "J1 proof, thermal and 10k cycles", "Retain/reject M-class architecture", "OPEN", "Mechanical"],
  ["G4", "Actuator torque-speed-efficiency map", "Freeze M actuator/reduction", "OPEN", "Actuation"],
  ["G5", "J2 H-class proof and endurance", "Freeze load-bearing leg architecture", "OPEN", "Mechanical"],
  ["G6", "Foot/ankle force and slip tests", "Freeze foot and force-sensor layout", "OPEN", "Mobility"],
  ["G7", "Object/rung retention on power loss", "Freeze hand and hook", "OPEN", "Manipulation"],
  ["G8", "Battery/power bench tests", "Freeze battery and distribution", "OPEN", "Electrical"],
  ["G9", "Suspended squat/step fault tests", "Authorize guarded stepping campaign", "OPEN", "Controls"],
  ["G10", "Repeatable stair tests", "Authorize ladder fixture progression", "OPEN", "Mobility"],
  ["G11", "Ladder contact/power-loss tests", "Decide whether ladder stays in scope", "OPEN", "Safety"],
];

const navy = "#17334A";
const blue = "#557994";
const wood = "#C99C60";
const pale = "#F6F0E5";
const red = "#B54035";
const green = "#3F7D55";
const amber = "#C77A28";

dashboard.showGridLines = false;
dashboard.getRange("A1:L2").merge();
dashboard.getRange("A1").values = [["LAMINA ENGINEERING BASELINE v0.6"]];
dashboard.getRange("A1:L2").format = {
  fill: navy,
  font: { bold: true, color: "#FFFFFF", size: 20 },
  verticalAlignment: "center",
  horizontalAlignment: "center",
};
dashboard.getRange("A3:L3").merge();
dashboard.getRange("A3").values = [["Pre-fabrication status: architecture complete; physical gates remain open"]];
dashboard.getRange("A3:L3").format = { fill: "#DDE7ED", font: { italic: true, color: navy }, horizontalAlignment: "center" };

dashboard.getRange("A5:L5").values = [["Controlled axes", "", "Mass estimate", "", "Mass review limit", "", "Average power", "", "Peak envelope", "", "Planning cost", ""]];
dashboard.getRange("A6:L7").values = [[31, "axes", 34.4, "kg", 35, "kg", 695, "W", 4230, "W", 12600, "USD"], [null,null,null,null,null,null,null,null,null,null,null,null]];
for (const col of ["A","C","E","G","I","K"]) {
  dashboard.getRange(`${col}5:${col}7`).format = { fill: pale, font: { bold: true, color: navy }, horizontalAlignment: "center", borders: { preset: "outside", style: "medium", color: wood } };
}
dashboard.getRange("A6:K6").format.font = { bold: true, color: red, size: 18 };
dashboard.getRange("B6:L6").format.font = { color: "#5B6B75" };

dashboard.getRange("A9:D14").values = [
  ["Readiness KPI", "Value", "Target", "Status"],
  ["Mass", 34.4, 32, "REDUCE"],
  ["Planning cost", 12600, 12000, "REDUCE"],
  ["URDF joint count", 31, 31, "PASS"],
  ["Open hardware gates", 11, 0, "BLOCKED"],
  ["Residual high risks (≥8)", 1, 0, "MITIGATE"],
];
dashboard.getRange("A9:D9").format = { fill: blue, font: { bold: true, color: "#FFFFFF" } };
dashboard.getRange("A10:D14").format.borders = { preset: "all", style: "thin", color: "#D2D8DC" };
dashboard.getRange("D10:D14").conditionalFormats.add("containsText", { text: "PASS", format: { fill: "#D9EAD3", font: { color: green, bold: true } } });
dashboard.getRange("D10:D14").conditionalFormats.add("containsText", { text: "REDUCE", format: { fill: "#FCE5CD", font: { color: amber, bold: true } } });
dashboard.getRange("D10:D14").conditionalFormats.add("containsText", { text: "BLOCKED", format: { fill: "#F4CCCC", font: { color: red, bold: true } } });
dashboard.getRange("D10:D14").conditionalFormats.add("containsText", { text: "MITIGATE", format: { fill: "#F4CCCC", font: { color: red, bold: true } } });

dashboard.getRange("F9:I14").values = [
  ["Build phase", "Purpose", "Cumulative spend", "Gate"],
  ["A", "Transmission truth", 1500, "G1–G4"],
  ["B", "Load-bearing truth", 5000, "G5–G7"],
  ["C", "Suspended lower body", 9000, "G8–G10"],
  ["D", "Full upper body", 12600, "Integration"],
  ["E", "Ladder decision", 12600, "G11"],
];
dashboard.getRange("F9:I9").format = { fill: blue, font: { bold: true, color: "#FFFFFF" } };
dashboard.getRange("F10:I14").format.borders = { preset: "all", style: "thin", color: "#D2D8DC" };
dashboard.getRange("H10:H14").format.numberFormat = "$#,##0";

dashboard.getRange("A17:B22").values = [
  ["Subsystem", "Target kg"],
  ["Structures", 13.7],
  ["Actuation", 9.0],
  ["Battery", 4.0],
  ["Electronics", 1.5],
  ["Hardware/guards", 3.0],
];
const massChart = dashboard.charts.add("bar", dashboard.getRange("A17:B22"));
massChart.title = "Mass concentration";
massChart.hasLegend = false;
massChart.setPosition("D16", "H29");

dashboard.getRange("J17:K22").values = [
  ["Build phase", "USD"], ["A",1500], ["B",5000], ["C",9000], ["D",12600], ["Target",12000]
];
const costChart = dashboard.charts.add("bar", dashboard.getRange("J17:K22"));
costChart.title = "Phased cost vs target";
costChart.hasLegend = false;
costChart.yAxis = { numberFormatCode: "$#,##0" };
costChart.setPosition("I16", "L29");

dashboard.freezePanes.freezeRows(3);
for (const width of [["A:A",22],["B:B",11],["C:C",17],["D:D",13],["E:E",17],["F:F",14],["G:G",15],["H:H",14],["I:I",14],["J:J",14],["K:K",15],["L:L",10]]) {
  dashboard.getRange(width[0]).format.columnWidth = width[1];
}

for (const [sheetName] of sources) {
  const sheet = wb.worksheets.getItem(sheetName);
  sheet.showGridLines = false;
  const used = sheet.getUsedRange();
  const rows = used.values.length;
  const cols = used.values[0].length;
  const header = sheet.getRangeByIndexes(0, 0, 1, cols);
  header.format = { fill: navy, font: { bold: true, color: "#FFFFFF" }, wrapText: true };
  sheet.freezePanes.freezeRows(1);
  used.format.borders = { preset: "all", style: "thin", color: "#D9DEE2" };
  used.format.wrapText = true;
  for (let c = 0; c < cols; c++) sheet.getRangeByIndexes(0, c, rows, 1).format.columnWidth = c === 0 ? 22 : Math.min(34, c > 3 ? 18 : 24);
}

const hazards = wb.worksheets.getItem("Hazards");
hazards.getRange("H2:H200").conditionalFormats.add("colorScale", { colors: ["#D9EAD3", "#FCE5CD", "#F4CCCC"], thresholds: ["min", "50%", "max"] });
hazards.getRange("M2:M200").conditionalFormats.add("colorScale", { colors: ["#D9EAD3", "#FCE5CD", "#F4CCCC"], thresholds: ["min", "50%", "max"] });

const verification = wb.worksheets.getItem("Verification");
verification.getRange("F2:F200").conditionalFormats.add("containsText", { text: "passed", format: { fill: "#D9EAD3", font: { color: green } } });
verification.getRange("F2:F200").conditionalFormats.add("containsText", { text: "blocked", format: { fill: "#F4CCCC", font: { color: red } } });

gates.showGridLines = false;
gates.getRange("A1:E12").format.borders = { preset: "all", style: "thin", color: "#D9DEE2" };
gates.getRange("A1:E1").format = { fill: navy, font: { bold: true, color: "#FFFFFF" } };
gates.getRange("D2:D12").conditionalFormats.add("containsText", { text: "OPEN", format: { fill: "#F4CCCC", font: { color: red, bold: true } } });
gates.freezePanes.freezeRows(1);
gates.getRange("A:A").format.columnWidth = 9;
gates.getRange("B:B").format.columnWidth = 35;
gates.getRange("C:C").format.columnWidth = 35;
gates.getRange("D:E").format.columnWidth = 16;
gates.getRange("A1:E12").format.wrapText = true;

for (const name of ["Dashboard", ...sources.map(x => x[0]), "Hardware Gates"]) {
  const sheet = wb.worksheets.getItem(name);
  const blob = await wb.render({ sheetName: name, autoCrop: "all", scale: name === "Dashboard" ? 1.2 : 0.8, format: "png" });
  await fs.writeFile(path.join(previewDir, `${name.replaceAll(" ", "-")}.png`), new Uint8Array(await blob.arrayBuffer()));
}

const inspect = await wb.inspect({ kind: "table", range: "Dashboard!A1:L22", include: "values,formulas", tableMaxRows: 22, tableMaxCols: 12 });
await fs.writeFile(path.join(previewDir, "dashboard-inspect.ndjson"), inspect.ndjson, "utf8");
const errors = await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "formula error scan" });
await fs.writeFile(path.join(previewDir, "formula-errors.ndjson"), errors.ndjson, "utf8");

const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(out);
console.log(out);
