import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Embeddings
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# LLaMA Model
LLAMA_MODEL_PATH = os.path.join(BASE_DIR, "llama-2-7b-chat.q4_0.bin")
LLAMA_N_CTX = 2048
LLAMA_TEMPERATURE = 0.7

# Chroma DB
CHROMA_PERSIST_DIRECTORY = os.path.join(BASE_DIR, "chroma_db")

# FAQ Data
FAQ_PATH = os.path.join(BASE_DIR, "data", "faq.pdf")
