# core/conversation.py

# Conversation memory
_recent_context = []

def chat_about(user_input, lesson):
    principle = lesson.get("title", "a core idea from the book")
    summary = lesson.get("summary", "")

    # Build a conversational response
    response = (
        f"That reminds me of \"{principle}\" from *How to Win Friends & Influence People.*\n"
        f"{summary}\n\n"
        f"What do you think about that? Have you ever tried something like this in real life?"
    )
    return response

def get_context(n=3):
    """Returns the last n user inputs for contextual memory."""
    return _recent_context[-n:]

def update_context(user_input):
    """Appends the latest user input to the context memory."""
    _recent_context.append(user_input)
