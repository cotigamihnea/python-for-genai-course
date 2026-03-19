import sys
import csv
import json
import os
import shutil
from datetime import datetime

# UI Colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
PURPLE = '\033[95m'
RESET = '\033[0m'

FIELDNAMES = ["StudentID", "Name", "Math", "Science", "English"]

# BONUS 
current_class = "Class_A"

def get_csv_filename():
    return f"students_{current_class}.csv"

def init_file():
    """Ensure the CSV file exists for the current class with proper headers."""
    filename = get_csv_filename()
    if not os.path.exists(filename):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
        except IOError as e:
            print(f"{RED}[!] Error initializing file: {e}{RESET}")

def load_students():
    init_file()
    students = []
    try:
        with open(get_csv_filename(), "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except IOError as e:
        print(f"{RED}[!] Error reading file: {e}{RESET}")
    return students

def save_students(students):
    try:
        with open(get_csv_filename(), "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(students)
    except IOError as e:
        print(f"{RED}[!] Error saving file: {e}{RESET}")

# BONUS
def get_valid_score(subject):
    while True:
        try:
            score = int(input(f"Enter {subject} score (0-100): "))
            if 0 <= score <= 100:
                return score
            print(f"{YELLOW}[!] Score must be between 0 and 100.{RESET}")
        except ValueError:
            print(f"{RED}[!] Please enter a valid whole number.{RESET}")

# BONUS
def get_letter_grade(average):
    if average >= 90: return "A"
    elif average >= 80: return "B"
    elif average >= 70: return "C"
    elif average >= 60: return "D"
    else: return "F"

def add_student():
    students = load_students()
    print(f"\n{CYAN}--- Add New Student ---{RESET}")
    
    student_id = input("Enter Student ID (e.g., S001): ").strip().upper()
    if any(s["StudentID"] == student_id for s in students):
        print(f"{RED}[!] A student with ID {student_id} already exists in {current_class}.{RESET}")
        return

    name = input("Enter Name: ").strip()
    if not name:
        print(f"{RED}[!] Name cannot be empty.{RESET}")
        return

    math_score = get_valid_score("Math")
    science_score = get_valid_score("Science")
    english_score = get_valid_score("English")

    students.append({
        "StudentID": student_id,
        "Name": name,
        "Math": math_score,
        "Science": science_score,
        "English": english_score
    })
    
    save_students(students)
    print(f"{GREEN}Student {name} added successfully!{RESET}")

def view_students():
    students = load_students()
    if not students:
        print(f"{YELLOW}No students found in {current_class}.{RESET}")
        return

    # BONUS
    print(f"\nSort by: {CYAN}[1]{RESET} ID  {CYAN}[2]{RESET} Name  {CYAN}[3]{RESET} Average Score")
    sort_choice = input("Choice (Default is ID): ").strip()
    
    for s in students:
        s['_avg'] = (int(s['Math']) + int(s['Science']) + int(s['English'])) / 3.0

    if sort_choice == '2':
        students.sort(key=lambda x: x['Name'].lower())
    elif sort_choice == '3':
        students.sort(key=lambda x: x['_avg'], reverse=True)
    else:
        students.sort(key=lambda x: x['StudentID'])

    print(f"\n{PURPLE}══════════════════════════════════════════════════════════════════════════")
    print(f"{'ID':<6} | {'Name':<20} | {'Math':<4} | {'Sci':<4} | {'Eng':<4} | {'Avg':<6} | {'Grade'}")
    print(f"══════════════════════════════════════════════════════════════════════════{RESET}")
    
    for s in students:
        avg = s['_avg']
        grade = get_letter_grade(avg)
        print(f"{s['StudentID']:<6} | {s['Name']:<20} | {s['Math']:<4} | {s['Science']:<4} | {s['English']:<4} | {avg:<6.2f} | {grade}")
    print(f"{PURPLE}══════════════════════════════════════════════════════════════════════════{RESET}")

def search_student():
    students = load_students()
    query = input("\nEnter Student Name or ID to search: ").strip().lower()
    
    matches = [s for s in students if query in s['Name'].lower() or query == s['StudentID'].lower()]
    
    if matches:
        print(f"\n{GREEN}Found {len(matches)} match(es):{RESET}")
        for s in matches:
            avg = (int(s['Math']) + int(s['Science']) + int(s['English'])) / 3.0
            print(f"- {s['StudentID']}: {s['Name']} (Math:{s['Math']}, Sci:{s['Science']}, Eng:{s['English']}) -> Avg: {avg:.2f}")
    else:
        print(f"{YELLOW}No students matched your search.{RESET}")

def update_student():
    students = load_students()
    student_id = input("\nEnter Student ID to update: ").strip().upper()
    
    for s in students:
        if s["StudentID"] == student_id:
            print(f"\n{CYAN}Updating {s['Name']} (Press Enter to keep current score){RESET}")
            
            m = input(f"Math (Current: {s['Math']}): ").strip()
            if m.isdigit() and 0 <= int(m) <= 100: s['Math'] = m
                
            sci = input(f"Science (Current: {s['Science']}): ").strip()
            if sci.isdigit() and 0 <= int(sci) <= 100: s['Science'] = sci
                
            eng = input(f"English (Current: {s['English']}): ").strip()
            if eng.isdigit() and 0 <= int(eng) <= 100: s['English'] = eng
                
            save_students(students)
            print(f"{GREEN}Student updated successfully!{RESET}")
            return
            
    print(f"{YELLOW}Student ID not found.{RESET}")

# BONUS
def delete_student():
    students = load_students()
    student_id = input("\nEnter Student ID to delete: ").strip().upper()
    
    for i, s in enumerate(students):
        if s["StudentID"] == student_id:
            confirm = input(f"{RED}Are you sure you want to delete {s['Name']}? (y/n): {RESET}").lower()
            if confirm == 'y':
                students.pop(i)
                save_students(students)
                print(f"{GREEN}Student deleted.{RESET}")
            return
            
    print(f"{YELLOW}Student ID not found.{RESET}")

# BONUS
def display_statistics():
    students = load_students()
    if not students:
        print(f"{YELLOW}No students to calculate statistics for.{RESET}")
        return

    math_scores = [int(s['Math']) for s in students]
    sci_scores = [int(s['Science']) for s in students]
    eng_scores = [int(s['English']) for s in students]
    
    avg_math = sum(math_scores) / len(students)
    avg_sci = sum(sci_scores) / len(students)
    avg_eng = sum(eng_scores) / len(students)
    overall_avg = (avg_math + avg_sci + avg_eng) / 3

    print(f"\n{PURPLE}════════════════════════════════════════════════════")
    print(f"Class Statistics: {current_class} (Total Students: {len(students)})")
    print(f"════════════════════════════════════════════════════{RESET}")
    
    print("\nSubject Averages & Performance Charts:")
    for subj, avg in [("Math", avg_math), ("Science", avg_sci), ("English", avg_eng)]:
        blocks = int((avg / 100) * 20)
        bar = '█' * blocks + '░' * (20 - blocks)
        print(f"  {subj:<8}: {avg:>6.2f} |{CYAN}{bar}{RESET}|")

    print(f"\nOverall Class Average: {overall_avg:.2f}")
    print(f"{PURPLE}════════════════════════════════════════════════════{RESET}")

def export_data():
    students = load_students()
    if not students: return
    
    json_file = f"export_{current_class}.json"
    try:
        with open(json_file, "w") as f:
            json.dump(students, f, indent=4)
        print(f"{GREEN}Exported data to {json_file}{RESET}")
    except Exception as e:
        print(f"{RED}Error saving JSON: {e}{RESET}")

# BONUS 
def import_data():
    filename = input("Enter JSON filename to import (e.g., export_Class_A.json): ").strip()
    try:
        with open(filename, "r") as f:
            new_students = json.load(f)
            
        current_students = load_students()
        existing_ids = {s['StudentID'] for s in current_students}
        
        imported_count = 0
        for s in new_students:
            if "StudentID" in s and "Name" in s and s['StudentID'] not in existing_ids:
                current_students.append(s)
                existing_ids.add(s['StudentID'])
                imported_count += 1
                
        save_students(current_students)
        print(f"{GREEN}Successfully imported {imported_count} new students!{RESET}")
    except FileNotFoundError:
        print(f"{RED}File not found.{RESET}")
    except json.JSONDecodeError:
        print(f"{RED}Invalid JSON format.{RESET}")

# BONUS 
def backup_data():
    source = get_csv_filename()
    if not os.path.exists(source):
        print(f"{YELLOW}No data to backup yet.{RESET}")
        return
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"backup_{current_class}_{timestamp}.csv"
    
    try:
        shutil.copy2(source, backup_file)
        print(f"{GREEN}Backup created successfully: {backup_file}{RESET}")
    except Exception as e:
        print(f"{RED}Backup failed: {e}{RESET}")

def main():
    global current_class
    
    while True:
        print(f"\n{PURPLE}╔════════════════════════════════════════════════════╗")
        print(f"║             STUDENT SCORE MANAGER                  ║")
        print(f"║             Current Class: {CYAN}{current_class:<23}{PURPLE} ║")
        print(f"╚════════════════════════════════════════════════════╝{RESET}")
        print("1. Add student            7. Export Data (JSON)")
        print("2. View all students      8. Import Data (JSON)")
        print("3. Search student         9. Create CSV Backup")
        print("4. Update student        10. Switch Class")
        print("5. Delete student        11. Exit")
        print("6. Calculate statistics")
        
        choice = input(f"\nEnter your choice (1-11): ").strip()
        
        if choice == '1': add_student()
        elif choice == '2': view_students()
        elif choice == '3': search_student()
        elif choice == '4': update_student()
        elif choice == '5': delete_student()
        elif choice == '6': display_statistics()
        elif choice == '7': export_data()
        elif choice == '8': import_data()
        elif choice == '9': backup_data()
        elif choice == '10': 
            new_class = input(f"Enter new class name (e.g., Class_B): ").strip().replace(" ", "_")
            if new_class: 
                current_class = new_class
                print(f"{GREEN}Switched workspace to {current_class}{RESET}")
        elif choice == '11':
            print(f"{GREEN}Goodbye!{RESET}")
            break
        else:
            print(f"{RED}[!] Invalid choice.{RESET}")

if __name__ == "__main__":
    sys.exit(main())