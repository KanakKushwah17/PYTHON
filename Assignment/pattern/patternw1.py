"""
        *
       * *
      *   *
     *     *
    *   *   *
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end=" ")
    for k in range(1,i*2):
        if k == 1 or k == i * 2 - 1 or i == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()