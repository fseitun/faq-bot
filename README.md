# FAQ Assistant

A conversational FAQ assistant built using free LLMs and embeddings.

## Features

- **Embeddings**: Utilizes SentenceTransformers for generating vector embeddings.
- **Retrieval**: Uses Chroma for efficient similarity search.
- **LLM Processing**: Implements LLaMA 2 for generating responses.
- **Memory**: Maintains conversation context for multi-turn interactions.

## Setup Instructions

### 1. Create and Activate Virtual Environment

Ensure you have Python 3.8 or higher installed.

```bash
python3 -m venv env --upgrade-deps
source env/bin/activate
```

### 2. Install Dependencies

It's recommended to pin package versions for reproducibility.

```bash
pip install -r requirements.txt
```

### 3. Prepare FAQ Data

- **Place your `faq.pdf`** in the `src/data/` directory. Make sure the file is named `faq.pdf` (or change the file name in `src/config/settings.py`).

- **Load and Split the FAQ Documents:**

```bash
python -m src.data.load_faq
```

### 4. Set Up Embeddings

```bash
python -m src.embeddings.setup_embeddings
```

### 5. Download LLaMA 2 Model

- **Download the `llama-2-7b-chat.q4_0.bin` model** from [Hugging Face](https://huggingface.co/models?search=llama).
- **Place the model file** in the location specified by `src/config/settings.py`. By default, it should be in the project root directory.

### 6. Run the Application

```bash
python -m src.app
```

## Usage

Interact with the FAQ Assistant in the terminal:

```bash
You: What is your return policy?
Bot: Our return policy allows returns within 30 days of purchase. Please ensure that the items are in original condition.
```

Type `exit` to quit the application.

## Configuration

Configurations are managed in `src/config/settings.py`. You can modify paths and parameters as needed. Alternatively, you can use environment variables for configuration by creating a `.env` file in the project root:

```bash
EMBEDDING_MODEL_NAME=sentence-transformers/all-MiniLM-L6-v2
LLAMA_MODEL_PATH=llama-2-7b-chat.q4_0.bin
LLAMA_N_CTX=2048
LLAMA_TEMPERATURE=0.7
CHROMA_PERSIST_DIRECTORY=chroma_db
FAQ_PATH=src/data/faq.pdf
```

Ensure to install `python-dotenv` if you choose to manage configurations via environment variables.

## Testing

Add your test cases in the `tests/` directory and run them using your preferred testing framework, such as `pytest`:

```bash
pytest tests/
```
