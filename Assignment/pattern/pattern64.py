"""
   1
  1 1
 1 2 1
 1 3 3 1
1 4 6 4 1

"""
n=int(input("Enter the number of rows: "))

for i in range(1,n+1):
    for j in range(i,n):
        print("",end=" ")
    el = 1
    for k in range(1,i+1):
        print(el,end=" ")

        el=el* (i - k) // k
    print()


