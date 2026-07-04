"""
5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed.
"""

isbn_set = set()

while True:
    print("\n1. Add ISBN")
    print("2. Remove ISBN")
    print("3. Search ISBN")
    print("4. Display ISBN List")
    print("5. Count Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            isbn = input("Enter ISBN: ")
            isbn_set.add(isbn)
            print("ISBN Added Successfully")

        case 2:
            isbn = input("Enter ISBN to remove: ")

            if isbn in isbn_set:
                isbn_set.remove(isbn)
                print("ISBN Removed Successfully")
            else:
                print("ISBN Not Found")

        case 3:
            isbn = input("Enter ISBN to search: ")

            if isbn in isbn_set:
                print("ISBN Found")
            else:
                print("ISBN Not Found")

        case 4:
            print("\nISBN List:")
            print(isbn_set)

        case 5:
            print("Total Books:", len(isbn_set))

        case 6:
            print("Exiting Program...")
            break