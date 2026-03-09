import sys
import json
import csv
import os

def task1():
    with open("todo.txt", "r") as file:
        for index, line in enumerate(file):
            print(f"{index + 1}: {line.strip()}")
    
    new_task = input("Please add a new task: ")
    with open("todo.txt", "a") as file:
        file.write(f"{new_task}\n")
    
    with open("todo.txt", "r") as file:
        for index, line in enumerate(file):
            print(f"{index + 1}: {line.strip()}")


def task2():
    students = {
        "Alice": {"age": 20, "grades": [85, 90, 92], "email": "alice@example.com"},
        "Bob": {"age": 22, "grades": [78, 82, 88], "email": "bob@example.com"},
        "Charlie": {"age": 21, "grades": [92, 88, 95], "email": "charlie@example.com"}
    }

    json_data = json.dumps(students, indent=4)
    with open("students.json", "w") as file:
        file.write(json_data)
    
    with open("students.json", "r") as file:
        loaded_students = json.load(file)
        for name, student in loaded_students.items():
            print(f"Name: {name}, Age: {student['age']}, Grades: {student['grades']}, Email: {student['email']}")
            
    with open("students.json", "r") as file:
        loaded_students = json.load(file)
        best_average = -1
        besty_student = None
        for name, student in loaded_students.items():
            average_grade = sum(student['grades']) / len(student['grades'])
            if average_grade > best_average:
                best_average = average_grade
                besty_student = name
        print(f"The student with the best average grade is {besty_student} with an average of {best_average:.2f}")
    
    with open("students.json", "r") as file:
        students = json.load(file)
        students["Alice"]["grades"][0] = 95
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)
            print("Alice's first grade has been updated to 95.")

    pass

def task3():
    with open("products.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Price", "Quantity", "Category"])
        writer.writerow(["Laptop", 999.99, 10, "Electronics"])
        writer.writerow(["Smartphone", 499.99, 20, "Electronics"])
        writer.writerow(["Book", 19.99, 50, "Books"])
        writer.writerow(["Headphones", 199.99, 15, "Electronics"])
        writer.writerow(["Coffee Maker", 79.99, 30, "Home Appliances"])
        
    with open("products.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            
    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)
        average_price = 0
        count = 0
        cheapest_product = None
        cheapest_price = float('inf')   
        most_expensive_product = None
        most_expensive_price = float('-inf')
        for row in reader:
            total_value = float(row["Price"]) * int(row["Quantity"])
            print(f"Product: {row['Name']}, Total Value: ${total_value:.2f}")
            if total_value < cheapest_price:
                cheapest_price = total_value
                cheapest_product = row["Name"]
            if total_value > most_expensive_price:
                most_expensive_price = total_value
                most_expensive_product = row["Name"]
            average_price += float(row["Price"])
            count += 1
        average_price /= count
        print(f"Average Price: ${average_price:.2f}")
        print(f"Cheapest Product: {cheapest_product}, Price: ${cheapest_price:.2f}")
        print(f"Most Expensive Product: {most_expensive_product}, Price: ${most_expensive_price:.2f}")

    pass

def task4():
    games = []
    with open("data.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            game = {}
            for part in parts:
                key_value = part.split(": ", 1)
                if len(key_value) == 2:
                    key, value = key_value
                    game[key] = value
            games.append(game)
    
    with open("data.json", "w") as file:
        json.dump(games, file, indent=4)
    
    if games:
        keys = games[0].keys()
        with open("data.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(games)
    
    with open("data.json", "r") as file:
        loaded_games_json = json.load(file)
        print("JSON data:")
        for game in loaded_games_json:
            print(game)
    
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        print("CSV data:")
        for row in reader:
            print(row)

def task5():
    with open("employee_data.json", "r") as file:
        data = json.load(file)
        employees = data["employees"]
    
    dept_sums = {}
    dept_counts = {}
    for emp in employees:
        dept = emp["department"]
        dept_sums[dept] = dept_sums.get(dept, 0) + emp["salary"]
        dept_counts[dept] = dept_counts.get(dept, 0) + 1
    avg_salaries = {dept: dept_sums[dept] / dept_counts[dept] for dept in dept_sums}
    
    high_exp_employees = [emp for emp in employees if emp["years_of_experience"] > 5]
    
    total_payroll = sum(emp["salary"] for emp in employees)
    
    with open("report.txt", "w") as file:
        file.write("Employee Report\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Total Payroll: ${total_payroll:,.2f}\n\n")
        file.write("Average Salary by Department:\n")
        for dept, avg in avg_salaries.items():
            file.write(f"  {dept}: ${avg:,.2f}\n")
        file.write("\nEmployees with >5 years experience:\n")
        for emp in high_exp_employees:
            file.write(f"  - Name: {emp['name']}, Department: {emp['department']}, Salary: ${emp['salary']:,.2f}, Experience: {emp['years_of_experience']} years\n")
    
    if high_exp_employees:
        keys = ["name", "department", "salary", "years_of_experience"]
        with open("high_experience_employees.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(high_exp_employees)
    
    print("Report generated: report.txt")
    print("High experience employees exported to: high_experience_employees.csv")

def task6():
    def create_file():
        filename = input("Enter filename: ")
        if not filename.endswith('.txt'):
            filename += '.txt'
        try:
            with open(filename, 'w') as f:
                content = input("Enter content: ")
                f.write(content)
            print("File created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")
    
    def read_file():
        filename = input("Enter filename: ")
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        try:
            with open(filename, 'r') as f:
                content = f.read()
                print("File content:")
                print(content)
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def append_file():
        filename = input("Enter filename: ")
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        try:
            with open(filename, 'a') as f:
                content = input("Enter content to append: ")
                f.write(content + '\n')
            print("Content appended successfully.")
        except Exception as e:
            print(f"Error appending to file: {e}")
    
    def delete_file():
        filename = input("Enter filename: ")
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        try:
            os.remove(filename)
            print("File deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")
    
    def list_txt_files():
        try:
            files = [f for f in os.listdir('.') if f.endswith('.txt')]
            if files:
                print("Text files in directory:")
                for f in files:
                    print(f"  {f}")
            else:
                print("No .txt files found in the directory.")
        except Exception as e:
            print(f"Error listing files: {e}")
    
    while True:
        print("\nFile Manager Menu:")
        print("1. Create new text file")
        print("2. Read existing file")
        print("3. Append to file")
        print("4. Delete file")
        print("5. List all .txt files in directory")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            create_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            append_file()
        elif choice == '4':
            delete_file()
        elif choice == '5':
            list_txt_files()
        elif choice == '6':
            print("Exiting File Manager...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())