class Inventory:
    def __init__(self):
        self.data = {}

    def add(self):
        item = input("Enter Item Name: ")
        qty = input("Enter Quantity: ")
        self.data[item] = qty
        print("Item added.")

    def view(self):
        for item, qty in self.data.items():
            print(f"Item: {item} | Quantity: {qty}")

    def menu(self):
        while True:
            print("\n--- INVENTORY MENU ---")
            print("1. Add Item")
            print("2. View Inventory")
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
