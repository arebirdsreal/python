import game_data
import random
import art_higherorlower
print(art_higherorlower.art1)

score = 0
keep_playing = True
while keep_playing:
    A = random.choice(game_data.data)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}\n")
    print(f"{art_higherorlower.art2}\n")
    B = random.choice(game_data.data)
    while A == B:
        B = random.choice(game_data.data)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}\n")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == 'a':
        if A['follower_count'] > B['follower_count']:
            score += 1
            print(f"You're right, Current Score: {score}")
            keep_playing = True
        else:
            print(f"Game over, You lost. Final Score: {score}")
            keep_playing = False
    elif choice == 'b':
        if B['follower_count'] > A['follower_count']:
            score += 1
            print(f"You're right, Current score: {score}")
            keep_playing = True
        else:
            print(f"Game over, You lost. Final Score: {score}")
            keep_playing = False
    else:
        print("Enter 'A' or 'B' only")



