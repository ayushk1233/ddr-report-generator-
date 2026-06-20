from app.services.llm.ddr_intelligence_generator import (
    DDRIntelligenceGenerator
)


def main():

    findings = [
        {
            "area": "Hall",
            "issue": "Skirting Dampness",
            "root_cause":
            "Concealed plumbing leakage",
            "severity": "HIGH",
            "recommendation":
            "Inspect plumbing"
        },
        {
            "area": "Kitchen",
            "issue": "Moisture Ingress",
            "root_cause":
            "External wall penetration",
            "severity": "MEDIUM",
            "recommendation":
            "Repair waterproofing"
        }
    ]

    result = (
        DDRIntelligenceGenerator()
        .generate(findings)
    )

    print("\nSUMMARY:\n")
    print(result.executive_summary)

    print("\nNARRATIVES:\n")

    for narrative in result.area_narratives:
        print("-" * 50)
        print(narrative)


if __name__ == "__main__":
    main()
