# core/responder.py

from core.vector_memory import search_vector_memory

def respond(user_input, context_inputs=None):
    # Combine recent conversation context into one string
    context_query = user_input
    if context_inputs:
        context_query = " ".join(context_inputs + [user_input])

    top_lessons = search_vector_memory(context_query)
    if not top_lessons:
        return "Hmm, I haven't learned much about that yet."

    best = top_lessons[0][0]
    return f"Based on what I learned: \"{best}\""
