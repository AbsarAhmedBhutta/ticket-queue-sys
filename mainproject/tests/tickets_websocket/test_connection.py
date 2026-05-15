import pytest
from channels.testing import WebsocketCommunicator
from mainproject.asgi import application

@pytest.mark.asyncio
async def test_web_socket_check_connection():
    communicator = WebsocketCommunicator(
        application,
        "ws/tickets/"
    )
    
    connected, _ = await communicator.connect()
    assert connected is True

    await communicator.disconnect()