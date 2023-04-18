import random
import socket
import MotorControl
from Card_Reader import CardScanner

LOCAL_SCANNER = False

ranks = {"ace","2","3","4","5","6","7","8","9","10","jack","queen","king"}
suits = {"clubs", "diamonds", "hearts", "spades"}
dealt = []
dealer = []
player = []

def start(client):
    global dealt
    global dealer 
    global player

    dealt = []
    dealer = []
    player = []

# Manual dealing to players and dealer in proper order.
    deal(player)

    deal(dealer)

    deal(player)

    deal(dealer)

    result = "\nDealer has the following hand: " + printHand(dealer, True) + "\nYou have the following hand: " + printHand(player, True) + "\nYou have a current score of " + str(check(player))

    client.send(bytes(result, "utf-8"))

def deal(hand):
    
    if LOCAL_SCANNER:
        card = CardScanner.scanCard
    else: 
        # TODO: Change this manual input into its respective DealerMotor.py function call.
        card = random.choice(ranks) + "_of_" + random.choice(suits)

        while card in dealt:
            card = random.choice(ranks) + "_of_" + random.choice(suits)

    hand.append(card)
    dealt.append(card)

    total = check(hand)
    blackjack = total == 21
    bust = total > 21

    return blackjack, bust

def hit(client):
    blackjack, bust = deal(player)

    result = ""

    if (blackjack):
        result = "\nYou got Blackjack!"
    elif(bust):
        result = "\nYou busted with the following hand!: " + printHand(player, True) + "\nYour score was " + str(check(player))
    else:
        result = "\nYou have the following hand:"  + printHand(player, True) + "\nYou have a current score of " + str(check(player))
    
    client.send(bytes(result, "utf-8"))

def stand(client):
    result = "You stand with a score of " + str(check(player)) + "\nDealer has the following hand: " + printHand(dealer, True)

    # Based on the rules, the dealer is forced to keep hitting until they reach 17 or more
    if check(dealer) < 17:
        result = result + "\nDealer's hand is less than 17, they must keeping hitting until their hand is equal or over 17.\n"
        while check(dealer) < 17:
            blackjack, bust = deal(dealer)
            if bust:
                result = result + "\nDealer busted! You won!"
            if blackjack:
                result = result + "\nDealer has Blackjack!"
            
                if(check(player) == 21):
                     result = result + " It's a draw!"
                else:
                     result = result + " Dealer wins!"

    result = result + "\nDealer ended the game with the following hand: " + printHand(dealer, True)

    # Here, we print off the status of each player in comparison to where the dealer stands
    # We should only use this if the dealer didn't get blackjack or didn't bust.
    if check(dealer) < 21:
        
        if check(player) > check(dealer):
            result = result + "\nYou beat the dealer!"
        elif check(player) < check(dealer):
            result = result + "\nYou lost to the dealer!"
        else:
            result = result + "\nYou drew with the dealer!"
    
    result = result + "\nYou ended with the following hand: " + printHand(player, True)
    
    client.send(bytes(result, "utf-8"))

def printHand(hand, reveal):
    # Reveal should only be false if we are printing the dealer's hand for the first time.
    handPrint = ""
    if reveal:
        for x in hand:
            handPrint = handPrint + "\n" + x
    else:
        handPrint = handPrint + "\n" + hand[0] + "\n******"
    
    return handPrint

def check(hand):

    total = 0
    aces = 0

    # First add up values of all non-ace cards in the hand.
    for x in hand:
        value = x.split(" ")
        if value[0] in ["Ten", "Jack", "Queen", "King"]:
            total += 10
        elif value[0] not in ["Ace"]:
            total += ranks.index(value[0]) + 2
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
   
HOST = "localhost"
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        client, address = s.accept()
        print(f"Connected by {address}")
        data = client.recv(1024)
        print(data)
        if(data == b'0'):
            hit(client)
        elif(data == b'1'):
            stand(client)
        elif(data == b'2'):
            start(client) 