class Customer:
    def __init__(self):
        self.data = {}
        self.next_id = 1

    def add(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        c_id = f"C{self.next_id}"
        self.next_id += 1
        self.data[c_id] = {"name": name, "phone": phone}
        print(f"Customer added with ID: {c_id}")

    def view(self):
        for c_id, details in self.data.items():
            print(f"ID: {c_id} | Name: {details['name']} | Phone: {details['phone']}")

    def menu(self):
        while True:
            print("\n--- CUSTOMER MENU ---")
            print("1. Add Customer")
            print("2. View Customers")
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
