"""
1)	WAP to find out the sum of all integer between 100 and 200 which are divisible by 9
"""
n=int(input("enter number: "))
sum=0
for i in range(100,n):
    if i%9==0:
        sum=sum+i
print(sum)