"""
MCP (Model Context Protocol) Sampling Client Implementation

This module demonstrates MCP sampling mode, where the client is responsible
for executing LLM operations instead of the server. In sampling mode, the
server only sends prompts and configuration, and the client handles the
actual LLM execution.

This is useful for:
- Client-side LLM processing
- Custom LLM integration
- Offline processing capabilities
- Testing and development

Author: AI Assistant
Date: 2024
"""

import asyncio
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.shared.context import RequestContext
from mcp.types import CreateMessageRequestParams, CreateMessageResult, ErrorData, TextContent


async def sampling_callback(
    context: RequestContext[ClientSession, Any], params: CreateMessageRequestParams
) -> CreateMessageResult | ErrorData:
    """
    Callback function that handles LLM execution in sampling mode.
    
    This function is called by the MCP client when the server requests
    message creation. Instead of the server executing the LLM, the client
    handles the execution and returns the result.
    
    Args:
        context (RequestContext[ClientSession, Any]): MCP request context
        params (CreateMessageRequestParams): Parameters for message creation
        
    Returns:
        CreateMessageResult | ErrorData: The generated message or error
        
    Example:
        The server sends a prompt like "write a poem about socks" and
        this callback generates the response "Socks for a fox."
    """
    # Log the system prompt for debugging
    print('sampling system prompt:', params.systemPrompt)
    #> sampling system prompt: always reply in rhyme
    
    # Log the user messages for debugging
    print('sampling messages:', params.messages)
    """
    sampling messages:
    [
        SamplingMessage(
            role='user',
            content=TextContent(
                type='text',
                text='write a poem about socks',
                annotations=None,
                meta=None,
            ),
        )
    ]
    """

    # TODO: Replace this with actual LLM integration
    # In a real implementation, you would:
    # 1. Extract the user's message from params.messages
    # 2. Send it to your chosen LLM (OpenAI, Anthropic, local model, etc.)
    # 3. Process the response and return it
    response_content = 'Socks for a fox.'

    # Return the generated message in the expected format
    return CreateMessageResult(
        role='assistant',
        content=TextContent(type='text', text=response_content),
        model='fictional-llm',  # Replace with actual model name
    )


async def client():
    """
    Main client function that demonstrates MCP sampling mode.
    
    This function:
    1. Sets up server parameters for the sampling server
    2. Establishes stdio communication
    3. Registers the sampling callback for LLM execution
    4. Calls a tool to demonstrate the sampling workflow
    
    In sampling mode, the server sends the prompt and the client
    executes the LLM operation via the sampling_callback.
    """
    # Configure server parameters for the sampling server
    server_params = StdioServerParameters(
        command='python', 
        args=['mcp_sampling_server.py']
    )
    
    # Establish stdio communication with sampling callback
    async with stdio_client(server_params) as (read, write):
        # Create session with sampling callback for client-side LLM execution
        async with ClientSession(read, write, sampling_callback=sampling_callback) as session:
            # Initialize the MCP session
            await session.initialize()
            
            # Call the poet tool - this will trigger the sampling callback
            result = await session.call_tool('poet', {'theme': 'socks'})
            print(result.content[0].text)
            #> Socks for a fox.


if __name__ == '__main__':
    """
    Entry point for the MCP sampling client.
    
    When run directly, this script:
    1. Starts the async event loop
    2. Runs the main client function
    3. Demonstrates MCP sampling mode where the client
       handles LLM execution instead of the server
    
    Usage:
        python mcp_sampling_client.py
        
    Prerequisites:
        - mcp_sampling_server.py must be available
        - The sampling server should be configured for sampling mode
    """
    asyncio.run(client())