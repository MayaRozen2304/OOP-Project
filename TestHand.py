from unittest import TestCase
from Domino import Domino
from Exceptions import NoSuchDominoException
from Hand import Hand


class TestHand(TestCase):
    def test_init(self):
        # check input
        d1 = Domino(4, 3)
        d2 = Domino(3, 3)
        hand = Hand([d1, d2])
        self.assertEqual([d1, d2], hand.array)

    def test_add(self):
        empty_hand = Hand([])
        d1 = Domino(4, 3)
        # adding none index
        self.assertEqual(empty_hand.add(d1), [d1])
        d2 = Domino(4, 5)
        # adding specific index
        self.assertEqual(empty_hand.add(d2, 1), [d1, d2])

    def test_remove(self):
        empty_hand = Hand([Domino(4, 3)])
        d2 = Domino(4, 5)
        # exception
        self.assertRaises(NoSuchDominoException, empty_hand.remove_domino, d2)
        # removing and returning index
        self.assertEqual(empty_hand.remove_domino(Domino(4, 3)), 0, 0)

