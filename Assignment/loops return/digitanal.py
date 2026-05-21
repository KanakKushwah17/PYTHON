"""
1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number
"""
n=int(input("Enter a number:"))
product=1
min=999999
sum=0
temp=n
count=0
while n>9:
    rem=n%10
    n=n//10
    rem1=n%10
    product=rem*rem1
    print("products:",product)
    if product<min:
        min=product
    sum=sum+product
    c=rem1
    rem1=rem
print("Sum:",sum)
print("Smallest:",min)
rem=0
while temp>0:
    rem=temp%10
    count=count+1
    temp=temp//10
if sum%count==0:
    print("Stable number ")
else:
    print("Unstable number")