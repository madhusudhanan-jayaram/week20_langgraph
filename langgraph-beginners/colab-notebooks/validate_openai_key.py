import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Check if OPENAI_API_KEY is set
if not os.getenv("OPENAI_API_KEY"):
    print("OPENAI_API_KEY not found in environment variables.")
    exit(1)

# Create ChatOpenAI instance
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Make a simple LLM call to validate the key
try:
    response = llm.invoke("Hello, can you respond with a simple greeting?")
    print("API Key is valid!")
    print("Response:", response.content)
except Exception as e:
    print("API Key validation failed:", str(e))
