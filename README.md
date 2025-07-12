# 🧠 Streamlit Chatbot with OpenAI API + PostgreSQL

A simple yet powerful chatbot app built with:

- 🧠 OpenAI ChatGPT API
- 🌐 Flask (Backend)
- 📦 Streamlit (Frontend)
- 🗃️ PostgreSQL (Database)
- 🐳 Docker + Docker Compose

This chatbot remembers previous conversations by storing them in a database and supports clearing chat history.

---

## 📁 Project Structure
```
.
├── backend/
│ ├── backend_api.py       # Flask API server
│ ├── requirements.txt     # Backend dependencies
├── frontend/
│ ├── frontend_app.py      # Streamlit app
│ ├── requirements.txt     # Frontend dependencies
├── db/
│ └── init.sql             # Database: Initial SQL setup
├── docker-compose.yml     # Compose file to orchestrate everything
├── .env                   # API key for OpenAI
└── README.md
```


---

## 🚀 Features

- Conversational UI powered by **Streamlit**
- Server-side response handling using **Flask**
- Memory persistence using **PostgreSQL**
- Chat history loaded on startup
- `Clear chat` button that clears both local and DB history
- Fully containerized for portability

---

## 🔧 Getting Started

### 1. Prerequisites

- Docker
- Docker Compose
- OpenAI API key (you can get one from https://platform.openai.com)

### 2. Setup

Create `.env` file at the **backend directory** :
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Run the App
```
docker-compose up
```
🖥️ Frontend: http://localhost:8501

🔙 Backend API: http://localhost:5000

🗃️ PostgreSQL: port 5434 (exposed for tools like DBeaver)