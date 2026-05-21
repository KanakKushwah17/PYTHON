"""
    1
   11
  1*1
 1**1
11111

"""
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(i,n+1):
        if k==i or i==1 or k==n :
            print("1",end=" ")
        else:
            print("*",end=" ")
    print()

