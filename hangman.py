import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = 0
lives = 7
correct_guesses = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    if len(guess) > 1:
        print("Please enter only one letter.")
        continue

    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(guess)
            
        elif letter in correct_guesses:
            display += letter
        else:
            
            display += "_"
    if guess not in chosen_word:
        lives -= 1
        print("Incorrect guess. You have", lives, "lives left.")

    
    print(display)

    if "_" not in display:
        game_over = True
        print(f"Congratulations! You've won with {lives} lives left")
    if lives == 0:
        game_over = True
        print("Sorry, you've ran out of lives. The word was:", chosen_word)





