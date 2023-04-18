import json
import asyncio
import websockets
import Player

playerClients = []

async def updatePlayers(message: str):
    for player in playerClients:
        await player.send(message)

async def new_player_connection(websocket, path):
    print("Hey guy?")

    while True:
        message = await websocket.recv()
        print(message)
        playerClients.append(Player(message, websocket))


# Start the WebSocket server
start_server = websockets.serve(new_player_connection, "localhost", 1337)

# Run the event loop to listen for incoming connections
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()