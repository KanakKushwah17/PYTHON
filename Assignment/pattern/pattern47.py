"""
    A
   AB
  A_C
 A__D
ABCDE
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(i, n):
        print(" ", end=" ")
    ch = 65
    for k in range(1, i + 1):
        if i == k or k == 1  or i==n:
            print(chr(ch), end=" ")
        else:
            print("_", end=" ")
        ch = ch + 1

    print()