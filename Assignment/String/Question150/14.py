"""

14Find the first occurrence of a character. S = "banana", Char = 'a' 1 (index)

"""
s=input("Enter a string: ")
char=input("Enter a character: ")
for i in range(len(s)):
    if s[i]==char:
        print(i)
        break
