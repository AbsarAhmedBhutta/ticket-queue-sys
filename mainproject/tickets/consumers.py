from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TicketsWebSocket(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        
        await self.send(text_data=json.dumps({
            "Message" : "Connected"
        }))
        
    async def disconnet(self, close_code):
        print("Disconnected")
         