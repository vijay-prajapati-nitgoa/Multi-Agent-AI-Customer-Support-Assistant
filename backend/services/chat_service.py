from agents.router import AgentRouter
from agents.response_generator import ResponseGenerator
from rag.rag_pipeline import RAGPipeline
from database.chat_history import save_chat


class ChatService:

    def __init__(self):
        self.router = AgentRouter()
        self.rag = RAGPipeline()
        self.response = ResponseGenerator()

    def process_message(self, session_id, message):

        # Detect which agent should answer
        agent = self.router.detector.detect(message)

        # Get answer from RAG
        answer = self.rag.answer(message)

        # Save chat history in MongoDB
        save_chat(session_id, message, answer)

        return {
            "agent": agent,
            "status": "success",
            "response": answer
        }