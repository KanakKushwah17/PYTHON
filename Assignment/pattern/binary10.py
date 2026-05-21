"""
4)
1
00
111
0000
11111

"""
n=int(input("Enter a number: "))
for i in range(0,n+1):
    for j in range(0,i):
        if i%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()


