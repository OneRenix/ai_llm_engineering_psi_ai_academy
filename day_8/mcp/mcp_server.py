"""
MCP (Model Context Protocol) Server Implementation

This module implements an MCP server that provides AI-powered tools including:
- Poem generation using Google's Gemini model
- Dice rolling functionality

The server can run in two modes:
1. Stdio mode: For MCP client communication (default)
2. HTTP mode: For web-based access via REST API

Author: AI Assistant
Date: 2024
"""

from mcp.server.fastmcp import FastMCP
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from dotenv import load_dotenv
from tool.dice_roller import DiceRoller
import os

# Load environment variables from .env file
load_dotenv()

# Get Google API key from environment variables
API_KEY = os.getenv('GOOGLE_API_KEY')

# Initialize the FastMCP server
server = FastMCP('Pydantic AI Server')

# Set up Google AI provider and model
provider = GoogleProvider(api_key=API_KEY)
model = GoogleModel('gemini-1.5-flash', provider=provider)

# Create the main AI agent for tool execution
server_agent = Agent(model)


@server.tool()
async def poet(theme: str) -> str:
    """
    Generate a poem about a specified theme using Google's Gemini AI model.
    
    Args:
        theme (str): The theme or topic for the poem
        
    Returns:
        str: A generated poem about the specified theme
        
    Example:
        >>> await poet("artificial intelligence")
        "A mind of silicon, a heart of code..."
    """
    r = await server_agent.run(f'write a poem about {theme}')
    return r.output


@server.tool()
def roll_dice(notation: str, num_rolls: int = 1) -> str:
    """
    Roll dice using standard dice notation (e.g., "2d6" for two six-sided dice).
    
    Args:
        notation (str): Dice notation in format "XdY" where X is number of dice and Y is sides
        num_rolls (int, optional): Number of times to roll. Defaults to 1.
        
    Returns:
        str: Formatted result of the dice rolls
        
    Examples:
        >>> roll_dice("1d20")
        "ROLLS: 15 -> RETURNS: 15"
        
        >>> roll_dice("2d6", 3)
        "Roll 1: ROLLS: 6, 2 -> RETURNS: 8\nRoll 2: ROLLS: 4, 3 -> RETURNS: 7..."
    """
    roller = DiceRoller(notation, num_rolls)
    return str(roller)


# Add HTTP endpoints for the tools
from starlette.requests import Request
from starlette.responses import JSONResponse

@server.custom_route("/tools", methods=["GET"])
async def list_tools(request: Request):
    """
    HTTP endpoint to list all available tools.
    
    Args:
        request (Request): Starlette request object
        
    Returns:
        JSONResponse: List of available tools with names and descriptions
    """
    tools = [
        {
            "name": "poet",
            "description": "Poem generator"
        },
        {
            "name": "roll_dice", 
            "description": "Roll the dice with the given notation"
        }
    ]
    return JSONResponse({"tools": tools})


@server.custom_route("/tools/poet", methods=["POST"])
async def call_poet(request: Request):
    """
    HTTP endpoint to call the poet tool.
    
    Args:
        request (Request): Starlette request object containing JSON with theme
        
    Returns:
        JSONResponse: Generated poem or error message
        
    Request body format:
        {"arguments": {"theme": "your_theme_here"}}
    """
    data = await request.json()
    theme = data.get("arguments", {}).get("theme", "artificial intelligence")
    
    try:
        r = await server_agent.run(f'write a poem about {theme}')
        return JSONResponse({"content": [{"text": r.output}]})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@server.custom_route("/tools/roll_dice", methods=["POST"])
async def call_roll_dice(request: Request):
    """
    HTTP endpoint to call the roll_dice tool.
    
    Args:
        request (Request): Starlette request object containing JSON with dice parameters
        
    Returns:
        JSONResponse: Dice roll results or error message
        
    Request body format:
        {"arguments": {"notation": "2d6", "num_rolls": 3}}
    """
    data = await request.json()
    args = data.get("arguments", {})
    notation = args.get("notation", "1d20")
    num_rolls = args.get("num_rolls", 1)
    
    try:
        roller = DiceRoller(notation, num_rolls)
        return JSONResponse({"content": [{"text": str(roller)}]})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--http':
        # Run as HTTP server for web-based access
        import uvicorn
        print("Starting MCP server in HTTP mode on http://localhost:8000")
        uvicorn.run(server.streamable_http_app(), host="0.0.0.0", port=8000)
    else:
        # Run in stdio mode for MCP client communication (default)
        print("Starting MCP server in stdio mode...")
        print("This server should be invoked by an MCP client, not run directly.")
        print("Use 'python mcp_server.py --http' to run in HTTP mode.")
        print("Use 'python mcp_client.py' to run the stdio client.")
        server.run()