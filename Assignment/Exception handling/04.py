'''
QNo 4:
1. Bank Account Management
Objective: Create a program to manage bank accounts and handle exceptions for insufficient balance and negative deposit amounts.

Details:
Create a BankAccount class with fields for accountNumber, accountHolder, and balance.
Define two custom exceptions:
InsufficientBalanceException for withdrawal amounts exceeding the balance.
NegativeDepositException for deposits with negative amounts.
Include methods for deposit(double amount) and withdraw(double amount) that throw the respective exceptions.
In the main method, demonstrate various cases like successful transactions, insufficient balance, and invalid deposits.
'''

class InsufficientBalanceException(Exception):
    pass
class NegativeDepositException(Exception):
    pass

class BankAccoount:
    def __init__(self,accountNumber,accountHolder,balance):
        self.accountNumber=accountNumber
        self.accountHolder=accountHolder
        self.balance=balance
    
    def deposit(self,amount):
        if amount<0:
            raise NegativeDepositException("Negative bank balance !!")
        self.balance=self.balance+amount
        print("Deposit successfull ")
        print("Current balance ", self.balance)
    
    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientBalanceException("Insufficient balance exception ")
        
        self.balance=self.balance-amount
        print("Withdraw successfull ")
        print("Current balance ",self.balance)
    
accountNumber=int(input("Enter account number "))
accountHolder=input("Enter account holder name ")
balance=float(input("Enter balance"))        

acc=BankAccoount(accountNumber,accountHolder,balance)

try:
    amount=float(input("Enter amount "))
    acc.deposit(amount)

except NegativeDepositException as e:
    print("negative ",e )

try:
    amount=float(input("Enter amount "))
    acc.withdraw(amount)       

except InsufficientBalanceException as e:
    print("insufficient ",e )   
        