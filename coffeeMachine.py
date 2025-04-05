moneyEarned = 0

def takeMoney(choice, quartersCount, dimesCount, nicklesCount, penniesCount):
    global moneyEarned
    amtRecieved = ((quartersCount * 0.25) + (dimesCount * 0.10) + (nicklesCount * 0.05) + (penniesCount * 0.01))

    prices = {
        'espresso': 1.50,
        'latte': 2.50, 
        'cappuccino': 3.00
        }

    if choice in prices:
        price = prices[choice]
        if amtRecieved < price:
            return False  # Not enough money
        amtTOreturn = amtRecieved - price
        moneyEarned += price
        return amtTOreturn
    else:
        print("Please enter a valid choice.")
        return


ingredients = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}

def checkAvailability(choice):
    requirements = {      #many dictionaries inside a dictionary
        'espresso': 
            {
                'water': 50,
                'coffee': 18
                },
        'latte': 
        {
            'water': 200, 
            'coffee': 24, 
            'milk': 150
            },
        'cappuccino': 
        {
            'water': 250, 
            'coffee': 24, 
            'milk': 100
            }
    }

    if choice not in requirements:
        return False  # Invalid choice

    for item, amount in requirements[choice].items():
        if ingredients[item] < amount:
            return False  # Not enough ingredients
    return True


def changeAmountsOfIngredients(choice):
    requirements = {
        'espresso': {'water': 50, 'coffee': 18},
        'latte': {'water': 200, 'coffee': 24, 'milk': 150},
        'cappuccino': {'water': 250, 'coffee': 24, 'milk': 100}
    }

    if choice in requirements:
        for item, amount in requirements[choice].items():
            ingredients[item] -= amount


def reportPrinter():
    print(f"You have {ingredients['water']}ml of water left")
    print(f"You have {ingredients['coffee']}g of coffee left")
    print(f"You have {ingredients['milk']}ml of milk left")
    print(f"Money earned: ${moneyEarned:.2f}")


# Main program flow
print(ingredients)
choice = input("What would you like to have? (espresso/latte/cappuccino): ").strip().lower()

if choice in ["espresso", "latte", "cappuccino"]:
    if not checkAvailability(choice):
        print("Not enough ingredients, please refill the machine.")
    else:
        print("Please insert coins: ")
        quartersCount = int(input("How many quarters: "))
        dimesCount = int(input("How many dimes: "))
        nicklesCount = int(input("How many nickles: "))
        penniesCount = int(input("How many pennies: "))

        amtTOreturn = takeMoney(choice, quartersCount, dimesCount, nicklesCount, penniesCount)

        if amtTOreturn is False:
            print("Not enough money, please insert more coins.")
        else:
            changeAmountsOfIngredients(choice)
            print(f"Here is your change: ${amtTOreturn:.2f}")
            print(f"Here is your {choice}, enjoy!")
else:
    print("Invalid choice. Please enter espresso, latte, or cappuccino.")

reportPrinter()
