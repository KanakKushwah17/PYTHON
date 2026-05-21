"""
4) Vertical Diamond
       *
      * *
     *   *
    *     *
     *   *
      * *
       *
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==5  or i==7 or j==7:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()