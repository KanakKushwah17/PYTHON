'''Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0
'''

class Shopping():
    def __init__(self,product_id,product_name,quantity,price_per_item):
        self.product_id=product_id
        self.product_name=product_name
        self.quantity=quantity
        self.price_per_item=price_per_item
    
    def bill_per_item(self):
        self.total_amount= self.quantity*self.price_per_item
    
 
    def discount(self):
        if self.total_amount > 5000:
            self.discount_amount = self.total_amount * 10 / 100
        else:
            self.discount_amount = self.total_amount * 5 / 100
        
    def final_amount(self):
        
        self.final_amt = self.total_amount - self.discount_amount
        

product_id=int(input("Enter Product Id : "))
product_name=input("Enter product name : ")
quantity=int(input("Enter quantity of product : "))
price_per_item=int(input("Enter price per item : "))
        
s=Shopping(product_id,product_name,quantity,price_per_item)

s.bill_per_item()
s.discount()
s.final_amount()

print("------ Shopping Bill ------")
print("Product ID        : ",product_id)
print("Product Name      : ",product_name)
print("Quantity          : ",quantity)
print("Price Per Item    : ",s.price_per_item)
print("Total Amount      : ",s.total_amount)
print("Discount          : ",s.discount_amount)
print("Final Amount      : ",s.final_amt)
            
        
        