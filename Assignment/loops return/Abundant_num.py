"""
9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number

"""
n=int(input("Enter a number:"))
sum=0
temp=n
for i in range(1,n//2+1):
    if n%i==0:
        sum=sum+i
if sum>temp:
    print("Abundant Number")
else:
    print("Not Abundant Number")
