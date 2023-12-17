import unittest
from unittest.mock import patch, mock_open, call
from facade import GameFacade, Level

class MockLevel:
    def __init__(self, filename):
        self.filename = filename

class TestGameFacade(unittest.TestCase):
    def setUp(self):
        self.game = GameFacade()

    @patch('builtins.open', new_callable=mock_open, read_data="player1,100,level1\nplayer2,200,level2\n")
    def test_load_high_scores(self, mock_file):
        self.game.load_high_scores("any_file_path")
        self.assertEqual(self.game.get_high_scores(), [('player1', 100, 'level1'), ('player2', 200, 'level2')])

    @patch('builtins.open', new_callable=mock_open)
    def test_save_high_scores(self, mock_file):
        self.game.level = MockLevel('test_level.txt')
        self.game.save_high_score('test_player', 150)
        mock_file.assert_called_once_with('high_scores.txt', 'w', encoding='utf-8')
        mock_file().write.assert_called_once_with('test_player,150, test_level\n')

if __name__ == '__main__':
    unittest.main()