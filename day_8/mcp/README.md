# 🚀 MCP (Model Context Protocol) Tutorial: Building AI-Powered Tools

Welcome to Day 8 of AI/LLM Engineering! This tutorial will guide you through building and running an MCP server with AI-powered tools including poem generation and dice rolling.

## 📚 What is MCP?

**Model Context Protocol (MCP)** is a standard for building AI applications where:
- **Servers** provide tools and capabilities
- **Clients** connect to servers and use their tools
- **Communication** happens via stdio or HTTP

Think of it like a plugin system for AI applications - you can build tools once and use them from many different clients!

## 🎯 What We're Building

Our MCP server provides two main tools:
1. **🎭 Poet Tool** - Generates poems about any theme using Google's Gemini AI
2. **🎲 Dice Roller Tool** - Rolls dice using standard RPG notation (e.g., "2d6", "4d6k3")

## 🛠️ Prerequisites

Before we start, make sure you have:

- **Python 3.13+** installed
- **Google AI API key** for Gemini access
- **Git** for cloning the repository

## 🚀 Getting Started

### Step 1: Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd day_8

# Initialize the project with uv
uv init

# Install dependencies
uv sync
```

### Step 2: Environment Setup

Create a `.env` file in your project root:

```bash
# Create .env file
echo '"GOOGLE_API_KEY=your_actual_api_key_here"' > .env
```

**⚠️ Important:** Replace `your_actual_api_key_here` with your actual Google AI API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## 🏃‍♂️ Running the Code

### Option 1: Stdio Mode (Recommended for Development)

Stdio mode runs the server and client together, perfect for development and testing:

```bash
# Run the client (which automatically starts the server)
uv run python mcp_client.py
```

**What happens:**
1. Client starts and spawns server as subprocess
2. Server provides interactive tool selection
3. Choose between poet and dice rolling tools
4. Enter parameters and see results

**Example interaction:**
```
Available tools:
  - poet: Poem generator
  - roll_dice: Roll the dice with the given notation

Enter tool name (or press Enter for 'poet'): 
Enter theme for poem: artificial intelligence

🎭 Poem about 'artificial intelligence':
A mind of silicon, a heart of code...
```

### Option 2: HTTP Mode (Great for Web Integration)

HTTP mode runs the server independently, allowing multiple clients to connect:

```bash
# Terminal 1: Start the server
uv run python mcp_server.py --http

# Terminal 2: Test with HTTP client
uv run python mcp_http_client.py
```

**What happens:**
1. Server starts on `http://localhost:8000`
2. HTTP client connects and lists available tools
3. Client demonstrates automatic tool testing
4. Interactive mode for manual testing

### Option 3: Sampling Mode (Client-Side LLM Execution)

Sampling mode demonstrates how clients can handle LLM execution instead of servers:

```bash
# Terminal 1: Start the sampling server
uv run python mcp_sampling_server.py

# Terminal 2: Run the sampling client
uv run python mcp_sampling_client.py
```

**What happens:**
1. Server provides prompts and configuration (no LLM execution)
2. Client receives the prompt via sampling callback
3. Client processes the prompt (currently returns mock response)
4. Client sends result back to server

**Key difference:** In sampling mode, the server never calls external AI APIs - it delegates all LLM operations to the client.

## 🔧 Understanding the Code Structure

### Core Files

```
day_8/
├── mcp_server.py              # Main MCP server with tools
├── mcp_client.py              # Stdio client for direct interaction
├── mcp_http_client.py         # HTTP client for web access
├── mcp_sampling_server.py     # Sampling mode server (client-side LLM)
├── mcp_sampling_client.py     # Sampling mode client with LLM callback
├── tool/
│   └── dice_roller.py         # Dice rolling utility
└── pyproject.toml             # Project configuration
```

### MCP Sampling Mode

**Sampling mode** is a special MCP feature where:
- **Server** provides prompts and configuration
- **Client** executes the actual LLM operations
- **Use case**: Client-side AI processing, custom LLM integration, offline capabilities

This is different from traditional MCP where the server handles LLM execution.

### How It Works

1. **Server (`mcp_server.py`)**:
   - Defines tools using `@server.tool()` decorators
   - Can run in stdio or HTTP mode
   - Integrates with Google Gemini AI for poem generation

2. **Stdio Client (`mcp_client.py`)**:
   - Spawns server process automatically
   - Provides interactive interface
   - Manages server lifecycle

3. **HTTP Client (`mcp_http_client.py`)**:
   - Connects to running HTTP server
   - Makes REST API calls to tools
   - Great for integration with other applications

## 🎭 Using the Tools

### Poet Tool

Generate poems about any theme:

```python
# Via stdio client
Enter tool name: poet
Enter theme for poem: coding

# Via HTTP client
POST /tools/poet
{
  "arguments": {
    "theme": "coding"
  }
}
```

### Dice Roller Tool

Roll dice using standard notation:

```python
# Via stdio client
Enter tool name: roll_dice
Enter dice notation: 2d6
Enter number of rolls: 3

# Via HTTP client
POST /tools/roll_dice
{
  "arguments": {
    "notation": "2d6",
    "num_rolls": 3
  }
}
```

**Dice Notation Examples:**
- `1d20` - Roll one 20-sided die
- `2d6` - Roll two 6-sided dice
- `4d6k3` - Roll four 6-sided dice, keep highest 3
- `1d100` - Roll one 100-sided die (percentile)

## 🌐 Advanced: HTTP API Endpoints

When running in HTTP mode, your server provides these endpoints:

```bash
# List available tools
GET http://localhost:8000/tools

# Generate a poem
POST http://localhost:8000/tools/poet
Content-Type: application/json
{
  "arguments": {
    "theme": "your_theme_here"
  }
}

# Roll dice
POST http://localhost:8000/tools/roll_dice
Content-Type: application/json
{
  "arguments": {
    "notation": "2d6",
    "num_rolls": 3
  }
}
```

## 🔍 Testing Your Setup

### Quick Test Commands

```bash
# Test HTTP endpoints with curl
curl http://localhost:8000/tools

# Test poem generation
curl -X POST http://localhost:8000/tools/poet \
  -H "Content-Type: application/json" \
  -d '{"arguments": {"theme": "testing"}}'

# Test dice rolling
curl -X POST http://localhost:8000/tools/roll_dice \
  -H "Content-Type: application/json" \
  -d '{"arguments": {"notation": "1d20", "num_rolls": 1}}'
```

### Integration Testing

```bash
# Run the full HTTP client demo
uv run python mcp_http_client.py

# Run stdio client for direct interaction
uv run python mcp_client.py
```

## 🚨 Troubleshooting

### Common Issues

1. **"ModuleNotFoundError: No module named 'pydantic_ai'"**
   ```bash
   uv sync  # Install dependencies
   ```

2. **"Invalid dice notation"**
   - Use format: `XdY` or `XdYkZ`
   - Examples: `1d20`, `2d6`, `4d6k3`

3. **"Google API key not found"**
   - Check your `.env` file exists
   - Verify `GOOGLE_API_KEY` is set correctly
   - Restart your terminal after creating `.env`

4. **Server won't start in HTTP mode**
   ```bash
   # Check if port 8000 is available
   lsof -i :8000
   
   # Kill any existing processes
   pkill -f "python mcp_server.py"
   ```

### Debug Mode

Enable verbose logging by setting environment variables:

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
export MCP_LOG_LEVEL=DEBUG
uv run python mcp_server.py --http
```

## 🎓 Learning Objectives

By completing this tutorial, you'll understand:

- ✅ **MCP Architecture**: How servers and clients communicate
- ✅ **Dual Mode Operation**: Stdio vs HTTP communication
- ✅ **Tool Development**: Creating and exposing AI-powered tools
- ✅ **Client Integration**: Building clients for different use cases
- ✅ **Error Handling**: Graceful failure and debugging
- ✅ **API Design**: RESTful endpoint design for tools

## 🔮 Next Steps

Now that you have a working MCP server, try:

1. **Add New Tools**: Create tools for image generation, code analysis, etc.
2. **Build Web UI**: Create a React/Vue frontend for your tools
3. **Integrate with Other MCP Servers**: Connect to servers for different domains
4. **Deploy**: Host your server on cloud platforms
5. **Extend**: Add authentication, rate limiting, and monitoring

### Extending Sampling Mode

The sampling client currently returns mock responses. To integrate with real LLMs:

```python
# In mcp_sampling_client.py, replace the mock response with:
import openai  # or your preferred LLM library

async def sampling_callback(context, params):
    # Extract user message
    user_message = params.messages[0].content.text
    
    # Call your LLM
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    
    return CreateMessageResult(
        role='assistant',
        content=TextContent(type='text', text=response.choices[0].message.content),
        model='gpt-4'
    )
```

This enables client-side AI processing while keeping the server lightweight.

## 📖 Additional Resources

- [MCP Official Documentation](https://modelcontextprotocol.io/)
- [FastMCP Framework](https://github.com/jlowin/fastmcp)
- [Google AI Studio](https://makersuite.google.com/)
- [Pydantic AI Documentation](https://docs.pydantic.ai/)

## 🤝 Contributing

Found a bug or have an idea? Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

**Happy coding! 🚀**

*This tutorial was created as part of Day 8 of AI/LLM Engineering. For questions or support, please open an issue in the repository.*

