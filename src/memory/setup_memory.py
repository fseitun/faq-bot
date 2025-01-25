from langchain.memory import ConversationBufferMemory

# Set up memory for tracking chat history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

print("Conversational memory set up successfully.") 