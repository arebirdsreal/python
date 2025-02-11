import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess letter: ")
guess.lower()

for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")

placeholder = ""
word_length = len(chosen_word)
for i in range(0, word_length):
    placeholder += "_"
print(placeholder)

display = ""


