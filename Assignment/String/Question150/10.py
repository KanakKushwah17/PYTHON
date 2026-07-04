"""
10Trim leading, trailing, or extra spaces. S = "  hello  world  " "hello world"

"""
s=input("Enter the string ")
new=""
s=s.split()
for i in s :
    if i==" ":
        pass
    else:
        new=new+i +" "
print(new)