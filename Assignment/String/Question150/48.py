"""
48Remove all vowels. S = "aeiou XYZ" " XYZ"

"""
str=input("Enter a string: ")
new=""
for i in range(len(str)):
    if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='u' or str[i]=='o':
        pass
    else:
        new=new+str[i]
print(new)
