import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', ',', '.', '/', '\\', '{', '}',
        '[', ']', '|', '`', '~', '<', '>', '?']

number_of_letters = int(input("How many letters do you want in your password? "))
number_of_numbers = int(input("How many numbers do you want in your passwodd? "))
number_of_symbols = int(input("how many symbols do you want in your password? "))


password = ""
random_char = ""
random_num = 1

for i in range(1, number_of_letters+1):
    random_char = random.choice(alphabet)
    password += random_char

for i in range(1, number_of_numbers+1):
    random_num = random.choice(numbers)
    password += str(random_num)

for i in range(1, number_of_symbols+1):
    random_symbol = random.choice(symbols)
    password += str(random_symbol)

print(password)

for i in password:
    print(password[random.randint(0, len(password)-1)])









