"""
    A
   ABC
  ABCDE
 ABCDEEF
ABCDEFGHI

"""
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    ch=65
    for k in range(1,i*2):
        print(chr(ch),end="")
        ch=ch+1
    print()