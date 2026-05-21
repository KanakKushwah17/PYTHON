"""
    1
    2
    3
    4
123454321
    4
    3
    2
    1

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n :
            print(j,end=" ")
        elif j==n :
            print(i,end=" ")
        else:
            print(" ",end=" ")
    for k in range(n-1,0,-1):
        if i==n:
            print(k,end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1,n+1):
        if j==n:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()