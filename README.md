---
title: Finance Agent

colorFrom: blue

colorTo: green

sdk: docker

pinned: false

---

---💰 Finance Intelligence Hybrid-RAG Agent---
A high-performance Financial AI Agent powered by Llama-3.3-70b, utilizing LangGraph for advanced reasoning and Hybrid RAG for combining internal knowledge with real-time web search.
<img width="1468" height="802" alt="image" src="https://github.com/user-attachments/assets/57b760dc-94ed-452b-9c47-3b09829fdc87" />
<img width="1493" height="791" alt="image" src="https://github.com/user-attachments/assets/3f47b6f7-799c-4f58-bf42-73c1b9c99340" />

📽️ Demo
[▶️ Watch Project Demo on Google Drive](https://drive.google.com/file/d/1f6cDOKJekP_kz3fGdzQ36ND4khtmEVW-/view?usp=drive_link)

🚀 Tech Stack :
LLM Inference: Llama-3.3-70b - High-performance inference for complex financial reasoning.

Orchestration: LangGraph - State-of-the-art agentic workflows with self-correction and cyclical logic.

Web Search: Tavily API - Specialized AI search for real-time financial data fetching.

Embeddings: Hugging Face Transformers - Local/Cloud high-dimensional vector embeddings.

Database: Vector Store Service - Efficient storage for RAG retrieval.

API Framework: FastAPI - Modern, asynchronous Python web framework.

Package Management: uv - Ultra-fast Python package installer and resolver.

Infrastructure: Docker & Docker Compose.

✨ Key Features
Hybrid RAG Architecture: Seamlessly switches between internal document retrieval and external web searching via Tavily.


## 🐳 Running with Docker (Recommended)

The fastest way to get the Finance Agent up and running is using Docker. This ensures all dependencies (including `uv` and `Llama-3.3` configurations) work out of the box.

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* Your API Keys (`HF_TOKEN`, `TAVILY_API_KEY`).

### Step-by-Step Guide

1. **Prepare your environment:**
   Create a `.env` file in the root directory and add your keys:
   ```env
   HF_TOKEN=your_huggingface_token
   TAVILY_API_KEY=your_tavily_key

Agentic Thinking: Uses LangGraph to implement a "Think-Act-Observe" loop, ensuring the agent verifies its answers before responding.

Financial Specialized: Optimized for analyzing market trends, financial reports, and real-time news.

Performance First: Built with uv for lightning-fast environment setup and Llama-3.3 for near-GPT-4o intelligence at lower latency.


## 📂 Project Structure

```text
FINANCE-AGENT/
├── app/
│   ├── core/           # Configuration and Loggers
│   ├── ingestion/      # Data loading and Vector store logic
│   └── services/       # LLM services (Llama-3.3) and Tools (Tavily)
├── chroma_db_local/    # Local Vector Database
├── main.py             # Entry point (FastAPI/Gradio)
├── Dockerfile          # Docker configuration
└── pyproject.toml      # Dependency management (uv)




