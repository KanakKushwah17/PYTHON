"""
ABCDE
A  D
A C
AB
A

"""
n=int(input("Enter a number: "))
for i in range(1,n+1):
    ch=65
    for j in range(1,n+1):
        if i+j==6 or i==1 or j==1:
            print(chr(ch),end=" ")
        else:
            print(" ",end=" ")
        ch=ch+1
    print()
