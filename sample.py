import os

def main():
    print("testing if I can access the API_KEY environment variable")
    print(os.getenv("API_KEY"))

if __name__ == "__main__":
    main()
