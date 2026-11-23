import os

def write_file(working_directory, file_path, content):
    abs_workingdirectory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_workingdirectory, file_path))
    if not abs_file_path.startswith(abs_workingdirectory):
        return f'Error: "{file_path}" is not in the working directory'
    
    parent_dir = os.path.dirname(abs_file_path)
    try:
        os.makedirs(parent_dir, exist_ok=True)
    except OSError as e:
        return f"Couldn't create parent directory: {parent_dir} = {e}"

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to {file_path} ({len(content)}) characters'
    except Exception as e:
        return f"Couldn't write to {file_path}, {e}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": (
            "Write text to a file inside the project's working directory. "
            "Creates the file and any missing parent directories. If the file "
            "already exists, replaces its entire contents."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": (
                        "Path to the file, relative to the working directory. "
                        "For example, 'notes.txt' or 'logs/today.txt'."
                    ),
                },
                "content": {
                    "type": "string",
                    "description": (
                        "The complete text the file should contain after writing. "
                        "An empty string leaves the file empty."
                    ),
                },
            },
            "required": ["file_path", "content"],
            "additionalProperties": False,
        },
    },
}