"""
1.

=========================================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6

"""

d={}
n=int(input("Enter number of products: "))
i=0
while i<n:
    product=input("Enter product name: ")
    quantity=int(input("Enter quantity: "))
    d[product]=quantity
    i=i+1

for x in d:
    print(x, "=", d[x])
q=0
for x in d:
    q=q+d[x]
print("Total Quantity = ", q)
