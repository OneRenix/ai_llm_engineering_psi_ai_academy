# Open Deep Research Notebook

This notebook implements an unrolled version of the **Open Deep Research** graph, a sophisticated AI-powered research and report generation system built with LangGraph.

## 🎯 What We're Building

The Open Deep Research system is an intelligent research assistant that can:

- **Automatically plan research reports** by breaking down complex topics into logical sections
- **Generate targeted search queries** for each section to gather relevant information
- **Perform web searches** using multiple search APIs (Tavily, Perplexity, Exa, arXiv, PubMed)
- **Write comprehensive report sections** based on gathered research
- **Iteratively refine content** through feedback loops and additional research
- **Compile final reports** that synthesize all research findings

## 🏗️ Architecture Overview

The system is built as a **state machine** with two main graphs:

### 1. **Report Planning Graph** (Main Graph)
- Generates initial report structure and sections
- Manages human feedback and approval workflow
- Orchestrates the entire research process
- Compiles final reports

### 2. **Section Building Graph** (Sub-graph)
- Generates search queries for specific sections
- Performs web searches using configured APIs
- Writes section content based on research
- Implements iterative refinement loops

## 🔧 Key Components

### **State Management**
- **ReportState**: Manages overall report progress, sections, and final output
- **SectionState**: Handles individual section research and writing
- **Configuration**: Centralized settings for search APIs, models, and report structure

### **Search APIs Supported**
- **Tavily**: General web search with raw content extraction
- **Perplexity**: AI-powered search with factual information
- **Exa**: Advanced web search with domain filtering and subpage retrieval
- **arXiv**: Academic paper search for research topics
- **PubMed**: Biomedical literature search

### **AI Model Providers**
- **Anthropic Claude**: Default for planning and writing (recommended)
- **OpenAI**: Alternative provider option
- **Groq**: High-speed inference option

## 🚀 Getting Started

### **Prerequisites**
You'll need API keys for the services you plan to use:

```python
# Required for default configuration
os.environ["ANTHROPIC_API_KEY"] = "your_anthropic_key"
os.environ["TAVILY_API_KEY"] = "your_tavily_key"

# Optional alternatives
os.environ["OPENAI_API_KEY"] = "your_openai_key"
os.environ["PERPLEXITY_API_KEY"] = "your_perplexity_key"
os.environ["EXA_API_KEY"] = "your_exa_key"
```

### **Installation**
```bash
cd day_8/deep_research
uv sync
```

### **Basic Usage**

1. **Initialize the graph**:
```python
graph_with_checkpoint = builder.compile(checkpointer=memory)
```

2. **Run research on a topic**:
```python
async def run_graph_and_show_report():
    async for chunk in graph_with_checkpoint.astream(
        {"topic": "Your Research Topic Here"}, 
        {"configurable": {"thread_id": str(uuid.uuid4())}},
        stream_mode="updates"
    ):
        # Process chunks and handle interrupts
        pass
```

3. **Handle user feedback** when prompted:
```python
# Approve the plan
await approve_plan()

# Or provide feedback
await provide_feedback("Your feedback here")
```

## ⚙️ Configuration Options

### **Report Structure**
Customize the default report template in `DEFAULT_REPORT_STRUCTURE`:
- Introduction (no research needed)
- Main body sections (research-enabled)
- Conclusion with structural elements

### **Search Parameters**
- **Number of queries per iteration**: Default 1, increase for more comprehensive research
- **Maximum search depth**: Default 1, increase for iterative refinement
- **Search API selection**: Choose from supported providers
- **API-specific configurations**: Customize parameters for each search service

### **Model Selection**
- **Planner models**: Choose AI models for report planning and section grading
- **Writer models**: Select models for content generation
- **Thinking mode**: Enable for Claude models with extended reasoning

## 🔄 Workflow Process

1. **Topic Input** → User provides research topic
2. **Plan Generation** → AI creates report structure and sections
3. **Human Review** → User approves or provides feedback on the plan
4. **Research Phase** → For each research-enabled section:
   - Generate search queries
   - Perform web searches
   - Write section content
   - Grade content quality
   - Iterate if needed
5. **Final Writing** → Generate non-research sections using completed research
6. **Report Compilation** → Combine all sections into final report

## 📊 Advanced Features

### **Checkpointing**
The system uses LangGraph's checkpoint system to maintain state across executions, allowing you to:
- Resume interrupted research sessions
- Review progress at any point
- Handle long-running research tasks

### **Parallel Processing**
- Multiple sections can be researched simultaneously using the `Send()` API
- Search operations are optimized for rate limits and API constraints

### **Quality Control**
- **Section grading**: AI evaluates content quality and identifies gaps
- **Iterative refinement**: Automatic follow-up queries for incomplete sections
- **Content validation**: Ensures sections meet length and style requirements

## 🎨 Customization Examples

### **Custom Report Structure**
```python
CUSTOM_REPORT_STRUCTURE = """
1. Executive Summary
2. Background and Context
3. Technical Analysis
4. Implementation Strategy
5. Risk Assessment
6. Recommendations
"""
```

### **Domain-Specific Search**
```python
# For academic research
search_api_config = {
    "include_domains": ["arxiv.org", "scholar.google.com"],
    "num_results": 10
}

# For technical documentation
search_api_config = {
    "include_domains": ["github.com", "stackoverflow.com"],
    "max_characters": 2000
}
```

## 🚨 Rate Limiting & Best Practices

- **Tavily**: 5 requests/second
- **Exa**: 4 requests/second
- **arXiv**: 1 request per 3 seconds
- **PubMed**: Conservative delays with exponential backoff

The system automatically handles rate limits with intelligent delays and retry logic.

## 🔍 Troubleshooting

### **Common Issues**
1. **API Key Errors**: Ensure all required API keys are set in environment variables
2. **Rate Limiting**: Reduce `number_of_queries` or `max_search_depth` if hitting limits
3. **Model Failures**: Switch to alternative model providers if encountering issues
4. **Search Failures**: Check API quotas and network connectivity

### **Performance Optimization**
- Use smaller `max_search_depth` for faster results
- Reduce `number_of_queries` to minimize API calls
- Consider using faster models (Groq) for real-time applications

## 📚 Additional Resources

- **Original Repository**: [Open Deep Research](https://github.com/langchain-ai/open_deep_research)
- **LangGraph Documentation**: [langchain.com/langgraph](https://langchain.com/langgraph)
- **LangChain Documentation**: [langchain.com](https://langchain.com)

## 🤝 Contributing

This notebook is part of the PSI AI Academy Course on AI/LLM Engineering. Feel free to:
- Experiment with different configurations
- Add new search APIs
- Customize report structures
- Share improvements and feedback

---

**Happy Researching! 🚀**
