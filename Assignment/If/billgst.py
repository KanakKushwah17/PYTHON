"""
12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680

"""
bill=int(input("Enter bill Amount : "))

if bill>=1000:
    GST=(5/100)*bill
   
    print("Final bill amount : ",bill )
elif bill>1001 and bill <= 5000:
    GST=(12//100)*bill
   
    print("Final bill amount : ",bill )
elif bill>=3000:
    GST=(12//100)*bill+200
    bill=GST+bill
    print("Final bill amount : ",bill )
else:
    GST=(18/100)*bill

bill=GST+bill
print("Final bill amount : ",bill )
