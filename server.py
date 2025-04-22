import shlex
import subprocess

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Fredrik's MCP server tools")


@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"


@mcp.tool()
def count_letter_in_text(text: str, letter: str) -> int:
    """Count occurrences of a letter in a text"""
    return text.count(letter)


@mcp.tool()
async def run_git_command(command: str) -> str:
    """
    Run a git command using the `git` command.
    Example command: `git --version`.
    """
    if command.startswith("git "):
        command = command[4:]

    args = shlex.split(command)

    try:
        result = subprocess.run(
            ["git"] + args, capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}\nStdout: {e.stdout}\nStderr: {e.stderr}"


if __name__ == "__main__":
    # mcp.run()
    mcp.run(transport="stdio")
