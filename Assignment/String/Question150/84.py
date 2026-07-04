"""
84Print ASCII value of each character. S = "A" A: 65

"""
s=input("Enter a string: ")
result=""
for i in s:
    result=ord(i)
print(result)