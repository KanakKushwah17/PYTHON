"""
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75
"""
bill=int(input("Enter the total bill amount "))
GST=int(input("Enter the GST percentage "))
charge=int(input("Enter the total charge:  "))
friends=int(input("Enter the number of friends : "))

GST=(GST/100)*bill
charge=(10/100)*bill
amount=charge+GST+bill

print("After adding Gst and extra charges : ",amount)


eachperson=amount/friends
print("Each person pays the bill : ",eachperson)
