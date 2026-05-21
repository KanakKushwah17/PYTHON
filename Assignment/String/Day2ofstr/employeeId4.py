"""
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
"""
enter=input("Enter Employee ID: ")
valid=1
if enter[0:3]=="EMP":
    if len(enter)==8:
        for i in range(3, len(enter)):
            if enter[i] < '0' or enter[i] > '9':
                valid = 0

    else:
            valid =0
else:
        valid=0

if valid==1:
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")


