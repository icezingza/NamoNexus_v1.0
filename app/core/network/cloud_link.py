"""
CloudLink — WebSocket communication layer for Namo Agents.
"""
import asyncio
import websockets
import json

class CloudLink:
    def __init__(self, uri: str):
        self.uri = uri

    async def broadcast(self, message: dict):
        async with websockets.connect(self.uri) as ws:
            await ws.send(json.dumps(message))
            reply = await ws.recv()
            return json.loads(reply)
