# core/thinker.py

def reflect_on_lessons(lessons):
    thoughts = []
    for lesson in lessons:
        if "name" in lesson.lower():
            thoughts.append("Using someone's name builds trust. I should remember names.")
        elif "empathy" in lesson.lower():
            thoughts.append("Empathy makes others feel heard. I should listen actively.")
        else:
            thoughts.append(f"I'm thinking about: {lesson}")
    return thoughts
