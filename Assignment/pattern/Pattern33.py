"""
ABCDE
ABCD
ABC
AB
A


"""
n=int(input("Enter a number: "))

for i in range(n,0,-1):
    ch = 65
    for j in range(i,0,-1):
        print(chr(ch),end=" ")
        ch=ch+1
    print()