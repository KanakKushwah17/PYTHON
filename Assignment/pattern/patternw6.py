"""
 - - - - 1
- - - 2 3
- - 3 4 5
- 4 5 6 7
5 6 7 8 9
"""
n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(i,n):
        print("-",end=" ")
    num=i
    for k in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()