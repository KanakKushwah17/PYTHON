"""
123456789
 1234567
  12345
   123
    1

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(1,2*(n-i)+2):
        print(k,end=" ")
    print()