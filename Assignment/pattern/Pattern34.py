"""
EEEEE
DDDD
CCC
BB
A
"""
n=int(input("Enter a number: "))
ch=69
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(chr(ch),end=" ")
    ch=ch-1
    print()