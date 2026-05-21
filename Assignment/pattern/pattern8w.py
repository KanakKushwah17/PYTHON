"""
8) Border Number Pattern
    1 2 3 4 5
    2       5
    3       5
    4       5
    5 5 5 5 5
"""
n = int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n or i==1:
            print(j,end=" ")
        elif i==n or j==1:
            print(i,end=" ")
        else:
            print(" " ,end=" ")
    print()