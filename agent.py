from registry import TOOLS

user_input = input("You: ").lower()

COMMANDS = {
    "list files": ("list_files", []),
    "read readme": ("read_file", ["README.md"])
}

if user_input in COMMANDS:

    tool_name, args = COMMANDS[user_input]

    result = TOOLS[tool_name](*args)

    print("\nAgent:")
    print(result)

else:
    print("Agent: I don't know how to do that yet.")