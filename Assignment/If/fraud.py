"""
6. Banking Fraud Detection System

A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.

If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.

Input:
Amount = 70000
Location = international
Device = new
Transactions = 4

Output:
Risk Level = High Risk (Blocked)
"""
amount =int(input("Enter marks : "))
location = input("Enter Location : ").lower()
Device =  input("Enter Device : ").lower()
trans =  int(input("Enter Transactions : "))


if amount>=50000:
    if location=="international":
        if Device=="new":
            if trans>=3:
                print("High risk(Blocked) ")
            else:
                print("Medium risk ")
        else:
            print("Medium risk")
    else:
        if trans>=5:
                print("Medium risk")
        else:
                print("Low risk ")
else:
    unusual = input("Is there unusual activity? (yes/no): ").lower()
    if unusual=="yes":
        if Device=="new":
            print("Medium risk ")
        else:
            print("Loww risk ")
    else:
        print("Safe")
   
        
  


