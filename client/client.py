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
