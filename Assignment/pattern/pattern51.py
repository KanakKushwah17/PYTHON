"""
12345
 1__4
  1_3
   12
    1

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i):
        print("*",end=" ")
    for k in range(1,n+2-i):
        if k == 1 or k == n + 1 - i or i == 1:
            print(k, end=" ")
        else:
            print("_", end=" ")
    print()
