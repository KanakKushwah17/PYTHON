"""
11Get the character at a given index. S = "Python", Index = 2 t'

"""
s=input("Enter a string: ")
index=int(input("Enter an index: "))
for i in range(len(s)):
    if index==i:
        print(s[i])
