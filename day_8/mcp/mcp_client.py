"""
MCP (Model Context Protocol) Stdio Client Implementation

This module implements an MCP client that communicates with an MCP server via
standard input/output streams (stdio). It provides an interactive interface
for users to interact with MCP tools.

The client automatically spawns the server process and manages the communication
between the user and the server's tools.

Features:
- Interactive tool selection
- Parameter input for each tool
- Support for poet and roll_dice tools
- Automatic server process management

Author: AI Assistant
Date: 2024
"""

import asyncio
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def client():
    """
    Main client function that establishes connection with the MCP server.
    
    This function:
    1. Sets up server parameters to spawn the MCP server process
    2. Establishes stdio communication with the server
    3. Lists available tools
    4. Provides interactive interface for tool selection and execution
    
    The server is automatically started as a subprocess and managed by the client.
    """
    # Configure server parameters - the client will spawn the server process
    server_params = StdioServerParameters(
        command='python',  # Command to run the server
        args=['mcp_server.py'],  # Arguments (server script)
        env=os.environ  # Pass current environment variables
    )
    
    # Establish stdio communication with the server
    async with stdio_client(server_params) as (read, write):
        # Create a client session for MCP communication
        async with ClientSession(read, write) as session:
            # Initialize the MCP session
            await session.initialize()
            
            # Get available tools from the server
            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")
            print()
            
            # Interactive tool selection and execution
            tool_name = input("Enter tool name (or press Enter for 'poet'): ").strip() or 'poet'
            
            # Execute the selected tool with user-provided parameters
            if tool_name == 'poet':
                # Handle poem generation tool
                theme = input("Enter theme for poem: ").strip()
                if not theme:
                    theme = "AI and technology"  # Default theme
                
                # Call the poet tool on the server
                result = await session.call_tool('poet', {'theme': theme})
                print(f"\nPoem about '{theme}':")
                print(result.content[0].text)
                
            elif tool_name == 'roll_dice':
                # Handle dice rolling tool
                notation = input("Enter dice notation (e.g., '2d6'): ").strip()
                if not notation:
                    notation = "1d20"  # Default dice notation
                
                num_rolls = input("Enter number of rolls (default 1): ").strip()
                num_rolls = int(num_rolls) if num_rolls.isdigit() else 1
                
                # Call the roll_dice tool on the server
                result = await session.call_tool('roll_dice', {'notation': notation, 'num_rolls': num_rolls})
                print(f"\nDice roll result: {result.content[0].text}")
                
            else:
                # Handle unknown tools
                print(f"Tool '{tool_name}' not implemented in this client yet.")


if __name__ == '__main__':
    """
    Entry point for the MCP client.
    
    When run directly, this script:
    1. Starts the async event loop
    2. Runs the main client function
    3. Manages the client-server communication lifecycle
    
    Usage:
        python mcp_client.py
        
    Note: This client automatically manages the MCP server process.
    Do not run mcp_server.py directly unless you want HTTP mode.
    """
    asyncio.run(client())