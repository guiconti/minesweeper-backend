import games.constants as constants

# TODO: Change to receive difficulty
def generate_board(rows, columns, mines):
  board = [[constants.EMPTY_SPACE for j in range(
    columns)] for i in range(rows)]
  return board