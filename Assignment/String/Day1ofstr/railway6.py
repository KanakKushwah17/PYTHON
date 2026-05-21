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
PNR=input("Enter PNR: ")

valid=0
if PNR[0]=='P' and PNR[1]=='N' and PNR[2]=='R':
    if len(PNR)==12:
        valid=1

for i in range(3,len(PNR)):
    if PNR[i]<'0' or PNR[i]>'9':
                valid=0

if valid==1:
    print("Valid PNR Number")
else:
    print("Invalid PNR Number")
