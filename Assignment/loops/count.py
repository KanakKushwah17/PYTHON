"""

*9. Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
"""
n=int(input("Enter the number : "))
count=0
count2=0
while n>0:
    rem=n%10
    if rem%2==0:
        count=count+1
    count2=count2+1
    n=n//10
if count==count2:
    print("All even")

n=int(input("Enter the number : "))
count=0
count2=0
while n>0:
    rem=n%10
    if rem%2==0:
        count=count+1
    count2=count2+1
    n=n//10
if count!=count2:
    print("Not all even ")

