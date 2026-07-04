"""
6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number

"""
PNR = input("Enter PNR: ")
valid = True
if PNR[0]=='P' and PNR[1]=='N' and PNR[2]=='R' and len(PNR)==12:
    valid = True

    for i in range(3, 12):
        if PNR[i] < '0' or PNR[i] > '9':
            valid = False
    if valid==True:
        print("Valid PNR Number")
    else:
        print("Not Valid PNR Number")
else:
    print("Invalid PNR Number")
