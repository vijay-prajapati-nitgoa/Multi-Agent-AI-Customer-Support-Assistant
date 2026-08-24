import os
import shutil
import traceback

import fitz
import pytesseract

from PIL import Image

from fastapi import APIRouter, UploadFile, File, HTTPException

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


UPLOAD_DIR = os.path.abspath("uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)


# ---------------------------------------------------------
# TESSERACT CONFIGURATION
# ---------------------------------------------------------

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if os.path.exists(TESSERACT_PATH):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


# ---------------------------------------------------------
# OCR FUNCTION
# ---------------------------------------------------------

def extract_text_with_ocr(pdf_path):

    print()
    print("🔍 Starting OCR...")
    print("📄 PDF:", pdf_path)

    documents = []

    pdf = fitz.open(pdf_path)

    print(
        f"📚 Total pages for OCR: {len(pdf)}"
    )

    for page_number, page in enumerate(pdf):

        print(
            f"🔎 OCR page {page_number + 1}/{len(pdf)}..."
        )

        # Render PDF page as image
        pix = page.get_pixmap(
            matrix=fitz.Matrix(2, 2),
            alpha=False
        )

        # Convert to PIL image
        image = Image.frombytes(
            "RGB",
            [pix.width, pix.height],
            pix.samples
        )

        # OCR
        text = pytesseract.image_to_string(
            image
        )

        text = text.strip()

        if text:

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": pdf_path,
                        "page": page_number + 1
                    }
                )
            )

            print(
                f"   ✅ Text extracted: {len(text)} characters"
            )

        else:

            print(
                "   ⚠️ No text detected on this page"
            )

    pdf.close()

    print()
    print(
        f"✅ OCR completed. Documents created: {len(documents)}"
    )

    return documents


# ---------------------------------------------------------
# UPLOAD ENDPOINT
# ---------------------------------------------------------

@router.post("/")
async def upload_pdf(
    file: UploadFile = File(...)
):

    try:

        print()
        print("=" * 60)
        print("📄 PDF UPLOAD")
        print("=" * 60)

        # -------------------------------------------------
        # CHECK FILE
        # -------------------------------------------------

        if not file.filename:

            raise HTTPException(
                status_code=400,
                detail="No file selected"
            )

        if not file.filename.lower().endswith(".pdf"):

            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed"
            )

        # -------------------------------------------------
        # SAVE FILE
        # -------------------------------------------------

        filename = os.path.basename(
            file.filename
        )

        file_path = os.path.join(
            UPLOAD_DIR,
            filename
        )

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        print(
            "📁 PDF saved at:",
            file_path
        )

        # -------------------------------------------------
        # FIRST TRY NORMAL PDF TEXT EXTRACTION
        # -------------------------------------------------

        print("📖 Reading PDF normally...")

        from langchain_community.document_loaders import PyPDFLoader

        loader = PyPDFLoader(
            file_path
        )

        documents = loader.load()

        print(
            f"📄 Pages loaded: {len(documents)}"
        )

        # -------------------------------------------------
        # REMOVE EMPTY DOCUMENTS
        # -------------------------------------------------

        text_documents = [

            doc

            for doc in documents

            if doc.page_content
            and doc.page_content.strip()

        ]

        print(
            f"📝 Pages containing text: {len(text_documents)}"
        )

        # -------------------------------------------------
        # FALLBACK TO OCR
        # -------------------------------------------------

        if len(text_documents) == 0:

            print()
            print(
                "⚠️ No text extracted from PDF."
            )

            print(
                "🔄 PDF appears to be scanned/image-based."
            )

            print(
                "🔍 Switching to OCR..."
            )

            documents = extract_text_with_ocr(
                file_path
            )

        else:

            documents = text_documents

        # -------------------------------------------------
        # CHECK DOCUMENTS
        # -------------------------------------------------

        if not documents:

            raise HTTPException(

                status_code=400,

                detail=(
                    "Could not extract readable text "
                    "from this PDF. OCR also returned "
                    "no text."
                )

            )

        print(
            f"📚 Documents available: {len(documents)}"
        )

        # -------------------------------------------------
        # CREATE CHUNKS
        # -------------------------------------------------

        print()
        print("✂️ Creating text chunks...")

        splitter = RecursiveCharacterTextSplitter(

            chunk_size=1000,

            chunk_overlap=150

        )

        chunks = splitter.split_documents(
            documents
        )

        # Remove empty chunks
        chunks = [

            chunk

            for chunk in chunks

            if chunk.page_content
            and chunk.page_content.strip()

        ]

        print(
            f"🧩 Chunks created: {len(chunks)}"
        )

        if not chunks:

            raise HTTPException(

                status_code=400,

                detail="No chunks were created from PDF"

            )

        # -------------------------------------------------
        # CREATE EMBEDDINGS
        # -------------------------------------------------

        print()
        print("🧠 Creating embeddings...")

        embedding_model = EmbeddingModel()

        embedding = (
            embedding_model.get_embeddings()
        )

        # -------------------------------------------------
        # CREATE VECTOR STORE
        # -------------------------------------------------

        print()
        print(
            "🔨 Creating FAISS vector database..."
        )

        vector_store = VectorStore(
            embedding
        )

        vector_store.create_vector_store(
            chunks
        )

        # -------------------------------------------------
        # SUCCESS
        # -------------------------------------------------

        print()
        print("=" * 60)
        print("✅ PDF INDEXED SUCCESSFULLY")
        print("=" * 60)

        return {

            "success": True,

            "message":
                "PDF uploaded and indexed successfully",

            "filename":
                filename,

            "documents":
                len(documents),

            "chunks":
                len(chunks)

        }

    except HTTPException:

        raise

    except Exception as e:

        print()
        print("=" * 60)
        print("❌ PDF UPLOAD ERROR")
        print("=" * 60)

        print(
            str(e)
        )

        traceback.print_exc()

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )