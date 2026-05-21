"""
25) Number Sandglass
    123454321
     1234321
      12321
       121
        1
       121
      12321
     1234321
    123454321
"""
n=int(input("Enter the number of rows: "))


for i in range(n,0,-1):

    for j in range(i,n):
        print(" ",end="")

    for k in range(1,i+1):
        print(k,end="")

    for k in range(i-1,0,-1):
        print(k,end="")

    print()


for i in range(2,n+1):

    for j in range(i,n+1):
        print("",end=" ")
    for k in range(1,i+1):
        print(k,end="")

    for k in range(i-1,0,-1):
        print(k,end="")

    print()