"""
13Get the Unicode code point before index. S = "Hello", Index = 1 72 (Unicode for 'H')

"""
s=input("Enter a string: ")
index=int(input("Enter a number: "))
print(ord(s[index-1]))