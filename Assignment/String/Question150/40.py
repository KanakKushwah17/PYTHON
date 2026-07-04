"""
40Search all occurrences of a word. S = "a b a b", Word='b' 2, 6 (start indices)

"""
s=input("Enter s: ")
char=input("char: ")
i=0
while i<len(s):
    if s[i]==char:
        print(i,end=",")
    i=i+1