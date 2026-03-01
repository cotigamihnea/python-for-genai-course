import sys

# BONUS: ANSI Color Codes for terminal formatting
PURPLE = '\033[95m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def main():
    print(f"{PURPLE}╔═══════════════════════════════════════════════════╗")
    print("║      Welcome to the User Info Collector Pro!      ║")
    print(f"╚═══════════════════════════════════════════════════╝{RESET}\n")

    print("Please provide the following information:\n")

    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()

    # BONUS: Input Validation for Age
    while True:
        try:
            age = int(input("Age: "))
            if age > 0:
                break
            print(f"{YELLOW}[!] Age must be a positive number. Try again.{RESET}")
        except ValueError:
            print(f"{YELLOW}[!] Please enter a valid number.{RESET}")

    # BONUS: Input Validation for Email
    while True:
        email = input("Email: ").strip()
        if "@" in email and "." in email:
            break
        print(f"{YELLOW}[!] Invalid email. Must contain '@' and/or a domain (e.g., .com).{RESET}")

    # BONUS: Input Validation for Phone
    while True:
        phone = input("Phone: ").strip()
        if phone.replace("-", "").replace(" ", "").replace("+", "").isdigit():
            break
        print(f"{YELLOW}[!] Invalid phone number. Please use only numbers, dashes, or spaces.{RESET}")

    # BONUS: Additional Information
    country = input("Country: ").strip()
    occupation = input("Current Occupation: ").strip()

    while True:
        try:
            num_languages = int(input("Number of programming languages you know: "))
            break
        except ValueError:
            print(f"{YELLOW}[!] Please enter a valid whole number.{RESET}")

    fav_language = input("Your favorite programming language: ").strip()

    while True:
        try:
            years_exp = float(input("Years of coding experience: "))
            if years_exp >= 0:
                break
            print(f"{YELLOW}[!] Experience cannot be negative.{RESET}")
        except ValueError:
            print(f"{YELLOW}[!] Please enter a valid number.{RESET}")
    
    is_student = None
    student_status = ""
    while is_student is None:
        answer = input("Are you currently a student? (y/n): ").lower()
        match answer:
            case 'y':
                is_student = True
                student_status = "Yes"
            case 'n':
                is_student = False
                student_status = "No"
            case _:
                print(f"{YELLOW}[!] Please enter y or n{RESET}")

    birth_year = 2026 - age
    # BONUS: Extra calculation
    approx_days_alive = int(age * 365.25) 
    
    # BONUS: Division by 0 handler
    if years_exp > 0:
        avg_languages = num_languages / years_exp
    else:
        avg_languages = 0.0

    if years_exp < 1:
        exp_level = "Beginner"
        message = "Welcome to the exciting world of coding!"
    elif 1 <= years_exp <= 3:
        exp_level = "Intermediate"
        message = "Building a solid foundation! Keep it up!"
    else:
        exp_level = "Advanced"
        message = "Wow, a pro! Keep sharing your knowledge!"

    # BONUS: Better formatting and building a single summary string
    summary = f"""
╔════════════════════════════════════════════════════╗
║             USER INFORMATION SUMMARY               ║
╠════════════════════════════════════════════════════╣
║ {f'Name: {first_name} {last_name}':<50} ║
║ {f'Age: {age} years old (Approx. {approx_days_alive:,} days)':<50} ║
║ {f'Birth Year: {birth_year}':<50} ║
║ {f'Location: {country}':<50} ║
║ {f'Occupation: {occupation}':<50} ║
║ {f'Email: {email}':<50} ║
║ {f'Phone: {phone}':<50} ║
║ {'':<50} ║
║ {'Programming Experience:':<50} ║
║ {f'   • Languages Known: {num_languages}':<50} ║
║ {f'   • Favorite Language: {fav_language}':<50} ║
║ {f'   • Years of Experience: {years_exp}':<50} ║
║ {f'   • Experience Level: {exp_level}':<50} ║
║ {f'   • Avg Languages/Year: {avg_languages:.2f}':<50} ║
║ {f'   • Student Status: {student_status}':<50} ║
║ {'':<50} ║
║ {message:<50} ║
╚════════════════════════════════════════════════════╝
    """

    print(f"{GREEN}{summary}{RESET}")

    # BONUS: Save to a text file
    filename = f"{first_name.lower()}_summary.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(summary.strip())
        print(f"{PURPLE}Summary successfully saved to '{filename}'!{RESET}")
    except Exception as e:
        print(f"{YELLOW}[!] Could not save file: {e}{RESET}")

    return 0

if __name__ == "__main__":
    sys.exit(main())