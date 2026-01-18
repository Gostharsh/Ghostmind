# core/lessons.py
import re

def extract_lessons(text):
    print("🧠 Extracting lessons from cleaned text...")
    # Look for common lesson patterns like:
    # "Principle 1:", "Rule 2:", "Remember that..."
    pattern = r"(Principle \d+.*?)(?=Principle \d+|$)"
    matches = re.findall(pattern, text, re.DOTALL)

    if not matches:
        # fallback: break text into logical paragraphs
        print("⚠️ Couldn't find structured principles, using fallback.")
        paragraphs = text.split(". ")
        return [p.strip() for p in paragraphs if len(p.strip()) > 50]
    
    return [match.strip() for match in matches]
