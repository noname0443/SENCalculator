import asyncio
import websockets
import http.server
import socketserver
import signal
import threading
import time
from http.server import ThreadingHTTPServer
import os 

async def ProcessRequests(websocket, path):
    while True:
        data = await websocket.recv()
        await websocket.send(str(eval(data)))

def WSCallback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    ws_server = websockets.serve(ProcessRequests, '0.0.0.0', 444)

    loop.run_until_complete(ws_server)
    loop.run_forever()
    loop.close()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/static"
        print(dir_path)
        super().__init__(*args, directory=dir_path, **kwargs)

def RunThreads():
    WSServer = threading.Thread(target=WSCallback, daemon=True)
    WSServer.start()

    HTTPServer = ThreadingHTTPServer(("127.0.0.1", 80), Handler)
    HTTPServer = threading.Thread(target=HTTPServer.serve_forever, daemon=True)
    HTTPServer.start()