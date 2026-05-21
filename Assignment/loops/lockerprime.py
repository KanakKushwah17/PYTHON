"""
2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
"""
from bdb import Breakpoint

n=int(input("Enter a number: "))
sum_digit=0
prod=1
count_digit=0
while n>0:
    rem=n%10
    sum_digit=sum_digit+rem
    prod=prod*rem
    n=n//10
print("Sum of digits: ",sum_digit)
print("Product of digits: ",prod)
Diff = abs(prod-sum_digit)
print("Difference: ",Diff)
tempdiff=Diff
while Diff>0:
    rem1=Diff%10
    count_digit=count_digit+1
    Diff=Diff//10
print("Count digits: ",count_digit)
Add= count_digit+tempdiff
print("Added digits: ",Add)

if Add<=1:
    print("Not Prime Number ")
else:
    i=2
    x = 0
    while i<=Add//2:
        if Add%i==0:
            x=1
            break
        i = i + 1
if x==0:
    print("Prime number ")
else:
    print("Not Prime Number ")

