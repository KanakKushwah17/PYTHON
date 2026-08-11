class InsufficientBalanceException(Exception):
    pass
class NegativeDepositException(Exception):
    pass
class BankAccount:
    def __init__(self,actnumber,acholder,balance):
        self.actnumber=actnumber
        self.acholder=acholder
        self.balance=balance
    
    def deposit(self,amount):
        if amount<0:
            raise NegativeDepositException("depsoit amount cannot be negative ")
        self.balance=self.balance+amount
        print("Deposit Successfull")
        print("Current balance ",self.balance)
    
    def withdraw(self,amount):
        if amount>self.balance:
            raise InsufficientBalanceException("Insufficient balance")
        self.balance = self.balance-amount
        print("Withdraw successfull")
        print("Current balance ",self.balance)
    
actnumber=int(input("enter account number "))
actholder=input("Enter account holder name")
balance=float(input("Enter balance "))


acc=BankAccount(actnumber,actholder,balance)

try:
    amount=float(input("Enter withdraw amount "))
    acc.deposit(amount)
except NegativeDepositException as e:
    print("negative",e)

try :
    amount=float(input("enter  deposit number "))
    acc.withdraw(amount)
except InsufficientBalanceException as e:
    print("insufficient ",e)