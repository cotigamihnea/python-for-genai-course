import sys
import random

PURPLE = '\033[95m'
RESET = '\033[0m'

def task1():
    number = random.randint(1, 100)
    guess = 0
    attempts = 0
    while number != guess:
        guess = int(input("Try to guess the number 1-100: "))
        attempts += 1
        if guess > number:
            print("try lower")
        elif guess < number:
            print("try higher")
        else:
            print(f"You got it! nr. of attempts: {attempts}")
            
    pass


def task2():
    cute_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squares_list = [x * x for x in cute_list]
    evens_list = [x for x in cute_list if x % 2 == 0]
    greater_list = [x * 2 for x in cute_list if x > 5]
    strings_list = [str(x) for x in cute_list]
    tuples_list = [(x, x * x) for x in cute_list]
    
    print ("Starting list:", cute_list)
    print ("Squares list:", squares_list)
    print ("Evens list:", evens_list)
    print ("Greater than 5 list:", greater_list)
    print ("Strings list:", strings_list)
    print ("Tuples list:", tuples_list)
     
    pass

def task3():
    
    def calculate_area(length, width):
        return length * width
    
    def is_even(number):
        return number % 2 == 0
    
    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
        
    def reverse_string(text):
        return text[::-1]
    
    def count_vowels(text):
        num_vowels = 0
        for char in text:
            if char in "aeiouAEIOU":
               num_vowels += 1
        return num_vowels

    result1 = calculate_area(int(input("Enter length: ")), int(input("Enter width: ")))
    print("Area of rectangle:", result1)
    
    result2 = is_even(int(input("Enter a number to check if it's even: ")))
    print("Is the number even?", result2)
    
    result3 = get_grade(int(input("Enter a score to get the grade: ")))
    print("Grade:", result3)
    
    result4 = reverse_string(input("Enter a string to reverse: "))
    print("Reversed string:", result4)
    
    result5 = count_vowels(input("Enter a string to count vowels: "))
    print("Number of vowels:", result5)
    
    pass

def task4():
    numbers = [12, 45, 8, 23, 56, 9, 34, 67, 3, 91]
    stats = {}
    stats["sum"] = sum(numbers)
    stats["average"] = sum(numbers) / len(numbers)
    stats["max"] = max(numbers)
    stats["min"] = min(numbers)
    stats["count"] = len(numbers)
    stats["evens"] = len([x for x in numbers if x % 2 == 0])
    stats["odds"] = len([x for x in numbers if x % 2 != 0])
    print("Statistics for the list of numbers:")
    for key, value in stats.items():
        print(f"{key}: {value}")
        
    pass

def task5():
    double = lambda x: x * 2
    print("Double 5 using lambda:", double(5))

    is_positive = lambda x: x > 0
    print("Is 3 positive?", is_positive(3))
    print("Is -1 positive?", is_positive(-1))

    original = [1, 2, 3, 4, 5]
    doubled_list = list(map(lambda x: x * 2, original))
    print("Original list:", original)
    print("Doubled list with map:", doubled_list)

    mixed = [-2, -1, 0, 1, 2, 3]
    positives = list(filter(lambda x: x > 0, mixed))
    print("Mixed list:", mixed)
    print("Filtered positives with filter:", positives)

    fruits = ["apple", "banana", "cherry"]
    sorted_by_length = sorted(fruits, key=lambda s: len(s))
    print("Fruits sorted by length:", sorted_by_length)
    
    pass

def task6(): 
    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def process_scores(scores):
        return [(s, get_grade(s)) for s in scores]

    collected = []
    print("Enter student scores between 0 and 100. Type 'done' to finish.")
    while True:
        inp = input("Score: ")
        if inp == "done":
            break
        val = int(inp)
        if val < 0 or val > 100:
            print("Score must be between 0 and 100.")
            continue
        collected.append(val)
    
    if not collected:
        print("No scores entered.")
        return
    
    processed = process_scores(collected)
    print("Processed scores and grades:")
    for score, grade in processed:
        print(f"{score} -> {grade}")

    highest = max(collected, key=lambda x: x)
    print("Highest score:", highest)

    average = sum(collected) / len(collected)
    print("Average score:", average)
    print("Maximum score:", max(collected))
    print("Minimum score:", min(collected))
    pass

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