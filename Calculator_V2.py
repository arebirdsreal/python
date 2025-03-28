import calculator_art as art

print(f"{art.art}")
print("""Use it like a Normal Calculator: 
        IF YOU WISH TO PERFORM MORE CALCULATIONS ON THAT NUMBER, CONTINUE BY ENTERING THE NEXT OPERATION FOLLOWED BY THE OTHER NUMBER""")
    
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b 
def div(a,b):
    if b == 0:
        return "Error: Division by Zero"
    return a/b 
def pow(a,b):
    return a ** b

operations = {
    "+" : add,
    "-" : sub,
    "*" : multi,
    "/" : div,
    "^" : pow
}

def calculator():
    num1 = float(input("Enter First number:\n"))
    want_to_continue = True                                                    #equivalent to should_Accumulate
    counter = 0
    while want_to_continue:
        if counter > 0:
            print("")
        else:
            for operation in operations:
                print(operation)
            perform = input("Enter operation to be performed: \n")             #equivalent to operation_symbol
        num2 = float(input("Enter Second number: \n"))
        answer = operations[perform](num1, num2)
        print(f"{num1} {perform} {num2} = {answer} \n")
        perform = input(f"{answer} Enter operation to continue with this number or Enter ac to start a fresh calculation\n")
        if ((perform == '+') or (perform == '-') or (perform == '*') or (perform == '/')):
            want_to_continue = True
            num1 = answer
            counter = 1
        elif(perform == 'ac'):
            want_to_continue = False
            counter = 0
            print("\n"*25)
            print(art.art)
            calculator()
        else:
            print("Invalid Input\nEnter one of the operations or ac only")
calculator()
    
