# AgentCLI - AI Coding Agent

AgentCLI is a lightweight, terminal-based AI coding assistant powered by **Google Gemini 2.0 Flash**. It can help you explore your codebase, read files, write code, and even execute Python scripts directly from your command line.

## Features

- **File System Awareness**: Can list files and directories to understand project structure.
- **Code Manipulation**: Read contents of existing files and write new files or update existing ones.
- **Script Execution**: Run Python scripts with optional arguments to test code or automate tasks.
- **Powered by Gemini 2.0 Flash**: Fast and intelligent responses using the latest Google GenAI SDK.
- **Functional Calling**: Seamlessly integrates AI reasoning with local file system tools.

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)
- A Google Gemini API Key

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/iamadityakumar/agentCLI.git
    cd agentCLI
    ```

2.  **Set up environment variables**:
    Create a `.env` file in the root directory and add your Gemini API key:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

3.  **Install dependencies**:
    If you have `uv` installed:
    ```bash
    uv sync
    ```
    Alternatively, using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the agent by providing a prompt as a command-line argument:

```bash
python main.py "your prompt here"
```

### Options
- `--verbose`: Display detailed token usage and the prompt sent to the model.

### Examples
- **Check files**: `python main.py "list the files in the current directory"`
- **Read code**: `python main.py "show me the content of main.py"`
- **Write code**: `python main.py "create a new python file called hello.py that prints hello world"`
- **Execute code**: `python main.py "run the hello.py file"`

## Project Structure

- `main.py`: The entry point for the CLI agent.
- `functions/`: Contains the tool schemas and implementation for the AI's capabilities (reading, writing, listing, running).
- `calculator/`: An example package/project used for testing.
- `pyproject.toml`: Project metadata and dependencies.

## License

[MIT](LICENSE) (or specify your license)
