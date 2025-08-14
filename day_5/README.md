# Advanced Retrieval and Synthetic Data Generation

This contains two Jupyter notebooks that explore advanced retrieval techniques and synthetic data generation for evaluating RAG pipelines.

## Notebooks

### 1. `1-advanced_retrievers.ipynb`

This notebook provides a hands-on guide to various advanced retrieval methods available in LangChain. It uses a dataset of loan complaints to demonstrate and compare the following techniques:

-   **Naive Retrieval:** A baseline similarity search.
-   **BM25:** A keyword-based retrieval method.
-   **Multi-Query Retrieval:** Using an LLM to generate multiple queries from the user's original query.
-   **Parent-Document Retrieval:** A "small-to-big" strategy that searches over smaller chunks but returns larger parent documents.
-   **Contextual Compression (Reranking):** Using a reranker (Cohere's Rerank model) to compress and refine retrieved documents.
-   **Ensemble Retrieval:** Combining multiple retrievers to leverage the strengths of each.
-   **Semantic Chunking:** Splitting documents based on semantic similarity.

The notebook concludes with an activity to evaluate these retrieval strategies using the Ragas framework to assess their performance, cost, and latency.

### 2. `2-SDG.ipynb`

This notebook focuses on Synthetic Data Generation (SDG) to create a "golden dataset" for evaluating RAG systems. It uses a collection of PDF documents related to AI regulation bills. The key steps covered are:

-   **Data Loading:** Loading PDF documents using `PyMuPDFLoader`.
-   **Knowledge Graph Creation:** Building a knowledge graph from the documents using Ragas.
-   **Test Set Generation:** Synthesizing a test set of questions, answers, and contexts from the knowledge graph. This includes single-hop and multi-hop questions.
-   **LangSmith Integration:** Creating a dataset in LangSmith from the generated test set.
-   **RAG Pipeline Evaluation:** Setting up and evaluating a RAG pipeline using the generated dataset on LangSmith. The notebook also includes the results of evaluating different retrievers.

## How to Use

1.  Install the required dependencies from `pyproject.toml`.
2.  Open and run the Jupyter notebooks to explore the different techniques.
3.  You will need API keys for OpenAI, Cohere, and LangChain (LangSmith).