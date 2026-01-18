from core.reader import read_book
from core.cleaner import clean_text
from core.extractor import extract_concepts
from core.thinker import reflect_on_lessons
from core.vector_memory import save_vector_memory
from core.responder import respond
from core.reasoner import reason_about
from core.conversation import chat_about, get_context, update_context

if __name__ == "__main__":
    pdf_path = r"E:/GhostMind/books/HOW TO WIN FRIENDS & INFLUENCE PEOPLE.pdf"

    # Step 1: Read and extract lessons only if not already embedded
    raw_text = read_book(pdf_path)
    cleaned = clean_text(raw_text)
    lessons = extract_concepts(cleaned)

    if lessons:
        print(f"🧠 Extracted {len(lessons)} lessons.")
        thoughts = reflect_on_lessons(lessons)
        for t in thoughts:
            print("💭", t)
        save_vector_memory(lessons)
        print("💾 Lessons embedded and saved to vector memory.")

    print("\n🤖 Chat with GhostMind (type 'exit' to quit):")
    while True:
        user_input = input("🗣️ You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        thoughts, relevant_lessons = reason_about(user_input)

        for t in thoughts:
            print(t)

        # Pass recent context to responder
        reply = respond(user_input, get_context())
        print("🤖 GhostMind:", reply)

        # Update the conversation context
        update_context(user_input)
