import uuid
import json
from django.db import models
from games.utils import generate_board
import games.constants as constants

app_name = 'games'

class Game(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  created = models.DateTimeField(auto_now_add=True)
  status = models.IntegerField(
    choices=constants.STATUS_CHOICES, default=constants.STATUS_PLAYING)
  board = models.TextField(blank=True, default='')
  rows = models.IntegerField(default=9)
  columns = models.IntegerField(default=9)
  mines = models.IntegerField(default=10)
  difficulty = models.IntegerField(
    choices=constants.DIFFICULTY_CHOICES, default=constants.DIFFICULTY_EASY)
  duration = models.IntegerField(default=0)
  score = models.IntegerField(default=0)

  class Meta:
    ordering = ['created']

  def __str__(self):
    return self.board

  def save(self, *args, **kwargs):
    new_board = generate_board(self.rows, self.columns, self.mines)
    self.board = json.dumps(new_board)
    super(Game, self).save(*args, **kwargs)
