from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from games.models import Game
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        try:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = 'game_%s' % self.room_name
            Game.objects.get(pk=self.room_name)
        except:
            return
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        pass
    
    def update_message(self, event):

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': 'update'
        }))