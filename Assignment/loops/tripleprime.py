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
n=int(input("Enter the number "))
sum_digit=0
rev=0
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    sum_digit = sum_digit + rem
    n=n//10
print("Sum of digits :",sum_digit)
print("Reverse :",rev)
diff = abs(rev-temp)
print("Difference :",diff)
Add=sum_digit+diff
print("Addition :",Add)


if Add<=1:
    print("Not Prime Number ")
else:
    i=2
    x = 0
    while i<=Add//2:
        if Add%i==0:
            x=1
            break
        i = i + 1
if x==0:
    print("Prime number ")
else:
    print("Not Prime Number ")


