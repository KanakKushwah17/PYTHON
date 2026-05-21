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
n=int(input("Enter a number: "))
sum=0
zero=0
min_digit=9
while n>0:
     rem=n%10
     sum=sum+rem
     if rem==0:
        zero=zero+1
     if rem<min_digit:
        min_digit=rem  
    
     n=n//10
print("Zero count",zero)
print("Sum =",sum)
print("smallest digit =",min_digit)

result = (sum + zero)*min_digit
print("Final Result =", result)

x=0
if result<=1:
   x=1
i=2
while i<result:
   if result%i==0:
       x=1
       break
   i=i+1
   
if x==0:
    print("Prime Number")
else:
    print("Not a prime number")


