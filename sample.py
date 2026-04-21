import os

from langchain_openai import AzureChatOpenAI
import dotenv
dotenv.load_dotenv()

REQUIRED_ENV_VARS = (
    "AZURE_OPENAI_API_KEY",
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_OPENAI_DEPLOYMENT",
    "OPENAI_API_VERSION",
)


def main():
    missing = [name for name in REQUIRED_ENV_VARS if not os.getenv(name)]
    if missing:
        print(
            "Skipping Azure OpenAI call: missing required environment variables: "
            + ", ".join(missing)
        )
        return

    llm = AzureChatOpenAI(
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        temperature=0,
    )

    try:
        print(llm.invoke("What is the capital of France?").content)
    except Exception as exc:
        print(f"Skipping Azure OpenAI call due to connection/configuration error: {exc}")


if __name__ == "__main__":
    main()
