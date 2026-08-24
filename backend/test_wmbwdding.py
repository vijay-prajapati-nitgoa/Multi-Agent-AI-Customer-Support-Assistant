from rag.embeddings import EmbeddingModel

embedding = EmbeddingModel().get_embeddings()

vector = embedding.embed_query("Hello World")

print("Vector Length:", len(vector))

print(vector[:10])