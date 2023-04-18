class Player:
    def __init__(self, username, websocket):
        self.username = username
        self.websocket = websocket
        self.gamemode = "lobby"
        self.state = "ready"
        self.hand = []
        self.bet = 0
        self.chips = 1000

    def setState(self, state):
        self.state = state

    def addCard(self, card):
        self.hand.append(card)

    def checkHand(self):
        total = 0
        aces = 0
        values = ["2", "3", "4", "5", "6", "7", "8", "9"]

        # First add up values of all non-ace cards in the hand.
        for x in self.hand:
            value = x.split("_")
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

    def clearHand(self):
        self.hand = []

    def setFolded(self):
        self.is_folded = True

    def setBet(self, bet):
        self.bet = bet

    def resetBet(self):
        self.bet = 0

    def removeChips(self, amount):
        self.chips -= amount

    def addChips(self, amount):
        self.chips += amount

    def gamemode(self, game):
        self.gamemode = game

    def send(self, json):
        self.websocket.send(json)

    def to_dict(self):
        return {
            'username': self.username,
            'ready': self.ready,
            'gamemode': self.gamemode,
            'hand': self.hand,
            'doubled': self.doubled,
            'folded': self.folded,
            'bet': self.bet,
            'chips': self.chips
        }


    
