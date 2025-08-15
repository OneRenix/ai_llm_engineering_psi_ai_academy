# AI/LLM Engineering Course

This repository contains Python notebooks and supplementary materials for the PSI AI Academy's course on AI/LLM Engineering. Designed as a hands-on companion to the lectures, it provides practical guides, examples, and resources for building, evaluating, and deploying LLM-powered applications.

## Folder Structure

Course content is organized by day/module:

- `day_1/`: Introduction to Large Language Models (LLMs) and prompt engineering.
- `day_3/`: Retrieval-Augmented Generation (RAG), covering basic and production systems.
- `day_4/`: Evaluation of RAG systems and synthetic data generation.
- `day_5/`: Advanced retrieval techniques and synthetic data generation for RAG evaluation.
- `day_6/`: Agentic architectures using LangGraph and OpenAI Agents SDK.

## How to Use

To work with the course materials:

1. **Navigate to the day's folder.**
    ```bash
    cd day_1
    ```
2. **Install dependencies.** This project uses [`uv`](https://github.com/astral-sh/uv) for package management:
    ```bash
    uv sync
    ```
3. **Explore the notebooks.** Launch Jupyter Notebook or your preferred IDE to open the `.ipynb` files.

---

## Module Overview

### Day 1: Introduction to LLMs and Prompt Engineering

- **Core Concepts:** Learn to interact with OpenAI GPT models via API.
- **Prompt Engineering:** Build effective prompts, including zero-shot, few-shot, and chain-of-thought (CoT) strategies.
- **Chat Architecture:** Understand system, user, and assistant roles in chat-based LLMs.
- **Application Building:** Create simple LLM-based tools and applications.
- **Model Reasoning:** Explore techniques for controlling and interpreting model responses.

---

### Day 2: *(No Content)*

---

### Day 3: Retrieval-Augmented Generation (RAG)

- **Basic RAG:** Introduction to retrieval-augmented generation principles.
- **Productionized RAG:** Build and deploy robust RAG pipelines using LangChain and LangSmith for monitoring and evaluation.

---

### Day 4: Evaluating RAG and Synthetic Data Generation

- **RAG Evaluation:** Assess RAG pipeline performance and reliability.
- **Synthetic Data Generation:** Use LangChain to generate test datasets for RAG evaluation.
- **RAGAS Framework:** Apply the RAGAS framework for systematic RAG system evaluation.

---

### Day 5: Advanced Retrieval and Synthetic Data Generation

Two notebooks guide you through advanced retrieval techniques and synthetic data generation for RAG pipeline evaluation:

1. **Advanced Retrievers**
   - Demonstrates advanced retrieval methods in LangChain using a loan complaints dataset:
     - Naive Retrieval, BM25, Multi-Query, Parent-Document, Contextual Compression (Cohere Rerank), Ensemble Retrieval, Semantic Chunking.
   - Includes an activity to evaluate retrieval strategies with the Ragas framework, comparing performance, cost, and latency.

2. **Synthetic Data Generation (SDG)**
   - Focuses on generating "golden datasets" for RAG evaluation using PDF documents on AI regulation bills:
     - Data loading (PyMuPDFLoader), knowledge graph creation (Ragas), test set synthesis (single-hop and multi-hop questions), LangSmith integration.
   - Shows how to set up and evaluate RAG pipelines with the generated datasets and compare retriever performance.

---

### Day 6: Agentic Architectures with LangGraph and OpenAI Agents

Learn how to build stateful, multi-agent applications using LangGraph and the OpenAI Agents SDK:

1. **LangGraph**
   - Introduction to LangGraph for multi-agent LLM applications.
   - Covers graph-based architecture: State, Nodes, Edges.
   - Includes a chatbot example that remembers conversation history.

2. **OpenAI Agents**
   - Demonstrates the OpenAI Assistants API for agentic workflows.
   - Step-by-step creation of an Assistant, Thread, Message, and running the Assistant.
   - Example: A "Math Tutor" assistant that solves math problems.

---

## Requirements & Setup

- Install dependencies using `uv sync`.
- API keys required for OpenAI, Cohere, and LangChain/LangSmith (see notebook instructions).
- Notebooks are self-contained and can be run in sequence or individually.

## Contribution

Want to improve or extend the course? Pull requests and issues are welcome!

---
