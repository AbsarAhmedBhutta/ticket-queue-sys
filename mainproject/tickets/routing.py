from tickets.consumers import TicketsWebSocket
from django.urls import path

websocket_urlpatterns = [
    path("ws/tickets/", TicketsWebSocket.as_asgi()),
]