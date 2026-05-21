"""
A
BCD
EFGHI
JKLMNOP

"""
n=int(input("Enter the number:"))
ch=65
for i in range(1,n+1):
    for j in range(1,i*2):
        print(chr(ch),end=" ")
        ch = ch + 1
    print()

