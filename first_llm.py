from dotenv import load_dotenv
from google import genai
import os

print("1. Starting script")

load_dotenv()

print("2. Loading API key")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("3. Client created")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Reply with exactly: Gemini connection successful"
)

print("4. Response received")

print(response.text)