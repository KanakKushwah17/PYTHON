"""
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong

---
"""
n=int(input("Enter the number : "))
copy=n
sum=0
while n>0:
    rem=n%10
    cube=rem*rem*rem
    sum=sum+cube
    n=n//10
print(sum)
if copy==sum:
    print("Armstrong")
else:
    print("Not Armstrong ")