"""
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
"""
n=int(input("Enter number "))
sum=0
while n>0:
    fact = 1
    rem=n%10
    for i in range(rem,0,-1):
        fact=fact*i
        print(fact)
    n=n//10
    sum=fact+sum
print("Sum = ",sum)