"""
Tool registry.

Maintains the list of tools available to the agent.
"""

from typing import Callable

from tools.file_tools import (
    list_files,
    read_file,
)

TOOLS: dict[str, Callable] = {
    "list_files": list_files,
    "read_file": read_file,
}