# Importing the relevent libraries
import websockets
import asyncio

PORT = 7896

print("Server listening on Port: " + str(PORT))

connected = set()

async def echo(websocket, path):
    print("Client is Connected")
    connected.add(websocket)
    try:
        async for message in websocket:
            print("Received message from the client: " + message)
            for conn in connected:
                if conn != websocket:
                    await conn.send("Someone said: " + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client is disconnected.",)
    finally:
        connected.remove(websocket)
    

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()