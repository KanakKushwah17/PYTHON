students=["cat","dog","bat"]
name=input("Enter the name:")
if name in students:
    if name>='A' and name<='Z':
        print("The name entered is in upper case")
    else:
        name=name.upper()
print(name)