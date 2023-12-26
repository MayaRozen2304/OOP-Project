from unittest import TestCase

from Board import Board
from Domino import Domino
from Hand import Hand
from NaivePlayer import NaivePlayer


class TestNaivePlayer(TestCase):
    def test_play_naive(self):
        board = Board(20)
        d1 = Domino(4, 3)
        d2 = Domino(3, 3)
        d3 = Domino(5,4)
        h1 = Hand([d1, d2, d3])
        noa = NaivePlayer('noa', 23, h1)
        #adding to right side
        self.assertEqual(noa.play(board), True)
        self.assertEqual(noa.play(board), True)
        #cant add at all- false
        h1 = Hand([Domino(5,5)])
        maya = NaivePlayer('maya', 23, h1)
        board2 = Board(20)
        board2.add(d1)
        self.assertEqual(maya.play(board2), False)
        #can only add to left side
        board3 = Board(20)
        board3.add(d1)
        h1 = Hand([Domino(5,5),Domino(5,4)])
        maya = NaivePlayer('maya', 23, h1)
        self.assertEqual(maya.play(board3), True)


