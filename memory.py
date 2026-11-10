messages = []

def add_message(role, content):
    messages.append({
        "role": role,
        "content": content
    })

def get_messages():
    return messages