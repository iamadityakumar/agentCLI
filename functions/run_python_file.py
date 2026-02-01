import os
import subprocess
import sys
from google.genai import types


def run_python_file(file_path, args=None, timeout=30):
    working_directory = os.getcwd()
    abs_working_dir = os.path.realpath(os.path.abspath(working_directory))
    abs_file_path = os.path.realpath(os.path.abspath(os.path.join(working_directory, file_path)))

    # ensure path is inside working directory using commonpath
    try:
        common = os.path.commonpath([abs_working_dir, abs_file_path])
    except ValueError:
        return f'Error: "{file_path}" is not in the working directory'
    if common != abs_working_dir:
        return f'Error: "{file_path}" is not in the working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a valid file'

    if not abs_file_path.lower().endswith('.py'):
        return f'Error: "{file_path}" is not a Python (.py) file'

    if args is None:
        args = []
    if not isinstance(args, list) or not all(isinstance(a, str) for a in args):
        return 'Error: "args" must be an array of strings'

    cmd = [sys.executable, abs_file_path] + args

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if result.returncode != 0:
            return f'Error running file "{file_path}": exit={result.returncode}\nstderr:\n{result.stderr}'
        return result.stdout
    except subprocess.TimeoutExpired as te:
        return f'Error: execution timed out after {timeout} seconds'
    except Exception as e:
        return f'Exception running file "{file_path}": {e}'


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file using the agent's Python interpreter. Accepts optional CLI args as an array of strings.",
    parameters={
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The file to run, relative to the working directory."
            },
            "args": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Optional array of CLI arguments to pass to the script.",
                "default": []
            },
            "timeout": {
                "type": "number",
                "description": "Optional timeout in seconds for script execution.",
                "default": 30
            }
        },
        "required": ["file_path"]
    }
)