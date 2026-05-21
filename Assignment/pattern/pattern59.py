"""
    X
   X X
   X__X
  X____X
X X X X X

"""
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(i,n):
        print("",end=" ")
    for k in range(1,i+1):
        if k==i or k==1 or i==n:
            print("X",end=" ")
        else:
            print("_",end=" ")
    print()