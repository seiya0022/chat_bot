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

.
├── backend/
│ ├── backend_api.py # Flask API server
│ ├── requirements.txt # Backend dependencies
├── frontend/
│ ├── frontend_app.py # Streamlit app
│ ├── requirements.txt # Frontend dependencies
├── db/
│ └── init.sql # Optional: Initial SQL setup
├── docker-compose.yml # Compose file to orchestrate everything
├── .env # API key for OpenAI
└── README.md