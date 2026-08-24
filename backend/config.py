MONGODB_URL = "mongodb://localhost:27017"
DATABASE_NAME = "customer_support_ai"

SECRET_KEY = "customer_support_secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

OLLAMA_MODEL = "gemma3:1b"
TEMPERATURE = 0.2

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

KNOWLEDGE_BASE_PATH = "../knowledge_base"
VECTOR_DB_PATH = "./vector_db/faiss_index"