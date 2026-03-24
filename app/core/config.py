import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Finance Agentic RAG"
    
    # API Keys extracted from environment variables
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY")
    
    # Vector DB Configuration
    CHROMA_DB_DIR: str = "./chroma_db"
    DATA_DIR: str = "./data"

settings = Settings()