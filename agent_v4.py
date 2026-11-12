from agent.planner import choose_tool
from agent.memory import add_message
from agent.executor import execute_tool

MAX_STEPS = 3

steps = 0

while steps < MAX_STEPS:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    add_message("user", user_input)

    decision = choose_tool(user_input)

    if decision:

        tool_name = decision["tool"]
        args = decision["args"]

        add_message(
            "assistant",
            f"Using tool: {tool_name}"
        )

        result = execute_tool(tool_name, args)

        add_message("tool", result)

        print("\nAgent:")
        print(result)

    else:
        print("Agent: No suitable tool found")

    steps += 1

print("\nStep limit reached or session ended.")