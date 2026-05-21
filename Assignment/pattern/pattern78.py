"""
1
1 2
1  3
1   4
1  3
1 2
1

"""
n=int(input("Enter the number of rows: "))
for i in range(1,n):
    for j in range(1,i+1):
        if i==j or j==1 :
            print(j,end=" ")
        else:
            print("",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        if i==j or j==1 :
            print(j,end=" ")
        else:
            print("",end=" ")
    print()

