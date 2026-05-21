"""
55555
4  4
3 3
22
1

"""
n=int(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i+j==6 or j==n or i==n:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()

