# Importing the relevant libraries
import websockets
import asyncio

async def listen():
    # Running Server URL
    url="ws://127.0.0.1:7896"

    async with websockets.connect(url) as ws:
        await ws.send("Hello Server!!")
        while True:
            msg = await ws.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())

# Create virtual environment 
#   - using python 3.7 and above

# Install websockets
#   - websockets requires Python ≥ 3.7
#   - $ pip install websockets



# To Check this program 
# on browser - https://sync-chasing-ball.glitch.me/
# running server url - "ws://simple-websocket-server-echo.glitch.me/
