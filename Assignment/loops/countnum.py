"""
2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4
"""
num1,num2=map(int,input("Enter the 2 number :").split())

count=0

while num1<=num2:
    if num1%7==0:
        count=count+1
    num1=num1+1
print("Output :",count)