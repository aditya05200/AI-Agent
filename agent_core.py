from gemini_planner import choose_tool
from executor import execute_tool

def run_agent(user_input):

    decision = choose_tool(user_input)

    if not decision:
        return "No suitable tool found"

    tool_name = decision["tool"]
    args = decision["args"]

    result = execute_tool(tool_name, args)

    return result