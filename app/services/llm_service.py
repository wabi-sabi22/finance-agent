import os
from langchain_groq import ChatGroq

class LLMService:
    def __init__(self):
        self._model = None

    def get_model(self):
        """Initialize and return the LLM instance (Singleton pattern)."""
        if self._model is None:
            # Using Llama-3.3-70b for high-performance inference
            self._model = ChatGroq(
                model_name="llama-3.3-70b-versatile",
                groq_api_key=os.getenv("GROQ_API_KEY"),
                temperature=0.1,
                max_tokens=800
            )
        return self._model

llm_service = LLMService()