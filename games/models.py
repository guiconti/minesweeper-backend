import uuid
import json
from django.db import models
from games.utils import generate_boards
import games.constants as constants

app_name = 'games'

class Game(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  created = models.DateTimeField(auto_now_add=True)
  status = models.IntegerField(
    choices=constants.STATUS_CHOICES, default=constants.STATUS_PLAYING)
  real_board = models.TextField(blank=True, default='')
  player_board = models.TextField(blank=True, default='')
  rows = models.IntegerField(default=9)
  columns = models.IntegerField(default=9)
  mines = models.IntegerField(default=10)
  difficulty = models.IntegerField(
    choices=constants.DIFFICULTY_CHOICES, default=constants.DIFFICULTY_EASY)
  duration = models.IntegerField(default=0)
  score = models.IntegerField(default=0)
  seed = models.IntegerField(null=True)

  class Meta:
    ordering = ['created']

  def __str__(self):
    return self.player_board

  def save(self, *args, **kwargs):
    if not self.pk:
      real_board, player_board = generate_boards(self.rows, self.columns, self.mines, self.seed)
      self.real_board = json.dumps(real_board)
      self.player_board = json.dumps(player_board)
    super(Game, self).save(*args, **kwargs)

  def mark_flag(self, x, y):
    board = json.loads(self.player_board)
    if board[y][x] == constants.CELL_UNKNOWN or board[y][x] == constants.CELL_QUESTION:
      board[y][x] = constants.CELL_FLAG
    elif board[y][x] == constants.CELL_FLAG:
      board[y][x] = constants.CELL_UNKNOWN
    self.player_board = json.dumps(board)

  def mark_question(self, x, y):
    board = json.loads(self.player_board)
    if board[y][x] == constants.CELL_UNKNOWN or board[y][x] == constants.CELL_FLAG:
      board[y][x] = constants.CELL_QUESTION
    elif board[y][x] == constants.CELL_QUESTION:
      board[y][x] = constants.CELL_UNKNOWN
    self.player_board = json.dumps(board)