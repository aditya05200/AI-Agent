from registry import TOOLS

def execute_tool(tool_name, args):

    if tool_name not in TOOLS:
        return "Tool not allowed"

    return TOOLS[tool_name](*args)