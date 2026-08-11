class Booking:
    def __init__(self):
        self.data = {}
        self.next_id = 1

    def add(self):
        c_id = input("Enter Customer ID: ")
        r_no = input("Enter Room Number: ")
        days = input("Enter Days: ")
        
        b_id = f"B{self.next_id}"
        self.next_id += 1
        
        self.data[b_id] = {"customer": c_id, "room": r_no, "days": days}
        print(f"Booking added with ID: {b_id}")

    def view(self):
        for b_id, details in self.data.items():
            print(f"Booking ID: {b_id} | Customer: {details['customer']} | Room: {details['room']} | Days: {details['days']}")

    def menu(self):
        while True:
            print("\n--- BOOKING MENU ---")
            print("1. Add Booking")
            print("2. View Bookings")
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
