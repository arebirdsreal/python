import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
lives = 7
correct_guesses = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(guess)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"
    else:
        lives -= 1
        print("You have", lives, "lives left.")
    print(display)

    if "_" not in display:
        game_over = True
        print("Congratulations! You've won!")
    if lives == 0:
        game_over = True
        print("Sorry, you've lost. The word was:", chosen_word)





