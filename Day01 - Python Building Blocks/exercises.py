import sys

def task1():
    name = input("enter your name: ")
    age = int(input("enter your age: "))
    height = float(input("enter your height: "))
    fav_prog_lang = input("enter your favourite programming language: ")
    years_exp = int(input("enter the number of your years of experience: "))
    learning_py = None

    while learning_py is None:
        answer = input("are you learning python? type y/n: ")
        match answer:
            case 'y':
                learning_py = True
            case 'n':
                learning_py = False
            case _:
                print("please enter y or n")

    # that's how I would store the data, this can apply for any next "store" tasks
    # class Person:
        # name: str
        # age: int
        # height: float
        # fav_prog_lang: str
        # years_exp: int
        # learning_py: bool
    # me = Person(name, age, height, fav_prog_lang, years_exp, learning_py)

    print("=== Personal Information ===")
    print(f"Name: {name}", type(name))
    print(f"Age: {age}", type(age))
    print(f"Height: {height}", type(height))
    print(f"Favourite programming language: {fav_prog_lang}", type(fav_prog_lang))
    print(f"Years of experience: {years_exp}", type(years_exp))
    print(f"Learning Python: {learning_py}", type(learning_py))

    pass


def task2():
    name = input("enter product name: ")
    price = float(input("enter price: "))
    quantity = int(input("enter quantity number: "))
    discount = int(input("enter the NUMBER of the percentage: "))

    before_discount = price * quantity
    discount_amount = before_discount * (discount / 100)
    final_price = before_discount - discount_amount

    print("=== Receipt ===")
    print(f"Name: {name}")
    print(f"Unit price: {price}")
    print(f"Quantity: {quantity}")
    print(f"Total before discount: {before_discount:.2f}")
    print(f"Discount percentage: {discount}%")
    print(f"Discount amount: {discount_amount:.2f}")
    print(f"Final price: {final_price:.2f}")

    pass

def task3():
    name = input("what is your first name?\n")
    surname = input("what is your last name?\n")
    birth_year = int(input("What year were you born in?\n"))
    favourite_number = int(input("What is your favourite number?\n"))

    print("=== YOUR INFORMATION ===")
    print(f"FULL NAME: {name} {surname}")
    print(f"AGE: {2025 - birth_year}")
    print(f"DOUBLE OF YOUR FAVOURITE NUMBER: {2 * favourite_number}")

    pass

def task4():
    values = [0, 1, "", "hello", [], [1, 2, 3], None, True, "False"]

    print("=== Truthy/Falsy Check ===")
    for value in values:
        if value:
            print(f"{repr(value)} is Truthy")
        else:
            print(f"{repr(value)} is Falsy")

def task5():
    print("=== Operator Examples ===")

    num1 = int(input("choose n1: "))
    num2 = int(input("choose n2: "))

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2}")
    print(f"{num1} // {num2} = {num1 // num2}")
    print(f"{num1} % {num2} = {num1 % num2}")
    print(f"{num1} ** {num2} = {num1 ** num2}")

def task6():
    age = int(input("What is your age?\n"))
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

    print(f"=== Comparison ===")
    if driver and age >= 18:
        print("You can drive!")
    else:
        print("You can't drive!")
    
    if age >= 65:
        print("You are a senior citizen.")
    elif age >= 13 and age < 20:
        print("You are a teenager.")
    elif age >= 20 and age < 65:
        print("You are an adult.")
    else:
        print("You are a child.")

    if age >= 18:
        print("Hey! You can vote!")
    else:
        print("Sorry, you can't vote yet!")

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