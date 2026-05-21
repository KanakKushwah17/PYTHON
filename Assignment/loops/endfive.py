"""
3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35

"""
num1,num2=map(int,input("Enter the 2 number :").split())

for i in range (num1,num2):
    if i%5==0 and i%10!=0:
        print("Output",i)
