# Update imports based on the new LangChain module structure
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import os


# Create a simple prompt template for conversation
template = "You are a helpful assistant. User: {input}. Assistant:"

# Define the prompt template
prompt = ChatPromptTemplate.from_template(template)

# Initialize the language model (OpenAI in this case)
model = OllamaLLM(model="llama3.1")

# Create an LLMChain with the prompt template
chain = prompt | model

# Start a simple text-based conversation loop
print("Chatbot is running! Type 'exit' to stop.")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Generate response using LangChain
    response = chain.invoke({"input": user_input})

    # Print the assistant's response
    print(f"Assistant: {response}")
