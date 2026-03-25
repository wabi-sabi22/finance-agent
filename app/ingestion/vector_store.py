from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_chroma import Chroma
import os

class VectorService:
    def __init__(self):
        
        
        self.hf_token = os.getenv("HF_TOKEN")
        
        if not self.hf_token:
            print("⚠️ CẢNH BÁO: Chưa tìm thấy HF_TOKEN trong Secrets!")

        self.embeddings = HuggingFaceInferenceAPIEmbeddings(
            api_key=self.hf_token,
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.persist_directory = "chroma_db"

    def get_relevant_docs(self, query: str, k: int = 2):
        if not os.path.exists(self.persist_directory):
            print(f"⚠️ Thư mục {self.persist_directory} không tồn tại!")
            return []
        
        vector_db = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings
        )
        return vector_db.similarity_search(query, k=k)