"""
5. Count Factors of Number
A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6
"""
fact=int(input("Enter number : "))
count=0
for i in range (1,fact+1):
    if fact % i == 0:
         count=count+1

print("Factors count ",count)
    
      