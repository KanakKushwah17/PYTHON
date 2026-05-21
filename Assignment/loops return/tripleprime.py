"""
1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime
"""

n=int(input("Enter the number: "))
sum=0
rev=0
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    sum= sum + rem
    n=n//10
print("Sum of Digits: ",sum)
print("Reverse: ",rev)
diff=abs(temp-rev)
print("Difference: ",diff)
add=sum+diff
print("final result: ",add)
x=0
if add<=1:
    print("Not prime number")
else:
    for i in range(2,add//2+1):
        if add%i==0:
            x=1
            break
        else:
            x=0

if x==0:
    print("Prime number")
else:
    print("Not prime number")