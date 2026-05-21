"""
17) Hollow Hourglass
    * * * * *
      *     *
        * *
          *
        * *
      *     *
    * * * * *
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i):
        print("",end=" ")
    for k in range(i,n+1):
        if i==1 or k==i or k==n :
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(2,n+1):
    for j in range(i,n):
        print("",end=" ")
    for k in range(1,i+1):
        if i==n or k==i or k==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
