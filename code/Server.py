import json
import asyncio
import websockets
import Blackjack
import Player
import random
import MotorControl

playerClients = {}
playerGameChoice = {"dud":"Blackjack"}
game = None

async def new_player_connection(websocket, path):
    while True:
        received = await websocket.recv()
        print(received)
        data = json.loads(received)
        username = data["username"]
        if username in playerClients:
            player = playerClients[username]

        match data["action"]:
            case "connection":
                if username in playerClients:
                    player.setSocket(websocket)
                    global game
                    if game is not None:
                        game.update(player)
                else:
                    playerClients[username] = Player.Player(username, websocket)
            case "Ready":
                if player.state == "Waiting":
                    player.setState("Ready")
                    # Assume we are starting unless proven otherwise 
                    start = True
                    for otherPlayer in playerClients:
                        if playerClients[otherPlayer].state != "Ready":
                            start = False

                    # If we are starting, pick randomly from the players to decide which game to start
                    if start:
                        choice = random.choice(list(playerGameChoice.values()))
                        players = []
                        for otherPlayer in playerClients:
                            playerClients[otherPlayer].setGame(choice)
                            players.append(playerClients[otherPlayer])
                        newmode = ""
                        match choice:
                            
                            case "Blackjack":
                                game = Blackjack.Blackjack(players)
                                newmode = "Blackjack"
                            # case "Texas Holdem":
                            #     game = Poker.Poker(playerClients)
                        game.start()
                else:
                    player.setState("Waiting")
                    
            case "setgame":
                player.choice = data["additional"]
                playerGameChoice[username] = data["additional"]
            case "bet":
                game.bet(player, data["additional"])
            case "hit":
                game.hit(player)
            case "stand":
                game.stand(player)
            case "double":
                game.double(player)
            case "shuffle":
                # Put stuff to shuffle cards here
                print("Shuffled!")
            case _:
               print("Error with keyword: " + data["action"])

        for otherPlayer in playerClients:
            playerClients[otherPlayer].updateGamestate()

        for otherPlayer in playerClients:
            print(playerClients[otherPlayer])
            await websocket.send(playerClients[otherPlayer].data)


# Start the WebSocket server
start_server = websockets.serve(new_player_connection, "localhost", 1337)

# Run the event loop to listen for incoming connections
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()