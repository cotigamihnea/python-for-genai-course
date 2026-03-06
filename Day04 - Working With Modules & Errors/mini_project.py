import sys
import requests
import json
import csv

CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
PURPLE = '\033[95m'
RESET = '\033[0m'

BASE_URL = "https://jsonplaceholder.typicode.com"

# BONUS 
api_cache = {}

def fetch_data(endpoint, params=None):
    """Helper function to make GET requests with caching and robust error handling."""
    cache_key = f"{endpoint}_{str(params)}"
    
    if cache_key in api_cache:
        print(f"{YELLOW}[Loaded from local cache]{RESET}")
        return api_cache[cache_key]
        
    url = f"{BASE_URL}{endpoint}"
    print(f"{CYAN}Fetching data from API...{RESET}")
    
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        api_cache[cache_key] = data
        return data
        
    except requests.exceptions.Timeout:
        print(f"{RED}[!] Request timed out. Please try again.{RESET}")
    except requests.exceptions.ConnectionError:
        print(f"{RED}[!] Connection error. Check your internet.{RESET}")
    except requests.exceptions.HTTPError as e:
        print(f"{RED}[!] HTTP error: {e}{RESET}")
    except json.JSONDecodeError:
        print(f"{RED}[!] Failed to parse JSON response.{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}[!] Request failed: {e}{RESET}")
        
    return None

def display_all_users():
    users = fetch_data("/users")
    if not users: return
    
    print(f"\n{PURPLE}═══════════════════════════════════════")
    print("All Users:")
    print(f"═══════════════════════════════════════{RESET}")
    for user in users:
        print(f"{user['id']}. {user['name']} (@{user['username']})")

def view_user_details():
    user_id = input("\nEnter user ID: ").strip()
    if not user_id.isdigit():
        print(f"{RED}[!] Please enter a valid numeric ID.{RESET}")
        return
        
    user = fetch_data(f"/users/{user_id}")
    if not user: return
    
    print(f"\n{PURPLE}═══════════════════════════════════════")
    print("User Details:")
    print(f"═══════════════════════════════════════{RESET}")
    print(f"Name: {user.get('name')}")
    print(f"Username: {user.get('username')}")
    print(f"Email: {user.get('email')}")
    print("Address:")
    address = user.get('address', {})
    print(f"  Street: {address.get('street')}")
    print(f"  City: {address.get('city')}")
    print(f"  Zipcode: {address.get('zipcode')}")
    print(f"Phone: {user.get('phone')}")
    print(f"Company: {user.get('company', {}).get('name')}")

def view_user_posts():
    user_id = input("\nEnter user ID to view posts: ").strip()
    if not user_id.isdigit():
        print(f"{RED}[!] Please enter a valid numeric ID.{RESET}")
        return
        
    # BONUS 5
    page = 1
    limit = 5
    
    while True:
        params = {"userId": user_id, "_page": page, "_limit": limit}
        posts = fetch_data("/posts", params=params)
        
        if not posts:
            if page == 1: print(f"{YELLOW}No posts found for this user.{RESET}")
            else: print(f"{YELLOW}No more posts.{RESET}")
            break
            
        print(f"\n{PURPLE}--- Posts (Page {page}) ---{RESET}")
        for post in posts:
            print(f"{post['id']}. {post['title']}")
            
        print(f"\nOptions: [ID] Read Post | [N] Next Page | [Q] Quit")
        choice = input("Choice: ").strip().lower()
        
        if choice == 'q':
            break
        elif choice == 'n':
            page += 1
        elif choice.isdigit():
            read_full_post(choice)
        else:
            print(f"{RED}Invalid choice.{RESET}")

def read_full_post(post_id):
    post = fetch_data(f"/posts/{post_id}")
    if not post: return
    
    print(f"\n{CYAN}Title: {post['title']}{RESET}")
    print(f"Body: {post['body']}")
    
    # BONUS
    view_comments = input(f"\n{YELLOW}View comments? (y/n): {RESET}").strip().lower()
    if view_comments == 'y':
        comments = fetch_data(f"/posts/{post_id}/comments")
        if comments:
            print(f"\n{PURPLE}--- Comments ---{RESET}")
            for c in comments:
                print(f"{GREEN}{c['email']}{RESET} says: {c['body']}\n")

# BONUS
def search_users():
    query = input("\nEnter name or email to search: ").strip().lower()
    users = fetch_data("/users")
    if not users: return
    
    matches = [u for u in users if query in u['name'].lower() or query in u['email'].lower()]
    
    if matches:
        print(f"\n{GREEN}Found {len(matches)} match(es):{RESET}")
        for user in matches:
            print(f"- {user['name']} | Email: {user['email']} | ID: {user['id']}")
    else:
        print(f"{YELLOW}No users matched your search.{RESET}")

# BONUS
def view_user_todos():
    user_id = input("\nEnter user ID to view Todos: ").strip()
    if not user_id.isdigit():
        print(f"{RED}[!] Please enter a valid numeric ID.{RESET}")
        return
        
    todos = fetch_data("/todos", params={"userId": user_id})
    if not todos: return
    
    print(f"\n{PURPLE}--- User {user_id}'s Task List ---{RESET}")
    for task in todos:
        status = f"{GREEN}[✓]{RESET}" if task['completed'] else f"{RED}[ ]{RESET}"
        print(f"{status} {task['title']}")

# BONUS
def export_user_data():
    users = fetch_data("/users")
    if not users: return
    
    try:
        with open("users_export.json", "w") as json_file:
            json.dump(users, json_file, indent=4)
            
        with open("users_export.csv", "w", newline='') as csv_file:
            fieldnames = ['id', 'name', 'username', 'email', 'city', 'company']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()
            for u in users:
                writer.writerow({
                    'id': u.get('id'),
                    'name': u.get('name'),
                    'username': u.get('username'),
                    'email': u.get('email'),
                    'city': u.get('address', {}).get('city', ''),
                    'company': u.get('company', {}).get('name', '')
                })
                
        print(f"{GREEN}Successfully exported to users_export.json and users_export.csv!{RESET}")
    except Exception as e:
        print(f"{RED}Failed to export data: {e}{RESET}")

def main():
    while True:
        print(f"\n{PURPLE}╔══════════════════════════════════════╗")
        print("║          API DATA FETCHER            ║")
        print(f"╚══════════════════════════════════════╝{RESET}")
        print("1. View all users")
        print("2. View user details")
        print("3. View user's posts (with comments & pagination)")
        print("4. Search users")
        print("5. View user's Todos")
        print("6. Export all user data (JSON & CSV)")
        print("7. Exit")
        
        choice = input(f"\n{CYAN}Enter your choice (1-7): {RESET}").strip()
        
        if choice == "1":
            display_all_users()
        elif choice == "2":
            view_user_details()
        elif choice == "3":
            view_user_posts()
        elif choice == "4":
            search_users()
        elif choice == "5":
            view_user_todos()
        elif choice == "6":
            export_user_data()
        elif choice == "7":
            print(f"{GREEN}Goodbye!{RESET}")
            break
        else:
            print(f"{RED}[!] Invalid choice.{RESET}")

if __name__ == "__main__":
    sys.exit(main())