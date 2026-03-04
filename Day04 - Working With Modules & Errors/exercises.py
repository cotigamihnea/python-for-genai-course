import sys
import random
import math
from datetime import datetime, timedelta
import requests

PURPLE = '\033[95m'
RESET = '\033[0m'

def task1():
    print(f"Square of 144 is {math.sqrt(144)}")
    print(f"Area of circle with r 5 is {math.pi * pow(5, 2)}")
    print(f"Factorial of 5 is {math.factorial(5)}")
    
    print(f"5 random numbers 1-100: {random.randint(1, 100)}, {random.randint(1, 100)}, " \
      f"{random.randint(1, 100)}, {random.randint(1, 100)}, {random.randint(1, 100)}")
    
    colors = ["red", "green", "purple"]
    print(f"Random color: {random.choice(colors)}")
    
    numbers = [1, 2, 3, 43, 543, 5345, 543543, 34, 55, 4554, 4]
    random.shuffle(numbers)
    print(f"Shuffled numbers: {numbers}")
    
    now = datetime.now()
    print(f"Today's date: {now}")
    nextw = now + timedelta(days = 7)
    print(f"Next week: {nextw}")
    
    pass


def task2():
    
    try:
        nr1 = int(input("pls insert nr1: "))
    except ValueError:
        print("nr1 is not a number")
        return 1
    
    try:
        nr2 = int(input("pls insert nr2: "))
    except ValueError:
        print("nr2 is not a number")
        return 1
        
    loop = None
    while loop is None:
        op = input("pls insert operator (or type exit): ")
        if op in ["+", "-", "*", "/"]:
            if op == "+":
                print(f"Sum of {nr1} and {nr2} is {nr1 + nr2}")
            elif op == "-":
                print (f"Difference of {nr1} and {nr2} is {nr1 - nr2}")
            elif op == "*":
                print (f"Product of {nr1} and {nr2} is {nr1 * nr2}")
            elif op == "/":
                try:
                    print (f"Quotient of {nr1} and {nr2} is {nr1 / nr2}")
                except ZeroDivisionError:
                    print("Cannot divide by zero")
        elif op == "exit":
            loop = False
        else:
            print("pls insert a valid operator")
    pass

def task3():
    filename = input("Give me the name of the file!\n")
    file = None 
    
    try:
        file = open(f"{filename}", "r")
        content = file.read()
        
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("No permis")
    except IOError:
        print("Random errors :(")
        
    else:
        num_lines = len(content.splitlines())
        num_words = len(content.split())
        num_chars = len(content)
        
        print("\n--- File Statistics ---")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")
        
    finally:
        if file is not None:
            file.close()
            
    pass

def task4():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        response.raise_for_status()

        post_data = response.json()

        print("Post Data:")
        print(f"Title: {post_data['title']}")
        print(f"Body: {post_data['body']}")
        print(f"User ID: {post_data['userId']}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except requests.exceptions.ConnectTimeout:
        print("Timeout")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except KeyError as e:
        print(f"Missing key in response: {e}")
        
    pass

def task5():
    try:
        data = {"title": "My Test Post", "body": "This is a test post", "userID" : 1}
        response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        
    if data:
        print(f"{response}")
        print(f"{data}")
    pass

def task6(): 
    
    def fetch_post(post_id):
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            post_data = response.json()
            
            print(f"\n{PURPLE}--- Post #{post_id} Retrieved ---{RESET}")
            print(f"Title: {post_data.get('title')}")
            print(f"Body: {post_data.get('body')}")
            print("-" * 30 + "\n")
            
        except requests.exceptions.HTTPError:
            print(f"\n[!] HTTP Error: Could not find post {post_id}. (It might not exist)\n")
        except requests.exceptions.RequestException as e:
            print(f"\n[!] Connection Error: {e}\n")

    def create_post(title, body):
        url = "https://jsonplaceholder.typicode.com/posts"
        payload = {
            "title": title,
            "body": body,
            "userId": 1
        }
        
        try:
            response = requests.post(url, json=payload, timeout=5)
            response.raise_for_status()
            new_post = response.json()
            
            print(f"\n{PURPLE}--- Post Created Successfully ---{RESET}")
            print(f"Assigned ID: {new_post.get('id')}")
            print(f"Title: {new_post.get('title')}")
            print(f"Body: {new_post.get('body')}")
            print("-" * 33 + "\n")
            
        except requests.exceptions.RequestException as e:
            print(f"\n[!] Failed to create post: {e}\n")


    while True:
        print(f"{PURPLE}API CLIENT MENU{RESET}")
        print("1. Fetch a post by ID (GET)")
        print("2. Create a new post (POST)")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            post_id = input("Enter post ID to fetch (e.g., 1 to 100): ").strip()
            if post_id.isdigit():
                fetch_post(post_id)
            else:
                print("[!] Please enter a valid number.\n")
                
        elif choice == "2":
            title = input("Enter post title: ").strip()
            body = input("Enter post body: ").strip()
            
            if title and body:
                create_post(title, body)
            else:
                print("[!] Title and body cannot be empty.\n")
                
        elif choice == "3":
            print("Exiting API Client. Goodbye!")
            break
            
        else:
            print("[!] Invalid choice. Please enter 1, 2, or 3.\n")

def main():
    
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    task6()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())