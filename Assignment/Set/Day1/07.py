"""
7.
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z.
"""
alphabets = set("abcdefghijklmnopqrstuvwxyz")
sentence = ""

while True:
    print("\n1. Enter Sentence")
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            sentence = input("Enter Sentence: ").lower()

        case 2:
            missing = alphabets.difference(set(sentence))
            print("Missing Alphabets:", missing)

        case 3:
            missing = alphabets.difference(set(sentence))
            print("Count of Missing Alphabets:", len(missing))

        case 4:
            print("Exiting Program...")
            break