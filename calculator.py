import calculator_art as art

def add(num1, num2):
    """adds num1 and num2"""
    return num1+num2
def sub(num1, num2):
    """subtracts num2 from num1"""
    return num1-num2
def multi(num1, num2):
    """mutliplies num1 with num2"""
    return num1*num2
def div(num1, num2):
    """divides num1 by num2"""
    return num1/num2

operations = {
    "+" : add,
    "-" : sub,
    "*" : multi,
    "/" : div
}
def calculator():
    print(art.themoloch_art)
    num1 = float(input("Enter First number: \n"))

    should_accumulate = True
    while should_accumulate: 
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter operation to be performed: ")
        num2 = float(input("Enter the other number: \n"))

        answer = operations[operation_symbol](num1=num1, num2=num2) 
        """here: operations[operation_symbol] is the function being called
            and then the num1 and num2 are the arguments"""
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Enter 'y' to continue performing calculations on answer\n"
                        "Enter 'n' to start a fresh calculation.")
        if choice == 'y':
            num1 = answer
        else:
            print("\n"*50)
            should_accumulate = False
            calculator()
calculator()
            









  
  
  
  
