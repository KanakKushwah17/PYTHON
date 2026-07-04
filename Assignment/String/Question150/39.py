"""
39Search all occurrences of a character. S = "banana", Char='a' 1, 3, 5 (indices)

"""

s=input("Enter s: ")
char=input("char: ")
i=0
while i<len(s):
    if s[i]==char:
        print(i,end=",")
    i=i+1