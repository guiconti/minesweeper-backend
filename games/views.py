from rest_framework.decorators import action
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from games.models import Game
from games.serializers import GameSerializer, NewGameSerializer
from rest_framework.response import Response

class GameViewSet(viewsets.ViewSet):
  queryset = Game.objects.all()

  def retrieve(self, request, pk=None):
    game = get_object_or_404(self.queryset, pk=pk)
    serializer = GameSerializer(game, context={'request': request})
    return Response(serializer.data)

  def create(self, request, pk=None):
    serializer = NewGameSerializer(data=request.data)
    game = None
    if serializer.is_valid(raise_exception=True):
      game = Game()
      # Rows, Columns and Mines will be removed from here
      # They will be automatically set when board is created based on difficulty
      game.rows = 9
      game.columns = 9
      game.mines = 10
      game.difficulty = serializer.validated_data['difficulty']
      game.save()
    serializer = GameSerializer(game, context={'request': request})
    return Response(serializer.data)