bids = {}
choice = ""
key = ''
choice = input("Enter choice: ")
while choice == 'yes':
    key = input("Enter your name: ")
    bids[key] = int(input("Enter your bid: "))
    if choice == 'yes':
        choice = input("Enter choice: ")
highest_bid = 0
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder
print(f"The highest bid is {highest_bid} by {winner}!")
