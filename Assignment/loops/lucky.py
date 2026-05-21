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
num=int(input("Enter the digit :"))
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
print("Sum =",sum)
isprime=0
if sum<=1:
   print("Not prime ")
i=2
while i<sum//2:#optimize Version
   if sum%i==0:
       isprime=1
       break
   i=i+1
if isprime==0:
    print("Lucky Number")
else:
    print("Normal number")