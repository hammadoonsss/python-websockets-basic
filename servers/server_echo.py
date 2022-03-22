# Importing the relevent libraries
import websockets
import asyncio

PORT = 7896

print("Server listening on Port: " + str(PORT))

async def echo(websocket, path):
    print("Client is Connected")
    try:
        async for message in websocket:
            print("Received message from the client " + message)
            await websocket.send("Response: " + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client is disconnected.\n",e)

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()