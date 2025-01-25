from langchain.llms import LlamaCpp

# Load the LLaMA model
llm = LlamaCpp(model_path="llama-2-7b-chat.q4_0.bin", n_ctx=2048, temperature=0.7)

print("LLaMA 2 model loaded successfully.") 