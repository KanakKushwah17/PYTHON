"""
2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.

"""
"""
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.
"""

python_course = set()
java_course = set()

while True:
    print("\n===== ONLINE COURSE ENROLLMENT SYSTEM =====")
    print("1. Enroll Student in Python")
    print("2. Enroll Student in Java")
    print("3. Display Python Students")
    print("4. Display Java Students")
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled Only in Python")
    print("7. Find Students Enrolled Only in Java")
    print("8. Check Enrollment in Python Course")
    print("9. Display Total Unique Students")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            n = int(input("Enter number of students: "))
            for i in range(n):
                email = input("Enter email ID: ")
                python_course.add(email)

        case 2:
            n = int(input("Enter number of students: "))
            for i in range(n):
                email = input("Enter email ID: ")
                java_course.add(email)

        case 3:
            print("\nPython Course Students:")
            print(python_course)

        case 4:
            print("\nJava Course Students:")
            print(java_course)

        case 5:
            print("\nStudents Enrolled in Both Courses:")
            print(python_course.intersection(java_course))

        case 6:
            print("\nStudents Enrolled Only in Python:")
            print(python_course.difference(java_course))

        case 7:
            print("\nStudents Enrolled Only in Java:")
            print(java_course.difference(python_course))

        case 8:
            email = input("Enter email ID to check: ")

            if email in python_course:
                print("Student is enrolled in Python Course.")
            else:
                print("Student is NOT enrolled in Python Course.")

        case 9:
            total = len(python_course.union(java_course))
            print("\nTotal Unique Students:", total)

        case 10:
            print("Exiting Program...")
            break