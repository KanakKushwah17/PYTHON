"""
   *
  *_*
 *___*
*_____*
 *___*
  *_*
   *

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n):
    for j in range(i,n):
        print(" ",end="")
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            print("*",end="")
        else:
            print("_",end="")
    print()
for i in range(n-2,0,-1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(1,i*2):
        if k == 1 or k == i * 2 - 1:
            print("*", end="")
        else:
            print("_", end="")
    print()