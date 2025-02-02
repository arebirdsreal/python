import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', ',', '.', '/', '\\', '{', '}',
        '[', ']', '|', '`', '~', '<', '>', '?']

number_of_letters = int(input("How many letters do you want in your password? "))
number_of_numbers = int(input("How many numbers do you want in your passwodd? "))
number_of_symbols = int(input("how many symbols do you want in your password? "))


random_char = ""
random_num = 0

# we want to use the shuffle() function which works only on lists, so storing the password in list
password_list =[]

for i in range(0, number_of_letters):
    random_char = random.choice(alphabet)
    password_list += random_char
    #could have used password_list.append(random_char) as well instead of "+="

for i in range(0, number_of_numbers):
    random_num = random.choice(numbers)
    password_list += str(random_num)
    #could have used password_list.append(random_char) as well instead of "+="


for i in range(0, number_of_symbols):
    random_symbol = random.choice(symbols)
    password_list += str(random_symbol)

# using the shuffle() function
random.shuffle(password_list)

# putting each character from the list to the string
password = ""
for character in password_list:
    password += character
print(f"Password: {password}")