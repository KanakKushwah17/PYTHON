"""

13) Number X Pattern
    1   5
     2 4
      3
     2 4
    1   5

"""
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(i,end="")
        elif i+j==6:
            print(j,end=" ")
        else:
            print(" ",end="")

    print()