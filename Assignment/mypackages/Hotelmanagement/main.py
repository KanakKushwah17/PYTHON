from Mypackage import appointment,billing,doctor,patient

while True:
    print("""
=========================================
      HOSPITAL MANAGEMENT SYSTEM
=========================================
1. Add Patient
2. Display Patients
3. Search Patient
4. Add Doctor
5. Display Doctors
6. Book Appointment
7. Show Appointments
8. Generate Bill
9. Exit
=========================================
""")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            patient.add_patient()

        case 2:
            patient.display()

        case 3:
            patient.search_patient()

        case 4:
            doctor.add_doctor()

        case 5:
            doctor.display_doctor()

        case 6:
            appointment.book_appointment()

        case 7:
            appointment.show_appointment()

        case 8:
            print("Total bill ",billing.generate_bill())

        case 9:
            print("Thank you for using Hospital Management System.")
            break

        case _:
            print("Invalid Choice! Please try again.")