from app.services.llm.gemini_client import GeminiClient


def main():
    client = GeminiClient()

    response = client.generate(
        "Say hello in one sentence."
    )

    print("\nGemini Response:\n")
    print(response)


if __name__ == "__main__":
    main()