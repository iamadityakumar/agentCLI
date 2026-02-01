import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(file_path):
    working_directory = os.getcwd()
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not in the working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a valid file'

    try:
        with open(abs_file_path, 'r', encoding='utf-8') as file:
            content = file.read(MAX_CHARS)
            if len(content) >= MAX_CHARS:
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f'Exception reading file "{file_path}": {e}'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the contents of a given file as a string, constrained to the working directory.",
    parameters={
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The path to the file relative to the working directory."
            }
        },
        "required": ["file_path"]
    }
)