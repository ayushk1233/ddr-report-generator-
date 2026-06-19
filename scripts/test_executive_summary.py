from app.services.llm.executive_summary_generator import (
    ExecutiveSummaryGenerator
)


def main():

    narratives = [
        "Hall dampness caused by concealed plumbing leakage.",
        "Bedroom moisture ingress observed.",
        "Kitchen thermal anomaly detected.",
    ]

    generator = (
        ExecutiveSummaryGenerator()
    )

    summary = generator.generate(
        narratives
    )

    print(summary)


if __name__ == "__main__":
    main()