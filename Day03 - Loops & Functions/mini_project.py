import sys
import json
import random

CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
PURPLE = '\033[95m'
RESET = '\033[0m'

quizez_data = []
results_data = []

def create_quiz():
    name = input(f"{CYAN}Enter quiz name: {RESET}").strip()
    quiz = {"name": name, "questions": []}
    
    while True:
        question = input("Enter a question? (y/n) ").strip().lower()
        if question == "n":
            break
        elif question == "y":
            q_text = input(f"{CYAN}Question text: {RESET}")
            options = []
            for i in range(4):
                opt = input(f"Option {i+1}: ")
                options.append(opt)
                
            while True:
                try:
                    correct = int(input("Correct option number (1-4): "))
                    if 1 <= correct <= 4:
                        break
                    print(f"{YELLOW}Please enter a valid option between 1 and 4.{RESET}")
                except ValueError:
                    print(f"{RED}Invalid input! Please enter a number.{RESET}")
                    
            quiz["questions"].append({"text": q_text, "options": options, "correct": correct})
        else:
            print(f"{YELLOW}Please enter 'y' or 'n'.{RESET}")
            
    quizez_data.append(quiz)
    print(f"{GREEN}Quiz '{quiz['name']}' created successfully.{RESET}")

def take_quiz():
    print(f"\n{CYAN}Choose a quiz to take:{RESET}")
    for idx, q in enumerate(quizez_data):
        print(f"{idx + 1}. {q['name']}")
        
    while True:
        try:
            choice = int(input("Enter quiz number: ")) - 1
            if 0 <= choice < len(quizez_data):
                break
            print(f"{YELLOW}Invalid quiz number.{RESET}")
        except ValueError:
            print(f"{RED}Invalid input! Please enter a number.{RESET}")

    selected_quiz = quizez_data[choice]
    print(f"\n{PURPLE}Starting quiz: {selected_quiz['name']}{RESET}")
    answers = []
    
    for q in selected_quiz["questions"]:
        print(f"\n{CYAN}{q['text']}{RESET}")
        for idx, opt in enumerate(q["options"]):
            print(f"{idx + 1}. {opt}")
            
        while True:
            try:
                ans = int(input("Your answer (1-4): "))
                if 1 <= ans <= 4:
                    answers.append(ans)
                    break
                print(f"{YELLOW}Please enter a number between 1 and 4.{RESET}")
            except ValueError:
                print(f"{RED}Invalid input! Please enter a number.{RESET}")
                
    score = calculate_score(selected_quiz, answers)
    results_data.append({"quiz": selected_quiz["name"], "score": score, "total": len(selected_quiz["questions"]), "answers": answers})
    print(f"\n{GREEN}Your score: {score}/{len(selected_quiz['questions'])}{RESET}")

def display_results(quiz, answers, score):
    print (f"\n{PURPLE}Results for quiz: {quiz['name']}{RESET}")
    for idx, q in enumerate(quiz["questions"]):
        print(f"\nQ{idx + 1}: {CYAN}{q['text']}{RESET}")
        user_ans_text = q['options'][answers[idx] - 1]
        correct_ans_text = q['options'][q['correct'] - 1]
        
        if answers[idx] == q['correct']:
            print(f"Your answer: {GREEN}{user_ans_text} (Correct){RESET}")
        else:
            print(f"Your answer: {RED}{user_ans_text}{RESET} (Correct was: {GREEN}{correct_ans_text}{RESET})")
            
    print(f"\nFinal Score: {score}/{len(quiz['questions'])}")
    print (f"Percentage: {(score / len(quiz['questions'])) * 100:.2f}%")

def calculate_score(quiz, answers):
    score = 0
    for q, a in zip(quiz["questions"], answers):
        if q["correct"] == a:
            score += 1
    return score

# Save/Load Features
def save_quiz():
    print(f"\n{CYAN}Choose a quiz to export:{RESET}")
    for idx, q in enumerate(quizez_data):
        print(f"{idx + 1}. {q['name']}")
        
    while True:
        try:
            choice = int(input("Enter quiz number to save: ")) - 1
            if 0 <= choice < len(quizez_data):
                selected_quiz = quizez_data[choice]
                break
            print(f"{YELLOW}Invalid quiz number.{RESET}")
        except ValueError:
            print(f"{RED}Invalid input! Please enter a number.{RESET}")
            
    filename = f"{selected_quiz['name'].replace(' ', '_').lower()}.json"
    try:
        with open(filename, 'w') as f:
            json.dump(selected_quiz, f, indent=4)
        print(f"{GREEN}Quiz successfully saved to {filename}{RESET}")
    except Exception as e:
        print(f"{RED}Error saving file: {e}{RESET}")

def load_quiz():
    filename = input("Enter the filename to load (e.g., my_quiz.json): ").strip()
    try:
        with open(filename, 'r') as f:
            quiz = json.load(f)
            if "name" in quiz and "questions" in quiz:
                quizez_data.append(quiz)
                print(f"{GREEN}Quiz '{quiz['name']}' loaded successfully!{RESET}")
            else:
                print(f"{RED}File does not match quiz format.{RESET}")
    except FileNotFoundError:
        print(f"{RED}File not found! Make sure you typed the name correctly.{RESET}")
    except json.JSONDecodeError:
        print(f"{RED}File is not a valid JSON.{RESET}")

# Question Bank
def question_bank():
    all_questions = []
    for quiz in quizez_data:
        all_questions.extend(quiz["questions"])
        
    if not all_questions:
        print(f"{YELLOW}No questions available. Please create or load a quiz first.{RESET}")
        return
        
    print(f"\n{PURPLE}--- Welcome to the Question Bank ---{RESET}")
    print("Answer randomized questions from all quizzes! Type '0' to quit at any time.")
    
    random.shuffle(all_questions)
    
    for q in all_questions:
        print(f"\n{CYAN}{q['text']}{RESET}")
        for idx, opt in enumerate(q["options"]):
            print(f"{idx + 1}. {opt}")
            
        while True:
            try:
                ans = int(input("Your answer (1-4) or 0 to quit: "))
                if 0 <= ans <= 4:
                    break
                print(f"{YELLOW}Please enter 1-4, or 0 to quit.{RESET}")
            except ValueError:
                print(f"{RED}Invalid input! Please enter a number.{RESET}")
                
        if ans == 0:
            print("Exiting Question Bank.")
            return
            
        if ans == q['correct']:
            print(f"{GREEN}Correct!{RESET}")
        else:
            correct_ans_text = q['options'][q['correct'] - 1]
            print(f"{RED}Wrong!{RESET} The correct answer was: {GREEN}{correct_ans_text}{RESET}")

# JSON Exporter
def export_results():
    if not results_data:
        print(f"{YELLOW}No results to export.{RESET}")
        return
    try:
        with open("all_results.json", 'w') as f:
            json.dump(results_data, f, indent=4)
        print(f"{GREEN}All results successfully exported to all_results.json{RESET}")
    except Exception as e:
        print(f"{RED}Error saving results: {e}{RESET}")

def main():
    while True:
        print(f"\n{PURPLE}╔══════════════════════════════════════╗")
        print("║          QUIZ CREATOR MENU           ║")
        print(f"╚══════════════════════════════════════╝")
        print("1. Create a new quiz")
        print("2. Take a quiz")
        print("3. View quiz results")
        print("4. Save a quiz to JSON")
        print("5. Load a quiz from JSON")
        print("6. Practice in Question Bank (Randomized)")
        print("7. Export all results to JSON")
        print("8. Exit")
        
        choice = input(f"\nEnter your choice (1-8): {RESET}").strip()
        
        if choice == "1":
            create_quiz()
        elif choice == "2":
            if not quizez_data:
                print(f"{YELLOW}No quizzes available. Please create or load a quiz first.{RESET}")
            else:
                take_quiz()
        elif choice == "3":
            if not results_data:
                print(f"{YELLOW}No results available. Please take a quiz first.{RESET}")
            else:
                for result in results_data:
                    quiz = next((q for q in quizez_data if q["name"] == result["quiz"]), None)
                    if quiz:
                        display_results(quiz, result["answers"], result["score"])
        elif choice == "4":
            if not quizez_data:
                print(f"{YELLOW}No quizzes available to save.{RESET}")
            else:
                save_quiz()
        elif choice == "5":
            load_quiz()
        elif choice == "6":
            question_bank()
        elif choice == "7":
            export_results()
        elif choice == "8":
            print(f"{GREEN}Exiting the program. Goodbye!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}Invalid choice. Please enter a number between 1 and 8.{RESET}")

if __name__ == "__main__":
    sys.exit(main())