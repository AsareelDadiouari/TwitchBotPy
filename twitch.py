import websocket
import os


def connect():
    ws = websocket.WebSocket()
    ws.connect("wss://irc-ws.chat.twitch.tv:443")
    ws.send(f"PASS {os.environ['TWITCH_OAUTH_TOKEN']}")
    ws.send(f"NICK {os.environ['TWITCH_CHANNEL']}")
    print(ws.recv())
    return ws.recv()
