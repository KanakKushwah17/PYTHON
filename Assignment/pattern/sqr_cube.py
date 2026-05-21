"""
2)	WAP to print Square, Cube and Square Root of all numbers from 1 to N
"""
n=int(input("enter number: "))
for i in range(1,n+1):
    sqr=i*i
    cube=i*i*i
    print("square root and cube root of ", i, " is ", sqr,"and ",cube)
