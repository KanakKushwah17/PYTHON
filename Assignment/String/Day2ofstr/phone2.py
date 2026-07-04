"""
2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12
"""
num=input("Enter contact number: ")
count=0
for i in range(len(num)):
    if num[i]!=' ' and num[i]!='-' and num[i]!='+':
        count=count+1

print("Total digits ",count)



