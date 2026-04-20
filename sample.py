import os

from langchain_openai import AzureChatOpenAI
import dotenv
dotenv.load_dotenv()

def main():
    

    llm = AzureChatOpenAI(model="gpt-4o-mini", temperature=0)

    print(llm.invoke("What is the capital of France?").content)


if __name__ == "__main__":
    main()
