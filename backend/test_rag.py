from rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

response = rag.answer("What is a database?")

print(response)