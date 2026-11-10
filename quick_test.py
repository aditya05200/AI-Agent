from dotenv import load_dotenv
from google import genai
import os
import time

load_dotenv()

print("1. Loading key")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("2. Client created")

start = time.time()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="hi"
    )

    print("3. Response received")
    print("Time:", round(time.time() - start, 2))
    print(response.text)

except Exception as e:
    print("ERROR:")
    print(type(e).__name__)
    print(e)