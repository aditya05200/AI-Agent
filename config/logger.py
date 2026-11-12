"""
Central logging configuration.

All application modules should import
the logger defined in this file.
"""

import logging
from pathlib import Path

# Ensure log directory exists
Path("logs").mkdir(
    exist_ok=True
)

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)

logging.basicConfig(
    filename="logs/agent.log",
    level=logging.INFO,
    format=LOG_FORMAT,
)

logger = logging.getLogger(
    "ai_agent"
)