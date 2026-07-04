Doctor=[]

def add_doctor():
    print("=======Add Doctor =========")
    
    doctor_id=int(input("Enter doctor Id "))
    doctor_name=input("Enter doctor name ")
    doctor_spec=input("Enter doctor specialization ")
    doctor_exp=int(input("Enter doctor experience "))
    doctor_consult_fee=int(input("Enter doctor consultaion fee "))
    
    print("=== Successfully addedd ====")
    
    doctor={
        "Doctor id  ": doctor_id,
        "Doctor name ": doctor_name,
        "Doctor special" : doctor_spec,
        "Doctor experience ": doctor_exp,
        "Doctor consult fee ": doctor_consult_fee
        
    }
    Doctor.append(doctor)

def display_doctor():
    for doctor in Doctor:
        for k,v in doctor.items():
            print(k,":",v)
        print()
    
    

        
    