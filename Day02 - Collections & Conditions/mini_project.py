import sys
import json

PURPLE = '\033[95m'
YELLOW = '\033[93m'
RESET = '\033[0m'
FILE_NAME = "grocery_list.json"

def main():
    grocery_list = []

    print(f"{PURPLE}╔════════════════════════════════════════════════════╗")
    print(f"║                 GROCERY PRICE TRACKER              ║")
    print(f"╚════════════════════════════════════════════════════╝\n")

    while True:
        print(f"{PURPLE}\nMain Menu:")
        print("1. Add item                  8. Search for item")
        print("2. View all items            9. Show statistics")
        print("3. Calculate total          10. Sort items")
        print("4. Filter by category       11. Apply discount")
        print("5. Find extremes            12. Save to file")
        print("6. Remove item              13. Load from file")
        print("7. Edit item                14. Exit")

        choice = input(f"\nEnter your choice (1-14): {RESET}").strip()

        match choice:
            case '1':
                name = input("Item name: ").strip()
                while True:
                    try:
                        price = float(input("Price per unit: "))
                        quantity = int(input("Quantity: "))
                        if price >= 0 and quantity > 0:
                            break
                        print(f"{YELLOW}[!] Price must be >= 0 and quantity > 0.{RESET}")
                    except ValueError:
                        print(f"{YELLOW}[!] Please enter numbers for price and quantity.{RESET}")
                
                category = input("Category: ").strip()
                grocery_list.append({"name": name, "price": price, "quantity": quantity, "category": category})
                print(f"{PURPLE}Item '{name}' added successfully!{RESET}")

            case '2':
                if not grocery_list:
                    print(f"{YELLOW}Your grocery list is empty.{RESET}")
                    continue
                
                print(f"{PURPLE}════════════════════════════════════════════════════{RESET}")
                for idx, item in enumerate(grocery_list, 1):
                    total = item['price'] * item['quantity']
                    print(f"{idx}. {item['name']} | Category: {item['category']}")
                    print(f"   Price: ${item['price']:.2f} x {item['quantity']} = ${total:.2f}")
                print(f"{PURPLE}════════════════════════════════════════════════════{RESET}")

            case '3':
                if not grocery_list:
                    print(f"{YELLOW}Your grocery list is empty.{RESET}")
                else:
                    total_cost = sum(item['price'] * item['quantity'] for item in grocery_list)
                    print(f"Total Cost: {PURPLE}${total_cost:.2f}{RESET}")

            case '4':
                if not grocery_list:
                    print(f"{YELLOW}Your list is empty.{RESET}")
                    continue
                cat = input("Enter category to filter: ").strip().lower()
                matches = [i for i in grocery_list if i['category'].lower() == cat]
                if matches:
                    print(f"\nItems in '{cat}':")
                    for item in matches:
                        print(f"- {item['name']}: ${(item['price'] * item['quantity']):.2f}")
                else:
                    print(f"{YELLOW}No items found in that category.{RESET}")

            case '5':
                if not grocery_list:
                    print(f"{YELLOW}Your list is empty.{RESET}")
                    continue
                
                # Using a lambda function to find max/min based on total cost
                max_item = max(grocery_list, key=lambda x: x['price'] * x['quantity'])
                min_item = min(grocery_list, key=lambda x: x['price'] * x['quantity'])
                
                print(f"Most expensive: {max_item['name']} (${(max_item['price'] * max_item['quantity']):.2f})")
                print(f"Least expensive: {min_item['name']} (${(min_item['price'] * min_item['quantity']):.2f})")

            case '6':
                name_to_remove = input("Item to remove: ").strip().lower()
                for item in grocery_list:
                    if item['name'].lower() == name_to_remove:
                        grocery_list.remove(item)
                        print(f"{PURPLE}Item removed.{RESET}")
                        break
                else:
                    print(f"{YELLOW}Item not found.{RESET}")

            case '7': 
                # BONUS: Edit
                name_to_edit = input("Enter item name to edit: ").strip().lower()
                for item in grocery_list:
                    if item['name'].lower() == name_to_edit:
                        print(f"Editing {item['name']}. Press Enter to keep current values.")
                        
                        new_price = input(f"New price (current: {item['price']}): ")
                        if new_price: item['price'] = float(new_price)
                            
                        new_qty = input(f"New quantity (current: {item['quantity']}): ")
                        if new_qty: item['quantity'] = int(new_qty)
                            
                        new_cat = input(f"New category (current: {item['category']}): ").strip()
                        if new_cat: item['category'] = new_cat
                            
                        print(f"{PURPLE}Item updated!{RESET}")
                        break
                else:
                    print(f"{YELLOW}Item not found.{RESET}")

            case '8': 
                # BONUS: Search
                query = input("Search for item: ").strip().lower()
                matches = [i for i in grocery_list if query in i['name'].lower()]
                if matches:
                    for item in matches:
                        print(f"- {item['name']} (${item['price']:.2f} each)")
                else:
                    print(f"{YELLOW}No items match your search.{RESET}")

            case '9': 
                # BONUS: Statistics
                if not grocery_list:
                    print(f"{YELLOW}Your list is empty.{RESET}")
                    continue
                total_items = sum(item['quantity'] for item in grocery_list)
                avg_price = sum(item['price'] for item in grocery_list) / len(grocery_list)
                
                categories = {}
                for item in grocery_list:
                    cat = item['category']
                    categories[cat] = categories.get(cat, 0) + 1

                print(f"\n{PURPLE}--- List Statistics ---{RESET}")
                print(f"Total individual items: {total_items}")
                print(f"Average price per unique item: ${avg_price:.2f}")
                print("Unique items per category:")
                for cat, count in categories.items():
                    print(f"  - {cat}: {count}")

            case '10': 
                # BONUS: Sorting
                if not grocery_list:
                    print(f"{YELLOW}Your list is empty.{RESET}")
                    continue
                sort_by = input("Sort by (name/price/category): ").strip().lower()
                if sort_by in ['name', 'price', 'category']:
                    grocery_list.sort(key=lambda x: x[sort_by])
                    print(f"{PURPLE}List sorted by {sort_by}! Use option 2 to view.{RESET}")
                else:
                    print(f"{YELLOW}Invalid sorting option.{RESET}")

            case '11': 
                # BONUS: Discount Calculator
                name_to_discount = input("Enter item name to discount (or 'all' for entire list): ").strip().lower()
                try:
                    percent = float(input("Enter discount percentage NUMBER: "))
                    multiplier = 1 - (percent / 100)
                    
                    if name_to_discount == 'all':
                        for item in grocery_list:
                            item['price'] *= multiplier
                        print(f"{PURPLE}Applied {percent}% discount to all items.{RESET}")
                    else:
                        for item in grocery_list:
                            if item['name'].lower() == name_to_discount:
                                item['price'] *= multiplier
                                print(f"{PURPLE}Applied {percent}% discount to {item['name']}.{RESET}")
                                break
                        else:
                            print(f"{YELLOW}Item not found.{RESET}")
                except ValueError:
                    print(f"{YELLOW}[!] Invalid percentage.{RESET}")

            case '12': 
                # BONUS: Save to file
                try:
                    with open(FILE_NAME, "w") as file:
                        json.dump(grocery_list, file, indent=4)
                    print(f"{PURPLE}Successfully saved to {FILE_NAME}!{RESET}")
                except Exception as e:
                    print(f"{YELLOW}[!] Error saving file: {e}{RESET}")

            case '13': 
                # BONUS: Load from file
                try:
                    with open(FILE_NAME, "r") as file:
                        grocery_list = json.load(file)
                    print(f"{PURPLE}Successfully loaded {len(grocery_list)} items from {FILE_NAME}!{RESET}")
                except FileNotFoundError:
                    print(f"{YELLOW}[!] No saved list found.{RESET}")
                except Exception as e:
                    print(f"{YELLOW}[!] Error loading file: {e}{RESET}")

            case '14':
                print(f"{PURPLE}Thank you for using Grocery Price Tracker!{RESET}")
                break

            case _:
                print(f"{YELLOW}[!] Invalid choice. Please enter a number between 1 and 14.{RESET}")

    return 0

if __name__ == "__main__":
    sys.exit(main())