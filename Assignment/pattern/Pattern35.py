"""
*****
*  *
* *
**
*

"""
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or  i==1 or i+j==6 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()