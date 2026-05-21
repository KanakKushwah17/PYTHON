"""
5.
Tech Number Checker

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number
"""
n=int(input("Enter number:"))
l=len(str(n))

count=0
temp=n
while n>0:
    rem=n%10
    count=count+1
    n=n//10
print(count)
if count%2==0:
    rem=n%10
    
