"""
1
10
1 1
1  0
10101

"""
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if  j==i or j==1 or i==n:
            if j%2==0:
                print("0",end=" ")
            else:
                print("1", end=" ")
        else:
            print(" ", end=" ")

    print()