# 🚀 AI/LLM Engineering Week 1 HW - PSI AI Academy

Welcome to the **AI/LLM Engineering Bootcamp** by **PSI AI Academy**!  
This repository contains hands-on notebooks, source code, and resources to help you get started with **Large Language Models (LLMs)**, **prompt engineering**, and **building AI-powered applications** using OpenAI's GPT models.

---

## 📁 Repository Overview

```
ai_llm_engineering_psi_ai_academy/
├── day_1/
│   └── Hello_LLM.ipynb      # Intro to LLMs and basic prompt engineering
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/OneRenix/ai_llm_engineering_psi_ai_academy.git
cd ai_llm_engineering_psi_ai_academy
```

### 2. Set Up Your Environment Using [UV](https://github.com/astral-sh/uv)

[UV](https://github.com/astral-sh/uv) is a lightning-fast Python package manager and environment tool.

```bash
# Install UV if not installed
pip install uv

# Create and activate a virtual environment
uv venv .venv
uv pip install -r requirements.txt
uv sync
```

### 3. Configure Your OpenAI API Key

- Sign in or create an account at [platform.openai.com](https://platform.openai.com/)
- Generate an API key
- Paste it into the notebook when prompted (or load via environment variable)

---

## 📓 Running the Notebook

- Open `day_1/Hello_LLM.ipynb`
- Follow the instructions in each cell
- Experiment with the prompts and outputs!

---

## 🧠 What You’ll Learn

By the end of this session, you’ll have hands-on experience with:

- 🌐 Interacting with OpenAI’s GPT models via API
- 🧩 Prompt engineering fundamentals (zero-shot, few-shot, CoT, etc.)
- 💬 Chat-based architecture using system/user/assistant roles
- 🛠️ Building simple LLM-based tools and apps
- 🧪 Exploring model reasoning and response control

---

## 🛠️ Optional: Push to Your Own GitHub Repository

To push your changes on your own github repo:

```bash
echo "# ai-llm-engineering_psi_ai" >> README.md
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

---

## 🙌 Credits

Developed by **PSI AI Academy**, with inspiration from **AI Makerspace** and the broader LLM research community.

---

## 💬 Questions or Feedback?

Open an issue in this repository or reach out to the PSI AI Academy team.  
We’re here to support your learning journey!

---

Happy building with LLMs! ✨
