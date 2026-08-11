class Bill:
    def __init__(self):
        self.data = {}
        self.next_id = 1

    def add(self):
        b_id = input("Enter Booking ID: ")
        amount = input("Enter Total Amount: ")
        
        bill_id = f"INV{self.next_id}"
        self.next_id += 1
        
        self.data[bill_id] = {"booking": b_id, "amount": amount, "paid": "Yes"}
        print(f"Bill created. ID: {bill_id} | Amount: {amount}")

    def view(self):
        for bill_id, details in self.data.items():
            print(f"Bill ID: {bill_id} | Booking: {details['booking']} | Amount: {details['amount']} | Paid: {details['paid']}")

    def menu(self):
        while True:
            print("\n--- BILL MENU ---")
            print("1. Add Bill")
            print("2. View Bills")
            print("0. Back")
            choice = input("Choice: ")
            if choice == '1':
                self.add()
            elif choice == '2':
                self.view()
            elif choice == '0':
                break
            else:
                print("Invalid Choice")
