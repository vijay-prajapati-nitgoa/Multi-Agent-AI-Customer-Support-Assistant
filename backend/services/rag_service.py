from rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

class RAGService:

    def ask(self, question):

        return rag.ask(question)