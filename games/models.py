import uuid
import json
import random
import queue
from django.db import models
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
        if not self.real_board:
            self.rows, self.columns, self.mines = constants.GAME_PARAMETERS[self.difficulty]
            self._generate_boards()
        super(Game, self).save(*args, **kwargs)

    def _generate_boards(self):
        random.seed(self.seed)

        real_board = [[constants.CELL_EMPTY for j in range(
            self.columns)] for i in range(self.rows)]
        player_board = [[constants.CELL_UNKNOWN for j in range(
            self.columns)] for i in range(self.rows)]
        mines_count = self.mines

        while mines_count >= 0:
            x = random.randint(0, self.columns - 1)
            y = random.randint(0, self.rows - 1)
            if real_board[y][x] != constants.CELL_MINE:
                real_board[y][x] = constants.CELL_MINE
                mines_count -= 1

        self.real_board = json.dumps(real_board)
        self.player_board = json.dumps(player_board)

    def is_over(self):
        return self.status == constants.STATUS_LOST or self.status == constants.STATUS_WON

    def mark_open(self, x, y):
        player_board = json.loads(self.player_board)
        if player_board[y][x] not in constants.VALID_CELLS_TO_OPEN:
            return
        real_board = json.loads(self.real_board)
        if real_board[y][x] == constants.CELL_MINE:
            return self._lost_game()
        self._expand_blank_cells(x, y)
        if self._is_finished():
            self._won_game()

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

    def _expand_blank_cells(self, x, y):
        real_board = json.loads(self.real_board)
        player_board = json.loads(self.player_board)
        remaining_cells_queue = queue.Queue(maxsize=0)
        remaining_cells_queue.put((x, y))

        # Depth first search
        while not remaining_cells_queue.empty():
            x, y = remaining_cells_queue.get()
            real_board[y][x] = 0

            for direction_x, direction_y in constants.CELL_ADJACENT_DIRECTIONS:
                current_y = y + direction_y
                current_x = x + direction_x
                valid_y = current_y >= 0 and current_y < self.rows
                valid_x = current_x >= 0 and current_x < self.columns
                if valid_y and valid_x and real_board[current_y][current_x] == constants.CELL_MINE:
                    real_board[y][x] += 1

            real_board[y][x] = str(real_board[y][x])
            player_board[y][x] = real_board[y][x]
            
            if real_board[y][x] == '0':
                player_board[y][x] = constants.CELL_EMPTY
                for direction_x, direction_y in constants.CELL_ADJACENT_DIRECTIONS:
                    current_y = y + direction_y
                    current_x = x + direction_x
                    valid_y = current_y >= 0 and current_y < self.rows
                    valid_x = current_x >= 0 and current_x < self.columns
                    if valid_y and valid_x and real_board[current_y][current_x] == constants.CELL_EMPTY:
                        remaining_cells_queue.put((current_x, current_y))

        self.real_board = json.dumps(real_board)
        self.player_board = json.dumps(player_board)

    def _is_finished(self):
        real_board = json.loads(self.real_board)
        player_board = json.loads(self.player_board)
        for y in range(self.rows):
            for x in range(self.columns):
                if real_board[y][x] == constants.CELL_EMPTY:
                    return False
                if real_board[y][x] == constants.CELL_MINE and player_board[y][x] != constants.CELL_FLAG:
                    return False
        return True

    def _won_game(self):
        self.status = constants.STATUS_WON

    def _lost_game(self):
        self.status = constants.STATUS_LOST
        real_board = json.loads(self.real_board)
        player_board = json.loads(self.player_board)
        for y in range(self.rows):
            for x in range(self.columns):
                if real_board[y][x] == constants.CELL_MINE:
                    player_board[y][x] = constants.CELL_MINE
        self.real_board = json.dumps(real_board)
        self.player_board = json.dumps(player_board)
