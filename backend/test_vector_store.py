from rag.document_loader import DocumentLoader
from rag.text_splitter import TextSplitter
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore

# Load documents
loader = DocumentLoader()
documents = loader.load_documents()

# Split documents
splitter = TextSplitter()
chunks = splitter.split_documents(documents)

# Create embeddings
embedding = EmbeddingModel().get_embeddings()

# Create FAISS vector database
vector_store = VectorStore(embedding)

db = vector_store.create_vector_store(chunks)

print("Total Chunks:", len(chunks))
print("FAISS Index Created Successfully!")