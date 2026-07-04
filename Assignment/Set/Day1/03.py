"""
3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations.
"""

"""
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.
"""

visitors = set()

while True:
    print("\n===== WEBSITE VISITOR TRACKING SYSTEM =====")
    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            visitor_id = int(input("Enter Visitor ID: "))
            visitors.add(visitor_id)
            print("Visitor Added Successfully!")

        case 2:
            visitor_id = int(input("Enter Visitor ID to Remove: "))

            if visitor_id in visitors:
                visitors.remove(visitor_id)
                print("Visitor Removed Successfully!")
            else:
                print("Visitor Not Found!")

        case 3:
            visitor_id = int(input("Enter Visitor ID to Check: "))

            if visitor_id in visitors:
                print("Visitor Exists.")
            else:
                print("Visitor Does Not Exist.")

        case 4:
            print("\nAll Visitors:")
            print(visitors)

        case 5:
            print("\nTotal Unique Visitors:", len(visitors))

        case 6:
            visitors.clear()
            print("All Visitor Data Cleared!")

        case 7:
            print("Exiting Program...")
            break

