"""
7Convert a string to lowercase. S = "HELLO" "hello"

"""
s = input("Enter a string")
new = ""

for i in s:
    if i >= 'a' and i <= 'z':
        new = new + i

    else:
        new = new + chr(ord(i) + 32)

print(new)
