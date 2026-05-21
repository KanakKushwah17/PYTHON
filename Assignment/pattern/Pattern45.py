"""
    A
   AB
  ABC
 ABCD
ABCDE
"""
n=int(input("Enter any number :"))
for i in range(1,n+1):
    ch = 65
    for j in range(i,n+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(chr(ch),end=" ")
        ch = ch + 1
    print()


