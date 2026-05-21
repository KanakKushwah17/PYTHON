"""
21) Hollow Pyramid
        *
       * *
      *   *
     *     *
    *********
"""

n=int(input("Enter a number: "))

for i in range(1,n+1):

    for j in range(i,n):
        print("",end=" ")

    for k in range(1,2*i):

        if i==n or k==1 or k==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")

    print()