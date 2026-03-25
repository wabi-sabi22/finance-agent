import os
from app.core.config import settings
from app.core.logger import agent_logger
from app.services.vector_service import VectorService
from app.ingestion.loader import load_pdfs
from app.ingestion.splitter import split_documents
from app.ingestion.vector_store import create_vector_store

def run_ingestion():
    """
    Main pipeline to convert raw PDFs into a searchable Vector Database.
    """
    agent_logger.info("--- STARTING DATA INGESTION PROCESS ---")
    
    # 1. Load: Check directory and read all PDF files
    if not os.path.exists(settings.DATA_DIR) or not os.listdir(settings.DATA_DIR):
        agent_logger.error(f"Data directory {settings.DATA_DIR} is empty!")
        return
    
    documents = load_pdfs(settings.DATA_DIR)
    agent_logger.info(f"Successfully loaded {len(documents)} document pages.")

    # 2. Split: Breakdown long text into manageable chunks
    
    chunks = split_documents(documents, chunk_size=1000, chunk_overlap=200)
    agent_logger.info(f"Text split into {len(chunks)} chunks for better retrieval.")

    # 3. Store: Initialize embeddings and save to ChromaDB
    
    vector_svc = VectorService()
    create_vector_store(
        chunks=chunks, 
        embeddings=vector_svc.embeddings, 
        persist_dir=settings.CHROMA_DB_DIR
    )
    
    agent_logger.info("--- INGESTION COMPLETED: Vector DB is ready ---")

if __name__ == "__main__":
    run_ingestion()