"""
1
01
101
0101
10101
"""
n=int(input("Enter a number: "))
for i in range(0,n+1):
    for j in range(0,i):
        if (i+j)%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()
