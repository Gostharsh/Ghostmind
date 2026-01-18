# from PyPDF2 import PdfReader

# def read_book(pdf_path):
#     reader = PdfReader(pdf_path)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text() + "\n"
#     return text


# core/reader.py
import pdfplumber

def read_book(pdf_path):
    print("📖 Using pdfplumber to extract text...")
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text
