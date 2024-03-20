from llama_index.llms.ollama import Ollama

llm = Ollama(model="mistral")
response = llm.complete("Who is Paul Graham?")
print(response)

