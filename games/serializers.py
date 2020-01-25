import json
from rest_framework import serializers
from games.models import Game
import games.constants as constants

class GameSerializer(serializers.ModelSerializer):
  board = serializers.SerializerMethodField()

  class Meta:
    model = Game
    fields = ('id', 'status', 'board', 'rows', 'columns',
              'mines', 'difficulty', 'duration', 'score')

  def get_board(self, obj):
    masked_board = json.loads(obj.board)
    for i in range(len(masked_board)):
      view_row = []
      for j in range(len(masked_board[i])):
        if masked_board[i][j] == constants.MINE:
          masked_board = constants.EMPTY_SPACE
    return masked_board

class NewGameSerializer(serializers.Serializer):
  difficulty = serializers.IntegerField(default=constants.DIFFICULTY_EASY)

class GameMarkSerializer(serializers.Serializer):
  x = serializers.IntegerField(min_value=0)
  y = serializers.IntegerField(min_value=0)