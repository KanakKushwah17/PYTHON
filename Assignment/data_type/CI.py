"""

Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0


"""





P = int(input("Enter Principal: "))
R = int(input("Enter Rate: "))
T = int(input("Enter Time: "))

A = P * (1 + R/100) ** T

print("Amount after interest =", A)