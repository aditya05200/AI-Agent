"""
Conversation memory management.
"""

from typing import Dict
from typing import List

messages: List[Dict[str, str]] = []


def add_message(
    role: str,
    content: str
) -> None:
    """
    Add a message to memory.

    Args:
        role: Message source
              (user, assistant, tool).

        content: Message content.
    """
    messages.append(
        {
            "role": role,
            "content": content,
        }
    )


def get_messages() -> List[Dict[str, str]]:
    """
    Retrieve conversation history.

    Returns:
        List of stored messages.
    """
    return messages


def clear_memory() -> None:
    """
    Clear all stored messages.
    """
    messages.clear()