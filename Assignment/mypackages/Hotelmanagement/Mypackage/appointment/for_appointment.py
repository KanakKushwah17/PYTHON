from datetime import datetime


appointment=[]

def book_appointment():
    appoint_id=int(input("Enter Appointment : "))
    patient_id=int(input("Enter patient Id : "))
    doctor_id=int(input("Enter doctor ID : "))
    a_date = datetime.strptime(input("Enter Date(dd-mm-yyyy): "),"%d-%m-%Y").date()
    a_time = datetime.strptime(input("Enter time (H:M): "),"%H:%M").time()
    
    print("Store appointment information successfully ")
    
    appoint={
         "Appointment ID " : appoint_id,
         "Patient ID " : patient_id,
         "Doctor ID " : doctor_id,
         "Appointment date " : a_date,
         "Appointment Time " : a_time 
    }
    
    appointment.append(appoint)
    
def show_appointment():
    for appoint in appointment:
        for k,v in appoint.items():
            print(k,":",v)
        print()
    