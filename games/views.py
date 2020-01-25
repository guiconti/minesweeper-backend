from rest_framework.decorators import action
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from games.models import Game
from games.serializers import GameSerializer, NewGameSerializer, GameMarkSerializer
from rest_framework.response import Response

class GameViewSet(viewsets.ViewSet):
  queryset = Game.objects.all()

  def create(self, request):
    serializer = NewGameSerializer(data=request.data, context={'request': request})
    game = None
    if serializer.is_valid(raise_exception=True):
      game = Game()
      # Rows, Columns and Mines will be removed from here
      # They will be automatically set when board is created based on difficulty
      game.rows = 9
      game.columns = 9
      game.mines = 10
      game.difficulty = serializer.validated_data.get('difficulty')
      game.seed = serializer.validated_data.get('seed', None)
      game.save()
    serializer = GameSerializer(game)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def retrieve(self, request, pk=None):
    game = get_object_or_404(self.queryset, pk=pk)
    serializer = GameSerializer(game)
    return Response(serializer.data)
  
  @action(detail=True, methods=['post'])
  def flag(self, request, pk=None):
    serializer = GameMarkSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      game = get_object_or_404(self.queryset, pk=pk)
      x = serializer.validated_data['x']
      y = serializer.validated_data['y']
      if y < 0 or y >= game.rows:
        return Response(status=status.HTTP_400_BAD_REQUEST)
      if x < 0 or x >= game.columns:
        return Response(status=status.HTTP_400_BAD_REQUEST)
      game.mark_flag(x, y)
      game.save()
    serializer = GameSerializer(game)
    return Response(serializer.data)
  
  @action(detail=True, methods=['post'])
  def question(self, request, pk=None):
    serializer = GameMarkSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      game = get_object_or_404(self.queryset, pk=pk)
      x = serializer.validated_data['x']
      y = serializer.validated_data['y']
      if y < 0 or y >= game.rows:
        return Response(status=status.HTTP_400_BAD_REQUEST)
      if x < 0 or x >= game.columns:
        return Response(status=status.HTTP_400_BAD_REQUEST)
      game.mark_question(x, y)
      game.save()
    serializer = GameSerializer(game)
    return Response(serializer.data)