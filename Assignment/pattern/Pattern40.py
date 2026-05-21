"""
*
**
****
*******
***********

"""
n=int(input("Enter a number:"))
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print("*",end=" ")
    print()
    k = k + i