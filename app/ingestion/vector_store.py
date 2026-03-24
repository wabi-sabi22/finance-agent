import shutil
import os
from langchain_chroma import Chroma

def create_vector_store(chunks, embeddings, persist_dir):
    """Handle persistence and cleanup of the vector database."""
    if os.path.exists(persist_dir):
        shutil.rmtree(persist_dir)
    
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )