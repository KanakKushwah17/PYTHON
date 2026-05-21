"""
2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
"""
from itertools import product
from unittest import result

n=int(input("Enter the number: "))
sum=0
temp=n
count=0
pro=1
while n>0:
    rem=n%10
    sum= sum + rem
    pro=pro*rem
    n=n//10
print("Sum of Digits: ",sum)
print("Product of Digits: ",pro)
diff=abs(sum-pro)
print("Difference: ",diff)
diff2=diff
rem=0
while diff>0:
    rem=diff%10
    count=count+1
    diff=diff//10
print("Count of Digits: ",count)
result=diff2+count
print("Sum of count and diff: ",result)
x=0
if result<=1:
    print("Not Prime")
else:
    i=2
    while i<=result//2+1:
        if result%i==0:
            x=1
        i = i + 1
        break

if x==0:
    print("Prime number ")
else:
    print("Not Prime")

