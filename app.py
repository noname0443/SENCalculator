import threading
from flask import Flask
from flask import render_template
import websockets_server
from waitress import serve


def start_servers(evaluator, http_port, websocket_port):
    app = Flask(__name__, static_folder='static')

    @app.route('/')
    def index():
        return render_template('index.html')

    http_server = threading.Thread(target=lambda: serve(app, host="0.0.0.0", port=http_port), daemon=True)
    http_server.start()

    websockets_server.start_websocket_server(evaluator, websocket_port)
