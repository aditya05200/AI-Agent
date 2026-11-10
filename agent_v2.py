# agent_v2.py

from registry import TOOLS
from planner import choose_tool

user_input = input("You: ")

decision = choose_tool(user_input)

if decision:

    tool_name = decision["tool"]
    args = decision["args"]

    result = TOOLS[tool_name](*args)

    print("\nAgent:")
    print(result)

else:

    print("Agent: No suitable tool found")
