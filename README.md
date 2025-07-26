# 💬 LLM Chatbot (Flask + SQLite + OpenAI)

This is a lightweight chatbot application that integrates OpenAI's GPT model via API, using a Flask backend, SQLite for storing chat history, and a simple HTML/JS frontend.

---

## 📌 Features

- Chat with OpenAI's GPT-3.5 model.
- Store chat history in SQLite database.
- Frontend with real-time messaging using Fetch API.
- Flask REST API with `/api/chat` endpoint.
- Easy setup using Docker or local Python environment.

---

## 🗂️ Project Structure

project-root/
│
├── frontend/
│ └── index.html # Simple UI to chat with the bot
│
├── backend/
│ ├── app.py # Flask backend app
│ ├── models.py # SQLAlchemy models (Chat table)
│ ├── requirements.txt # Flask, OpenAI, SQLAlchemy
│ └── .env # Contains OPENAI_API_KEY
│
├── db.sqlite3 # SQLite DB storing chat history
└── README.md

## 🚀 How It Works

### 🔄 Workflow

1. User types message in the **frontend**.
2. Message is sent to Flask backend via `POST /api/chat`.
3. Backend sends the message to **OpenAI ChatCompletion API**.
4. OpenAI generates a response.
5. Both user message and bot response are stored in **SQLite**.
6. Response is sent back to frontend and displayed.

---

## ⚙️ Setup Instructions

### 🧪 Prerequisites

- Python 3.8+
- OpenAI API key (get from: https://platform.openai.com/account/api-keys)

### 📦 Install Dependencies

```bash
cd backend
pip install -r requirements.txt
