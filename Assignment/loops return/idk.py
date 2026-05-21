"""
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
"""

n=int(input("Enter Number:"))
small=9
temp=n
sum=0
count=0
while n>0:
    rem=n%10
    sum=sum+rem
    if rem==0:
        count=count+1
    n=n//10
print("Zero count = ",count)
print("Sum = ",sum)
add=count+sum
print("Add = ",add)
rem=0
while temp>0:
    rem=temp%10
    if  small>rem:
        small=rem
    temp=temp//10
print("Smallest digit = ",small)
mult=small*add
print("Multiply number is : ",mult)
x=0
if mult<=1:
    print("Not prime number")
else:
    for i in range(2,mult//2+1):
        if mult%i==0:
            x=1
            break
        else:
            x=0
if x==0:
    print("Prime number")
else:
    print("Not prime number")

