# 🤖 AI LLM Engineering - Day 9: A2A Protocol Agent

A sophisticated LangGraph agent implementation featuring the **A2A (Agent-to-Agent) Protocol** with intelligent helpfulness evaluation and comprehensive tool integration.

## 🚀 Quick Start

```bash
# Clone and setup
git clone <repository-url>
cd day_9-A2A

# Run quickstart script
chmod +x quickstart.sh
./quickstart.sh

# Start the agent server
uv run python -m app

# Test the agent (in another terminal)
uv run python app/test_client.py
```

## ✨ Key Features

- **🤖 LangGraph Agent**: Advanced agent architecture with state management
- **🔗 A2A Protocol**: Full compliance with Agent-to-Agent communication standards
- **📊 Helpfulness Evaluation**: Intelligent response quality assessment with loop protection
- **🔍 Multi-Tool Integration**: Web search, academic papers, and document retrieval
- **📚 RAG System**: Retrieval-Augmented Generation with vector storage
- **🌊 Streaming Support**: Real-time response streaming for better UX
- **⚡ FastAPI Server**: High-performance async server implementation

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input   │───▶│  LangGraph Agent │───▶│  Tool Execution │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        │
                       ┌──────────────────┐              │
                       │ Helpfulness Eval│              │
                       │   (A2A Loop)    │              │
                       └──────────────────┘              │
                                │                        │
                                ▼                        │
                       ┌──────────────────┐              │
                       │  Response or    │◀──────────────┘
                       │  Continue Loop  │
                       └──────────────────┘
```

## 🛠️ Available Tools

| Tool | Description | Use Case |
|------|-------------|----------|
| **🌐 Web Search** | Real-time internet search via Tavily | Current events, live information |
| **📚 Academic Papers** | arXiv research paper search | Research, literature review |
| **📄 Document Retrieval** | RAG system for loaded documents | Internal knowledge, policies |

## 📋 Prerequisites

- **Python 3.12+**
- **uv package manager** (auto-installed by quickstart script)
- **API Keys**:
  - OpenAI API Key
  - Tavily API Key (optional, for web search)

## ⚙️ Configuration

### Environment Setup

Create a `.env` file in the project root:

```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional (for enhanced functionality)
TAVILY_API_KEY=your_tavily_api_key_here
TOOL_LLM_URL=https://api.openai.com/v1
TOOL_LLM_NAME=gpt-4o-mini
OPENAI_CHAT_MODEL=gpt-4o-mini
RAG_DATA_DIR=data
```

### Document Setup for RAG

```bash
# Create data directory
mkdir -p data

# Add your PDF documents
cp /path/to/your/documents/*.pdf data/
```

## 🚀 Running the Project

### 1. Development Server

```bash
# Start the A2A protocol server
uv run python -m app

# Custom host/port
uv run python -m app --host 0.0.0.0 --port 8080
```

### 2. LangGraph Development Server

```bash
# Start LangGraph dev server
uv run langgraph dev

# Access points:
# API: http://localhost:2024
# Studio: https://smith.langchain.com/studio?baseUrl=http://localhost:2024
```

### 3. Test the Agent

```bash
# Run the test client
uv run python app/test_client.py

# Or use direct API calls
curl -X POST http://localhost:10000/v1/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "assistant_id": "agent",
    "messages": [{
      "role": "user",
      "content": "What are the latest developments in AI?"
    }]
  }'
```

## 🔧 Project Structure

```
📦 day_9-A2A/
├── 📁 app/                           # Main application package
│   ├── 📄 __init__.py               # Package initialization
│   ├── 📄 __main__.py               # A2A server entry point
│   ├── 📄 agent.py                  # Core agent with streaming
│   ├── 📄 agent_executor.py         # A2A protocol executor
│   ├── 📄 agent_graph_with_helpfulness.py  # LangGraph + evaluation
│   ├── 📄 rag.py                    # RAG implementation
│   ├── 📄 tools.py                  # Tool belt configuration
│   ├── 📄 test_client.py            # Test client
│   └── 📄 README.md                 # Detailed technical docs
├── 📄 pyproject.toml                # Project configuration
├── 📄 setup.py                      # Environment setup
├── 📄 quickstart.sh                 # Quick start script
├── 📄 check_env.py                  # Environment validation
└── 📄 README.md                     # This file
```

## 🧪 Example Usage

### Web Search Query
```
User: "What are the latest AI developments in 2024?"
Agent: [Uses Tavily web search] → Provides current information
```

### Academic Research
```
User: "Find recent papers on multimodal transformers"
Agent: [Uses ArXiv search] → Returns relevant research papers
```

### Document Analysis
```
User: "What do our policy documents say about requirements?"
Agent: [Uses RAG system] → Retrieves relevant document sections
```

### Multi-Tool Integration
```
User: "Compare recent research with our internal guidelines"
Agent: [Combines ArXiv + RAG] → Comprehensive analysis
```

## 🔄 A2A Protocol Features

### Helpfulness Evaluation Loop

The agent implements an intelligent evaluation system:

1. **Process Request**: User input is processed through the agent
2. **Tool Execution**: Relevant tools are called as needed
3. **Response Generation**: Agent generates comprehensive response
4. **Helpfulness Check**: A2A evaluation determines response quality
5. **Loop Decision**: Continue improving or finalize response

### Loop Protection

- **Maximum Iterations**: 10 loops to prevent infinite cycles
- **Smart Termination**: Automatic exit on satisfactory responses
- **State Management**: Maintains conversation context throughout

## 🎯 Customization

### Adding New Tools

```python
# In app/tools.py
from langchain_core.tools import tool

@tool
def my_custom_tool(query: str) -> str:
    """Description of what your tool does"""
    # Implementation here
    return result

# Add to tool belt
def get_tool_belt() -> List:
    return [
        # ... existing tools
        my_custom_tool
    ]
```

### Customizing Helpfulness Criteria

Modify evaluation criteria in `agent_graph_with_helpfulness.py`:

```python
prompt_template = """
A helpful response should:
- [Your custom criteria]
- Be factually accurate
- Address the user's specific need
- Use appropriate tools when necessary
"""
```

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **Missing API Keys** | Check `.env` file and run `python check_env.py` |
| **Tool Failures** | Verify API keys and internet connectivity |
| **RAG Errors** | Ensure documents exist in `data/` directory |
| **Import Errors** | Run `uv sync` to install dependencies |

### Debug Mode

```bash
# Enable detailed logging
export LANGCHAIN_VERBOSE=true

# Or in Python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Quick Diagnostics

```bash
# Check environment
uv run python check_env.py

# Test tool availability
uv run python -c "from app.tools import get_tool_belt; print([tool.name for tool in get_tool_belt()])"

# Test RAG system
uv run python -c "from app.rag import get_rag_graph; rag = get_rag_graph(); print('RAG loaded successfully')"
```

## 📊 Performance Tips

- **Chunk Size**: Optimize RAG chunk size for your documents
- **Model Selection**: Choose appropriate OpenAI model for your use case
- **Tool Limits**: Adjust `max_results` in tool configurations
- **Caching**: Consider persistent vector storage for large document collections

## 🔮 Advanced Features

### Multi-Agent Communication
Extend the A2A protocol for agent-to-agent communication with specialized domain agents.

### Custom Evaluation Metrics
Implement additional evaluation criteria like factual accuracy, completeness, and source quality.

### External Service Integration
Connect to external APIs and services through custom tool implementations.

## 📚 Additional Resources

- **Detailed Technical Docs**: See `app/README.md` for comprehensive implementation details
- **LangGraph Documentation**: [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)
- **A2A Protocol**: [https://github.com/a2a-protocol](https://github.com/a2a-protocol)
- **OpenAI API**: [https://platform.openai.com/docs](https://platform.openai.com/docs)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is part of the AI LLM Engineering course. See the course materials for licensing information.

---

**Built with ❤️ using LangGraph, OpenAI, and the A2A Protocol**

*For detailed technical implementation, see `app/README.md`*
