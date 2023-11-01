import json
from difflib import get_close_matches

file_path = r"D:\Programming Languages\VS Code\CHATBOT\Knowledge.json"
# Load the knowledge base from a JSON file
def load_Knowledge(file_path: str):
    data = {}
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
# Save the updated knowledge base to the JSON file
def save_Knowledge(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
# Find the closest matching question
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None
# Main function to handle user input and respond
def chatbot():
    Knowledge: dict = load_Knowledge(file_path)
    while True:
        user_input: str = input("You: ")
        if user_input.lower() == 'quit':
            break
        # Finds the best match, otherwise returns None
        best_match: str | None = find_best_match(user_input, [q["question"] for q in Knowledge["questions"]])
        if best_match:
            # If there is a best match, return the answer from the knowledge base
            answer: str = get_answer_for_question(best_match, Knowledge)
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answer. Can you teach me?")
            new_answer: str = input("Type the answer or 'skip' to skip: ")

            if new_answer.lower() != 'skip':
                Knowledge["questions"].append({"question": user_input, "answer": new_answer})
                save_Knowledge(file_path, Knowledge)
                print("Bot: Thank you! I've learned something new.")
if __name__ == "__main__":
    chatbot()