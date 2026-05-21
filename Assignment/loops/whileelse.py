attempts=0
while attempts<3:
    password = input("Enter password: ")
    if password=="admin":
        print("Granted")
        break
    attempts+=1
else:
    print("Too many failed attempts")