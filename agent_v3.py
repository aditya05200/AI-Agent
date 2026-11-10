from registry import TOOLS
from planner import choose_tool
from memory import add_message, get_messages

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    add_message("user", user_input)

    decision = choose_tool(user_input)

    if decision:

        tool_name = decision["tool"]
        args = decision["args"]

        result = TOOLS[tool_name](*args)

        add_message("tool", result)

        print("\nAgent:")
        print(result)

    else:
        print("Agent: No suitable tool found")

    print("\nMemory:")
    print(get_messages())