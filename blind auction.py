auction_info = {}
choice = ""
key = ''
choice = input("Enter choice: ")
while choice == 'yes':
    key = input("Enter your name: ")
    auction_info[key] = int(input("Enter your bid: "))
    if choice == 'yes':
        choice = input("Enter choice: ")
highest_bid = 0
for bidder in auction_info:
    if auction_info[bidder] > highest_bid:
        highest_bid = auction_info[bidder]
        winner = bidder
print(f"The highest bid is {highest_bid} by {winner}!")
