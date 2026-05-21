"""
14) Spiral Number Square
     1   2   3   4
    12  13  14   5
    11  16  15   6
    10   9   8   7

"""
n=int(input("Enter a number: "))
for i in range(1,n+1):
    #right
    right=1
    for j in range(1,n+1):
