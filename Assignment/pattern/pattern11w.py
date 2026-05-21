"""
11) Butterfly Number Pattern
    1      1
    12    21
    123  321
    12344321
    123  321
    12    21
    1      1

"""
n=int(input("Enter a number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(i*2-1,n*2-1):
        print(" ",end=" ")
    for l in range(i,0,-1):
        print(l,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(i*2-1,n*2-1):
        print(" ",end=" ")
    for l in range(i,0,-1):
        print(l,end=" ")

    print()