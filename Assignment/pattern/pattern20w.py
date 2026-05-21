"""
20) Continuous Diamond Numbers
           1
          2 3
         4 5 6
        7 8 9 10
         4 5 6
          2 3
           1
"""
n=int(input("Enter a number: "))
num=1

for i in range(1,n+1):
    for j in range(i,n):
        print("",end=" ")
    temp = num
    for k in range(1,i):
        print(num,end=" ")
        num=num+1
    print()

for i in range(n-1,0,-1):

    for j in range(n,i,-1):
        print("",end=" ")

    temp=temp-i+1

    x=temp

    for k in range(1,i+1):
        print(x,end=" ")
        x=x+1

    print()
