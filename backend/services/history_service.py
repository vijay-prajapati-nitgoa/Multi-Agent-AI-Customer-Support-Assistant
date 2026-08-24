from rag.rag_pipeline import RAGPipeline


class ChatService:

    def __init__(self):

        self.rag = RAGPipeline()

    def process_message(
        self,
        message: str
    ):

        answer = self.rag.answer(
            message
        )

        return answer