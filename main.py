import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file





load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents of a file
- Write or update files
- Execute Python scripts with optional arguments

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""




if len(sys.argv) <2:
    print("A prompt is required as an argument")
    sys.exit(1)
prompt = sys.argv[1]
print("Args", sys.argv)

verbose_flag = False
if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
    verbose_flag = True





available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

config=types.GenerateContentConfig(
    tools=[available_functions], 
    system_instruction=system_prompt
)

chat = client.chats.create(
    model="gemini-2.0-flash-001",
    history=[],
    config=config

)



response = chat.send_message(prompt)


if response is None or response.usage_metadata is None:
    print("No response or usage metadata received.")
    exit(1)



if verbose_flag:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    
if response.function_calls:
    for function_call_part in response.function_calls:
        print(
            f"Calling function: {function_call_part.name}({function_call_part.args})"
        )
else:
    print(response.text)
