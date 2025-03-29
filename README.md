# mcp-tools

## Quickstart

```sh
cd mcp-tools

# install uv (if not already available), macOS example
brew install uv

# install dependencies
uv sync
```

Add to the MCP server JSON settings (path depends on which app you're using):

```json
{
  "mcpServers": {
    "github.com/fredrikaverpil/mcp-tools": {
      "command": "uv",
      "args": ["--directory", "/absolute/path/to/mcp-tools", "run", "server.py"]
    }
  }
}
```

Make sure to run neovim/claude desktop/vscode/cursor from a shell which has
access to the `uv` binary.
