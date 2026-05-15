"""
ASGI config for mainproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import tickets.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainproject.settings')

django_app_asgi = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http" : django_app_asgi,
        "websocket" : AuthMiddlewareStack(
            URLRouter(tickets.routing.websocket_urlpatterns)
        )
    }
)