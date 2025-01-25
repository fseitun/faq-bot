import sys
import os

# Add project root to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from src.config.settings import FAQ_PATH

def load_documents():
    """Load and split FAQ documents."""
    # Load FAQ PDF or text
    loader = PyPDFLoader(FAQ_PATH)  # Ensure the path is correct
    documents = loader.load()

    # Split into smaller chunks for retrieval
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    print(f"Loaded and split {len(docs)} documents.")
    return docs

# Export 'docs' for other modules
docs = load_documents()

if __name__ == "__main__":
    load_documents() 