"""
2.
NUMBER ANALYSIS SYSTEM

Scenario:

A software company wants to develop a Number Analysis System. The application should be menu-driven and perform different mathematical operations on a given number.

MENU

1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit

Requirements

Choice 1 – Check Perfect Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return True if the number is Perfect, otherwise False.
* Display an appropriate message based on the returned value.

Choice 2 – Check Prime Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return a message such as "Prime Number" or "Not a Prime Number".
* Display the returned message.

Choice 3 – Find Reverse of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return the reversed number.
* Display the returned value.

Choice 4 – Calculate Factorial

* Accept a number from the user.
* Pass the number to a function.
* The function should return the factorial value.
* Display the returned value.

Choice 5 – Display Factors of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return all factors of the given number.
* Display the returned factors.

Choice 6 – Exit

Sample Output

Enter Choice : 1

Enter Number : 28

28 is a Perfect Number

---

Enter Choice : 2

Enter Number : 17

Prime Number

---

Enter Choice : 3

Enter Number : 1234

Reverse Number : 4321

---

Enter Choice : 4

Enter Number : 5

Factorial : 120

---

Enter Choice : 5

Enter Number : 12

Factors : 1 2 3 4 6 12

---

Important Instructions

1. Create separate functions for each operation.
2. Use parameters to pass values to functions.
3. Use return statements appropriately.
4. Different functions should return different types of values such as Boolean, String, Integer, and Collection/List.
5. Avoid using global variables.
6. Implement the solution using a menu-driven approach.
7. Write meaningful function names and maintain proper code readability.
"""

while True:
    print("Enter Choice : ")
    print("1. Check Perfect Number")
    print("2. Check Prime Number")
    print("3. Find Reverse of a Number")
    print("4. Calculate Factorial")
    print("5. Display Factors of a Number")
    print("6. Exit")
    choice = int(input("Enter Choice : "))
    match choice:
        case 1:

            def perfect(num):
                sum = 0
                for i in range(1,num):
                    if num%i==0:
                        sum=sum+i
                if sum==num:
                    return True
                else:
                    return False


            num = int(input("Enter Number : "))
            print("================================")
            print("Perfect number is :",perfect(num))
            print("=================================")


        case 2:
            def prime(num):
                isprime = 0
                if num <= 1:
                    print("Not prime ")
                i = 2
                while i < num // 2:
                    if num % i == 0:
                        isprime = 1
                        break
                    i = i + 1
                if isprime == 0:
                   return "Prime Number"
                else:
                   return "Not a Prime Number"
            num = int(input("Enter Number : "))
            print("==========================")
            print("Number is : ",prime(num))
            print("==========================\n ")

        case 3:
            def reverse(num):
                  rev=""
                  for i in num:
                      rev=i+rev
                  return rev

            num = input("Enter Number : ")
            print("===================================")
            print("Reverse Number is : ",reverse(num))
            print("===================================")
            print()


        case 4:
            def factorial(num):
                fact=1
                for i in range(1,num+1):
                    fact=i*fact
                return fact
            num = int(input("Enter Number : "))
            print("=====================================")
            print("Factorial number is : ",factorial(num))
            print("======================================")
            print()

        case 5:
            def factors(num):
                fact=[]
                for i in range(1,num+1):
                    if num%i==0:
                        fact=i
                return fact

            num=int(input("Enter Number : "))
            print("Factorial number is : ",factors(num))
            print("====================================")
            print()

        case 6:
            break





