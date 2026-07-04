"""
4.
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed.

"""
subjects = frozenset(["Python", "Java", "MySQL", "React", "Spring Boot"])

while True:
    print("\n1. Display Subjects")
    print("2. Search Subject")
    print("3. Count Subjects")
    print("4. Attempt to Add Subject")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            print(subjects)

        case 2:
            sub = input("Enter subject: ")

            if sub in subjects:
                print("Subject Found")
            else:
                print("Subject Not Found")

        case 3:
            print("Total Subjects:", len(subjects))

        case 4:
            print("Cannot add subject.")
            print("Frozen Set is immutable (cannot be modified).")

        case 5:
            break

