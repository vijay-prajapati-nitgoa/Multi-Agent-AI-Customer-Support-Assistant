import os

from langchain_community.vectorstores import FAISS

from config import VECTOR_DB_PATH


class VectorStore:

    def __init__(self, embedding):

        self.embedding = embedding

    def create_vector_store(self, chunks):

        print("\n")
        print("=" * 60)
        print("CREATING FAISS VECTOR DATABASE")
        print("=" * 60)

        if not chunks:

            raise ValueError(
                "No chunks received."
            )

        print(
            "Number of chunks:",
            len(chunks)
        )

        os.makedirs(
            VECTOR_DB_PATH,
            exist_ok=True
        )

        db = FAISS.from_documents(
            chunks,
            self.embedding
        )

        db.save_local(
            VECTOR_DB_PATH
        )

        print(
            "FAISS database created successfully."
        )

        print(
            "Location:",
            os.path.abspath(
                VECTOR_DB_PATH
            )
        )

        index_file = os.path.join(
            VECTOR_DB_PATH,
            "index.faiss"
        )

        pkl_file = os.path.join(
            VECTOR_DB_PATH,
            "index.pkl"
        )

        print(
            "index.faiss:",
            os.path.exists(index_file)
        )

        print(
            "index.pkl:",
            os.path.exists(pkl_file)
        )

        return db

    def load_vector_store(self):

        path = os.path.abspath(
            VECTOR_DB_PATH
        )

        print(
            "\nLooking for FAISS database at:"
        )

        print(path)

        if not os.path.exists(path):

            print(
                "FAISS directory does not exist."
            )

            return None

        index_file = os.path.join(
            path,
            "index.faiss"
        )

        pkl_file = os.path.join(
            path,
            "index.pkl"
        )

        if not os.path.exists(index_file):

            print(
                "index.faiss does not exist."
            )

            return None

        if not os.path.exists(pkl_file):

            print(
                "index.pkl does not exist."
            )

            return None

        print(
            "FAISS database found."
        )

        try:

            db = FAISS.load_local(
                path,
                self.embedding,
                allow_dangerous_deserialization=True
            )

            print(
                "FAISS database loaded successfully."
            )

            try:

                print(
                    "FAISS VECTOR COUNT:",
                    db.index.ntotal
                )

            except Exception:
                pass

            return db

        except Exception as e:

            print(
                "FAISS LOAD ERROR:"
            )

            print(e)

            return None