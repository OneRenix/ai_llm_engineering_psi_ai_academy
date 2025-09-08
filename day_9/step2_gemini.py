import chainlit as cl  
import google.generativeai as genai  
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

# Configure the Generative AI client  
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))  
  
# Initialize the GenerativeModel  
model = genai.GenerativeModel("gemma-3-27b-it")  
  
@cl.on_message
async def handle_message(message: cl.Message):  
    # Generate content based on the user's input asynchronously
    response = await asyncio.to_thread(
        model.generate_content, 
        contents=[message.content]
    )
    reply = response.text  
    # Send the generated response back to the user  
    await cl.Message(content=reply).send()