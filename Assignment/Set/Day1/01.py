"""
1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.

"""

coding_club=set()
robotics_club=set()

while True:
    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in both Club")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club")
    print("8. Display All Unique Club Members")
    print("9. Display Total Unique Club Members")
    print("10. Exit")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            n1=int(input("Enter number of clubs: "))
            for i in range(n1):
                #coding=input("Enter coding club: ")
                coding_club.add(int(input("Enter coding club :")))

        case 2:
            n2=int(input("Enter number of clubs: "))
            for i in range(n2):
                robotics_club.add(int(input("Enter number of clubs: ")))
        case 3:
            print("\n Display students in coding Clubs")
            for i in coding_club:
                print(i,end=" ")
        case 4:
            print("\n Display students in robotics Clubs")
            for i in robotics_club:
                print(i,end=" ")

        case 5:
            print("\n students in both Clubs")
            print(coding_club.intersection(robotics_club))

        case 6:
            print("\n Display students in coding Clubs")
            print(coding_club.difference(robotics_club))

        case 7:
            print("\n Display students in robotics Clubs")
            print(robotics_club.difference(coding_club))

        case 8:
            print("\n Display unique in both Clubs")
            print(coding_club.union(robotics_club))

        case 9:
            print("\n Display total unique in coding Clubs")
            count=0
            if len(coding_club)==len(coding_club.union(robotics_club)):
                   pass
            else:
                count=count+1
        case 10:
            break








