# core/extractor.py


import re

def extract_concepts(text):
    lines = text.split("\n")
    lessons = []
    for line in lines:
        if re.search(r'\b(tip|rule|lesson|advice)\b', line.lower()):
            lessons.append(line.strip())
    return lessons
