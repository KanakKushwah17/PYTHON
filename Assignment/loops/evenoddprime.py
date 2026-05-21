"""
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
"""
n=int(input("Enter a number: "))
count=0
count2=0
while n>0:
    rem=n%10
    if rem%2==0:
        count=count+1
    else:
        count2=count2+1
    n=n//10

print("Even Count =", count)
print("Odd Count =", count2)

diff=abs(count-count2)
print("Difference :",diff)
x=0
if diff<=1:
   x=1
i=2
while i<diff:
   if diff%i==0:
       x=1
       break
   i=i+1
   
if x==0:
    print("Prime Number")
else:
    print("Not a prime number")
   


