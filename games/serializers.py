import json
from rest_framework import serializers
from games.models import Game
import games.constants as constants


class GameSerializer(serializers.ModelSerializer):
    board = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ('id', 'status', 'board', 'rows', 'columns',
                  'mines', 'difficulty', 'seed')

    def get_board(self, obj):
        board = json.loads(obj.player_board)
        return board


class NewGameSerializer(serializers.Serializer):
    difficulty = serializers.IntegerField(
        min_value=constants.DIFFICULTY_EASY,
        max_value=constants.DIFFICULTY_HARD,
        default=constants.DIFFICULTY_EASY,
        required=False
    )
    seed = serializers.IntegerField(required=False)


class GameMarkSerializer(serializers.Serializer):

    def validate_x(self, value):
        if value >= self.context.get('columns'):
            raise serializers.ValidationError(
                'X value is bigger that the amount of columns.')
        return value

    def validate_y(self, value):
        if value >= self.context.get('rows'):
            raise serializers.ValidationError(
                'Y value is bigger that the amount of rows.')
        return value

    x = serializers.IntegerField(min_value=0)
    y = serializers.IntegerField(min_value=0)
