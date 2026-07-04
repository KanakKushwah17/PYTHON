"""
18Replace occurrences of a character. S = "apple", Old='p', New='x' "axxle"

"""
s=input("Enter a string")
old=input("Enter a old string")
new=input("Enter a new string")
renew=""
for i in s:
    if i == old:
         renew=renew+new
    else:
        renew+=i
print(renew)