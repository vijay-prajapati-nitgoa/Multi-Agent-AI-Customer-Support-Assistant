from rag.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve("What is a database?")

print("=" * 60)

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 60)
    print(doc.page_content)