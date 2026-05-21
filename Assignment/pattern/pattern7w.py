"""
7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5
"""
n = int(input("Enter number of rows: "))
n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    num = 2 * (i - 1)
    for j in range(1, i):
        print(num, end=" ")
        num -= 1
    for k in range(i, n):
        print("-", end=" ")
    print()