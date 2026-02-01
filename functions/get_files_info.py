import os
from google.genai import types

def get_files_info(directory="."):
    working_directory = os.getcwd()
    # resolve real paths to handle symlinks and compare using commonpath
    abs_working_dir = os.path.realpath(os.path.abspath(working_directory))
    abs_directory = os.path.realpath(os.path.abspath(os.path.join(working_directory, directory)))
    try:
        common = os.path.commonpath([abs_working_dir, abs_directory])
    except ValueError:
        return f'Error: "{directory}" is not in the working directory'
    if common != abs_working_dir:
        return f'Error: "{directory}" is not in the working directory'
    if not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'
    final_response = ""
    try:
        contents = sorted(os.listdir(abs_directory))
    except Exception as e:
        return f'Error listing directory "{directory}": {e}'
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_response += f" - {content} : file_size = {size} bytes, is_dir={is_dir}\n"
    return final_response

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters={
        "type": "object",
        "properties": {
            "directory": {
                "type": "string",
                "description": "The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                "default": "."
            }
        },
        "required": []
    }
)