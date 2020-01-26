from django.urls import re_path
import games.consumers as consumers

websocket_urlpatterns = [
    re_path(r'ws/game/(?P<room_name>.*)', consumers.ChatConsumer),
]