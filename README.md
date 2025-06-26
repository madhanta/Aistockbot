# 📈 LLM Stock Price Bot

An interactive web app built with Python and Streamlit that uses a **locally hosted Large Language Model (LLM)** to understand natural language queries about stock prices and visualize them with elegant Plotly charts.

High-Level Architecture

        ┌────────────────────┐
        │    User Prompt     │
        └────────┬───────────┘
                 ↓
        ┌─────────────────────┐
        │  🧠 AI Agent (LLM)  │  ←  host this locally (e.g., LLaMA 3)
        │  - Understand prompt│
        │  - Extract ticker   │
        │  - Extract intent   │
        └────────┬────────────┘
                 ↓
       ┌─────────────────────────┐
       │  Query Handler / Logic  │
       │ - Use yfinance API      │
       │ - Fetch stock data      │
       └────────┬-───────────────┘
                ↓
       ┌─────────────────────────┐
       │ Streamlit UI & Charts   │
       └─────────────────────────┘


![image](https://github.com/user-attachments/assets/2dd9448f-2bc9-48ad-8579-d56a5904dbb6)
---

## 🔍 Features

- 💬 Natural language input (e.g. "Show me Apple stock for last 5 days")
- 🧠 Local LLM parsing via [Ollama](https://ollama.com/) using `llama3`
- 📊 Interactive price charts powered by Plotly
- 🔘 Built-in chart range selector (1D, 5D, 1M, 6M, YTD)
- 📈 Price + percentage change indicator
- 🌙 Dark themed UI for a clean, professional look

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
- [yFinance](https://github.com/ranaroussi/yfinance)
- [Ollama](https://ollama.com/) for local LLM

---

## 🚀 Installation

### 🧱 Prerequisites

- A medium configuration machine with atleast 8 GB of Memory (i used Apple Macbook Air with M1 chip)
- Python 3.9+
- Ollama with `llama3` model installed
- Streamilit (Web App Framework for Python)

### 📦 Setup

# 1. create directory (aigentor Clone the repository, open the terminal and switch to the directory 
cd aiagent

# 2. Create a virtual environment and activate 
- /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" (to install brew)
- brew install python
- python3 -m venv stockbot-env
- source stockbot-env/bin/activate

# 3. Install dependencies
pip install streamlit yfinance plotly requests

# 4. Install LLM (example - ollama)

- brew install ollama
- ollama pull llama3 (i used llama3:instruct	as it requires less resources)
- ollama run llama3 (a pop up appears for you to select your choice to run it either as a background service or as a interactive process)
# this will start ollama api server running at http://localhost:11434

# 5. AI Agent for handling NLP from user chat box
- stock_bot.py # from the repo 
- streamlit run stock_bot.py

# starts the app in browser at http://localhost:8501
