from unittest import TestCase
from Domino import Domino
from Exceptions import EmptyBoardException, FullBoardException, NoSuchDominoException, InvalidNumberException

class TestDomino(TestCase):
    def init_test(self):
        left = 4
        right = 2
        domino = Domino(left,right)
        self.assertEqual(4, domino.get_left())
        self.assertEqual(2, domino.get_left())
        # error - exception case
        left = 8
        right = 2
        self.assertRaises(InvalidNumberException, Domino,left, right)
        left = -8
        right = 2
        self.assertRaises(InvalidNumberException, Domino, left, right)
        left = 3
        right = 12
        self.assertRaises(InvalidNumberException, Domino, left, right)
        left = 3
        right = -12
        self.assertRaises(InvalidNumberException, Domino, left, right)

    def test_get_left(self):
        d1 = Domino(2, 3)
        self.assertEqual(d1.get_left(), 2)

    def test_get_right(self):
        d2 = Domino(2, 4)
        self.assertEqual(d2.get_right(), 4)

    def test_str(self):
        d3 = Domino(3, 4)
        self.assertEqual(d3.__str__(), f'[{3}|{4}]')

    def test_repr(self):
        d4 = Domino(4, 4)
        self.assertEqual(d4.__repr__(), f'[{4}|{4}]')

    def test_eq(self):
        # true - regular and flipped
        notdomino = 5
        identical1 = Domino(2, 4)
        identical2 = Domino(2, 4)
        identical3 = Domino(4, 2)
        notidentical1 = Domino(4,4)
        notidentical2 = 5
        self.assertEqual(identical1 == identical2, True)
        self.assertEqual(identical1 == identical3, True)
        # false - regular and flipped
        self.assertEqual(identical1 == notidentical1, False)
        self.assertEqual(identical1 == notidentical2, False)

    def test_ne(self):
        # true - regular and flipped
        identical1 = Domino(2, 4)
        identical2 = Domino(2, 4)
        identical3 = Domino(4, 2)
        notidentical1 = Domino(4, 4)
        notidentical2 = 5
        self.assertEqual(identical1 != identical2, False)
        self.assertEqual(identical1 != identical3, False)
        # false - regular and flipped
        self.assertEqual(identical1 != notidentical1, True)
        self.assertEqual(identical1 != notidentical2, True)

    def test_gt(self):
        d1 = Domino(2, 4)
        d2 = Domino(1, 1)
        notdomino = 5
        # different type
        self.assertEqual(d1.__gt__(notdomino), False)
        # true
        self.assertEqual(d1.__gt__(d2), True)
        # false
        self.assertEqual(d2.__gt__(d1), False)


    def test_contains(self):
        d1 = Domino(2, 4)
        #true
        self.assertEqual(d1.__contains__(2), True)
        #false
        self.assertEqual(d1.__contains__(5), False)

    def test_flip(self):
        d1 = Domino(2, 4)
        self.assertEqual(d1.flip(), Domino(4, 2))



