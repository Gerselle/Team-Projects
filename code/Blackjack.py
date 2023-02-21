import Dealer

dealer = []
players = [[]]
values = ["Two","Three","Four","Five","Six","Seven","Eight","Nine"]

def dealCard(hand, facedUp):

    # TODO: Change this manual input into its respective DealerMotor.py function call.
    input("Press enter button to deal card.")
    card = Dealer.deal(facedUp)

    hand.append(card)

    total = check(hand)
    blackjack = total == 21
    bust = total > 21

    return blackjack, bust


def printHand(hand, reveal):
    # Reveal should only be false if we are printing the dealer's hand for the first time.
    if reveal:
        for x in hand:
            print(x)
    else:
        print(hand[0])
        print("******")

def check(hand):

    total = 0
    aces = 0

    # First add up values of all non-ace cards in the hand.
    for x in hand:
        value = x.split(" ")
        if value[0] in ["Ten", "Jack", "Queen", "King"]:
            total += 10
        elif value[0] not in ["Ace"]:
            total += values.index(value[0]) + 2
        else:
            aces += 1     

    # All aces expect for one will always add 1 to the total.
    # The last ace will add 11 to the total iff the result does not exceed 21, otherwise it will also add 1.
    if (aces):
        while(aces > 1):
            total += 1
            aces -= 1

        if total + 11 <= 21:
            aces += 10

    return total + aces
   

# CLI game starts here.
print("Welcome to Blackjack!")

# Dealing to players and dealer in proper order.
for player in players:
    dealCard(player, True)
    printHand(player, True)

dealCard(dealer, False)
printHand(dealer, True)

for player in players:
    dealCard(player, True)
    printHand(player, True)

dealCard(dealer, True)
printHand(dealer, True)

print("\nDealer has the following hand:")
printHand(dealer, False)

# All players are assumed to be in the "remaining" array unless they bust, in which they will be removed.
remaining = []

# Perform hitting/standing sequence for each player, automatically report standing value unless player busts.
for player in players:
    print("\nPlayer has the following hand:")
    printHand(player, True)
    remaining.append(player)

    if (check(player) == 21):
        print("Player has Blackjack!")
    else:
        hitMe = input("Do you want to hit? Press y if so.\n")
        if (hitMe == "y"):
            while(hitMe == "y"):
                blackjack, bust = dealCard(player)
                if (blackjack):
                    print("Player has Blackjack!")
                    break
                elif(bust):
                    print("You busted with the following hand!: " )
                    printHand(player, True)
                    remaining.remove(player)
                    break
                else:
                    print("\nPlayer has the following hand:")
                    printHand(player, True)
                    hitMe = input("Do you want to hit again? Press y if so.\n")

        if player in remaining:
            print("Player stands with a score of " + str(check(player)))

# Dealer sequence starts here
print("\nDealer has the following hand: ")
printHand(dealer, True)

# Based on the rules, the dealer is forced to keep hitting until they reach 17 or more
if check(dealer) < 17:
    print("\nDealer's hand is less than 17, they must keeping hitting until their hand is equal or over 17.")
    while check(dealer) < 17:
        blackjack, bust = dealCard(dealer)
        if bust:
            print("Dealer busted!\n The following player hands won the game: ")
            for player in remaining:
                printHand(player, True)
        if blackjack:
            print("Dealer has Blackjack!")
            drawPlayers = []
            for player in remaining:
                if check(player) == 21:
                    drawPlayers.append(player)
            if(len(drawPlayers) > 0):
                print("The following hands have drawn with the dealer: ")
                for player in drawPlayers:
                    printHand(player, True)
            else:
                print("Dealer wins!")

# Here, we print off the status of each player in comparison to where the dealer stands
# We should only use this if the dealer didn't get blackjack or didn't bust.
if check(dealer) < 21:
    for player in remaining:
        if check(player) > check(dealer):
            print("Player with the following hand has beaten the dealer!")
        elif check(player) < check(dealer):
            print("Player with the following hand lost to the dealer!")
        else:
            print("Player with the following hand has drawn with the dealer!")
        printHand(player, True)