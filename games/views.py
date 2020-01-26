from rest_framework.decorators import action
from rest_framework import status, serializers, viewsets
from django.shortcuts import get_object_or_404
from games.models import Game
from games.serializers import GameSerializer, NewGameSerializer, GameMarkSerializer
from rest_framework.response import Response


class GameViewSet(viewsets.ViewSet):
    queryset = Game.objects.all()

    """
    @api {post} minesweeper/v1/games/ Create a new game
    @apiName CreateGame
    @apiGroup Game
    @apiVersion 1.0.0

    @apiParam {Number} [difficulty] Game's difficulty.
    @apiParam {Number} [seed] Game's board generation seed.

    @apiSuccess {String} id Game's id.
    @apiSuccess {Number} status Game's status.
    @apiSuccess {Array} board Game's board.
    @apiSuccess {Number} rows Game's amount of rows.
    @apiSuccess {Number} columns Game's amount of columns.
    @apiSuccess {Number} mines Game's amount of mines.
    @apiSuccess {Number} difficulty Game's difficulty.
    @apiSuccess {Number} seed Game's board seed.

    @apiError InvalidDifficulty Difficulty sent is invalid.
    @apiError InvalidSeed Seed sent is invalid.
    """
    def create(self, request):
        serializer = NewGameSerializer(
            data=request.data, context={'request': request})
        game = None
        if serializer.is_valid(raise_exception=True):
            game = Game()
            game.difficulty = serializer.validated_data.get('difficulty')
            game.seed = serializer.validated_data.get('seed', None)
            game.save()
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    """
    @api {get} minesweeper/v1/games/:id/ Retrieve a game
    @apiName RetrieveGame
    @apiGroup Game
    @apiVersion 1.0.0

    @apiParam {String} id Game's uuid.

    @apiSuccess {String} id Game's id.
    @apiSuccess {Number} status Game's status.
    @apiSuccess {Array} board Game's board.
    @apiSuccess {Number} rows Game's amount of rows.
    @apiSuccess {Number} columns Game's amount of columns.
    @apiSuccess {Number} mines Game's amount of mines.
    @apiSuccess {Number} difficulty Game's difficulty.
    @apiSuccess {Number} seed Game's board seed.

    @apiError GameNotFound Game was not found.
    """
    def retrieve(self, request, pk=None):
        uuid = serializers.UUIDField().to_internal_value(data=pk)
        game = get_object_or_404(self.queryset, pk=uuid)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    """
    @api {patch} minesweeper/v1/games/:id/open/ Open a cell in the game
    @apiName OpenCell
    @apiGroup Game
    @apiVersion 1.0.0

    @apiParam {String} id Game's uuid.
    @apiParam {Number} x X Position of the desired cell to open
    @apiParam {Number} x Y Position of the desired cell to open

    @apiSuccess {String} id Game's id.
    @apiSuccess {Number} status Game's status.
    @apiSuccess {Array} board Game's board.
    @apiSuccess {Number} rows Game's amount of rows.
    @apiSuccess {Number} columns Game's amount of columns.
    @apiSuccess {Number} mines Game's amount of mines.
    @apiSuccess {Number} difficulty Game's difficulty.
    @apiSuccess {Number} seed Game's board seed.

    @apiError GameNotFound Game was not found.
    @apiError InvalidX X sent is not within the board's range
    @apiError InvalidY Y sent is not within the board's range
    @apiError GameOver You cannot change a game that is over
    """
    @action(detail=True, methods=['patch'])
    def open(self, request, pk=None):
        uuid = serializers.UUIDField().to_internal_value(data=pk)
        game = get_object_or_404(self.queryset, pk=uuid)
        if game.is_over():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = GameMarkSerializer(
            data=request.data,
            context={
                'rows': game.rows,
                'columns': game.columns
            }
        )
        if serializer.is_valid(raise_exception=True):
            x = serializer.validated_data['x']
            y = serializer.validated_data['y']
            game.mark_open(x, y)
            game.save()
        serializer = GameSerializer(game)
        return Response(serializer.data)

    """
    @api {patch} minesweeper/v1/games/:id/flag/ Flag a cell in the game
    @apiName FlagCell
    @apiGroup Game
    @apiVersion 1.0.0

    @apiParam {String} id Game's uuid.
    @apiParam {Number} x X Position of the desired cell to flag
    @apiParam {Number} x Y Position of the desired cell to flag

    @apiSuccess {String} id Game's id.
    @apiSuccess {Number} status Game's status.
    @apiSuccess {Array} board Game's board.
    @apiSuccess {Number} rows Game's amount of rows.
    @apiSuccess {Number} columns Game's amount of columns.
    @apiSuccess {Number} mines Game's amount of mines.
    @apiSuccess {Number} difficulty Game's difficulty.
    @apiSuccess {Number} seed Game's board seed.

    @apiError GameNotFound Game was not found.
    @apiError InvalidX X sent is not within the board's range
    @apiError InvalidY Y sent is not within the board's range
    @apiError GameOver You cannot change a game that is over
    """
    @action(detail=True, methods=['patch'])
    def flag(self, request, pk=None):
        uuid = serializers.UUIDField().to_internal_value(data=pk)
        game = get_object_or_404(self.queryset, pk=uuid)
        if game.is_over():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = GameMarkSerializer(
            data=request.data,
            context={
                'rows': game.rows,
                'columns': game.columns
            }
        )
        if serializer.is_valid(raise_exception=True):
            x = serializer.validated_data['x']
            y = serializer.validated_data['y']
            game.mark_flag(x, y)
            game.save()
        serializer = GameSerializer(game)
        return Response(serializer.data)

    """
    @api {patch} minesweeper/v1/games/:id/question/ Question a cell in the game
    @apiName QuestionCell
    @apiGroup Game
    @apiVersion 1.0.0

    @apiParam {String} id Game's uuid.
    @apiParam {Number} x X Position of the desired cell to question
    @apiParam {Number} x Y Position of the desired cell to question

    @apiSuccess {String} id Game's id.
    @apiSuccess {Number} status Game's status.
    @apiSuccess {Array} board Game's board.
    @apiSuccess {Number} rows Game's amount of rows.
    @apiSuccess {Number} columns Game's amount of columns.
    @apiSuccess {Number} mines Game's amount of mines.
    @apiSuccess {Number} difficulty Game's difficulty.
    @apiSuccess {Number} seed Game's board seed.

    @apiError GameNotFound Game was not found.
    @apiError InvalidX X sent is not within the board's range
    @apiError InvalidY Y sent is not within the board's range
    @apiError GameOver You cannot change a game that is over
    """
    @action(detail=True, methods=['patch'])
    def question(self, request, pk=None):
        uuid = serializers.UUIDField().to_internal_value(data=pk)
        game = get_object_or_404(self.queryset, pk=uuid)
        if game.is_over():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = GameMarkSerializer(
            data=request.data,
            context={
                'rows': game.rows,
                'columns': game.columns
            }
        )
        if serializer.is_valid(raise_exception=True):
            x = serializer.validated_data['x']
            y = serializer.validated_data['y']
            game.mark_question(x, y)
            game.save()
        serializer = GameSerializer(game)
        return Response(serializer.data)
