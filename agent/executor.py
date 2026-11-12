"""
Tool execution layer.

Responsible for:
- Validating tools
- Executing tools
- Logging execution details
"""

from config.logger import logger
from tools.tool_registry import TOOLS


def execute_tool(
    tool_name: str,
    args: list
) -> str:
    """
    Execute a registered tool.

    Args:
        tool_name: Tool identifier.
        args: Arguments passed to the tool.

    Returns:
        Tool execution result.
    """
    if tool_name not in TOOLS:
        logger.warning(
            "Rejected tool execution: %s",
            tool_name
        )

        return f"Tool not allowed: {tool_name}"

    logger.info(
        "Executing tool: %s | args=%s",
        tool_name,
        args
    )

    result = TOOLS[tool_name](*args)

    logger.info(
        "Tool execution completed: %s",
        tool_name
    )

    return result