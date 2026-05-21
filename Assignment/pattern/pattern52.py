"""
55555
 4__4
  3_3
   22
    1

"""
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(i+1,n+1):
       print("*",end=" ")
    for k in range(1,i+1):
        if k==1 or i==n or k==i:
            print(i, end=" ")
        else:
            print("_", end=" ")

    print()

