# 📈 StockTradingNewsAlert

> Automated AI-based news and stock summarizer with SMS alerts — stay ahead of the market without constantly watching the screen.

## 📌 About

Are you actively trading stocks but tired of constantly monitoring prices, news, and trends?  
**StockTradingNewsAlert** is a fully automated Python solution that leverages real-time APIs, machine learning models, and SMS integration to keep you informed effortlessly.

With this tool, you can receive AI-generated summaries of news and stock changes for selected companies directly via **SMS**, or in any other output format you prefer.

---

## 🚀 Key Features

- 📊 **Alpha Vantage API** — Retrieves real-time stock data for your selected companies
- 📰 **News API** — Gathers the 3 most relevant articles per company, sorted by popularity
- 🤖 **Hugging Face / OpenAI** — Uses the LLaMA 3.2 model to summarize and combine news + stock data into human-readable insights
- 📱 **Twilio API** — Sends you daily SMS alerts with AI-curated summaries
- 🕒 **PythonAnywhere Deployment** — Automatically runs daily at your preferred time

---

## 🔁 Workflow

1. `stock.json` contains the list of stock tickers to track.
2. For each company:
   - Fetch stock data using **Alpha Vantage** (`alpha_vantage_api.py`)
   - Retrieve related news articles using **News API** (`news_api.py`)
   - Keep only top 3 articles based on popularity.
3. Combine both sources into a single prompt and send it to **OpenAI/Hugging Face LLaMA 3.2** (`hugging_face_api.py`).
4. Collect AI-generated summaries for each company.
5. Send all results via **SMS using Twilio** (`twilio_provider.py`).
6. Everything is scheduled and hosted on **PythonAnywhere**, ensuring daily delivery without user interaction.

---

## 📦 Requirements

- Python 3.9+
- `requests`, `openai`, `transformers`, `twilio`, `schedule`, `dotenv`, etc.
- API keys for:
  - [Alpha Vantage](https://www.alphavantage.co/)
  - [News API](https://newsapi.org/)
  - [OpenAI / Hugging Face](https://huggingface.co/)
  - [Twilio](https://www.twilio.com/)
  - [PythonAnywhere](https://www.pythonanywhere.com/) (for deployment)

## 💡 Motivation
I actively trade stocks but found it exhausting to track real-time movements and financial news every day.
So I built this automated solution to combine the best of stock data, relevant news, and AI summarization — and now I just read an SMS in the morning. Simple.

## 📬 Example Output (SMS format)
📈 TSLA Update:
Tesla stock rose 3.2% yesterday. Top headline: "Tesla expands into India market." Analysts optimistic about growth potential.
📈 AAPL Update:
Apple dropped -1.4%. News highlights delays in iPhone 16 production. Model suggests short-term volatility.


