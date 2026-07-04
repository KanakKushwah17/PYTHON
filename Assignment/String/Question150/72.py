
"""
72Print all substrings of length n. S = "abc", n = 2 "ab, bc"
"""

s=input("Enter a string: ")
n=int(input("Enter a number: "))
for i in range(len(s)):
    for j in range(i,len(s)):
        sub=s[i:j+1]
        if len(sub)==n:
            print(sub)