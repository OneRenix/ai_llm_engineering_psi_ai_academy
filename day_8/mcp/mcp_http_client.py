"""
MCP (Model Context Protocol) HTTP Client Implementation

This module implements an HTTP client that communicates with an MCP server via
HTTP REST API endpoints. It provides both programmatic and interactive interfaces
for accessing MCP tools over the web.

The client communicates with a server running in HTTP mode and provides:
- Tool discovery and listing
- Tool execution with parameters
- Error handling and response parsing
- Interactive command-line interface

Author: AI Assistant
Date: 2024
"""

import requests
import json
import asyncio
from typing import Dict, Any, Optional


class MCPHTTPClient:
    """
    HTTP client for communicating with an MCP server via REST API.
    
    This client provides methods to interact with MCP tools over HTTP,
    including tool discovery, execution, and result handling.
    
    Attributes:
        base_url (str): Base URL of the MCP server (default: http://localhost:8000)
        session (requests.Session): HTTP session for making requests
    """
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        """
        Initialize the MCP HTTP client.
        
        Args:
            base_url (str): Base URL of the MCP server. Defaults to localhost:8000.
        """
        self.base_url = base_url
        # Create a persistent HTTP session for connection pooling
        self.session = requests.Session()
    
    def list_tools(self) -> Dict[str, Any]:
        """
        Retrieve a list of available tools from the MCP server.
        
        Makes a GET request to the /tools endpoint to discover
        what tools are available on the server.
        
        Returns:
            Dict[str, Any]: Dictionary containing tool information or empty dict on error
            
        Example:
            >>> client = MCPHTTPClient()
            >>> tools = client.list_tools()
            >>> print(tools)
            {'tools': [{'name': 'poet', 'description': 'Poem generator'}, ...]}
        """
        try:
            response = self.session.get(f"{self.base_url}/tools")
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error listing tools: {e}")
            return {}
    
    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Optional[str]:
        """
        Execute a specific tool on the MCP server with given arguments.
        
        Makes a POST request to the tool's endpoint with the provided arguments
        and returns the tool's output.
        
        Args:
            tool_name (str): Name of the tool to execute
            arguments (Dict[str, Any]): Arguments to pass to the tool
            
        Returns:
            Optional[str]: Tool output as string, or None if execution failed
            
        Example:
            >>> result = client.call_tool('poet', {'theme': 'coding'})
            >>> print(result)
            "The screen glows bright, a digital dawn..."
        """
        try:
            # Prepare the request payload
            payload = {
                "tool": tool_name,
                "arguments": arguments
            }
            
            # Make POST request to the tool endpoint
            response = self.session.post(
                f"{self.base_url}/tools/{tool_name}",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            
            # Parse and return the response
            result = response.json()
            return result.get("content", [{}])[0].get("text", "No output")
            
        except requests.exceptions.RequestException as e:
            print(f"Error calling tool {tool_name}: {e}")
            return None
    
    def generate_poem(self, theme: str) -> Optional[str]:
        """
        Generate a poem about a specific theme using the poet tool.
        
        Convenience method that calls the poet tool with the given theme.
        
        Args:
            theme (str): The theme or topic for the poem
            
        Returns:
            Optional[str]: Generated poem or None if generation failed
            
        Example:
            >>> poem = client.generate_poem("artificial intelligence")
            >>> print(poem)
            "A mind of silicon, a heart of code..."
        """
        return self.call_tool("poet", {"theme": theme})
    
    def roll_dice(self, notation: str, num_rolls: int = 1) -> Optional[str]:
        """
        Roll dice using the roll_dice tool.
        
        Convenience method that calls the roll_dice tool with the given parameters.
        
        Args:
            notation (str): Dice notation (e.g., "2d6" for two six-sided dice)
            num_rolls (int, optional): Number of times to roll. Defaults to 1.
            
        Returns:
            Optional[str]: Dice roll results or None if rolling failed
            
        Example:
            >>> result = client.roll_dice("1d20", 3)
            >>> print(result)
            "Roll 1: ROLLS: 15 -> RETURNS: 15\nRoll 2: ROLLS: 8 -> RETURNS: 8..."
        """
        return self.call_tool("roll_dice", {"notation": notation, "num_rolls": num_rolls})


def main():
    """
    Main function demonstrating the HTTP client usage.
    
    This function provides:
    1. A demonstration of the client's capabilities
    2. An interactive interface for testing tools
    3. Examples of tool discovery and execution
    
    The function runs automatically when the script is executed directly.
    """
    # Initialize the HTTP client
    client = MCPHTTPClient()
    
    print("🎭 MCP HTTP Client Demo")
    print("=" * 40)
    
    # Demonstrate tool discovery
    print("\n📋 Available tools:")
    tools = client.list_tools()
    if tools:
        for tool in tools.get("tools", []):
            print(f"  - {tool.get('name', 'Unknown')}: {tool.get('description', 'No description')}")
    else:
        print("  No tools found or server not responding")
    
    # Demonstrate automatic tool testing
    print("\n🚀 Testing tools...")
    
    # Test poem generation
    print("\n🎭 Generating a poem about 'artificial intelligence':")
    poem = client.generate_poem("artificial intelligence")
    if poem:
        print(poem)
    else:
        print("Failed to generate poem")
    
    # Test dice rolling
    print("\n🎲 Rolling 3 dice with 2d6 notation:")
    dice_result = client.roll_dice("2d6", 3)
    if dice_result:
        print(dice_result)
    else:
        print("Failed to roll dice")
    
    # Interactive mode for user testing
    print("\n💬 Interactive mode (press Ctrl+C to exit):")
    try:
        while True:
            print("\nChoose an action:")
            print("1. Generate a poem")
            print("2. Roll dice")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == "1":
                # Handle poem generation
                theme = input("Enter theme for poem: ").strip()
                if theme:
                    poem = client.generate_poem(theme)
                    if poem:
                        print(f"\n🎭 Poem about '{theme}':")
                        print(poem)
                    else:
                        print("Failed to generate poem")
                else:
                    print("Theme cannot be empty")
            
            elif choice == "2":
                # Handle dice rolling
                notation = input("Enter dice notation (e.g., '1d20'): ").strip()
                if notation:
                    num_rolls = input("Enter number of rolls (default 1): ").strip()
                    num_rolls = int(num_rolls) if num_rolls.isdigit() else 1
                    
                    dice_result = client.roll_dice(notation, num_rolls)
                    if dice_result:
                        print(f"\n🎲 Dice roll result: {dice_result}")
                    else:
                        print("Failed to roll dice")
                else:
                    print("Dice notation cannot be empty")
            
            elif choice == "3":
                print("Goodbye! 👋")
                break
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    
    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")


if __name__ == "__main__":
    """
    Entry point for the MCP HTTP client.
    
    When run directly, this script:
    1. Creates an HTTP client instance
    2. Demonstrates the client's capabilities
    3. Provides an interactive interface for testing
    
    Usage:
        python mcp_http_client.py
        
    Prerequisites:
        - MCP server must be running in HTTP mode
        - Server should be accessible at http://localhost:8000
    """
    main()
