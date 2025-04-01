moneyEarned = 0
def takeMoney(choice, quartersCount, dimesCount, nicklesCount, penniesCount):
    global moneyEarned
    amtRecieved = ((quartersCount*0.25) + (dimesCount*0.10) + (nicklesCount*0.05) + (penniesCount*0.01))
    if choice == 'espresso':
        price = 1.50
        if amtRecieved < price:
            print("Insufficient Funds")
        amtTOreturn = amtRecieved - price
        moneyEarned += price
        return amtTOreturn
    elif choice == 'latte':
        price = 2.50
        if amtRecieved < price:
            print("Insufficient Funds")
        amtTOreturn = amtRecieved - price
        moneyEarned += price
        return amtTOreturn
    elif choice == 'cappuccino':
        price = 3
        if amtRecieved < price:
            print("Insufficient Funds")
        amtTOreturn - amtRecieved - price
        moneyEarned += price
        return amtTOreturn
    else:
        print("Please enter a valid choice.")

ingridients = {
    'water' : 300,
    'milk' : 200,
    'coffee' : 100
}


def checkAvailability(choice):
    if choice == 'espresso':
        if ((ingridients['water'] < 50) or (ingridients['coffee'] < 18)):
            return "Insufficient Ingridients"
    elif choice == 'latte':
        if ((ingridients['water'] < 200) or (ingridients['coffee'] < 24) or (ingridients['milk'] < 150)):
            return "Insufficient Ingridients"
    elif choice == 'cappuccino':
        if ((ingridients['water'] < 250) or (ingridients['coffee'] < 24) or (ingridients['milk'] < 100)):
            return "Insufficient Ingridients"
    else:
        return f"here is your {choice}"
    
def changeAmountsofIngridients(choice):
    global ingridients
    if choice == 'espresso':
        ingridients['water'] -= 50
        ingridients['coffee'] -= 18
    elif choice == 'latte':
        ingridients['water'] -= 200
        ingridients['coffee'] -= 24
        ingridients['milk'] -= 150
    elif choice == 'cappuccino':
        ingridients['water'] -= 250
        ingridients['coffee'] -= 24
        ingridients['milk'] -= 100

def reportPrinter():
    print(f"You have {ingridients['water']}ml of water left")
    print(f"You have {ingridients['coffee']}g of coffee left")
    print(f"You have {ingridients['milk']}ml of milk left")

        




    







print(ingridients)
choice = input("What would you like to have? (espresso/latte/cappuccino): ")
print("Please insert coins: ")
quartersCount = int(input("How many quarters: "))
dimesCount = int(input("How many dimes: "))
nicklesCount = int(input("How many nickles: "))
penniesCount = int(input("How many pennies: "))
amtTOreturn = takeMoney(choice, quartersCount, dimesCount, nicklesCount, penniesCount)
changeAmountsofIngridients()


# report = {
#     'Water' : '100ml',
#     'Milk' : '50ml',
#     'Coffee' : '76g',
#     'moneyEarned' : '$2.5'
# }

# if choice == 'off':
#     exit()
# if choice == 'report':
#     print(report)


