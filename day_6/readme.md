# Jupyter Notebook Summaries

This document breaks down the key theories and practical steps learned from the Jupyter notebooks in this directory.

---

## 1-langgraph.ipynb

This notebook provides a deep dive into building complex, stateful, and cyclical applications with Large Language Models using the LangGraph library.

### Theories & Concepts Learned

- **Stateful, Multi-Agent Applications:** Understanding how to build applications that maintain a persistent state across multiple interactions, enabling more complex conversations and workflows.
- **Graph-Based Architecture:** Learning to represent application logic as a graph, where nodes are functions (computational units) and edges define the flow of control and data. This is ideal for managing the complex, often cyclical, logic required by agentic systems.
- **Centralized State (`AgentState`):** Grasping the concept of a shared state object (defined with `TypedDict`) that is passed between all nodes in the graph. This ensures every part of the application has a consistent view of the current context.
- **Tool Binding and Function Calling:** Seeing how to equip an LLM with external tools (e.g., web search). The notebook demonstrates how the model uses its function-calling capabilities to decide which tool to invoke based on the user's prompt.

### Steps Learned

1.  **Setup:** Install necessary libraries (`langgraph`, `langchain`, etc.) and configure environment variables for API keys (OpenAI, Tavily, LangSmith).
2.  **Tool Definition:** Create a "tool belt" by initializing and listing tools like `TavilySearchResults` and `ArxivQueryRun`.
3.  **Model Initialization:** Instantiate a chat model (`ChatOpenAI`) and bind the tool belt to it, enabling function-calling.
4.  **State Definition:** Define the data structure for the shared `AgentState` that will be passed through the graph.
5.  **Node Creation:** Implement Python functions that will serve as the nodes of the graph. This includes a primary `call_model` node and a `ToolNode` for executing actions.
6.  **Graph Construction:**
    - Instantiate a `StateGraph` with the `AgentState`.
    - Add the defined nodes (`agent`, `action`) to the graph.
    - Set the graph's **entry point** to designate the starting node.
    - Define **conditional edges** to create branches in the logic (e.g., call a tool if the model requests it, otherwise end).
    - Add **standard edges** for fixed transitions (e.g., always return to the agent after a tool action).
7.  **Compilation & Execution:** Compile the graph into a runnable object and execute it by streaming inputs, observing how the state flows through the nodes in real-time.
8.  **Evaluation (Optional with LangSmith):** Learn to create a dataset of questions and expected answers, define custom evaluators (e.g., checking for keywords), and run experiments to measure the agent's performance.

---

## 2-openai_agents.ipynb

This notebook demonstrates how to build a multi-agent research assistant using the high-level `openai-agents` SDK.

### Theories & Concepts Learned

- **OpenAI Assistants API Abstraction:** Understanding the `openai-agents` SDK as a higher-level framework that simplifies agent creation by managing conversation history (Threads) and tool execution automatically.
- **Structured Outputs (Pydantic):** Learning the critical importance of defining a strict schema for an agent's output using Pydantic models. This makes the agent's response predictable, reliable, and easy to parse for use in subsequent steps.
- **Multi-Agent Collaboration:** Witnessing a powerful pattern where specialized agents collaborate to achieve a complex goal. The workflow uses a **Planner** agent to define tasks, a **Searcher** agent to execute them, and a **Writer** agent to synthesize the results into a final report.
- **Asynchronous Execution:** Understanding how to use `asyncio` to run tasks concurrently (like multiple web searches), which dramatically improves the application's performance and efficiency.

### Steps Learned

1.  **Setup:** Install the `openai-agents` library and configure the `OPENAI_API_KEY`.
2.  **Agent Definition:**
    - For each agent, write a clear `instruction` prompt that defines its specific role and goal.
    - Define Pydantic `BaseModel` classes (`WebSearchPlan`, `ReportData`) to enforce a structured output.
    - Instantiate each `Agent`, providing its unique name, instructions, model, tools, and the desired `output_type`.
3.  **Tool Usage:** Provide an agent with pre-built tools like `WebSearchTool` and enforce its use when necessary by setting `tool_choice="required"`.
4.  **Orchestration:**
    - Create a `ResearchManager` class to orchestrate the end-to-end workflow.
    - The manager first calls the **Planner Agent** to generate a research plan.
    - It then executes the plan by running parallel searches with the **Search Agent**.
    - Finally, it passes the aggregated research to the **Writer Agent** to produce the final, structured report.
5.  **Execution and Display:**
    - Implement a `main` async function to capture user input and initiate the `ResearchManager`.
    - Use a utility class (`Printer`) built with the `rich` library to provide a clean, real-time, in-console display of the agent's progress.
6.  **Running the Agent:** Start the entire asynchronous process with a single call to `asyncio.run(main())`.