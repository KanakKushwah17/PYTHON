"""
    1
   10
  101
 1010
10101

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(1,i+1):
        if k%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")

    print()