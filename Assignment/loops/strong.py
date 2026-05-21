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
num=int(input("Enter the digit :"))
temp=num
fact=1
sum=0
while num>0:
    rem=num%10
    fact = 1
    while rem>0:
        fact=fact*rem
        rem=rem-1
    sum=sum+fact
    num=num//10
print("sum :",sum)
if sum==temp:
    print("Strong number ")
else:
    print("Not strong number ")
        