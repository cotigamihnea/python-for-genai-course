import sys

PURPLE = '\033[95m'
RESET = '\033[0m'

def task1():
    # didn't prioritize nesting 
    age = int(input("What's your age?: "))
    if age <= 12:
        print("You are a child!")
    elif age >= 13 and age <= 19:
        print("You are a teen!")
    elif age >= 20 and age <= 64:
        print("You are an adult!")
    else:
        print("You are a senior!")
    
    driver = None

    while driver is None:
        answer = input("Dou you have a driver's license? type y/n: ")
        match answer:
            case 'y':
                driver = True
            case 'n':
                driver = False
            case _:
                print("please enter y or n")

    if age >= 18 and driver:
        print("You can drive!")
    if age >= 18:
        print("You can vote!")
    if age >= 21:
        print("You can drink in the US!")
    if age >= 65:
        print("You can get a senior discount!")
    
    pass


def task2():
    cute_list = []
    loop = None
    
    while loop is None:
        answer = input("Please choose a valid option (add/del/done): ")
        match answer:
            case 'add':
                cute_list.append(input("Type the element that you wanna add: "))
                print(f"List looks like this: {cute_list}")
            case 'del':
                print(f"List looks like this: {cute_list}")
                cute_list.remove(input("What do you want to remove?\n"))
            case 'done':
                print(f"Almost final list looks like this: {cute_list}")
                print(f"Number of items: {len(cute_list)}")
                print(f"First item: {cute_list[0]}")
                print(f"Last item: {cute_list[-1]}")
                cute_list.sort()
                print(f"Sorted list: {cute_list}")
                ans = input("Do you want to remove any item? Enter to skip, or write the item: ")
                if ans:
                    cute_list.remove(ans)
                print(f"Final list: {cute_list}")
                loop = "done"
            case _:
                print("Enter a valid option.")
    pass

def task3():
    fixed_list = [5, 2, 8, 1, 9, 3, 7, 4, 6, 2]
    maximum = max(fixed_list)
    print(f"Maximum: {maximum}")
    minimum = min(fixed_list)
    print(f"Minimum: {minimum}")
    no2 = fixed_list.count(2)
    print(f"Number of 2's: {no2}")
    i = 0
    while i < no2:
        fixed_list.remove(2)
        i += 1
    print(f"List without 2's: {fixed_list}")
    fixed_list.sort()
    print(f"Sorted list: {fixed_list}")
    fixed_list.reverse()
    print(f"Reversed list: {fixed_list}")
    fixed_list.insert(3, 10)
    print(f"List with 10 inserted at index 3: {fixed_list}")
    new_list = fixed_list.copy()
    fixed_list.clear()
    print(f"Original list cleared: {fixed_list}")
    print(f"New list: {new_list}")
           
    pass

def task4():
    book = {"Title" : "Chess Basics",
            "Author" : "George Georger",
            "Year" : 2015,
            "Pages" : 245,
            "Rating" : 3}
    
    for key in book:
        print(f"{key}: {book[key]}")
    
    book["Rating"] = 4
    book["Genre"] = "Learning"
    
    if book.get("Publisher") is None:
        book["Publisher"] = None
    
    book["Publisher"] = "Bookling"
    
    book.pop("Year")
    
    print(f"Final book: {book}")
    
    pass

def task5():
    list_nr = []
    even_numbers = []
    div3_numbers = []
    sum = 0
    prod = 1
    for i in range(1, 21):
        list_nr.append(i)
    print(f"Starting list: {list_nr}")
    
    for i in list_nr:
        if i % 2 == 0:
            even_numbers.append(i)
        if i % 3 == 0:
            div3_numbers.append(i)
        sum += i
        prod *= i
        
    print(f"Even numbers: {even_numbers}")
    print(f"Numbers div by 3: {div3_numbers}")
    print(f"Sum: {sum}")
    print(f"Product: {prod}")
    
    for index, element in enumerate(list_nr):
        print(f"Index: {index} Elem: {element}")
    
    print("10 to 1:", end = " ") 
    for i in range(11, 21):
        print(list_nr[i * -1], end = " ")
    print()
    
    pass

def task6(): 
    my_list = []
    sum = 0
    minimum = float("inf")
    maximum = float("-inf")

    print("Enter 5 numbers")
    for i in range(5):
        value = int(input(f"Number {i + 1}: "))
        my_list.append(value)

        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
        sum += value

    average = sum / len(my_list)

    categories = []
    for num in my_list:
        if num >= 80:
            cat = "High"
        elif num >= 50:
            cat = "Medium"
        else:
            cat = "Low"
        categories.append((num, cat))

    list_info = {
        "max": maximum,
        "min": minimum,
        "average": average,
        "categories": categories,
    }
    
    print(f"Dictionary: {list_info}")

    categories_lines = "\n".join(
        f"║ {num:<3} -> {cat:<43} ║" for num, cat in categories
    )

    summary = f"""{PURPLE}
╔════════════════════════════════════════════════════╗
║                  LIST STATISTICS                   ║
╠════════════════════════════════════════════════════╣
║ {'Maximum:':<15}{maximum:<35} ║
║ {'Minimum:':<15}{minimum:<35} ║
║ {'Average:':<15}{average:<35} ║
╠════════════════════════════════════════════════════╣
║ Number categories:                                 ║
║                                                    ║
{categories_lines}
╚════════════════════════════════════════════════════╝
    {RESET}"""

    print(summary)

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