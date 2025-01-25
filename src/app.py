from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
from langchain.memory import ConversationBufferMemory

def main():
    # Load embeddings and vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":3})

    # Load LLaMA model
    llm = LlamaCpp(model_path="llama-2-7b-chat.q4_0.bin", n_ctx=2048, temperature=0.7)

    # Set up memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Create the conversational FAQ assistant
    qa_chain = ConversationalRetrievalChain(
        retriever=retriever,
        memory=memory,
        llm=llm
    )

    # Interaction loop
    print("FAQ Assistant is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = qa_chain.run({"question": user_input})
        print(f"Bot: {response}")

if __name__ == "__main__":
    main() 