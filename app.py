from flask import Flask
from flask import render_template
import websockets_server
import threading

def StartServers(evaluator, httpPort, websocketPort):
    app = Flask(__name__, static_folder='static')

    @app.route('/')
    def index():
        return render_template('index.html')

    http_server = threading.Thread(target=lambda: app.run(port=httpPort), daemon=True)
    http_server.start()

    websockets_server.StartWebsocketServer(evaluator, websocketPort)