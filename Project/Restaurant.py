from bdb import Breakpoint

print("     WELCOME TO AVNI RESTAURANT")
print("       Delicious Food Hub 🍔")
print("\n=========== MENU CARD ===========")
print("\n 1. Pizza ")
print("\n 2. Burgers ")
print("\n 3. Noodles ")
print("\n 4. Momos ")
print("\n 5. Pasta ")
print("\n 6. Sandwich ")
print("\n 7. Dosa  ")
print("\n 8. Icecream ")
print("\n 9. Fries ")
print("\n 10.Cold Drinks ")
amount=0
while True:
    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Pizza")
            print("   1• Margherita Pizza -rs.250")
            print("   2• Farmhouse Pizza -rs.350")
            print("   3• Cheese Burst Pizza -rs.450")
            pizza = input("Which pizza do you want? ")
            if pizza == "Margherita Pizza":
                print("Amount = 250")
                amount=amount+250
            elif pizza == "Farmhouse Pizza":
                print("Amount = 350")
                amount = amount + 250
            elif pizza == "Cheese Burst Pizza":
                print("Amount = 450")
                amount = amount + 250
            else:
                print("Choose Next food ")
        case 2:
            print("Burgers")
            print("   • Veg Burger -rs.250")
            print("   • Cheese Burger -rs.350")
            print("   • Crispy Burger -rs.450")
            burger=input("Which burger do you want? ")
            if burger == "Burger":
                print("Amount = 250")
                amount=amount+250
            elif burger == "Cheese Burger":
                print("Amount = 350")
                amount = amount + 350
            elif burger == "Crispy Burger":
                print("Amount = 450")
                amount = amount + 450
            else:
                print("Choose Next food ")

        case 3:
            print("Noodles ")
            print("   • Hakka Noodles -rs.250")
            print("   • Schezwan Noodles -rs.150")
            print("   • Veg Noodles -rs.50")
            noodles=input("Which noodle do you want? ")
            if noodles == "Hakka Noodles":
                print("Amount = 250")
                amount=amount+250
            elif noodles == "Schezwan Noodles":
                print("Amount = 150")
                amount = amount + 150
            elif noodles == "Veg Noodles":
                print("Amount = 50")
                amount = amount + 50
            else:
                print("Choose Next food ")
        case 4:
            print("Momos ")
            print("   • Veg Momos -rs.70")
            print("   • Fried Momos -rs.110")
            print("   • Tandoori Momos -rs.120")
            momos=input("Which momos do you want? ")
            if momos == "Veg Momos":
                print("Amount = 70")
                amount = amount + 70
            elif momos == "Fried Momos":
                print("Amount = 110")
                amount = amount + 110
            elif momos == "Tandoori Momos":
                print("Amount = 120")
                amount = amount + 120
            else:
                print("Choose Next food ")
        case 5:
            print("Pasta ")
            print("   • White Sauce Pasta -rs.450")
            print("   • Red Sauce Pasta -rs.350")
            print("   • Mix Sauce Pasta -rs.500")
            pasta=input("Which pasta do you want? ")
            if pasta == "White Sauce Pasta":
                print("Amount = 450")
                amount = amount + 450
            elif pasta == "Red Sauce Pasta":
                print("Amount = 350")
                amount = amount + 350
            elif pasta == "Mix Sauce Pasta":
                print("Amount = 500")
                amount = amount + 500
            else:
                print("Choose Next food ")
        case 6:
            print("Sandwich ")
            print("   • Veg Sandwich -rs.70")
            print("   • Grilled Sandwich -rs.80")
            print("   • Cheese Sandwich -100")
            pasta=input("Which pasta do you want? ")
            if pasta == "Veg Sandwich":
                print("Amount = 70")
                amount = amount + 70
            elif pasta == "Grilled Sandwich":
                print("Amount = 80")
                amount = amount + 80
            elif pasta == "Cheese Sandwich":
                print("Amount = 100")
                amount = amount + 100
            else:
                print("Choose Next food ")

        case 7:
            print("Dosa ")
            print("   • Plain Dosa -rs.150")
            print("   • Masala Dosa -rs.250")
            print("   • Cheese Dosa -rs.199")
            Dosa=input("Which Dosa do you want? ")
            if Dosa == "Masala Dosa":
                print("Amount = 150")
                amount = amount + 150
            elif Dosa == "Cheese Dosa":
                print("Amount = 199")
                amount = amount + 199
            elif Dosa == "Masala Dosa":
                print("Amount = 250")
                amount = amount + 250
            else:
                print("Choose Next food ")
        case 8:
            print("Icecream ")
            print("   • Vanilla -rs.90")
            print("   • Chocolate -rs.80")
            print("   • Butterscotch -rs.100")
            Icecream=input("Which icecream do you want? ")
            if Icecream == "Chocolate":
               print("Amount = 90")
               amount = amount + 90
            elif Icecream == "Butterscotch":
                print("Amount = 80")
                amount = amount + 80
            elif Icecream == "Chocolate Butterscotch":
                print("Amount = 100")
                amount = amount + 100
            else:
                print("Choose Next food ")
        case 9:
            print("Fries ")
            print("   • French Fries -rs.210")
            print("   • Peri Peri Fries -rs.210")
            print("   • Cheese Fries -rs.100")
            Fries=input("Which Fries do you want? ")
            if Fries == "Cheese Fries":
                print("Amount = 100")
                amount = amount + 100
            elif Fries == "Fries Peri Fries":
                print("Amount = 210")
                amount = amount + 210
            elif Fries == "Cheese Fries Peri Fries":
                print("Amount = 250")
                amount = amount + 250
            else:
                print("Choose Next food ")
        case 10:
            print("Cold Drink :")
            print("    • Coca Cola -rs.99")
            print("    • Sprite -rs.80")
            print("    • Fanta -rs.100")
            Cold=input("Which Cold Drink do you want? ")
            if Cold == "Fanta":
                print("Amount = 100")
                amount = amount + 100
            elif Cold == "Coca Cola":
                print("Amount = 99")
                amount = amount + 99
            elif Cold == "Sprite":
                print("Amount = 80")
                amount = amount + 80
            else:
                print("Choose Next food ")

        case 11:
            print("\n========== FINAL BILL ==========")
            print("Total Amount =", amount)
            print("Thankyou for eating food in our restaurant ❤️")
            break

        case _:
            print("Invalid Choice ❌")
