"""
82Create a string from a character array. Char[] = {'h', 'i'} "hi"

"""

s=list(input("Enter a character array: "))
print(s)
new=""
for i in s:
    new+=i
print(new)
