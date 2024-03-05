import app
import evaluator

def main():
    app.StartServers(evaluator.SimpleEvaluator(), httpPort=80, websocketPort=31234)

if __name__ == "__main__":
    main()
