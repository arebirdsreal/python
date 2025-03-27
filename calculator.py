import calculator_art as art
print(art.art)
def calc(operator, operand_1, operand_2):
    if operator == '+':
        return operand_1 + operand_2
    elif operator == '-':
        return operand_1 - operand_2
    elif operator == '*':
        return operand_1 * operand_2
    elif operator == '/':
        return operand_1 / operand_2
choice = ''
choice = input("+ for addition \n- for subtraction \n* for multiplication \n"
                "/ for division: \n")
a,b = input("Enter the 2 operands seperated by comma: \n").split(',')
operand_1, operand_2 = int(a), int(b)

want_to_continue = ''
while want_to_continue != 'n':
    result = calc(operator=choice, operand_1=operand_1, operand_2=operand_2)
    print(f"{result}\n\n")
    want_to_continue = input("Do you want to continue? Enter 'y' or 'n' only.")
    if want_to_continue == 'y' or want_to_continue == 'n':
            None
    else:
        print("Strictly enter 'y' or 'n' only")


    while want_to_continue == 'y':
        choice = input("+ for addition \n, - for subtraction \n, * for multiplication \n, "
                "/ for division: \n")
        operand_2 = int(input("Enter second operand: "))
        result = calc(operator=choice, operand_1=result, operand_2=operand_2)
        print(result)
        want_to_continue = input("Do you want to continue? ")
        if want_to_continue == 'y' or want_to_continue == 'n':
            None
        else:
            print("Strictly enter 'y' or 'n' only")
        




  
  
  
  
