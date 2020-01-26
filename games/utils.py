from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_update_notification(game_id):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'game_%s' % game_id,
        {'type': 'update_message', 'message': ''}
    )
