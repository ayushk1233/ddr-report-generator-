import json
from app.services.pipeline.ddr_pipeline import DDRPipeline

pipeline = DDRPipeline()
report = pipeline.run(inspection_pdf="Sample Report.pdf", thermal_pdf="Thermal Images.pdf")

# report is a Pydantic model DDRReport
bundles = [b.model_dump() for b in report.evidence_bundles]
output = {"evidence_bundles": bundles}

with open("evidence_bundles_output.json", "w") as f:
    json.dump(output, f, indent=2)

print("Dumped evidence bundles to evidence_bundles_output.json")
