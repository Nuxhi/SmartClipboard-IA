import threading
import uvicorn
import webbrowser
import time
import sys

server = None
thread = None


def run_server():
    global server
    print("Run server")
    config = uvicorn.Config("mainserveur:app", host="127.0.0.1", port=6767, log_level="warning")
    server = uvicorn.Server(config)
    server.run()
    print("fin de run_server")


def start_server():
    global thread
    print("Start server")
    thread = threading.Thread(target=run_server)
    thread.start()
    webbrowser.open("http://127.0.0.1:6767/")


def stop_server():
    global server
    print("Stop server")
    if server:
        print("Arrêt du serveur")
        server.should_exit = True


if __name__ == "__main__":
    start_server()

    thread.join()

    print("Programme terminé")
    sys.exit(0)