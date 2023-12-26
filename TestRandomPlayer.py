from unittest import TestCase

from Board import Board
from Domino import Domino
from Hand import Hand
from RandomPlayer import RandomPlayer


class TestRandomPlayer(TestCase):
    def test_play(self):
        board = Board(20)
        board.add(Domino(2, 4))
        # fit to right only
        hand1 = Hand([Domino(4, 5), Domino(3, 1)])
        maya = RandomPlayer('maya',23,hand1)
        self.assertEqual(maya.play(board), True)
        # fit to left only
        hand1 = Hand([Domino(1, 2), Domino(3, 3)])
        maya = RandomPlayer('maya',23,hand1)
        self.assertEqual(maya.play(board), True)
        # not fit at all - returns false
        hand1 = Hand([Domino(6, 6)])
        maya = RandomPlayer('maya', 23, hand1)
        self.assertEqual(maya.play(board), False)