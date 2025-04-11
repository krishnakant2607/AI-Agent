# Agenti: LangGraph-Powered AI Chatbot

## Overview

Agenti is a full-stack AI chatbot application that integrates FastAPI and Streamlit for backend and frontend communication. It uses LangGraph's ReAct agent framework to enable intelligent reasoning and response generation. The system supports multiple LLM providers including Groq and OpenAI, and optionally integrates real-time search with Tavily.

## Features

- Built with FastAPI (backend) and Streamlit (frontend)
- Supports multiple model providers:
  - Groq (`gemma2-9b-it`)
  - OpenAI (`gpt-4o-mini`)
- Web-augmented answers via Tavily Search (optional)
- Modular agent design using LangGraph ReAct
- Simple REST API for interaction
- Environment-based API key management (`.env`)

## Requirements

- Python 3.10+
- `pip` or `conda` for package management

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/agenti-chatbot.git
   cd agenti-chatbot
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Unix/macOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory and add the following:
   ```
   GROQ_API_KEY=your_groq_api_key
   OPENAI_API_KEY=your_openai_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

## Running the App

1. **Start the FastAPI backend**
   ```bash
   python backend.py
   ```

2. **Run the Streamlit frontend**
   ```bash
   streamlit run frontend.py
   ```

3. **Access the app**
   Open `http://localhost:8501` in your browser.

## Project Structure

```
.
├── ai_agent.py          # Core agent logic
├── backend.py           # FastAPI backend
├── frontend.py          # Streamlit frontend
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables
```

## API Endpoint

**POST** `/chat`

Request Body:
```json
{
  "model_name": "gemma2-9b-it",
  "model_provider": "groq",
  "system_prompt": "You are a helpful assistant.",
  "messages": ["What is LangGraph?"],
  "allow_search": true
}
```
