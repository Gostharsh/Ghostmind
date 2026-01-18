# core/cleaner.py
import re

def clean_text(raw_text):
    print("🧽 Cleaning text...")
    # Remove line breaks inside sentences
    text = re.sub(r'\n+', ' ', raw_text)
    # Remove multiple spaces
    text = re.sub(r'\s{2,}', ' ', text)
    # Optionally remove page numbers (if any patterns)
    text = re.sub(r'Page \d+ of \d+', '', text)
    return text.strip()
