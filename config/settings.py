"""
Application configuration.

Central location for:
- Environment variables
- Model configuration
- Runtime settings
"""

import os

from dotenv import load_dotenv

load_dotenv()

MODEL_NAME: str = "gemini-3.5-flash-lite"

MAX_STEPS: int = 5

GEMINI_API_KEY: str | None = os.getenv(
    "GEMINI_API_KEY"
)

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not configured."
    )