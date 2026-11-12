"""
Gemini-based planner.

Responsible for:
- Understanding user requests
- Selecting the appropriate tool
- Returning structured tool decisions
"""

import json

from google import genai

from config.logger import logger
from config.settings import GEMINI_API_KEY
from config.settings import MODEL_NAME
from tools.tool_descriptions import TOOLS_INFO

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def choose_tool(user_input: str) -> dict:
    """
    Select the appropriate tool using Gemini.

    Args:
        user_input: Natural language user request.

    Returns:
        Tool decision dictionary.
    """
    prompt = f"""
{TOOLS_INFO}

User Request:
{user_input}

IMPORTANT:
Return ONLY valid JSON.
Do not use markdown.
Do not add explanations.

Example:
{{
    "tool": "list_files",
    "args": []
}}
"""

    logger.info(
        "Sending planner request"
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    raw_response = response.text.strip()

    logger.info(
        "Planner raw response: %s",
        raw_response
    )

    try:
        clean_text = (
            raw_response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        decision = json.loads(clean_text)

        logger.info(
            "Planner decision: %s",
            decision
        )

        return decision

    except json.JSONDecodeError as error:

        logger.error(
            "Planner JSON parsing failed: %s",
            error
        )

        return {
            "tool": None,
            "args": []
        }