import json
from django.test import TestCase
from games.models import Game
import games.constants as constants

class GamesModelsTestCase(TestCase):
    def test_game_created_with_no_params_should_have_all_params(self):
        game = Game.objects.create()
        self.assertIsNotNone(game.created)
        self.assertIsNotNone(game.status)
        self.assertIsNotNone(game.real_board)
        self.assertIsNotNone(game.player_board)
        self.assertIsNotNone(game.rows)
        self.assertIsNotNone(game.columns)
        self.assertIsNotNone(game.difficulty)
        self.assertIsNone(game.seed)

    def test_game_will_only_have_mines_after_first_opening(self):
        game = Game.objects.create()
        self.assertNotIn(constants.CELL_MINE, game.real_board)
        game.mark_open(0, 0)
        self.assertIn(constants.CELL_MINE, game.real_board)

    def test_game_will_have_open_cells_only_after_opening(self):
        game = Game.objects.create()
        # Seeding for no flake test
        game.seed = 1
        self.assertNotIn(constants.CELL_EMPTY, game.player_board)
        game.mark_open(0, 0)
        self.assertIn(constants.CELL_EMPTY, game.player_board)

    def test_game_will_only_have_flags_after_first_flagging(self):
        game = Game.objects.create()
        self.assertNotIn(constants.CELL_FLAG, game.player_board)
        game.mark_flag(0, 0)
        self.assertIn(constants.CELL_FLAG, game.player_board)

    def test_game_will_only_have_questoion_after_first_flagging(self):
        game = Game.objects.create()
        self.assertNotIn(constants.CELL_QUESTION, game.player_board)
        game.mark_question(0, 0)
        self.assertIn(constants.CELL_QUESTION, game.player_board)

    def test_game_status_changes_to_lost_when_opening_a_mine(self):
        game = Game.objects.create()
        # Seeding for no flake test
        game.seed = 1
        self.assertNotEqual(game.status, constants.STATUS_LOST)
        game.mark_open(0, 0)
        real_board = json.loads(game.real_board)
        mine_x = mine_y = 0
        for y in range(len(real_board)):
            found = False
            for x in range(len(real_board[y])):
                if real_board[y][x] == constants.CELL_MINE:
                    mine_y = y
                    mine_x = x
                    found = True
                    break
            if found:
                break
        game.mark_open(mine_x, mine_y)
        self.assertEqual(game.status, constants.STATUS_LOST)

    def test_game_status_changes_to_won_when_all_cells_are_open_and_mines_flagged(self):
        game = Game.objects.create()
        # Seeding for no flake test
        game.seed = 1
        self.assertNotEqual(game.status, constants.STATUS_WON)
        game.mark_open(0, 0)
        real_board = json.loads(game.real_board)
        for y in range(len(real_board)):
            for x in range(len(real_board[y])):
                if real_board[y][x] == constants.CELL_MINE:
                    game.mark_flag(x, y)
                else:
                    game.mark_open(x, y)
        self.assertEqual(game.status, constants.STATUS_WON)
