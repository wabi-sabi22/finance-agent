from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

def load_pdfs(directory_path: str):
    """Load all PDF files from a specific directory."""
    loader = DirectoryLoader(directory_path, glob="./*.pdf", loader_cls=PyPDFLoader)
    return loader.load()