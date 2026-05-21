"""
2. An e-commerce website provides discounts based on the cart value and user type. 
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000, 
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise, 
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium

Output:
Final Amount = 4800
"""
Cart_value=int(input("Enter the cart value  : "))
User_type= input("Enter User type  : ").lower()

if Cart_value>=5000:
    if User_type=="premium":
        Discount=(20/100)*Cart_value
        Cart_value=int(Cart_value-Discount)
        print("Final Amount ",Cart_value)
    else:
        Discount=(10/100)*Cart_value
        Cart_value=int(Cart_value-Discount) 
        print("Final Amount ",Cart_value)
else:
    if Cart_value>=2000:
        Discount=(5/100)*Cart_value
        Cart_value=int(Cart_value-Discount)
        print("Final Amount ",Cart_value)
    else:
        print("No discount is applied ")
    
