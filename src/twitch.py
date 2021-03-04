import websocket
import os


class Twitch:

    def connect(self):
        ws = websocket.WebSocket()
        ws.connect("wss://irc-ws.chat.twitch.tv:443")
        ws.send(f"PASS {os.environ['TWITCH_OAUTH_TOKEN']}")
        ws.send(f"NICK {os.environ['TWITCH_CHANNEL']}")
        return ws.recv()
