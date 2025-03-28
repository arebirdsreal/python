import random
def deal_card():        #works
  """Returns a random card value"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)  

def calculate_score(list):
  """Returns sum of face values of cards in list,
    Also replaces 11(if present) with 1 if score is already greater than 21"""
  score = sum(list)
  if len(list) == 2 and score == 21:
    return 0
  while score > 21 and 11 in list:
     list.remove(11)
     list.append(1)
     score = sum(list)
  return score   

#initializing user's and computer's card lists
user_cards = []
computer_cards = []

#giving 1 card to both parties for the first time
user_cards.append(deal_card())
computer_cards.append(deal_card())

while True:         #loop will be exitted using a break statement on line 43
    user_score = calculate_score(user_cards)
    print(f"Your cards: {user_cards}, Your Current Score: {user_score}")

   #check if user is losing or winning FIRST ONLY, without even letting the computer play
    if user_score == 0:
      print("BlackJack, USER Wins")
      exit()    #this quits the program entirely

    elif user_score > 21:
      print("Bust, COMPUTER Wins")
      exit()    #this quits the program entirely
    
    choice = input("Enter Hit to draw another card and try getting closer to 21\n"
                "or Enter Stand to end your:\n: ").lower()
    if choice == 'stand':
       break      #breaks out of the while loop and ends the user's turn (does not quit the program entirely)
    elif choice == 'hit':
       user_cards.append(deal_card())

computer_score = calculate_score(computer_cards)
print(f"Computer's first card: {computer_cards[0]}, Computer's current score: {computer_score}")

while computer_score < 17:
   computer_cards.append(deal_card())
   computer_score = calculate_score(computer_cards)

print(f"Computer's Final Hand: {computer_cards}, Computer's Final Score: {computer_score}")

#To determine the winner
if computer_score == 0:
   print("BlackJack, COMPUTER Wins")
   exit()
elif computer_score > 21:
   print("Bust, USER Wins")
   exit()
elif computer_score > user_score:
   print("COMPUTER Wins")
   exit()
elif user_score > computer_score:
   print("USER Wins")
   exit()
else:
   print("DRAW, PUSH")
   exit()
   





   
if computer_score > user_score:
    print("COMPUTER Wins")
else:
    print("USER Wins")




