from services.llm_service import LLMService

llm = LLMService()

response = llm.generate("Introduce yourself in one sentence.")

print(response)