# Chainlit AI Chatbot Examples

This project demonstrates different approaches to building AI chatbots using Chainlit, including LangChain integration and Google Gemini API.

## Prerequisites

- Python 3.12+
- UV package manager
- OpenAI API key (for LangChain example)
- Google Gemini API key (for Gemini example)

## Setup

1. **Install dependencies using UV:**
   ```bash
   uv sync
   ```

2. **Set up environment variables:**
   Create a `.env` file in the project root with your API keys:
   ```bash
   # For LangChain example
   OPENAI_API_KEY=your_openai_api_key_here
   
   # For Gemini example  
   GOOGLE_GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Running the Examples

### 1. Basic Chainlit Hello
Start with the basic Chainlit example:
```bash
chainlit hello
```
This starts a basic Chainlit server accessible via browser with a simple chat interface.

### 2. LangChain Integration (`step1_langchain.py`)
A chatbot that uses LangChain with OpenAI's GPT model, featuring:
- Streaming responses
- Historical knowledge specialization
- LangChain callback integration

**To run:**
```bash
chainlit run step1_langchain.py
```

**Features:**
- Uses OpenAI's streaming API for real-time responses
- Implements a historian persona for specialized knowledge
- Integrates LangChain's callback system with Chainlit

### 3. Google Gemini Integration (`step2_gemini.py`)
A chatbot powered by Google's Gemini model (Gemma-3-27B-IT), featuring:
- Direct Gemini API integration
- Asynchronous content generation
- Simple, lightweight implementation

**To run:**
```bash
chainlit run step2_gemini.py
```

**Features:**
- Uses Google's Generative AI client
- Leverages the Gemma-3-27B-IT model
- Asynchronous message handling for better performance

## Project Structure

```
day_9/
├── step1_langchain.py    # LangChain + OpenAI integration
├── step2_gemini.py       # Google Gemini integration
├── gemma/                # Additional Gemma-related files
├── pyproject.toml        # Project dependencies
└── README.md            # This file
```

## Environment Variables

Make sure to set the following environment variables in your `.env` file:

- `OPENAI_API_KEY`: Required for the LangChain example
- `GOOGLE_GEMINI_API_KEY`: Required for the Gemini example

## Accessing the Chatbots

After running any of the examples, open your browser and navigate to:
- **Local development**: `http://localhost:8000`
- **Default Chainlit port**: Usually `http://localhost:8000`

## Troubleshooting

- **API Key Issues**: Ensure your `.env` file is properly configured with valid API keys
- **Port Conflicts**: If port 8000 is busy, Chainlit will automatically use the next available port
- **Dependencies**: Run `uv sync` to ensure all required packages are installed

### Common Import Error: "No module named 'langchain_openai'"

**Problem**: You may encounter this error even after running `uv sync`:
```
ModuleNotFoundError: No module named 'langchain_openai'
```

**Cause**: This happens when using the global `chainlit` command instead of the one in your project's virtual environment.

**Solution**: Always use the chainlit executable from within your project's virtual environment:

```bash
# ❌ Don't use this (global chainlit)
chainlit run step1_langchain.py

# ✅ Use this instead (project-specific chainlit)
.venv/bin/chainlit run step1_langchain.py --port 8001
```

**Why this happens**: 
- Global `chainlit` (installed via pipx) runs in a different Python environment
- Project dependencies are installed in `.venv/` via UV
- The global command can't see your project's installed packages

## Next Steps

- Customize the prompts in each example for your specific use case
- Add more sophisticated conversation memory
- Implement additional AI model integrations
- Explore Chainlit's advanced features like file uploads and custom UI elements
