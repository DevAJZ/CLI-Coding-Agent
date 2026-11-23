import os
import argparse
import sys
import json
from dotenv import load_dotenv
from openai import OpenAI
from functions.get_files_info import get_files_info
from prompts import system_prompt
from call_function import call_function, available_functions

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key or any(marker in api_key for marker in ("...", "…", "*")):
    raise SystemExit("Set OPENROUTER_API_KEY in .env to the full key copied from OpenRouter.")

client = OpenAI(
 base_url="https://openrouter.ai/api/v1",
 api_key=api_key,)

prompt = sys.argv[1]

messages = [
    {
        "role": "system", "content": system_prompt
    },
    {
     "role": "user", "content": prompt
    },
]  
for x in range(20):
    response = client.chat.completions.create(
            model="openrouter/free", messages=messages, tools=available_functions,
        )

    message = response.choices[0].message
    messages.append(message)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            tool_message = call_function(tool_call)
            messages.append(tool_message)
    else:
        # final agent text message
        print(message.content)
        break
else:
    sys.exit("The agent reached 20 iterations without a final response.")