import os
import subprocess
import sys

def run_python_file(working_directory: str, file_path: str):
    abs_workingdirectory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_workingdirectory, file_path))
    if not abs_file_path.startswith(abs_workingdirectory):
        return f'Error: "{file_path}" is not in the working directory'
    if not os.path.isfile(file_path):
        return f'Error: {file_path} is not a file'
    if not file_path.endswith(".py"):
        return f'Error: {file_path} is not a python file'
    try:
        output = subprocess.run(
            [sys.executable, file_path],
            cwd=abs_workingdirectory,
            timeout=30,
            capture_output=True,
            text=True,
        )

        final_string = f"STDOUT: {output.stdout}, STDERR: {output.stderr}"
        if output.returncode != 0:
            final_string += f"Process exited with code {output.returncode}"
        if output.stdout == "" and output.stderr == "":
            final_string = "No output produced.\n"
        return final_string
    except Exception as e:
        return f'Error executing Python file: {e}'

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": (
            "Run an existing Python script with the project's working directory "
            "as its current directory. Use this to run a script or its tests "
            "and inspect the output. The script runs without command-line "
            "arguments and has a 30-second timeout."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": (
                        "Path to an existing .py file, relative to the working "
                        "directory. For example, use 'main.py' to run the app "
                        "or 'tests.py' to run its tests."
                    ),
                },
            },
            "required": ["file_path"],
            "additionalProperties": False,
        },
    },
}