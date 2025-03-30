# mcp-tools

## Quickstart

### Go

Add to the MCP server JSON settings (path depends on which app you're using):

#### Local

```json
{
  "mcpServers": {
    "github.com/fredrikaverpil/mcp-tools": {
      "command": "go",
      "args": [
        "-C",
        "/absolute/path/to/mcp-tools",
        "run",
        "./cmd/cmd-tools/main.go"
      ]
    }
  }
}
```

#### Non-local

```json
{
  "mcpServers": {
    "github.com/fredrikaverpil/mcp-tools": {
      "command": "go",
      "args": [
        "run",
        "github.com/fredrikaverpil/mcp-tools/cmd/cmd-tools@latest"
      ]
    }
  }
}
```

### Python

#### Local

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
access to the `uv` binary _and_ the required dependencies specified in the
`pyproject.toml`.

## References

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [Model Context Protocol GitHub organization](https://github.com/modelcontextprotocol)
- [Unofficial Go implementation of the Model Context Protocol](https://github.com/mark3labs/mcp-go)
- [Official Python SDK](https://github.com/modelcontextprotocol/python-sdk)
