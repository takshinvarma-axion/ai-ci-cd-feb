import os
from langchain_openai import AzureChatOpenAI
import dotenv
dotenv.load_dotenv()


def main():
    llm = AzureChatOpenAI(
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        temperature=0,
    )

    try:
        print(llm.invoke("Give me a funny joke about a programmer").content)
    except Exception as exc:
        print(f"Skipping Azure OpenAI call due to connection/configuration error: {exc}")


if __name__ == "__main__":
    main()
