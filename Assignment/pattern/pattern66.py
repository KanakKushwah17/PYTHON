"""
    A
   B B
  C  C
 D    D
EEEEEEEEE

"""
n=int(input("Enter the number of rows: "))
ch = 65
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(1,i*2):
        if k==1 or i==n or k==i*2-1:
            print(chr(ch),end="")
        else:
            print("",end=" ")
    ch=ch+1
    print()