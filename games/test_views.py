import json
from django.test import TestCase
from rest_framework.test import RequestsClient
from games.models import Game
import games.constants as constants


class GamesViewsTestCase(TestCase):
    client = RequestsClient()

    def test_sending_a_post_on_games_should_return_a_created_game(self):
        body = json.dumps({
            'difficulty': 0
        })
        response = self.client.post(
            '/minesweeper/v1/games/', data=body, format='json', content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual('id' in data, True)
        self.assertEqual('status' in data, True)
        self.assertEqual('board' in data, True)
        self.assertEqual('rows' in data, True)
        self.assertEqual('columns' in data, True)
        self.assertEqual('mines' in data, True)
        self.assertEqual('difficulty' in data, True)
        self.assertEqual('seed' in data, True)

    def test_retrieved_game_board_after_creation_should_only_includes_maked_data(self):
        body = json.dumps({
            'difficulty': 0
        })
        response = self.client.post(
            '/minesweeper/v1/games/', data=body, format='json', content_type='application/json'
        )
        data = json.loads(response.content)
        error = False
        for row in data['board']:
            for cell in row:
                if cell != constants.CELL_UNKNOWN:
                    error = True
                    break
        self.assertEqual(error, False)

    def test_retrieved_game_details_should_return_success_with_game_fields(self):
        body = json.dumps({
            'difficulty': 0
        })
        response = self.client.post(
            '/minesweeper/v1/games/', data=body, format='json', content_type='application/json'
        )
        data = json.loads(response.content)
        response = self.client.get('/minesweeper/v1/games/' + data['id'] + '/')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('id' in data, True)
        self.assertEqual('status' in data, True)
        self.assertEqual('board' in data, True)
        self.assertEqual('rows' in data, True)
        self.assertEqual('columns' in data, True)
        self.assertEqual('mines' in data, True)
        self.assertEqual('difficulty' in data, True)
        self.assertEqual('seed' in data, True)

    def test_fetching_invalid_pk_uuid_returns_bad_request(self):
        response = self.client.get('/minesweeper/v1/games/test/')
        self.assertEqual(response.status_code, 400)

    def test_retrieved_game_board_should_only_includes_masked_data(self):
        body = json.dumps({
            'difficulty': 0
        })
        response = self.client.post(
            '/minesweeper/v1/games/', data=body, format='json', content_type='application/json'
        )
        data = json.loads(response.content)
        response = self.client.get('/minesweeper/v1/games/' + data['id'] + '/')
        data = json.loads(response.content)
        error = False
        for row in data['board']:
            for cell in row:
                if cell != constants.CELL_UNKNOWN:
                    error = True
                    break
        self.assertEqual(error, False)

    def test_opening_a_cell_should_reveal_on_board(self):
        # Seeding for no flake test
        body = json.dumps({
            'difficulty': 0,
            'seed': 1
        })
        response = self.client.post(
            '/minesweeper/v1/games/', data=body, format='json', content_type='application/json'
        )
        data = json.loads(response.content)
        body = json.dumps({
            'x': 0,
            'y': 0
        })
        response = self.client.patch(
            '/minesweeper/v1/games/' + data['id'] + '/open/', data=body, format='json', content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        found_empty_cell = False
        for row in data['board']:
            for cell in row:
                if cell == constants.CELL_EMPTY:
                    found_empty_cell = True
                    break
        self.assertEqual(found_empty_cell, True)

    def test_opening_a_cell_next_to_a_mine_should_reveal_a_number_on_board(self):
        # Seeding for no flake test
        body = json.dumps({
            'difficulty': 0,
            'seed': 0
        })
        response = self.client.post(
            '/minesweeper/v1/games/', data=body, format='json', content_type='application/json'
        )
        data = json.loads(response.content)
        body = json.dumps({
            'x': 0,
            'y': 0
        })
        response = self.client.patch(
            '/minesweeper/v1/games/' + data['id'] + '/open/', data=body, format='json', content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        found_number_cell = False
        for row in data['board']:
            for cell in row:
                if cell == '1':
                    found_number_cell = True
                    break
        self.assertEqual(found_number_cell, True)

    def test_flagging_a_cell_should_reveal_on_board(self):
        body = json.dumps({
            'difficulty': 0
        })
        response = self.client.post(
            '/minesweeper/v1/games/', data=body, format='json', content_type='application/json'
        )
        data = json.loads(response.content)
        body = json.dumps({
            'x': 0,
            'y': 0
        })
        response = self.client.patch(
            '/minesweeper/v1/games/' + data['id'] + '/flag/', data=body, format='json', content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        body = json.loads(body)
        self.assertEqual(data['board'][body['y']][body['x']], constants.CELL_FLAG)

    def test_questioning_a_cell_should_reveal_on_board(self):
        body = json.dumps({
            'difficulty': 0
        })
        response = self.client.post(
            '/minesweeper/v1/games/', data=body, format='json', content_type='application/json'
        )
        data = json.loads(response.content)
        body = json.dumps({
            'x': 0,
            'y': 0
        })
        response = self.client.patch(
            '/minesweeper/v1/games/' + data['id'] + '/question/', data=body, format='json', content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        body = json.loads(body)
        self.assertEqual(data['board'][body['y']][body['x']], constants.CELL_QUESTION)

    def test_opening_a_cell_with_missing_parameters_should_give_bad_request(self):
        body = json.dumps({
            'difficulty': 0
        })
        response = self.client.post(
            '/minesweeper/v1/games/', data=body, format='json', content_type='application/json'
        )
        data = json.loads(response.content)
        body = json.dumps({
            'y': 0
        })
        response = self.client.patch(
            '/minesweeper/v1/games/' + data['id'] + '/question/', data=body, format='json', content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
    
    def test_opening_a_cell_with_invalid_parameters_should_give_bad_request(self):
        body = json.dumps({
            'difficulty': 0
        })
        response = self.client.post(
            '/minesweeper/v1/games/', data=body, format='json', content_type='application/json'
        )
        data = json.loads(response.content)
        body = json.dumps({
            'x': -1,
            'y': 0
        })
        response = self.client.patch(
            '/minesweeper/v1/games/' + data['id'] + '/question/', data=body, format='json', content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)