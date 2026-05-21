"""
7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
"""
n=int(input("Enter number:"))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("Sum of digits =",sum)
x=0
if sum<=1:
    print("Normal Number")
else:
    i = 2
    while i<=sum//2+1:
        if sum%i==0:
            x=1
            break
        i=i+1

if x==0:
    print("Lucky Number")
else:
    print("Normal Number")


