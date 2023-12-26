from unittest import TestCase
from Board import Board
from Domino import Domino
from Hand import Hand
from MaxScorePlayer import MaxScorePlayer


class TestMaxScorePlayer(TestCase):
    def test_play(self):
        board = Board(20)
        board.add(Domino(1, 2))
        a = Hand([Domino(1, 3), Domino(2, 6)])
        maya = MaxScorePlayer('Maya', 22, a)
        # right side - true
        self.assertEqual(maya.play(board), True)
        # left side - true
        self.assertEqual(maya.play(board), True)
        # empty hand - returns false, no options to add
        self.assertEqual(maya.play(board), False)
        # no option for the player to add - returns false
        board = Board(20)
        board.add(Domino(1, 2))
        a = Hand([Domino(3, 3), Domino(6, 6)])
        maya = MaxScorePlayer('Maya', 22, a)
        self.assertEqual(maya.play(board), False)
        #full board - false
        board = Board(2)
        board.add(Domino(1, 2))
        board.add(Domino(1, 2))
        a = Hand([Domino(1, 1), Domino(2, 1)])
        maya = MaxScorePlayer('Maya', 22, a)
        self.assertEqual(maya.play(board), False)

    def test_str_max_player(self):
        a = Hand([])
        maya = MaxScorePlayer('Maya', 22, a)
        self.assertEqual(maya.__str__(), 'Name: Maya, Age: 22, Hand: [], Score: 0, I can win the game!')
