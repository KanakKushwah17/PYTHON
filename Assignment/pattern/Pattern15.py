"""
A
BB
CCC
DDDD
EEEEE

"""
n=int(input("Enter the number:"))
ch=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch), end="")
    ch=ch+1
    print()

