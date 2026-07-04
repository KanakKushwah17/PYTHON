"""
3.
ONLINE SHOPPING SYSTEM

Scenario:

An e-commerce company wants to develop an Online Shopping System. The application should be menu-driven and should demonstrate different types of arguments used in Python functions.

MENU

1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit

Requirements

Choice 1 – Customer Registration

* Accept Customer Name, Email, and Mobile Number.
* Pass the values to a function using Positional Arguments.
* Display the registered customer details.

Choice 2 – Product Information

* Accept Product Name, Price, and Category.
* Call the function using Keyword Arguments.
* Display the product details.

Choice 3 – Generate Invoice

* Accept Product Name and Price.
* Tax Percentage should have a default value.
* Use Default Arguments while generating the invoice.
* Display the final amount.

Choice 4 – Add Multiple Products

* Allow the user to enter any number of product prices.
* Pass all prices to a function using Variable Length Arguments (*args).
* Calculate and display the total bill amount.

Choice 5 – Display Customer Profile

* Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
* Pass the details using Arbitrary Keyword Arguments (**kwargs).
* Display all customer information.

Choice 6 – Exit

Sample Execution

Enter Choice : 1

Enter Name : Ajay
Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
Enter Mobile : 9876543210

Customer Registered Successfully

---

Enter Choice : 2

Enter Product Name : Laptop
Enter Price : 55000
Enter Category : Electronics

Product Details Displayed Successfully

---

Enter Choice : 3

Enter Product Name : Laptop
Enter Price : 55000

Invoice Generated Successfully

---

Enter Choice : 4

Enter Number of Products : 4

Enter Price 1 : 100
Enter Price 2 : 200
Enter Price 3 : 300
Enter Price 4 : 400

Total Bill Amount : 1000

---

Enter Choice : 5

Customer Profile Displayed Successfully

---

Enter Choice : 6

Thank You. Program Terminated.

Important Instructions

1. Choice 1 must use Positional Arguments.
2. Choice 2 must use Keyword Arguments.
3. Choice 3 must use Default Arguments.
4. Choice 4 must use Variable Length Arguments (*args).
5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
6. Use separate functions for each menu option.
7. Implement the solution using a menu-driven approach.
8. Maintain proper code readability and formatting.

Note:
Marks will be awarded based on the correct usage of the specified argument type in each menu option
"""

while True:
     print()
     print(" =========== Menu ========")
     print("1. Customer Registration")
     print("2. Product Information")
     print("3. Generate Invoice")
     print("4. Add Multiple Products")
     print("5. Display Customer Profile")
     print("6. Exit")
     print()
     choice =int(input("Enter Choice : "))
     match choice:
          case 1:
               def call(Name,Email,Mobile):
                    print("Name is ",Name)
                    print("Email is ",Email)
                    print("Mobile number is ",Mobile)

               name=input("Enter Customer Name : ")
               email=input("Enter Email : ")
               mobilenumber=int(input("Enter Mobile Number : "))
               call(name,email,mobilenumber)
               print("Customer Registered Successfully")
               print("=================================")
               print()

          case 2:
               print()
               def prod(Name,Price,Category):
                    print("Product name is ",Name)
                    print("Enter price ",Price)
                    print("Category is ",Category)
                    print()


               product_name=input("Enter Product Name : ")
               price=int(input("Enter Product Price : "))
               Category=input("Enter Product Category : ")
               prod(product_name,price,Category)
               print("Product Details Displayed Successfully")
               print("================================ \n")



          case 3:
               def invoice(Product_name,Price,tax=18):
                    final_amount = price + (price * tax / 100)
                    print("Product Name is ",Product_name)
                    print("Total Amount is ",final_amount)

               print()
               product_name=input("Enter Product Name : ")
               price=int(input("Enter Product Price : "))
               invoice(product_name,price)

               print("Invoice Generated Successfully")
               print("===============================")
               print()

          case 4:
               def bill(*prices):
                    total_sum=sum(prices)
                    print("Total Bill Amount is ",total_sum)
               n=int(input("Enter Number of Products : "))
               prices=[]
               for i in range(1,n+1):
                 price=int(input("Enter Number of Products :" ))
                 prices.append(price)
               bill(*prices)
               print("========================================")

          case 5:
               def customer(**info):
                    for key,value in info.items():
                         print(key, ":", value)

               name=input("Enter Customer Name : ")
               city=input("Enter City : ")
               email=input("Enter Email : ")
               mobilenumber=int(input("Enter Mobile Number : "))
               membership=input("Enter membership : ")

               customer(
                    Name=name,
                    City=city,
                    Email=email,
                    Mobile=mobilenumber,
                    member=membership
               )
               print("Customer Profile Displayed Successfully")
               print("================================")
               print()

          case 6:
               break

