# Game Status
STATUS_PLAYING = 0
STATUS_WON = 1
STATUS_LOST = 2
STATUS_CHOICES = (
    (STATUS_PLAYING, 'playing'),
    (STATUS_WON, 'won'),
    (STATUS_LOST, 'lost'),
)

# Game Difficulties
DIFFICULTY_EASY = 0
DIFFICULTY_INTERMEDIATE = 1
DIFFICULTY_HARD = 2
DIFFICULTY_CHOICES = (
    (DIFFICULTY_EASY, 'easy'),
    (DIFFICULTY_INTERMEDIATE, 'intermediate'),
    (DIFFICULTY_HARD, 'hard'),
)

# Game cell options
CELL_EMPTY = '.'
CELL_UNKNOWN = '*'
CELL_MINE = 'M'
CELL_FLAG = 'F'
CELL_QUESTION = '?'
VALID_CELLS_TO_OPEN = (CELL_UNKNOWN, CELL_FLAG, CELL_QUESTION)
CELL_ADJACENT_DIRECTIONS = [(-1, -1), (0, -1), (1, -1), (1, 0),
                            (1, 1), (0, 1), (-1, 1), (-1, 0)]
