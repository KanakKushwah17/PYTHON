"""
7.
enter n6
     *
    **
   ***
  ****
 *****
******
"""
n=int(input("enter the number :"))
for i in range(1,n+1):
    print()
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")