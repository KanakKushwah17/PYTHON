"""
   #
  *#*
 **#**
 ***#***
****#****

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(1,i*2):
        if k==i:
            print("#",end=" ")
        else:
            print("*",end=" ")

    print()