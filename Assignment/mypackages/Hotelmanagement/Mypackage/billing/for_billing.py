
def generate_bill():
    patient_id=int(input("Enter patient ID : "))
    patient_consult_fee=int(input("Enter Consultation fee :"))
    patient_meds_cost=int(input("Enter medicine cost :"))
    patient_charges=int(input("Pateint test charges : "))
    totalbill=  patient_consult_fee + patient_meds_cost + patient_charges
    return totalbill


    
    
    
    
