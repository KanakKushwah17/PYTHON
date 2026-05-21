"""
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong
"""
n=int(input("Enter number: "))
cube=1
sum_digit=0
temp=n
while n>0:
    rem=n%10
    cube=rem*rem*rem
    sum_digit=cube+sum_digit
    n=n//10
if sum_digit==temp:
    print("Armstrong number ")
else:
    print("Not a Armstrong number")

