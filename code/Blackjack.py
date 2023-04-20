import random
import Player
import json

REAL_CARDS = False

class Blackjack:
    def __init__(self, players):
        self.players = players
        self.dealt = []
        self.dealer = Player.Player()

    def start(self):

        for player in self.players:
            self.deal(player)

        self.deal(self.dealer)

        for player in self.players:
            self.deal(player)

        self.deal(self.dealer)

        # Update all the players
        for player in self.players:
            self.update(player)

    def deal(self, player):

        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
        suits = ["hearts", "diamonds", "clubs", "spades"]

        # TODO: Change this manual input into its respective DealerMotor.py function call.
        if(REAL_CARDS):
            print("Totally real here")
        else:
            card = random.choice(values) + "_of_" + random.choice(suits)
            while card in self.dealt:
                card = random.choice(values) + "_of_" + random.choice(suits)
            self.dealt.append(card)

        player.addCard(card)
        total = player.check()
     
        blackjack = total == 21
        bust = total > 21

        return blackjack, bust

    def hit(self, player):
        blackjack, bust = self.deal(player)

        if (blackjack):
            player.setState("Blackjack!")
        elif(bust):
            player.setState("Busted!")
        else:
            player.setState(player.check())

        # Update all the players
        for otherPlayer in self.players:
            self.update(otherPlayer)

    def stand(self, player):
        player.setState("Stand")

        lobbyStand = True

        for player in self.players:
            if(player.state != "Stand"):
                lobbyStand = False

        if(lobbyStand):
            # Based on the rules, the dealer is forced to keep hitting until they reach 17 or more
            if self.check(self.dealer) < 17:
                while self.check(self.dealer) < 17:
                    blackjack, bust = self.deal(self.dealer)

                for player in self.players:
                    if(not bust):
                        if player.check() > self.dealer.check():
                            player.setState("Won!")
                            player.addChips(int(player.bet * 1.5))
                        elif player.check() == self.dealer.check():
                            player.setState("Draw!")
                            player.addChips(player.bet)
                        else:
                            player.setState("Lost!")
                    else:
                        player.setState("Draw!")
                        player.addChips(player.bet)
                    player.resetBet()
        
        # Update all the players
        for otherPlayer in self.players:
            self.update(otherPlayer)

    def double(self, player):
        if player.bet != 0:
            player.setBet(2 * player.bet)
            player.removeChips(player.bet)
            player.setState(player.bet)

        # Update all the players
        for otherPlayer in self.players:
            self.update(otherPlayer)


    def bet(self, player, bet):
        if player.bet == 0:
            player.setBet(bet)
            player.removeChips(bet)
            player.setState(player.bet)
            
        # Update all the players
        for otherPlayer in self.players:
            self.update(otherPlayer)

    def check(hand):
        total = 0
        aces = 0
        values = ["2", "3", "4", "5", "6", "7", "8", "9"]

        # First add up values of all non-ace cards in the hand.
        for card in hand:
            value = card.split("_")
            if value[0] in ["10", "jack", "queen", "king"]:
                total += 10
            elif value[0] not in ["ace"]:
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
    
    def update(self, player):

        updateData = {
            "dealer-hand": self.dealer.hand,
            "dealer-score": self.dealer.check(),
            "blackjack-hand": player.hand,            
            "blackjack-score": player.check(),
            "blackjack-bet": player.bet,
            "blackjack-chips": player.chips,
            "gamemode": player.gamemode
        }

        print(updateData)
        
        player.update(updateData)