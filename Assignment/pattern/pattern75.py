"""
x
xx
xxx
xxxx
xxx
xx
x


"""
n=int(input("Enter the number of rows: "))

# upper part
for i in range(1, n+1):

    for j in range(1,i+1):
        print("*", end="")

    print()


# lower part
for i in range(n-1, 0, -1):

    for j in range(1,i+1):
        print("*", end="")

    print()
