"""
5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1****1
"""
n=int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        print(j, end="")
    for k in range(1, i * 2 - 1):
        print("*", end="")
    for l in range(n - i + 1, 0, -1):
        print(l, end="")

    print()