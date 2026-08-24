import os
import fitz
import pytesseract

from PIL import Image
from io import BytesIO

from langchain_core.documents import Document


TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if os.path.exists(TESSERACT_PATH):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def load_pdf(pdf_path):

    print("\n" + "=" * 60)
    print("📄 PDF PROCESSING")
    print("=" * 60)

    print("📁 PDF:", pdf_path)

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(
            f"PDF not found: {pdf_path}"
        )

    pdf = fitz.open(pdf_path)

    print("📄 Total pages:", len(pdf))

    documents = []

    for page_number, page in enumerate(pdf):

        print(
            f"📖 Processing page "
            f"{page_number + 1}/{len(pdf)}"
        )

        text = page.get_text("text").strip()

        if not text:

            print(
                f"🔍 No text found on page "
                f"{page_number + 1}. Running OCR..."
            )

            pix = page.get_pixmap(
                matrix=fitz.Matrix(2, 2)
            )

            image_bytes = pix.tobytes("png")

            image = Image.open(
                BytesIO(image_bytes)
            )

            try:
                text = pytesseract.image_to_string(
                    image
                ).strip()

            except Exception as e:
                print("❌ OCR failed:", e)
                text = ""

        if text:

            print(
                f"✅ Text extracted from page "
                f"{page_number + 1}: "
                f"{len(text)} characters"
            )

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": os.path.basename(pdf_path),
                        "page": page_number + 1
                    }
                )
            )

        else:

            print(
                f"⚠️ No text found on page "
                f"{page_number + 1}"
            )

    pdf.close()

    print("-" * 60)

    print(
        "📝 Pages containing text:",
        len(documents)
    )

    if not documents:
        raise ValueError(
            "No text could be extracted from the PDF."
        )

    print("✅ PDF text extraction completed")

    return documents