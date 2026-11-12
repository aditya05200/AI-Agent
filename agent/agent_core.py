"""
Core agent orchestration layer.

Responsibilities:
- Receive user requests
- Invoke planner
- Invoke executor
- Return structured results
"""

import time
from typing import Any

from agent.executor import execute_tool
from agent.planner import choose_tool
from config.logger import logger


def run_agent(user_input: str) -> dict[str, Any]:
    """
    Execute the complete agent workflow.

    Args:
        user_input: User request.

    Returns:
        Structured response containing:
        - selected tool
        - tool arguments
        - result
        - execution time
        - status
    """
    logger.info(
        "Received user request: %s",
        user_input
    )

    start_time = time.time()

    decision = choose_tool(user_input)

    if not decision:
        logger.warning(
            "No planner decision generated"
        )

        return {
            "status": "FAILED",
            "reason": "No suitable tool found",
        }

    tool_name = decision["tool"]
    args = decision["args"]

    logger.info(
        "Planner selected tool: %s | args=%s",
        tool_name,
        args
    )

    result = execute_tool(
        tool_name,
        args
    )

    execution_time = round(
        time.time() - start_time,
        2
    )

    logger.info(
        "Execution completed in %s seconds",
        execution_time
    )

    return {
        "status": "SUCCESS",
        "tool": tool_name,
        "args": args,
        "execution_time": execution_time,
        "result": result,
    }