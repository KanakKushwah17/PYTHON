from MyPackage1 import reversenum, primenumber, calculatefactorial,perfect_number

perfect = perfect_number.perfect
prime = primenumber.prime
reverse = reversenum.reverse
factorial = calculatefactorial.factorial

while True:
    print("""

=================================
      NUMBER ANALYSIS SYSTEM
=================================
1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit    
""")
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            n = int(input("Enter Number : "))
            print(f"{n}",perfect(n))
        
        case 2:
            n = int(input("Enter Number : "))
            print(f"{n}",prime(n))
            
        case 3:
            n = int(input("Enter Number : "))
            print("Reverse : ",reverse(n))
            
        case 4:
            n = int(input("Enter Number : "))
            print("Factorial : ",factorial(n))
                     
        case 5:
            print("Thanks for using NUMBER ANALYSIS SYSTEM.\nVisit again ...")
            break
            
        case _:
            break