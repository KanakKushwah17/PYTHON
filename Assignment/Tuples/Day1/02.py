"""
2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")
"""
n=int(input("Enter an integer: "))
password=[]
for i in range(n):
    password.append(input("Enter an element: "))
print(password)

count=0


for i in range(n):
    found = 0
    for j in range(i+1,n):
        word=password[i]
        for a in password[j]:
            if a in word:
                found=1
                break
        if found==0:
            count+=1

print("count",count)