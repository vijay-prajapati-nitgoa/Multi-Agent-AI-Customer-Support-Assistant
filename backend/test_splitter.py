from rag.document_loader import DocumentLoader
from rag.text_splitter import TextSplitter

loader = DocumentLoader()

documents = loader.load_documents()

splitter = TextSplitter()

chunks = splitter.split_documents(documents)

print(chunks[0].page_content)