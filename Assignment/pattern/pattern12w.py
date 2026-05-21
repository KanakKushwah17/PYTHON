"""

12) Hollow Diamond Numbers
       1
      2 2
     3   3
    4     4
     3   3
      2 2
       1
"""
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n:
            print(i,end="")
        else:
            print(" ",end="")
    for k in range(2,n):
        if i==k:
            print(i,end=" ")
        else:
            print(" ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n):
        if i+j==n:
            print(i,end="")
        else:
            print(" ",end="")
    for k in range(1,n):
        if i==k:
            print(i,end="")
        else:
            print(" ",end="")

    print()