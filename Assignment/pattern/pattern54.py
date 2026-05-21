"""
ABCDE
 ABCD
  ABC
   AB
    A

"""
n=int(input("Enter the number of rows: "))

for i in range(1,n+1):
    for j in range(2,i+1):
        print("*",end=" ")
    ch = 65
    for k in range(i,n+1):
            print(chr(ch),end=" ")
            ch=ch+1
    print()
