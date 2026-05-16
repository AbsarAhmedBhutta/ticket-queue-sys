from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TicketsWebSocket(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.group_name = "tickets_dashboard"
        await self.channel_layer.group_add(self.group_name, self.channel_name)        
        await self.accept()
        print("connected")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        print("Disconnected")
         
    async def ticket_created(self, event):
        await self.send(text_data=json.dumps({
            "type": "ticket_created",
            "ticket": event["ticket"]
        }))
        print("ticket_created")