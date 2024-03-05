import app
import evaluator

def main():
    app.start_servers(evaluator.SimpleEvaluator(), http_port=80, websocket_port=31234)

if __name__ == "__main__":
    main()
