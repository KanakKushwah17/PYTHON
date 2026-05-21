"""

    1
   212
  32123
 4321234
543212345

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    for l in range(2,i+1):
        print(l,end=" ")
    print()