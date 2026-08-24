from rag.vector_store import VectorStore
from rag.embeddings import EmbeddingModel


class Retriever:

    def __init__(self):
        print("\n" + "=" * 60)
        print("INITIALIZING RETRIEVER")
        print("=" * 60)

        self.embedding = EmbeddingModel().get_embeddings()

        self.vector_store = VectorStore(
            self.embedding
        )

        self.db = None

        self.reload()

    def reload(self):

        print("\nRELOADING FAISS DATABASE")

        try:

            self.db = self.vector_store.load_vector_store()

            if self.db is None:
                print("NO FAISS DATABASE LOADED")
            else:
                print("FAISS DATABASE LOADED SUCCESSFULLY")

                try:
                    print(
                        "FAISS DOCUMENT COUNT:",
                        self.db.index.ntotal
                    )
                except Exception:
                    pass

        except Exception as e:

            print("ERROR LOADING FAISS:")
            print(e)

            self.db = None

    def retrieve(self, query, k=4):

        print("\n" + "=" * 60)
        print("RETRIEVING DOCUMENTS")
        print("=" * 60)

        print("QUERY:", query)

        # Always reload latest FAISS database.
        self.reload()

        if self.db is None:

            print("ERROR: DB IS NONE")

            return []

        try:

            print("Searching FAISS...")

            results = self.db.similarity_search_with_score(
                query,
                k=k
            )

            print(
                "NUMBER OF RESULTS:",
                len(results)
            )

            documents = []

            for i, (doc, score) in enumerate(results):

                print("\n-----------------------------")
                print("RESULT:", i + 1)
                print("SCORE:", score)
                print("METADATA:", doc.metadata)
                print("TEXT:")

                print(
                    doc.page_content[:1000]
                )

                if doc.page_content.strip():

                    documents.append(doc)

            print("\nFINAL DOCUMENT COUNT:")
            print(len(documents))

            return documents

        except Exception as e:

            print("\nFAISS SEARCH ERROR:")
            print(e)

            return []