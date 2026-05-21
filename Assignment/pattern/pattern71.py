"""
A B C D E
 A B C D
  A B C
   A B
    A
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("",end=" ")
    ch=65
    for j in range(i,n+1):
        print(chr(ch),end=" ")
        ch=ch+1
    print()
