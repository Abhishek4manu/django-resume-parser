import pytesseract
from pdf2image import convert_from_path

def extract_pdf_ocr(path):
    text = ""
    images = convert_from_path(path)
    for img in images:
        text += pytesseract.image_to_string(img)
    return text
