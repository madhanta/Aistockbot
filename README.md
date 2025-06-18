# 📈 LLM Stock Price Bot

An interactive web app built with Python and Streamlit that uses a **locally hosted Large Language Model (LLM)** to understand natural language queries about stock prices and visualize them with elegant Plotly charts.

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

- A medium config machine with atleast 8 GB of Mem (depends on LLM Model)
- Python 3.9+
- Ollama with `llama3` model installed
- Streamilit

### 📦 Setup

# 1. Clone the repository, open the terminal and switch to the directory 
cd llm-stock-bot

# 2. (Optional but recommended) Create a virtual environment
python3 -m venv stockbot-env
source stockbot-env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
