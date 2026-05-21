"""
123456789
 1+++++7
  1+++5
   1+3
    1

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(1,2*(n-i)+2):
        if k==1 or i==1 or k== 2*(n-i)+1:
            print(k,end=" ")
        else:
            print("+",end=" ")
    print()