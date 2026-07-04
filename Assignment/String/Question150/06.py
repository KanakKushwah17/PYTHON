"""
6Convert a string to uppercase. S = "hello" "HELLO"

"""
s=input("Enter a string: ")
res=0
new=""
for i in s:
    res=ord(i)-32
    new=new+chr(res)
print(new)

    
