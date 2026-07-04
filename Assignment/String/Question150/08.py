"""
8Toggle the case of each character. S = "MiXED" "mIxeD"

"""
s=input("Enter a string")
new=""
low=""
up=""
for i in s:
    if i>='A' and i<='Z':
        low=chr(ord(i)+32)
        new+=low
    else:
        up=chr(ord(i)-32)
        new+=up
    #new=low+up
print(new)

