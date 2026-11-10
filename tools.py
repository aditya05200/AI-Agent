import os

def list_files():
    files = os.listdir(".")
    return "\n".join(files)

def read_file(filename):

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        return f"File not found: {filename}"