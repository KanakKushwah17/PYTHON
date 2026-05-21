"""
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
"""
n=int(input("Enter a number: "))
temp=n

while True:
    n=n+1
    if n<=1:
        continue
    else:
        x=0
        i=2
        while i<=n//2+1:
            if n%i==0:
                x=1
                i = i + 1
                continue
            else:
                i=i+1
        if x==0:
            print("Prime Number",n)
            break



