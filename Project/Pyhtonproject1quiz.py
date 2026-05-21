print("===================================")
print("     WELCOME TO PYTHON QUIZ")
print("      Developed By Kanak")
print("Test Your Python Knowledge 🐍")
print("===================================")
print("====================================")
print("     PYTHON TOPIC QUIZ PROJECT      ")
print("====================================\n")

print("Learn Python interactively and test your knowledge with exciting quizzes!\n")

print("1. Intro")
print("2. Python")
print("3. Internal Working")
print("4. Input & Output")
print("5. Data Types")
print("6. Complex Class")
print("7. Complex 2.0")
print("8. Precedence")
print("9. Control Flow - If")
print("10. Control Flow - Else")
print("11. Loop")
print("12. Loop 2.0")
print("13. Break & Continue")
print("14. For-Else & While-Else")
print("15. Membership Operator")
print("16. Conditional Expression (Ternary Operator)")
print("17. Match Case 2.0")
print("18. Nested-Loops")
print("19. Pattern Printing")
print("20. Exit")
print("\nStart learning and level up your coding skills!")
while True:
    choice = int(input("\nEnter Topic Number: "))
    match choice:
        case 1:
            print("\n========== INTRO QUIZ ==========")
            score = 0
            q1 = input("1. Python is a ______ language.\n(a) Programming\n(b) Markup\n(c) Styling\nAnswer: ")
            if q1.lower() == "a":
                score += 1
            q2 = input("\n2. Python is developed by?\n(a) James Gosling\n(b) Guido van Rossum\n(c) Dennis Ritchie\nAnswer: ")
            if q2.lower() == "b":
                score += 1
            q3 = input("\n3. Python is a _____ level language.\n(a) Low\n(b) Machine\n(c) High\nAnswer: ")
            if q3.lower() == "c":
                score += 1
            q4 = input("\n4. Python code file extension is?\n(a) .java\n(b) .py\n(c) .html\nAnswer: ")
            if q4.lower() == "b":
                score += 1
            q5 = input("\n5. Python is famous for?\n(a) Easy syntax\n(b) Complex syntax\n(c) No syntax\nAnswer: ")
            if q5.lower() == "a":
                score += 1
            q6 = input("\n6. Which symbol is used for comments in Python?\n(a) //\n(b) #\n(c) <!--\nAnswer: ")
            if q6.lower() == "b":
                score += 1
            q7 = input("\n7. Which function is used to display output?\n(a) input()\n(b) print()\n(c) show()\nAnswer: ")
            if q7.lower() == "b":
                score += 1
            q8 = input("\n8. Python supports OOP?\n(a) Yes\n(b) No\n(c) Maybe\nAnswer: ")
            if q8.lower() == "a":
                score += 1
            q9 = input("\n9. Python is used in?\n(a) AI\n(b) Web Development\n(c) Both\nAnswer: ")
            if q9.lower() == "c":
                score += 1
            q10 = input("\n10. Python is an _____ language.\n(a) Interpreted\n(b) Assembly\n(c) Hardware\nAnswer: ")
            if q10.lower() == "a":
                score += 1
            print("\nYour Final Score =", score, "/10")
        case 2:

            print("\n========== PYTHON QUIZ ==========")

            score = 0

            q1 = input(
                "1. Who developed Python?\n(a) James Gosling\n(b) Guido van Rossum\n(c) Dennis Ritchie\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input("\n2. Python was released in?\n(a) 1991\n(b) 2000\n(c) 1985\nAnswer: ")
            if q2.lower() == "a":
                score += 1

            q3 = input(
                "\n3. Python is which type of language?\n(a) High Level\n(b) Machine Level\n(c) Assembly Level\nAnswer: ")
            if q3.lower() == "a":
                score += 1

            q4 = input("\n4. Which symbol is used for comments in Python?\n(a) //\n(b) #\n(c) <!--\nAnswer: ")
            if q4.lower() == "b":
                score += 1

            q5 = input("\n5. Which function is used to take input?\n(a) print()\n(b) scan()\n(c) input()\nAnswer: ")
            if q5.lower() == "c":
                score += 1

            q6 = input("\n6. Which function is used for output?\n(a) show()\n(b) print()\n(c) display()\nAnswer: ")
            if q6.lower() == "b":
                score += 1

            q7 = input("\n7. Python file extension is?\n(a) .java\n(b) .py\n(c) .html\nAnswer: ")
            if q7.lower() == "b":
                score += 1

            q8 = input("\n8. Python supports Object Oriented Programming?\n(a) Yes\n(b) No\n(c) Maybe\nAnswer: ")
            if q8.lower() == "a":
                score += 1

            q9 = input("\n9. Which keyword is used to define a function?\n(a) function\n(b) define\n(c) def\nAnswer: ")
            if q9.lower() == "c":
                score += 1

            q10 = input("\n10. Python is an _____ language.\n(a) Interpreted\n(b) Hardware\n(c) Machine\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")

        case 3:

            print("\n========== INTERNAL WORKING QUIZ ==========")

            score = 0

            q1 = input("1. Python is an _____ language.\n(a) Compiled\n(b) Interpreted\n(c) Assembly\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input(
                "\n2. Python code is first converted into?\n(a) Machine Code\n(b) Bytecode\n(c) Binary File\nAnswer: ")
            if q2.lower() == "b":
                score += 1

            q3 = input(
                "\n3. Which component executes Python bytecode?\n(a) Compiler\n(b) Linker\n(c) Python Virtual Machine\nAnswer: ")
            if q3.lower() == "c":
                score += 1

            q4 = input(
                "\n4. PVM stands for?\n(a) Python Virtual Machine\n(b) Program Virtual Memory\n(c) Python Variable Manager\nAnswer: ")
            if q4.lower() == "a":
                score += 1

            q5 = input("\n5. Python executes code?\n(a) Line by line\n(b) All at once\n(c) Randomly\nAnswer: ")
            if q5.lower() == "a":
                score += 1

            q6 = input("\n6. Which file stores Python bytecode?\n(a) .py\n(b) .exe\n(c) .pyc\nAnswer: ")
            if q6.lower() == "c":
                score += 1

            q7 = input("\n7. Python automatically manages?\n(a) Memory\n(b) Hardware\n(c) CPU\nAnswer: ")
            if q7.lower() == "a":
                score += 1

            q8 = input("\n8. Python supports dynamic typing?\n(a) Yes\n(b) No\n(c) Sometimes\nAnswer: ")
            if q8.lower() == "a":
                score += 1

            q9 = input("\n9. Python uses which translator?\n(a) Interpreter\n(b) Assembler\n(c) Loader\nAnswer: ")
            if q9.lower() == "a":
                score += 1

            q10 = input(
                "\n10. Python source code is written in?\n(a) .py file\n(b) .html file\n(c) .exe file\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")

        case 4:

            print("\n========== INPUT & OUTPUT QUIZ ==========")

            score = 0

            q1 = input(
                "1. Which function is used to take input in Python?\n(a) print()\n(b) input()\n(c) scan()\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input(
                "\n2. Which function is used to display output?\n(a) output()\n(b) show()\n(c) print()\nAnswer: ")
            if q2.lower() == "c":
                score += 1

            q3 = input(
                "\n3. input() function returns value in which type by default?\n(a) int\n(b) string\n(c) float\nAnswer: ")
            if q3.lower() == "b":
                score += 1

            q4 = input(
                "\n4. Which symbol is used to separate multiple outputs in print()?\n(a) ,\n(b) :\n(c) ;\nAnswer: ")
            if q4.lower() == "a":
                score += 1

            q5 = input(
                "\n5. Which keyword is used to move output to next line automatically?\n(a) print()\n(b) next\n(c) line\nAnswer: ")
            if q5.lower() == "a":
                score += 1

            q6 = input(
                "\n6. Which argument is used to avoid new line in print()?\n(a) stop\n(b) end\n(c) skip\nAnswer: ")
            if q6.lower() == "b":
                score += 1

            q7 = input("\n7. Which escape sequence is used for new line?\n(a) \\t\n(b) \\n\n(c) \\a\nAnswer: ")
            if q7.lower() == "b":
                score += 1

            q8 = input("\n8. Which escape sequence is used for tab space?\n(a) \\n\n(b) \\b\n(c) \\t\nAnswer: ")
            if q8.lower() == "c":
                score += 1

            q9 = input("\n9. Which function converts input into integer?\n(a) str()\n(b) int()\n(c) float()\nAnswer: ")
            if q9.lower() == "b":
                score += 1

            q10 = input(
                "\n10. What is the output type of print(5)?\n(a) Integer Output\n(b) String Output\n(c) Error\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")

        case 5:

            print("\n========== DATA TYPES QUIZ ==========")

            score = 0

            q1 = input("1. Which data type stores whole numbers?\n(a) float\n(b) int\n(c) str\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input("\n2. Which data type stores decimal numbers?\n(a) int\n(b) str\n(c) float\nAnswer: ")
            if q2.lower() == "c":
                score += 1

            q3 = input("\n3. Which data type stores text?\n(a) str\n(b) int\n(c) bool\nAnswer: ")
            if q3.lower() == "a":
                score += 1

            q4 = input("\n4. Which data type stores True or False values?\n(a) float\n(b) bool\n(c) tuple\nAnswer: ")
            if q4.lower() == "b":
                score += 1

            q5 = input("\n5. Which brackets are used in list?\n(a) ()\n(b) {}\n(c) []\nAnswer: ")
            if q5.lower() == "c":
                score += 1

            q6 = input("\n6. Which brackets are used in tuple?\n(a) ()\n(b) []\n(c) {}\nAnswer: ")
            if q6.lower() == "a":
                score += 1

            q7 = input("\n7. Which brackets are used in dictionary?\n(a) []\n(b) {}\n(c) ()\nAnswer: ")
            if q7.lower() == "b":
                score += 1

            q8 = input("\n8. Which data type stores unique values only?\n(a) list\n(b) tuple\n(c) set\nAnswer: ")
            if q8.lower() == "c":
                score += 1

            q9 = input("\n9. type() function is used for?\n(a) Input\n(b) Checking Data Type\n(c) Output\nAnswer: ")
            if q9.lower() == "b":
                score += 1

            q10 = input("\n10. Which data type is mutable?\n(a) tuple\n(b) string\n(c) list\nAnswer: ")
            if q10.lower() == "c":
                score += 1

            print("\nYour Final Score =", score, "/10")

        case 6:

            print("\n========== COMPLEX CLASS QUIZ ==========")

            score = 0

            q1 = input(
                "1. Which keyword is used to create a class in Python?\n(a) function\n(b) class\n(c) object\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input("\n2. An object is created from?\n(a) Variable\n(b) Function\n(c) Class\nAnswer: ")
            if q2.lower() == "c":
                score += 1

            q3 = input(
                "\n3. Which method is called automatically when object is created?\n(a) __start__\n(b) __init__\n(c) __create__\nAnswer: ")
            if q3.lower() == "b":
                score += 1

            q4 = input("\n4. self keyword refers to?\n(a) Class\n(b) Object itself\n(c) Function\nAnswer: ")
            if q4.lower() == "b":
                score += 1

            q5 = input(
                "\n5. Which concept combines data and methods together?\n(a) Encapsulation\n(b) Looping\n(c) Operator\nAnswer: ")
            if q5.lower() == "a":
                score += 1

            q6 = input(
                "\n6. Which function is used to check object type?\n(a) isinstance()\n(b) print()\n(c) input()\nAnswer: ")
            if q6.lower() == "a":
                score += 1

            q7 = input(
                "\n7. What is used to access object variables?\n(a) Dot Operator\n(b) Colon\n(c) Slash\nAnswer: ")
            if q7.lower() == "a":
                score += 1

            q8 = input("\n8. A class is a blueprint of?\n(a) Function\n(b) Object\n(c) Loop\nAnswer: ")
            if q8.lower() == "b":
                score += 1

            q9 = input(
                "\n9. Which concept allows one class to use properties of another class?\n(a) Inheritance\n(b) Compilation\n(c) Iteration\nAnswer: ")
            if q9.lower() == "a":
                score += 1

            q10 = input("\n10. Which symbol is used to access methods in object?\n(a) ,\n(b) .\n(c) :\nAnswer: ")
            if q10.lower() == "b":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 8:

            print("\n========== PRECEDENCE QUIZ ==========")

            score = 0

            q1 = input("1. Which operator has highest precedence?\n(a) +\n(b) *\n(c) =\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input("\n2. What will be the output of 2 + 3 * 4?\n(a) 20\n(b) 14\n(c) 24\nAnswer: ")
            if q2.lower() == "b":
                score += 1

            q3 = input("\n3. Which brackets are used to change precedence?\n(a) {}\n(b) []\n(c) ()\nAnswer: ")
            if q3.lower() == "c":
                score += 1

            q4 = input("\n4. What will be the output of (2 + 3) * 4?\n(a) 20\n(b) 14\n(c) 9\nAnswer: ")
            if q4.lower() == "a":
                score += 1

            q5 = input(
                "\n5. Which operator is evaluated first in 10 - 2 * 3?\n(a) -\n(b) *\n(c) Both Together\nAnswer: ")
            if q5.lower() == "b":
                score += 1

            q6 = input("\n6. Which operator has lower precedence?\n(a) +\n(b) *\n(c) /\nAnswer: ")
            if q6.lower() == "a":
                score += 1

            q7 = input("\n7. What will be output of 8 / 2 + 2?\n(a) 2\n(b) 6\n(c) 8\nAnswer: ")
            if q7.lower() == "b":
                score += 1

            q8 = input("\n8. Exponent operator in Python is?\n(a) ^\n(b) **\n(c) //\nAnswer: ")
            if q8.lower() == "b":
                score += 1

            q9 = input("\n9. What will be output of 2 ** 3 * 2?\n(a) 16\n(b) 8\n(c) 12\nAnswer: ")
            if q9.lower() == "a":
                score += 1

            q10 = input(
                "\n10. Operator precedence helps in?\n(a) Deciding execution order\n(b) Printing Output\n(c) Taking Input\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 7:

            print("\n========== COMPLEX 2.0 QUIZ ==========")

            score = 0

            q1 = input(
                "1. Which concept allows same function name with different behavior?\n(a) Polymorphism\n(b) Looping\n(c) Iteration\nAnswer: ")
            if q1.lower() == "a":
                score += 1

            q2 = input(
                "\n2. Which method is known as constructor in Python?\n(a) __main__\n(b) __init__\n(c) __create__\nAnswer: ")
            if q2.lower() == "b":
                score += 1

            q3 = input("\n3. Which keyword is used for inheritance?\n(a) extend\n(b) inherit\n(c) class\nAnswer: ")
            if q3.lower() == "c":
                score += 1

            q4 = input(
                "\n4. What is the process of hiding internal details called?\n(a) Abstraction\n(b) Compilation\n(c) Iteration\nAnswer: ")
            if q4.lower() == "a":
                score += 1

            q5 = input(
                "\n5. Which method is used to represent object as string?\n(a) __str__\n(b) __loop__\n(c) __next__\nAnswer: ")
            if q5.lower() == "a":
                score += 1

            q6 = input(
                "\n6. Which function is used to get length of object?\n(a) count()\n(b) len()\n(c) size()\nAnswer: ")
            if q6.lower() == "b":
                score += 1

            q7 = input("\n7. Which keyword refers to parent class?\n(a) super()\n(b) upper()\n(c) parent()\nAnswer: ")
            if q7.lower() == "a":
                score += 1

            q8 = input("\n8. Method overriding is related to?\n(a) Inheritance\n(b) Input\n(c) Output\nAnswer: ")
            if q8.lower() == "a":
                score += 1

            q9 = input("\n9. Which concept allows data protection?\n(a) Encapsulation\n(b) Loop\n(c) Pattern\nAnswer: ")
            if q9.lower() == "a":
                score += 1

            q10 = input(
                "\n10. OOP stands for?\n(a) Object Oriented Programming\n(b) Only Object Program\n(c) Object Output Program\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 8:

            print("\n========== PRECEDENCE QUIZ ==========")

            score = 0

            q1 = input("1. Which operator has highest precedence?\n(a) +\n(b) *\n(c) =\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input("\n2. What will be the output of 2 + 3 * 4?\n(a) 20\n(b) 14\n(c) 24\nAnswer: ")
            if q2.lower() == "b":
                score += 1

            q3 = input("\n3. Which brackets are used to change precedence?\n(a) {}\n(b) []\n(c) ()\nAnswer: ")
            if q3.lower() == "c":
                score += 1

            q4 = input("\n4. What will be the output of (2 + 3) * 4?\n(a) 20\n(b) 14\n(c) 9\nAnswer: ")
            if q4.lower() == "a":
                score += 1

            q5 = input(
                "\n5. Which operator is evaluated first in 10 - 2 * 3?\n(a) -\n(b) *\n(c) Both Together\nAnswer: ")
            if q5.lower() == "b":
                score += 1

            q6 = input("\n6. Which operator has lower precedence?\n(a) +\n(b) *\n(c) /\nAnswer: ")
            if q6.lower() == "a":
                score += 1

            q7 = input("\n7. What will be output of 8 / 2 + 2?\n(a) 2\n(b) 6\n(c) 8\nAnswer: ")
            if q7.lower() == "b":
                score += 1

            q8 = input("\n8. Exponent operator in Python is?\n(a) ^\n(b) **\n(c) //\nAnswer: ")
            if q8.lower() == "b":
                score += 1

            q9 = input("\n9. What will be output of 2 ** 3 * 2?\n(a) 16\n(b) 8\n(c) 12\nAnswer: ")
            if q9.lower() == "a":
                score += 1

            q10 = input(
                "\n10. Operator precedence helps in?\n(a) Deciding execution order\n(b) Printing Output\n(c) Taking Input\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 9:

            print("\n========== CONTROL FLOW - IF QUIZ ==========")

            score = 0

            q1 = input(
                "1. Which keyword is used for condition checking in Python?\n(a) loop\n(b) if\n(c) case\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input("\n2. if statement executes when condition is?\n(a) False\n(b) True\n(c) None\nAnswer: ")
            if q2.lower() == "b":
                score += 1

            q3 = input("\n3. Which symbol is used for equality checking?\n(a) =\n(b) ==\n(c) !=\nAnswer: ")
            if q3.lower() == "b":
                score += 1

            q4 = input(
                "\n4. What will happen if condition is False?\n(a) if block executes\n(b) Error occurs\n(c) if block skips\nAnswer: ")
            if q4.lower() == "c":
                score += 1

            q5 = input("\n5. Which operator means 'not equal to'?\n(a) ==\n(b) !=\n(c) >=\nAnswer: ")
            if q5.lower() == "b":
                score += 1

            q6 = input(
                "\n6. Which keyword is used for multiple conditions?\n(a) elif\n(b) break\n(c) continue\nAnswer: ")
            if q6.lower() == "a":
                score += 1

            q7 = input("\n7. Which operator is used for AND condition?\n(a) &&\n(b) and\n(c) &\nAnswer: ")
            if q7.lower() == "b":
                score += 1

            q8 = input("\n8. Which operator is used for OR condition?\n(a) or\n(b) ||\n(c) /\nAnswer: ")
            if q8.lower() == "a":
                score += 1

            q9 = input("\n9. Indentation is important in if statement?\n(a) Yes\n(b) No\n(c) Sometimes\nAnswer: ")
            if q9.lower() == "a":
                score += 1

            q10 = input(
                "\n10. What will be output?\nif 5 > 2:\n    print('Hello')\n(a) Hello\n(b) Error\n(c) Nothing\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 10:

            print("\n========== CONTROL FLOW - ELSE QUIZ ==========")

            score = 0

            q1 = input(
                "1. Which keyword is used when if condition becomes False?\n(a) else\n(b) elif\n(c) break\nAnswer: ")
            if q1.lower() == "a":
                score += 1

            q2 = input(
                "\n2. else block executes when?\n(a) Condition is True\n(b) Condition is False\n(c) Always\nAnswer: ")
            if q2.lower() == "b":
                score += 1

            q3 = input(
                "\n3. Which statement is correct?\n(a) else needs condition\n(b) else has no condition\n(c) else uses loop\nAnswer: ")
            if q3.lower() == "b":
                score += 1

            q4 = input(
                "\n4. Which keyword is used between if and else for multiple conditions?\n(a) elif\n(b) while\n(c) continue\nAnswer: ")
            if q4.lower() == "a":
                score += 1

            q5 = input(
                "\n5. What will be output?\nif 2 > 5:\n    print('A')\nelse:\n    print('B')\n(a) A\n(b) B\n(c) Error\nAnswer: ")
            if q5.lower() == "b":
                score += 1

            q6 = input("\n6. Can we use else without if?\n(a) Yes\n(b) No\n(c) Sometimes\nAnswer: ")
            if q6.lower() == "b":
                score += 1

            q7 = input(
                "\n7. Which statement executes if all conditions become False?\n(a) if\n(b) elif\n(c) else\nAnswer: ")
            if q7.lower() == "c":
                score += 1

            q8 = input("\n8. Indentation is compulsory in else block?\n(a) Yes\n(b) No\n(c) Optional\nAnswer: ")
            if q8.lower() == "a":
                score += 1

            q9 = input(
                "\n9. What will be output?\nif False:\n    print('Hi')\nelse:\n    print('Bye')\n(a) Hi\n(b) Bye\n(c) Error\nAnswer: ")
            if q9.lower() == "b":
                score += 1

            q10 = input("\n10. else statement improves?\n(a) Decision Making\n(b) Loop Speed\n(c) Memory\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 11:

            print("\n========== LOOP QUIZ ==========")

            score = 0

            q1 = input("1. Which loop is best when iterations are known?\n(a) while\n(b) for\n(c) if\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input("\n2. Which loop works on condition?\n(a) for\n(b) while\n(c) match\nAnswer: ")
            if q2.lower() == "b":
                score += 1

            q3 = input(
                "\n3. Which function is commonly used with for loop?\n(a) type()\n(b) range()\n(c) len()\nAnswer: ")
            if q3.lower() == "b":
                score += 1

            q4 = input("\n4. What will range(5) generate?\n(a) 1 to 5\n(b) 0 to 5\n(c) 0 to 4\nAnswer: ")
            if q4.lower() == "c":
                score += 1

            q5 = input("\n5. Infinite loop mostly occurs in?\n(a) if\n(b) while\n(c) print\nAnswer: ")
            if q5.lower() == "b":
                score += 1

            q6 = input("\n6. Which loop is used to traverse list?\n(a) for\n(b) while\n(c) nested\nAnswer: ")
            if q6.lower() == "a":
                score += 1

            q7 = input(
                "\n7. Nested loop means?\n(a) Multiple conditions\n(b) Loop inside loop\n(c) Multiple variables\nAnswer: ")
            if q7.lower() == "b":
                score += 1

            q8 = input("\n8. Which keyword exits loop immediately?\n(a) continue\n(b) skip\n(c) break\nAnswer: ")
            if q8.lower() == "c":
                score += 1

            q9 = input("\n9. Which keyword skips current iteration?\n(a) continue\n(b) break\n(c) stop\nAnswer: ")
            if q9.lower() == "a":
                score += 1

            q10 = input(
                "\n10. Loops help in?\n(a) Repeating tasks\n(b) Creating errors\n(c) Deleting variables\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 12:

            print("\n========== LOOP 2.0 QUIZ ==========")

            score = 0

            q1 = input(
                "1. Which loop can run forever if condition never becomes False?\n(a) for\n(b) while\n(c) if\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input(
                "\n2. What will be output of:\nfor i in range(3):\n    print(i)\n(a) 1 2 3\n(b) 0 1 2\n(c) 0 1 2 3\nAnswer: ")
            if q2.lower() == "b":
                score += 1

            q3 = input("\n3. Which loop is better for counting?\n(a) for\n(b) while\n(c) else\nAnswer: ")
            if q3.lower() == "a":
                score += 1

            q4 = input(
                "\n4. Which loop is mostly used when condition is unknown?\n(a) for\n(b) while\n(c) nested\nAnswer: ")
            if q4.lower() == "b":
                score += 1

            q5 = input(
                "\n5. Which keyword is used with loop to do nothing?\n(a) stop\n(b) pass\n(c) continue\nAnswer: ")
            if q5.lower() == "b":
                score += 1

            q6 = input("\n6. What is the starting value in range(5)?\n(a) 1\n(b) 0\n(c) 5\nAnswer: ")
            if q6.lower() == "b":
                score += 1

            q7 = input("\n7. What will len([1,2,3]) return?\n(a) 2\n(b) 3\n(c) 4\nAnswer: ")
            if q7.lower() == "b":
                score += 1

            q8 = input("\n8. Which loop can iterate through string characters?\n(a) for\n(b) while\n(c) both\nAnswer: ")
            if q8.lower() == "c":
                score += 1

            q9 = input("\n9. Which symbol is used after loop statement?\n(a) ;\n(b) .\n(c) :\nAnswer: ")
            if q9.lower() == "c":
                score += 1

            q10 = input(
                "\n10. Loop control statements are?\n(a) break and continue\n(b) if and else\n(c) print and input\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 13:

            print("\n========== BREAK & CONTINUE QUIZ ==========")

            score = 0

            q1 = input(
                "1. Which keyword is used to stop a loop immediately?\n(a) continue\n(b) break\n(c) pass\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input("\n2. Which keyword skips current iteration?\n(a) continue\n(b) break\n(c) stop\nAnswer: ")
            if q2.lower() == "a":
                score += 1

            q3 = input(
                "\n3. break statement is mostly used inside?\n(a) Conditions\n(b) Loops\n(c) Functions\nAnswer: ")
            if q3.lower() == "b":
                score += 1

            q4 = input(
                "\n4. continue statement sends control to?\n(a) Program End\n(b) Next Iteration\n(c) Previous Iteration\nAnswer: ")
            if q4.lower() == "b":
                score += 1

            q5 = input(
                "\n5. What will break do in infinite loop?\n(a) Continue forever\n(b) Stop loop\n(c) Skip one iteration\nAnswer: ")
            if q5.lower() == "b":
                score += 1

            q6 = input(
                "\n6. Which statement is correct?\n(a) break skips iteration\n(b) continue stops loop\n(c) break exits loop\nAnswer: ")
            if q6.lower() == "c":
                score += 1

            q7 = input(
                "\n7. What will continue do?\n(a) Stop program\n(b) Skip current iteration\n(c) Exit function\nAnswer: ")
            if q7.lower() == "b":
                score += 1

            q8 = input("\n8. Can break be used in while loop?\n(a) Yes\n(b) No\n(c) Sometimes\nAnswer: ")
            if q8.lower() == "a":
                score += 1

            q9 = input(
                "\n9. Which statement is used to control loop flow?\n(a) break\n(b) continue\n(c) Both\nAnswer: ")
            if q9.lower() == "c":
                score += 1

            q10 = input(
                "\n10. break and continue improve?\n(a) Loop Control\n(b) Memory Size\n(c) File Handling\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 14:

            print("\n========== FOR-ELSE & WHILE-ELSE QUIZ ==========")

            score = 0

            q1 = input(
                "1. else block in loop executes when?\n(a) Loop ends normally\n(b) break is used\n(c) Error occurs\nAnswer: ")
            if q1.lower() == "a":
                score += 1

            q2 = input(
                "\n2. Which loops support else block in Python?\n(a) for only\n(b) while only\n(c) both for and while\nAnswer: ")
            if q2.lower() == "c":
                score += 1

            q3 = input("\n3. If break executes, else block will?\n(a) Execute\n(b) Skip\n(c) Repeat\nAnswer: ")
            if q3.lower() == "b":
                score += 1

            q4 = input("\n4. for-else is mostly used in?\n(a) Searching\n(b) Printing\n(c) Input\nAnswer: ")
            if q4.lower() == "a":
                score += 1

            q5 = input("\n5. Which keyword stops loop immediately?\n(a) continue\n(b) break\n(c) else\nAnswer: ")
            if q5.lower() == "b":
                score += 1

            q6 = input(
                "\n6. while-else executes else when condition becomes?\n(a) True\n(b) False\n(c) Integer\nAnswer: ")
            if q6.lower() == "b":
                score += 1

            q7 = input("\n7. Which loop checks condition first?\n(a) while\n(b) for\n(c) else\nAnswer: ")
            if q7.lower() == "a":
                score += 1

            q8 = input("\n8. continue statement affects else block?\n(a) Yes\n(b) No\n(c) Sometimes\nAnswer: ")
            if q8.lower() == "b":
                score += 1

            q9 = input(
                "\n9. Which statement is correct?\n(a) else cannot be used with loops\n(b) else works with loops\n(c) else only works with if\nAnswer: ")
            if q9.lower() == "b":
                score += 1

            q10 = input(
                "\n10. for-else and while-else improve?\n(a) Decision Making\n(b) Loop Logic\n(c) Graphics\nAnswer: ")
            if q10.lower() == "b":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 15:

            print("\n========== MEMBERSHIP OPERATOR QUIZ ==========")

            score = 0

            q1 = input("1. Which membership operator checks presence of value?\n(a) in\n(b) is\n(c) ==\nAnswer: ")
            if q1.lower() == "a":
                score += 1

            q2 = input("\n2. Which operator checks value is NOT present?\n(a) not\n(b) not in\n(c) !=\nAnswer: ")
            if q2.lower() == "b":
                score += 1

            q3 = input(
                "\n3. Membership operators mostly work with?\n(a) Collections\n(b) Loops only\n(c) Conditions only\nAnswer: ")
            if q3.lower() == "a":
                score += 1

            q4 = input("\n4. What will be output?\n'a' in 'apple'\n(a) True\n(b) False\n(c) Error\nAnswer: ")
            if q4.lower() == "a":
                score += 1

            q5 = input("\n5. Which data type supports membership operator?\n(a) list\n(b) string\n(c) both\nAnswer: ")
            if q5.lower() == "c":
                score += 1

            q6 = input("\n6. What will be output?\n5 in [1,2,3,4]\n(a) True\n(b) False\n(c) Error\nAnswer: ")
            if q6.lower() == "b":
                score += 1

            q7 = input("\n7. Membership operators return?\n(a) Integer\n(b) Boolean\n(c) String\nAnswer: ")
            if q7.lower() == "b":
                score += 1

            q8 = input("\n8. What will be output?\n2 in [1,2,3]\n(a) True\n(b) False\n(c) None\nAnswer: ")
            if q8.lower() == "a":
                score += 1

            q9 = input("\n9. Which keyword checks absence of element?\n(a) in\n(b) not in\n(c) else\nAnswer: ")
            if q9.lower() == "b":
                score += 1

            q10 = input(
                "\n10. Membership operators are useful for?\n(a) Searching values\n(b) Creating loops\n(c) Memory management\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 16:

            print("\n========== CONDITIONAL EXPRESSION QUIZ ==========")

            score = 0

            q1 = input(
                "1. Conditional expression is also called?\n(a) Nested Loop\n(b) Ternary Operator\n(c) Membership Operator\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input(
                "\n2. Conditional expression is used for?\n(a) Short decision making\n(b) Looping\n(c) Pattern printing\nAnswer: ")
            if q2.lower() == "a":
                score += 1

            q3 = input("\n3. Which keyword is used in ternary operator?\n(a) if\n(b) while\n(c) break\nAnswer: ")
            if q3.lower() == "a":
                score += 1

            q4 = input(
                "\n4. What will be output?\nprint('Yes' if 5 > 2 else 'No')\n(a) Yes\n(b) No\n(c) Error\nAnswer: ")
            if q4.lower() == "a":
                score += 1

            q5 = input("\n5. Conditional expression returns?\n(a) One value\n(b) Multiple loops\n(c) Object\nAnswer: ")
            if q5.lower() == "a":
                score += 1

            q6 = input(
                "\n6. Which statement is correct?\n(a) Ternary operator shortens code\n(b) Ternary operator creates loop\n(c) Ternary operator deletes variables\nAnswer: ")
            if q6.lower() == "a":
                score += 1

            q7 = input("\n7. else keyword in ternary operator is?\n(a) Optional\n(b) Compulsory\n(c) Invalid\nAnswer: ")
            if q7.lower() == "b":
                score += 1

            q8 = input(
                "\n8. Conditional expression improves?\n(a) Code readability\n(b) Memory size\n(c) Hardware speed\nAnswer: ")
            if q8.lower() == "a":
                score += 1

            q9 = input(
                "\n9. Which operator is mostly replaced by ternary operator?\n(a) if-else\n(b) for loop\n(c) while loop\nAnswer: ")
            if q9.lower() == "a":
                score += 1

            q10 = input(
                "\n10. Ternary operator is best for?\n(a) Simple conditions\n(b) Long programs\n(c) Nested classes\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 17:

            print("\n========== MATCH CASE QUIZ ==========")

            score = 0

            q1 = input("1. Which keyword starts match-case statement?\n(a) case\n(b) match\n(c) switch\nAnswer: ")
            if q1.lower() == "b":
                score += 1

            q2 = input("\n2. match-case is similar to?\n(a) switch statement\n(b) loop\n(c) function\nAnswer: ")
            if q2.lower() == "a":
                score += 1

            q3 = input("\n3. Which keyword defines different options?\n(a) if\n(b) loop\n(c) case\nAnswer: ")
            if q3.lower() == "c":
                score += 1

            q4 = input("\n4. Which symbol is used as default case?\n(a) *\n(b) _\n(c) #\nAnswer: ")
            if q4.lower() == "b":
                score += 1

            q5 = input("\n5. match-case was introduced in Python?\n(a) 3.10\n(b) 2.0\n(c) 1.0\nAnswer: ")
            if q5.lower() == "a":
                score += 1

            q6 = input("\n6. match statement compares?\n(a) Conditions\n(b) Values\n(c) Variables only\nAnswer: ")
            if q6.lower() == "b":
                score += 1

            q7 = input(
                "\n7. Which statement is correct?\n(a) match-case improves readability\n(b) match-case creates loops\n(c) match-case deletes variables\nAnswer: ")
            if q7.lower() == "a":
                score += 1

            q8 = input("\n8. Which keyword works like default option?\n(a) else\n(b) _\n(c) break\nAnswer: ")
            if q8.lower() == "b":
                score += 1

            q9 = input("\n9. Indentation is important in match-case?\n(a) Yes\n(b) No\n(c) Sometimes\nAnswer: ")
            if q9.lower() == "a":
                score += 1

            q10 = input(
                "\n10. match-case is best for?\n(a) Multiple choices\n(b) Pattern printing\n(c) File handling\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 18:

            print("\n========== NESTED LOOPS QUIZ ==========")

            score = 0

            q1 = input(
                "1. Nested loop means?\n(a) Loop inside another loop\n(b) Multiple variables\n(c) Function inside function\nAnswer: ")
            if q1.lower() == "a":
                score += 1

            q2 = input(
                "\n2. Nested loops are mostly used for?\n(a) Pattern printing\n(b) Memory management\n(c) File handling\nAnswer: ")
            if q2.lower() == "a":
                score += 1

            q3 = input("\n3. Which loop can be nested?\n(a) for\n(b) while\n(c) both\nAnswer: ")
            if q3.lower() == "c":
                score += 1

            q4 = input("\n4. Outer loop controls?\n(a) Columns\n(b) Rows\n(c) Variables\nAnswer: ")
            if q4.lower() == "b":
                score += 1

            q5 = input("\n5. Inner loop mostly controls?\n(a) Rows\n(b) Columns\n(c) Functions\nAnswer: ")
            if q5.lower() == "b":
                score += 1

            q6 = input(
                "\n6. How many times inner loop runs?\n(a) Depends on outer loop\n(b) Only one time\n(c) Never\nAnswer: ")
            if q6.lower() == "a":
                score += 1

            q7 = input("\n7. Nested loops increase?\n(a) Complexity\n(b) Simplicity only\n(c) Comments\nAnswer: ")
            if q7.lower() == "a":
                score += 1

            q8 = input("\n8. Which symbol is required after loop statement?\n(a) ;\n(b) :\n(c) ,\nAnswer: ")
            if q8.lower() == "b":
                score += 1

            q9 = input("\n9. Which keyword exits loop immediately?\n(a) continue\n(b) break\n(c) pass\nAnswer: ")
            if q9.lower() == "b":
                score += 1

            q10 = input(
                "\n10. Nested loops are important for?\n(a) Matrix operations\n(b) Audio editing\n(c) Browser opening\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 19:

            print("\n========== PATTERN PRINTING QUIZ ==========")

            score = 0

            q1 = input("1. Pattern printing mostly uses?\n(a) Loops\n(b) Functions\n(c) Classes\nAnswer: ")
            if q1.lower() == "a":
                score += 1

            q2 = input("\n2. Which loop is mostly used in pattern printing?\n(a) for\n(b) if\n(c) match\nAnswer: ")
            if q2.lower() == "a":
                score += 1

            q3 = input(
                "\n3. Which concept is commonly used with patterns?\n(a) Nested loops\n(b) File handling\n(c) Exception handling\nAnswer: ")
            if q3.lower() == "a":
                score += 1

            q4 = input("\n4. Outer loop represents?\n(a) Rows\n(b) Columns\n(c) Variables\nAnswer: ")
            if q4.lower() == "a":
                score += 1

            q5 = input("\n5. Inner loop represents?\n(a) Functions\n(b) Columns\n(c) Comments\nAnswer: ")
            if q5.lower() == "b":
                score += 1

            q6 = input("\n6. Which symbol is commonly printed in patterns?\n(a) *\n(b) @\n(c) Both\nAnswer: ")
            if q6.lower() == "c":
                score += 1

            q7 = input(
                "\n7. Pattern printing improves understanding of?\n(a) Loops\n(b) Conditions\n(c) Both\nAnswer: ")
            if q7.lower() == "c":
                score += 1

            q8 = input("\n8. Which loop can also be used for patterns?\n(a) while\n(b) for\n(c) both\nAnswer: ")
            if q8.lower() == "c":
                score += 1

            q9 = input(
                "\n9. Which statement is important in pattern printing?\n(a) Proper indentation\n(b) Browser\n(c) Audio\nAnswer: ")
            if q9.lower() == "a":
                score += 1

            q10 = input(
                "\n10. Pattern printing mainly helps in understanding?\n(a) Logic building\n(b) Gaming\n(c) Networking\nAnswer: ")
            if q10.lower() == "a":
                score += 1

            print("\nYour Final Score =", score, "/10")
        case 20:

            print("\nThank You For Using Python Quiz ❤️")
            print("Keep Learning Python 🚀")

            break
        case _:
            print("\nInvalid Choice ❌")