from app.services.llm.openrouter_client import (
    OpenRouterClient
)


def main():

    client = OpenRouterClient()

    response = client.generate(
        "Say hello in one sentence."
    )

    print(response)


if __name__ == "__main__":
    main()