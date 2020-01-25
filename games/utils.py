import games.constants as constants
import random

# TODO: Change to receive difficulty
def generate_boards(rows, columns, mines, seed=None):
  random.seed(seed)

  real_board = [[constants.CELL_EMPTY for j in range(
    columns)] for i in range(rows)]
  player_board = [[constants.CELL_UNKNOWN for j in range(
    columns)] for i in range(rows)]
  
  while mines >= 0:
    x = random.randint(0, columns - 1)
    y = random.randint(0, rows - 1)
    if real_board[y][x] != constants.CELL_MINE:
      real_board[y][x] = constants.CELL_MINE
      mines -= 1

  return real_board, player_board

