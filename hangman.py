import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

word_length = len(chosen_word)
for i in range(0, word_length):
    placeholder += "_"
print(placeholder)
list(placeholder)

guess = input("Guess letter: ")
guess.lower()

number_of_guesses = 0
while number_of_guesses < 7:
    for char in chosen_word:
        if char == guess:
            print("you got letter/s right")
            placeholder[char] = guess
        else:
            print("The secret word does not contain this letter.")
            break


display = ""
for letter in chosen_word:
    if guess == letter:
        # print("Right")
        display += letter
    else:
        # print("Wrong")
        display += "_"

print(display)





