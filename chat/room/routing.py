from django.urls import path
from . import conusmer
websocket_urlpatterns = [
    path('ws/<str:room_name>/', conusmer.ChatConsumer.as_asgi()),
]