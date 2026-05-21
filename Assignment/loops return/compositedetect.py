"""
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2

"""

n=int(input("Enter the number :"))
temp=n

count=0
for i in range(1,n//2+1):
     if n%i==0:
         count=count+1

if count>=2:
    print("Composite Number")
else:
    print("Not Composite Number")
fact=0
min=0
for i in range(1,temp+1):
    if temp%i==0:
        fact=fact+1
        if i > 1 and min == 0:
            min = i

print("Factors count =",fact)
print("Smallest Factor =",min)







