"""
Given two binary strings a and b, return their sum as a binary string.
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""

a=input("Enter the first binary string: ")
b=input("Enter the second binary string: ")

c=int(a,2)

d=int(b,2)

sum=c+d

res=bin(sum)[2:]
print(res)



