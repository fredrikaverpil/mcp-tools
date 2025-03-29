# mcp-tools

## Quickstart

```sh
cd mcp-tools

# install dependencies
uv sync
```

Add the MCP server to the mcphub.nvim/Claude/vscode JSON settings:

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

Make sure to run Neovim/Claude Desktop/vscode from a shell which has access to
the `uv` binary.
