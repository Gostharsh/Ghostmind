# core/reasoner.py

from collections import deque
from core.vector_memory import get_relevant_lessons

# Keeps last N user inputs
context_window = deque(maxlen=5)

def update_context(user_input):
    context_window.append(user_input)

def get_context():
    return list(context_window)

def reason_about(user_input):
    # Step 1: Update context
    update_context(user_input)
    full_context = " ".join(get_context())

    # Step 2: Retrieve memory based on current + past inputs
    related_lessons = get_relevant_lessons(full_context, top_k=5)

    # Step 3: Prioritize lessons (for now: sort by length as importance proxy)
    prioritized = sorted(related_lessons, key=lambda x: len(x), reverse=True)

    # Step 4: Form a thought using top 1-2
    thoughts = []
    if prioritized:
        top = prioritized[:2]
        for idea in top:
            thoughts.append(f"🤔 Based on our convo, this idea might help: {idea}")
    else:
        thoughts.append("Hmm... I don't have a strong memory to connect with this yet.")

    return thoughts, prioritized
