patients = []

def add_patient():
    print("\n===== Add Patient =====")

    patient_id = input("Enter Patient ID: ")
    patient_name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    mobile = input("Enter Mobile Number: ")
    print("\nPatient added successfully!")
    
    
    patient = {
        "Patient ID": patient_id,
        "Patient Name": patient_name,
        "Age": age,
        "Gender": gender,
        "Disease": disease,
        "Mobile Number": mobile

    }

    patients.append(patient)
    
    
def display():
    for patient in patients:
        for k,v in patient.items():
            print(k,":",v)
        print()
        
def search_patient():
    p_id=input("Enter patient for searching ")
    for patient in patients:
        if patient["Patient ID"]==p_id:
        
            for k,v in patient.items():
                print(k,":",v)
            return
    print("Patient ID not found !!!! ")
        
    

    
