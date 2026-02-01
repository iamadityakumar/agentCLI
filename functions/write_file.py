import os
from google.genai import types


def write_file(file_path, content):
    working_directory = os.getcwd()
    abs_working_dir = os.path.realpath(os.path.abspath(working_directory))
    abs_file_path = os.path.realpath(os.path.abspath(os.path.join(working_directory, file_path)))

    # Ensure the target path is inside the working directory
    try:
        common = os.path.commonpath([abs_working_dir, abs_file_path])
    except ValueError:
        return f'Error: "{file_path}" is not in the working directory'
    if common != abs_working_dir:
        return f'Error: "{file_path}" is not in the working directory'

    if os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory'

    if not isinstance(content, str):
        return 'Error: "content" must be a string'

    parent_dir = os.path.dirname(abs_file_path)
    if parent_dir and not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir, exist_ok=True)
        except Exception as e:
            return f'Could not create parent directory "{parent_dir}": {e}'

    try:
        with open(abs_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Success: Written to "{file_path}"'
    except Exception as e:
        return f'Failed writing to "{file_path}": {e}'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file relative to the working directory. Creates parent directories if needed.",
    parameters={
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Target file path relative to the working directory."
            },
            "content": {
                "type": "string",
                "description": "Content to write into the file."
            }
        },
        "required": ["file_path", "content"]
    }
)