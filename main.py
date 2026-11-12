"""
FastAPI entry point for AI Automation Agent.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from agent.agent_core import run_agent

app = FastAPI(
    title="AI Automation Agent",
    description=(
        "Gemini-powered tool-calling agent "
        "with FastAPI integration."
    ),
    version="1.0.0",
)


class ChatRequest(BaseModel):
    """
    Chat request payload.
    """

    message: str


@app.get("/")
def home() -> dict:
    """
    Root endpoint.

    Returns:
        Application status.
    """
    return {
        "message": (
            "AI Automation Agent "
            "is running"
        )
    }


@app.get("/health")
def health() -> dict:
    """
    Health check endpoint.

    Returns:
        Service health status.
    """
    return {
        "status": "UP"
    }


@app.post("/chat")
def chat(
    request: ChatRequest
) -> dict:
    """
    Execute the agent workflow.

    Args:
        request: Incoming chat request.

    Returns:
        Structured agent response.
    """
    return run_agent(
        request.message
    )