"""
A
AB
A C
A  D
ABCDE

"""
n=int(input("Enter a number: "))
for i in range(1,n+1):
    ch=65
    for j in range(1,i+1):
        if j==i or j==1 or i==n:
            print(chr(ch),end=" ")
        else:
            print(" ",end=" ")
        ch=ch+1
    print()