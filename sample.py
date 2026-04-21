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
