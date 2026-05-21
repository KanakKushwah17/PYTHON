"""
   1
  12
 123
1234
 123
  12
   1

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i,n):
        print("",end=" ")
    for k in range(1,i):
        print(k,end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i,n):
        print("",end=" ")
    for k in range(1,i):
        print(k,end="")
    print()