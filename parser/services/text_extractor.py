from .ocr_engine import extract_pdf_ocr
import pdfplumber
from docx import Document

def extract_text(path):
    if path.endswith(".pdf"):
        return extract_pdf_text(path)
    elif path.endswith(".docx" or "doc"):
        return extract_docx(path)
    else:
        raise Exception("Unsupported format")

def extract_pdf_text(path):
    text = ""
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        if text.strip():
            return text
    except:
        pass

    
    return extract_pdf_ocr(path)
def extract_docx(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)
