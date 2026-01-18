# core/memory.py
import os
import json

MEMORY_PATH = r"E:\GhostMind\books\memory.json"

def save_memory(lessons):
    os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(lessons, f, indent=2)

def load_memory():
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
def search_memory(query):
    memory = load_memory()
    results = []
    query_lower = query.lower()
    for lesson in memory:
        if query_lower in lesson.lower():
            results.append(lesson)
    return results



