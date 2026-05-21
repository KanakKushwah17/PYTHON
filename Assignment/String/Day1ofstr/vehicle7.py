"""
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
"""
vehicle_number = input("Enter vehicle number: ").upper()
count=0
valid=False
if vehicle_number[0]>='A' and vehicle_number[1]>='A' and vehicle_number[0]<='Z' and vehicle_number[1]<='Z':

    if vehicle_number[2]>='0' and vehicle_number[3]>='0' and vehicle_number[2]<='9' and vehicle_number[3]<='9':
        valid =True
if len(vehicle_number)==10 and valid==True:
    print("Valid PNR Number")
else:
    print("Invalid PNR Number")