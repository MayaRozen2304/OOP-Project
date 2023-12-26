from unittest import TestCase
from Board import Board
from Domino import Domino
from Exceptions import EmptyBoardException, FullBoardException, NoSuchDominoException, InvalidNumberException


class TestBoard(TestCase):
    def test_init(self):
        max_capacity = 20
        board = Board(max_capacity)
        self.assertEqual(20, board.max_capacity)
        # error - exception case
        max_capacity = -5
        self.assertRaises(InvalidNumberException, Board, max_capacity)

    def test_in_left(self):
        board1 = Board(20)
        board2 = Board(20)
        board1.add(Domino(2, 1))
        self.assertEqual(board1.in_left(), 2)
        # empty board - exception
        self.assertRaises(EmptyBoardException, board2.in_left)

    def test_in_right(self):
        board3 = Board(20)
        board4 = Board(20)
        board3.add(Domino(2, 1))
        self.assertEqual(board3.in_right(), 1)
        # empty board - exception
        self.assertRaises(EmptyBoardException, board4.in_right)

    def test_add(self):
        max_capacity = 1
        board = Board(max_capacity)
        board.add(Domino(2, 2))
        # error - exception case
        domino = Domino(2, 2)
        self.assertRaises(FullBoardException, board.add, domino, True)
        # empty board
        max_capacity = 10
        board2 = Board(max_capacity)
        self.assertEqual(board2.add(domino), True)
        # add to right
        d_to_right = Domino(2, 1)
        d_not_to_right = Domino(4, 4)
        d_flipped = Domino(2, 1)
        # add
        self.assertEqual(board2.add(d_to_right, True), True)
        # not add
        self.assertEqual(board2.add(d_not_to_right, True), False)
        # add flip
        self.assertEqual(board2.add(d_flipped, True), True)
        # add to left
        board3 = Board(max_capacity)
        d_to_left = Domino(4, 1)
        d_not_to_left = Domino(5, 5)
        d_flipped = Domino(4, 1)
        # add
        self.assertEqual(board3.add(d_to_left, False), True)
        # not add
        self.assertEqual(board3.add(d_not_to_left, False), False)
        # add flip
        self.assertEqual(board3.add(d_flipped, False), True)

    def test_right(self):
        empty_b = Board(15)
        d = Domino(3, 3)
        # adding to empty list to right
        self.assertEqual(empty_b.add_right(d), True)

    def test_left(self):
        empty_b = Board(15)
        d = Domino(3, 3)
        d2 = Domino(4, 3)
        # adding to empty list to left
        self.assertEqual(empty_b.add_left(d), True)
        self.assertEqual(empty_b.add_left(d2), True)

    def test_eq(self):
        b = Board(20)
        b2 = Board(13)
        notb = [1, 2, 3]
        # different types
        self.assertEqual(b == notb, False)
        # different max capacity
        self.assertEqual(b == b2, False)
        b.add(Domino(1, 2))
        # different dominoes
        self.assertEqual(b == b2, False)
        b3 = Board(13)
        # same board and max capacity
        self.assertEqual(b2 == b3, True)
        b2.add(Domino(1, 1))
        # different dominoes
        self.assertEqual(b2 == b3, False)
        b3.add(Domino(1, 1))
        self.assertEqual(b2 == b3, True)
        # same max capacity different domino
        b4 = Board(13)
        b4.add(Domino(1, 2))
        self.assertEqual(b2 == b4, False)

    def test_str(self):
        # print as domino
        b = Board(20)
        b.add(Domino(3, 3))
        self.assertEqual(b.__str__(), '[3|3]')
