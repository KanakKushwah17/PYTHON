"""
52Remove all special characters. S = "a!@b#c" "abc"

"""
s=input("Enter s: ")
new=""
for i in s:
    if i=='!' or i=='@' or i=='#' or i=='#':
        continue
    else:
        new=new+i
print(new)