"""
1
222
33333
4444444
555555555

"""
n=int(input("Enter a number "))
for i in range(1,n+1):
    for j in range(1,i*2):
        print(i,end=" ")
    print()
