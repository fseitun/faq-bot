from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from src.data.load_faq import docs  # Updated import path

# Use SentenceTransformers for embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create a vector database
db = Chroma.from_documents(docs, embeddings, persist_directory="chroma_db")

# Save the database for later use
db.persist()
print("Embeddings setup complete and database persisted.") 