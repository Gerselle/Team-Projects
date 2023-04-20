import json

class Player:
    def __init__(self, username=None, websocket=None):
        self.username = username
        self.websocket = websocket
        self.choice = "Blackjack"
        self.gamemode = "lobby"
        self.state = "Waiting"
        self.hand = []
        self.bet = 0
        self.chips = 1000
        self.gamestate = [[self.username, self.state, self.bet, self.choice]]
        self.data = json.dumps({
            "gamestate": self.gamestate,         
            "gamemode" : "lobby"
        })
        

    def __str__(self):
        return f"username: {self.username}, websocket: {self.websocket}, choice: {self.choice}, gamemode: {self.gamemode}, state: {self.state}, hand: {self.hand}, bet: {self.bet}, chips: {self.chips}, gamestate: {self.gamestate}, data: {self.data}"


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

    def setSocket(self, websocket):
        self.websocket = websocket

    def setState(self, state):
        self.state = state

    def setGame(self, game):
        self.gamemode = game
        self.data = json.dumps({
            "gamestate": self.gamestate,         
            "gamemode" : game
        })

    def setGamestate(self, players):
        playersGamestate = []
        for player in players:
            playersGamestate.append([player.username, player.state, player.bet, player.choice])
        self.gamestate = playersGamestate

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

    async def update(self, updateJSON):

        update = json.loads(self.data)
        for element in updateJSON:
            print(element)
            update[element] = updateJSON[element]
    
        self.data = json.dumps(update)

    def updateGamestate(self):
        self.gamestate = [[self.username, self.state, self.bet, self.choice]]

    def check(self):
        total = 0
        aces = 0
        values = ["2", "3", "4", "5", "6", "7", "8", "9"]

        # First add up values of all non-ace cards in the hand.
        for card in self.hand:
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
    
