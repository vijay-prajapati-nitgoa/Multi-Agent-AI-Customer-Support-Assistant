from rag.rag_pipeline import RAGPipeline


class BaseAgent:

    def __init__(self, rag_pipeline):

        self.rag = rag_pipeline

    def ask(self, system_prompt, user_query):

        return self.rag.answer(
            user_query,
            system_prompt
        )