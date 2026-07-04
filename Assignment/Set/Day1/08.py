"""
8.
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters.
"""
allowed_chars = frozenset(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
)

username = ""

while True:
    print("\n1. Enter Username")
    print("2. Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            username = input("Enter Username: ")

        case 2:
            valid = True

            for ch in username:
                if ch not in allowed_chars:
                    valid = False
                    break

            if valid:
                print("Valid Username")
            else:
                print("Invalid Username")

        case 3:
            print("Allowed Characters:")
            print(allowed_chars)

        case 4:
            print("Exiting Program...")
            break
