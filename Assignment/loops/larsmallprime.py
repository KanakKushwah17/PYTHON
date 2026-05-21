"""
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
"""
n=int(input("Enter a number: "))
max=0
min=9
temp=n

#big
while n>0:
    rem=n%10
    if max<rem:
        max=rem
    n=n//10
print("Largest = ",max)
# small
rem=0
while temp>0:
    rem=temp%10
    if min>rem:
        min=rem
    temp=temp//10
print("smallest = ",min)

sum=min+max
print("Sum =",sum)

x=0
if sum<=1:
   print("Not prime ")
i=2
while i<sum:
   if sum%i==0:
       x=1
       break
   i=i+1
   
if x==0:
    print("Prime Number")
else:
    print("Not a prime number")
   
       