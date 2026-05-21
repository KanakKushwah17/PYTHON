
"""
8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4
"""

num=int(input("Enter number : "))
num2 = int(input("Enter number : "))
count=0
while num<=num2:
    if num%5==0:
        count=count+1
    num=num+1
print("Output : ",count)