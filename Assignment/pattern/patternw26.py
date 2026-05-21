"""
26) Right Hollow Number Triangle
    1
    12
    1 3
    1  4
    12345
"""
n=int(input("Enter a number: "))
for i in range(1,n+1):

    for j in range(1,i+1):

        if i==1 or i==2 or i==n or j==1 or j==i:
            print(j,end="")
        else:
            print(" ",end="")

    print()