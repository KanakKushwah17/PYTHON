class Guest:
    
    def __init__(self, guest_id, guest_name, number_of_days, room_charge_per_day):
        self.guest_id = guest_id
        self.guest_name = guest_name
        self.number_of_days = number_of_days
        self.room_charge_per_day = room_charge_per_day

    def room_bill(self):
        self.bill = self.number_of_days * self.room_charge_per_day

    def gst(self):
        self.gst_amount = self.bill * 12 / 100

    def final_bill(self):
        self.final_amount = self.bill + self.gst_amount

    def display(self):
        print("------ Hotel Bill ------")
        print("Guest ID              :", self.guest_id)
        print("Guest Name            :", self.guest_name)
        print("Number of Days        :", self.number_of_days)
        print("Room Charge Per Day   : ₹", self.room_charge_per_day)
        print("Room Bill             : ₹", self.bill)
        print("GST (12%)             : ₹", self.gst_amount)
        print("Final Bill            : ₹", self.final_amount)


guest_id = input("Enter Guest ID : ")
guest_name = input("Enter Guest Name : ")
number_of_days = int(input("Enter Number of Days : "))
room_charge_per_day = float(input("Enter Room Charge Per Day : "))

g = Guest(guest_id, guest_name, number_of_days, room_charge_per_day)

g.room_bill()
g.gst()
g.final_bill()
g.display()