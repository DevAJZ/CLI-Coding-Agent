# Python CLI Coding Agent

A Python coding agent built for a Boot.dev project. Give it a task in plain English and it uses OpenRouter to choose tools for listing files, reading code, writing changes, and running Python scripts in a sample calculator project.

## Four handwritten tools

I wrote all four tools by hand in Python, along with the schemas that tell the model how to request them.

| Tool | What it does |
| --- | --- |
| [`get_files_info`](functions/get_files_info.py) | Lists entries in a directory, including each entry's size and whether it is a directory. |
| [`get_file_content`](functions/get_file_content.py) | Reads a text file and returns up to 10,000 characters of its contents. |
| [`write_file`](functions/write_file.py) | Writes text to a file, creates missing parent directories, and replaces the contents of an existing file. |
| [`run_python_file`](functions/run_python_file.py) | Runs a Python script and captures its standard output and standard error. |

## How it works

The agent sends your prompt and four tool descriptions to OpenRouter using the OpenAI Python SDK. When the model requests a tool, the program calls the corresponding Python function and sends its result back to the model. The loop ends when the model gives a final answer or reaches 20 model calls.

The calculator is the agent's default working directory. The script runner accepts a Python file path and has a 30-second timeout. It runs with the current user's permissions, so use it with trusted code.

## Run locally

Use Python 3.14 or later and uv. From the repository root, run `uv sync`, then create a local `.env` file containing:

```dotenv
OPENROUTER_API_KEY=your-full-openrouter-key
```

Ask the agent a question:

```sh
uv run main.py "Explain how the calculator renders the result to the console."
```

To run the calculator's unit tests directly:

```sh
uv run calculator/tests.py
```
