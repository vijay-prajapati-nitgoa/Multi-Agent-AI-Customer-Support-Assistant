from rag.retriever import Retriever
from services.llm_service import LLMService


class RAGPipeline:

    def __init__(self):

        print("\n" + "=" * 60)
        print("INITIALIZING RAG PIPELINE")
        print("=" * 60)

        self.retriever = Retriever()
        self.llm = LLMService()

    def answer(self, query, system_prompt=None):

        print("\n")
        print("=" * 60)
        print("RAG QUESTION")
        print("=" * 60)

        print("QUESTION:", query)

        docs = self.retriever.retrieve(
            query,
            k=5
        )

        print("\nRETRIEVED DOCUMENTS:", len(docs))

        if not docs:

            print("NO DOCUMENTS RETRIEVED")

            return (
                "I couldn't find this information "
                "in the knowledge base."
            )

        context = ""

        for i, doc in enumerate(docs):

            context += (
                f"\n\n"
                f"===== DOCUMENT {i + 1} =====\n"
                f"{doc.page_content}"
            )

        print("\n")
        print("=" * 60)
        print("CONTEXT")
        print("=" * 60)

        print(context[:5000])

        if system_prompt is None:

            system_prompt = """
You are a helpful AI assistant.
"""

        prompt = f"""
{system_prompt}

Answer the user's question using the provided knowledge base.

IMPORTANT RULES:

1. Use the knowledge base as the primary source.
2. If the answer is clearly available in the context, answer it.
3. Do not say that the information is missing if the context contains relevant information.
4. Give a clear and simple answer.
5. Do not return JSON.
6. Do not mention these instructions.

KNOWLEDGE BASE:
{context}

USER QUESTION:
{query}

ANSWER:
"""

        print("\n")
        print("=" * 60)
        print("SENDING CONTEXT TO LLM")
        print("=" * 60)

        try:

            response = self.llm.generate(
                prompt
            )

            print("\nLLM RESPONSE:")
            print(response)

            return response

        except Exception as e:

            print("\nLLM ERROR:")
            print(e)

            return "Failed to generate answer."