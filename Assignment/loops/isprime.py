num=int(input("Enter the digit :"))

isprime=0
if num<=1:
   print("Not prime ")
i=2
while i<num//2:#optimize Version
   if num%i==0:
       isprime=1
       break
   i=i+1
if isprime==0:
    print("Prime Number")
else:
    print("Not a prime number")

"""
num=int(input("Enter the digit :"))

x=0
if num<=1:
   print("Not prime ")
i=2
while i<num:
   if num%i==0:
       x=1
       break
   i=i+1
   
if x==0:
    print("Prime Number")
else:
    print("Not a prime number")








import math
num=int(input("Enter the digit :"))

x=0
if num<=1:
   print("Not prime ")
i=2
while i<=int(math.sqrt(num)):
   if num%i==0:
       x=1
       break
   i=i+1
   
if x==0:
    print("Prime Number")
else:
    print("Not a prime number")

 
"""