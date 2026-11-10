import json
import os

from dotenv import load_dotenv
from google import genai

from tool_descriptions import TOOLS_INFO

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# def choose_tool(user_input):

#     print("1. Planner started")

#     prompt = f"""
# {TOOLS_INFO}

# User Request:
# {user_input}

# Return JSON only.
# """

#     print("2. Sending request")

#     response = client.models.generate_content(
#         model="gemini-3.8-flash",
#         contents=prompt
#     )

#     print("3. Response received")
#     print(response.text)

#     return json.loads(response.text)

def choose_tool(user_input):

    prompt = f"""
{TOOLS_INFO}

User Request:
{user_input}

Return JSON only.
"""

    print("Sending planner request...")

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("Raw Response:")
    print(response.text)

    return json.loads(response.text)