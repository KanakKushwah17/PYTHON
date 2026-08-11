from rooms.rooms import Room
from customers.customers import Customer
from bookings.bookings import Booking
from billing.billing import Bill
from inventory.inventory import Inventory
from staff.staff import Staff

class Hotel:
    def __init__(self):
        self.room = Room()
        self.customer = Customer()
        self.booking = Booking()
        self.bill = Bill()
        self.inventory = Inventory()
        self.staff = Staff()

    def menu(self):
        while True:
            print("\n========================================")
            print("      HOTEL MANAGEMENT SYSTEM")
            print("========================================")
            print("1. Room")
            print("2. Customer")
            print("3. Booking")
            print("4. Bill")
            print("5. Inventory")
            print("6. Staff")
            print("0. Exit")

            choice = input("\nEnter Choice: ")

            if choice == '1':
                self.room.menu()
            elif choice == '2':
                self.customer.menu()
            elif choice == '3':
                self.booking.menu()
            elif choice == '4':
                self.bill.menu()
            elif choice == '5':
                self.inventory.menu()
            elif choice == '6':
                self.staff.menu()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid Choice")

if __name__ == "__main__":
    h = Hotel()
    h.menu()
