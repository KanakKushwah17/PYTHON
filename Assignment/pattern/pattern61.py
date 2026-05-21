"""
    1
   123
  12345
 1234567
123456789

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(1,i*2):
        print(k,end="")
    print()