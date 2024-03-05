import asyncio
import websockets
import http.server
import socketserver
import signal
import time
import os

async def ProcessRequests(evaluator, websocket, path):
    while True:
        data = await websocket.recv()
        await websocket.send(str(evaluator.eval(data)))

def StartWebsocketServer(evaluator, websocketPort):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    Processor = lambda w, p : ProcessRequests(evaluator, w, p)
    ws_server = websockets.serve(Processor, '0.0.0.0', websocketPort)

    loop.run_until_complete(ws_server)
    loop.run_forever()
    loop.close()