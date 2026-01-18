from sentence_transformers import SentenceTransformer, util
import json
import os
import torch

MEMORY_PATH = r"E:\GhostMind\books\vector_memory.json"
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_lesson(lesson):
    return model.encode(lesson, convert_to_tensor=True).tolist()

def save_vector_memory(lessons):
    embedded = [{"text": l, "vector": embed_lesson(l)} for l in lessons]
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(embedded, f, indent=2)

def search_vector_memory(query, top_k=3):
    if not os.path.exists(MEMORY_PATH): return []
    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    query_vec = model.encode(query, convert_to_tensor=True)
    results = []
    for item in data:
        vector_tensor = torch.tensor(item["vector"])
        similarity = util.cos_sim(query_vec, vector_tensor)[0].item()
        results.append((item["text"], similarity))

    return sorted(results, key=lambda x: x[1], reverse=True)[:top_k]
