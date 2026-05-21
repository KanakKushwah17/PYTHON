"""
Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0

---
"""
Mobile_Price = int(input("Mobile_Pricen = "))
Down_Payment = int(input("Down_Payment = "))
Interest = int(input("Interest rate = "))
Months = int(input("Monts = "))
Remaining_amount =Mobile_Price - Down_Payment
Interest = Remaining_amount * Interest/100
Total_with_Interest = Remaining_amount + Interest
Monthly_EMI = Total_with_Interest/Months
print("Remaining_amount  = ",Remaining_amount)
print("Total_with_Interest = ",Total_with_Interest)
print("Monthly_EMI = ",Monthly_EMI)