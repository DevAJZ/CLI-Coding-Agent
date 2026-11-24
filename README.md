# CLI Coding Agent

A Python command-line agent that can inspect a codebase, edit a file, and run its tests in response to a plain-English request. I built it to learn how a language model goes from suggesting a change to making one and checking the result.

## The agent can fix your coding bugs
During development, the agent can fix your coding bugs by telling it which bugs you got, and it will scan the whole working directory searching for bugs and fixes them.


## Four handwritten Python tools

I wrote each tool and its JSON schema by hand. The schema tells the model which arguments it can request. The Python function performs the operation.

| Tool | Implementation |
| --- | --- |
| [`get_files_info`](functions/get_files_info.py) | Lists directory entries with their sizes and identifies subdirectories so the agent can decide what to open next. |
| [`get_file_content`](functions/get_file_content.py) | Reads a text file and returns up to 10,000 characters of its contents to the model. |
| [`write_file`](functions/write_file.py) | Creates missing parent directories and writes the supplied text, replacing the contents of an existing file. |
| [`run_python_file`](functions/run_python_file.py) | Runs a script with the current Python interpreter, captures standard output and error, and applies a 30-second timeout. |

## How the agent loop works

The [CLI](main.py) sends the prompt, conversation history, and tool schemas to OpenRouter through the OpenAI Python SDK. When the model requests a tool, the [dispatcher](call_function.py) looks up its name in a map of four Python functions, supplies the working directory, and executes the call.

Each result goes back into the conversation with the ID of the request that produced it. That lets the model read a directory listing before choosing a file, or inspect test output before deciding whether to edit again. The CLI prints the requested tool names as it works. It stops on a final answer or after 20 model calls.

## Run the agent

From the repository root, use Python 3.14 or later and install the locked dependencies with `uv sync`. Create a local `.env` file with your OpenRouter API key:

```dotenv
OPENROUTER_API_KEY=your-full-openrouter-key
```

Start with a question you can check against the source:

```sh
uv run main.py "Explain how the calculator renders the result to the console."
```

The agent currently uses `calculator/` as its working directory as an example but you can specify the working directory you like, the agent will scan your specified working directory and have access to the files inside it. Scripts run with your local user permissions, and tool output is sent to OpenRouter. Use a trusted project with files you are comfortable sharing with the model.
