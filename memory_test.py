from memory import add_message, get_messages

add_message("user", "list files")
add_message("agent", "returned file list")

print(get_messages())