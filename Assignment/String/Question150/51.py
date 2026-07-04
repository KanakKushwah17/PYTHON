"""
51Extract only digits. S = "a1b2c3" "123"

"""
s=input("Enter s: ")
res=""
for i in s:
    if i>='0' and i<='9':
        res=res+i
print(res)