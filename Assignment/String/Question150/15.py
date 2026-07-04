"""
15Find the last occurrence of a character. S = "banana", Char = 'a' 5 (index)

"""
s=input("Enter a string: ")
char=input("Enter a character: ")

pos=-1
for i in range(len(s)):
    if char==s[i]:
        pos=i
print(pos)