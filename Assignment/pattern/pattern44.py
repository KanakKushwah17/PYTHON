"""
    5
   44
  333
 2222
11111

"""
n=int(input("Enter a number "))
for i in range(n,0,-1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(n+1,i,-1):
        print(i,end=" ")
    print()
