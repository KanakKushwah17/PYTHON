class Room:
    def __init__(self):
        self.data = {}

    def add(self):
        r_no = input("Enter Room Number: ")
        r_type = input("Enter Type: ")
        price = input("Enter Price: ")
        self.data[r_no] = {"type": r_type, "price": price, "status": "Available"}
        print("Room added.")

    def view(self):
        for r_no, details in self.data.items():
            print(f"Room: {r_no} | Type: {details['type']} | Price: {details['price']} | Status: {details['status']}")

    def update(self):
        r_no = input("Enter Room Number to update status: ")
        if r_no in self.data:
            status = input("Enter new status (Available/Occupied): ")
            self.data[r_no]["status"] = status
            print("Status updated.")
        else:
            print("Room not found.")

    def menu(self):
        while True:
            print("\n--- ROOM MENU ---")
            print("1. Add Room")
            print("2. View Rooms")
            print("3. Update Status")
            print("0. Back")
            choice = input("Choice: ")
            if choice == '1':
                self.add()
            elif choice == '2':
                self.view()
            elif choice == '3':
                self.update()
            elif choice == '0':
                break
            else:
                print("Invalid Choice")
