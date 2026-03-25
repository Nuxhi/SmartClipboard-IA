from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
import os
import threading
from web import launch_web_ui

app = FastAPI()

path = os.path.dirname(os.path.abspath(__file__))


@app.get("/")
def get():
    return FileResponse(os.path.join(path, "index.html"))

@app.get("/test")
def test():
    return "Hello tester"

@app.post("/inverse")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client websocket connecté")

    try:
        while True:
            # We only need to wait here; when the page closes, disconnect is raised.
            await websocket.receive_text()
    except WebSocketDisconnect:
        print("Client websocket déconnecté, arrêt du serveur")

        def stop():
            launch_web_ui.stop_server()
            #os._exit(0)

        threading.Thread(target=stop, daemon=True).start()