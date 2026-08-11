class Staff:
    def __init__(self):
        self.data = {}
        self.next_id = 1

    def add(self):
        name = input("Enter Name: ")
        role = input("Enter Role: ")
        s_id = f"S{self.next_id}"
        self.next_id += 1
        self.data[s_id] = {"name": name, "role": role}
        print(f"Staff added with ID: {s_id}")

    def view(self):
        for s_id, details in self.data.items():
            print(f"ID: {s_id} | Name: {details['name']} | Role: {details['role']}")

    def menu(self):
        while True:
            print("\n--- STAFF MENU ---")
            print("1. Add Staff")
            print("2. View Staff")
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
