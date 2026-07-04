"""
11.

=========================================
PRODUCT SALES ANALYSIS
======================

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1

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