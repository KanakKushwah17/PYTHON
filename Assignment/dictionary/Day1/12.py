"""
12.

=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza
"""

n=int(input("Enter the number of products: "))
products=[]
for i in range(n):
    product=input("Enter the product name: ")
    products.append(product)
print(products)
d={}
for i in products:
    d[i] = d.get(i, 0) + 1
print(d)

highest=0
for k,v in d.items():
    if v>highest:
        highest=v
print("Highest ",highest)