"""
     1
    101
   10101
  1010101
 101010101
10101010101

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end=" ")
    for k in range(1,i*2):
        if  k%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
