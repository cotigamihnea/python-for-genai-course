import sys

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

    pass

def task4():
    
    pass

def task5():
    
    pass

def task6(): 
        
    pass

def main():
    # task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())