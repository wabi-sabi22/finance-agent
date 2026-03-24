
🏦 Finance Intelligence RAG Agent (Llama & Web-Enhanced)
📌 Project Overview
The Finance Intelligence Agent is a sophisticated Agentic RAG (Retrieval-Augmented Generation) system designed to provide expert financial advice. The core innovation lies in its autonomous decision-making engine, which intelligently bridges the gap between static internal knowledge bases (PDFs) and the dynamic, real-time pulse of the Internet.

⚡ Real-time Web Intelligence
Financial data is highly volatile. This agent is equipped with an "adaptive brain" to harness the power of the web:

Heuristic-Driven Retrieval: Unlike naive RAG systems, this agent uses Heuristic Logic to detect knowledge gaps. It triggers web searches only when necessary—such as for the latest bank interest rates, competitor comparisons, or newly updated financial policies.

Multi-Source Synthesis: Integrated with Tavily Search API, the agent crawls high-authority financial news and official bank portals to extract verified, up-to-the-minute data.

Intelligent Data Distillation: Web content undergoes rigorous Normalization and Context-Aware Truncation to ensure it fits perfectly within the Llama model's context window without sacrificing accuracy.

🛠 Tech Stack & Detailed Architecture
Core Stack
LLM Engine: Llama API (optimized for complex logical reasoning and natural Vietnamese/English dialogue).

Embeddings: sentence-transformers/all-MiniLM-L6-v2 (HuggingFace) for high-dimensional semantic vector mapping.

Orchestration: LangGraph (State Machine framework).

Environment: UV (Lightning-fast Python package manager) & Docker.

System Architecture
The system is built on a Stateful Graph architecture, ensuring predictable and reliable agent behavior:

Intent Classification Layer:
Utilizes a specialized detect_mode function to classify user queries into domains: Savings, Credit Cards, Loans, or General Finance. This adjusts the system's "persona" and retrieval strategy dynamically.

Context Augmentation (Hybrid RAG):

Internal Retrieval: Queries ChromaDB for specialized financial documents (PDFs).

Grounding Logic: The heuristic_need_web module analyzes the internal context. If information is insufficient or outdated, it autonomously spawns a web search task.

Refined Generation (Prompt Engineering):
The response engine uses a No-Link UX Strategy. While the agent processes URLs for grounding, the final output is a clean, professional financial summary with numerical examples and risk assessments, removing technical clutter (like raw URLs) for a superior user experience.

State Management:
Leverages LangGraph's AgentState to maintain conversation history and internal summaries, preventing "memory loss" during complex, multi-turn financial consultations.