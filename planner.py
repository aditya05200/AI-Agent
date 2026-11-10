def choose_tool(user_input):

    user_input = user_input.lower().strip()

    if "file" in user_input:
        return {
            "tool": "list_files",
            "args": []
        }

    if "read " in user_input:

        parts = user_input.split()

        filename = parts[-1]

        return {
            "tool": "read_file",
            "args": [filename]
        }

    return None