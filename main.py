from strengthchecker import check_password_strength
from wordlistgenerator import generate_wordlist

def menu():
    print("\nCRYPTIX (Password Strength Checker)")
    print("1. Check password strength")
    print("2. Generate custom wordlist")
    print("3. Exit")

while True:
    menu()
    choice = input("\nEnter choice (1/2/3): ")

    if choice == "1":
        pwd = input("\nEnter password to analyze: ")
        result = check_password_strength(pwd)  
        print("\n" + result)  

    elif choice == "2":
        name = input("\nEnter name / keyword: ")
        year = input("Enter year (ex: 2002): ")
        extra = input("Extra word (pet name / nickname — optional): ")

        filepath = generate_wordlist(name, year, extra)
        print(f"\nWordlist saved at: {filepath}")

    elif choice == "3":
        print("\nExiting tool.")
        break

    else:
        print("\nInvalid choice — try again.")
