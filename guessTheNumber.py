import random

attempts = 0

print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' or number of attempts you want\n: ")
if difficulty.isdigit():       #converting it to integer datatype if its a number OR leaving it as it is (string) for easy or hard
    difficulty = int(difficulty)
    attempts = difficulty
    print(f"You chose {attempts} attempts to guess the number i am thinking of.")
    
elif difficulty == 'easy':
    print("You chose easy: You have 10 attempts to guess the number i am thinking of.")
    attempts = 10
elif difficulty == 'hard':
    print("You chose hard: You have only 5 attempts to guess the number i am thinking of.")
    attempts = 5
else:
    print("Invalid Input: Enter easy, hard or integer value")
    exit()

myNumber = random.randint(1,100)

while attempts > 0:
    guess = 0
    guess = int(input("Make a guess: "))
    if guess > myNumber:
        if guess - myNumber >= 10:
            print("Too High")
        else:
            print("Bit High")
    elif myNumber > guess:
        if myNumber - guess >= 10:
            print("Too Low")
        else:
            print("Bit Low")
    elif myNumber == guess:
        print("You Win.")
        exit()
    attempts -= 1

print("\n\nSad, you ran out of attempts. I win".upper())

    



