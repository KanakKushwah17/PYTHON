"""
46Check if a substring appears at both the start and end. S = "abcabca", Sub="abca" TRUE
"""

s=input("Enter a string: ")
sub=input("Enter a substring: ")
flag=0
for i in range(len(sub)):
        if s[i]!=sub[i]:
            flag=1
            break

for i in range(1,len(sub)+1):
    if s[-i]!=sub[-i]:
        flag=1
        break

if flag==0:
    print("True")
else:
    print("False")