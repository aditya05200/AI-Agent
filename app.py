"""
Streamlit UI for AI Automation Agent.
"""

import streamlit as st

from agent.agent_core import run_agent

st.set_page_config(
    page_title="AI Automation Agent",
    layout="wide"
)

st.title("🤖 AI Automation Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )

prompt = st.chat_input(
    "Enter your request..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = run_agent(prompt)

    with st.chat_message("assistant"):

        st.subheader(
            "Planner Decision"
        )

        st.json(
            {
                "tool": response["tool"],
                "args": response["args"],
            }
        )

        st.subheader(
            "Execution Details"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Status",
                response["status"]
            )

        with col2:
            st.metric(
                "Execution Time",
                f"{response['execution_time']}s"
            )

        st.subheader(
            "Tool Result"
        )

        st.code(
            response["result"]
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": (
                f"Tool: {response['tool']}\n\n"
                f"Result:\n{response['result']}"
            ),
        }
    )