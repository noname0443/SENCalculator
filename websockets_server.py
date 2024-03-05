import asyncio
import websockets

def start_websocket_server(evaluator, websocket_port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def process_requests(websocket, path):
        while True:
            data = await websocket.recv()
            await websocket.send(str(evaluator.eval(data)))

    ws_server = websockets.serve(process_requests, '0.0.0.0', websocket_port)

    loop.run_until_complete(ws_server)
    loop.run_forever()
    loop.close()
