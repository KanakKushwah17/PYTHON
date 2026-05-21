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
yes=1
count=0
for i in range(0,len(num)):
    if num[i]==' ' or num[i]=='-' or num[i]=='+':
        yes=0
    if num[i]>='0' and num[i]<='9':
        count=count+1
        yes=1
if yes==1 :
    print("Total digits: ",count)
