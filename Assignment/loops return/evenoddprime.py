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
n=int(input("Enter a number:"))
even=0
odd=0
while n>0:
    rem=n%10
    if rem%2==0:
        even=even+1
    else:
        odd=odd+1
    n=n//10
print("Even Count =",even)
print("Odd Count =",odd)
diff=abs(even-odd)
print("Difference =",diff)
x=0
if diff<=1:
    print("Not Prime")
else:
    for i in range (2,diff//2+1):
        if diff%i==0:
            x=1
            break

    if x==0:
        print("Prime")
    else:
        print("Not Prime")
