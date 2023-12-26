from unittest import TestCase

from Domino import Domino
from Hand import Hand
from MaxScorePlayer import MaxScorePlayer
from NaivePlayer import NaivePlayer


class TestPlayer(TestCase):
    def test_score(self):
        d1 = Domino(4, 3)
        d2 = Domino(3, 3)
        h1 = Hand([d1, d2])
        maya = NaivePlayer('maya', 23, h1)
        self.assertEqual(maya.score(), 13)

    def test_has_dominoes(self):
        d1 = Domino(4, 3)
        d2 = Domino(3, 3)
        h1 = Hand([d1, d2])
        maya = NaivePlayer('maya', 23, h1)
        # has dominoes , len > 0 , true
        self.assertEqual(maya.has_dominoes(), True)
        h1 = Hand([])
        maya = NaivePlayer('maya', 23, h1)
        self.assertEqual(maya.has_dominoes(), False)

    def test_str(self):
        d1 = Domino(4, 3)
        d2 = Domino(3, 3)
        h1 = Hand([d1, d2])
        maya = NaivePlayer('maya', 23, h1)
        self.assertEqual(maya.__str__(), 'Name: maya, Age: 23, Hand: ' + f'[{4}|{3}][{3}|{3}]' + ', ' + 'Score: 13')

    def test_repr(self):
        d1 = Domino(4, 3)
        d2 = Domino(3, 3)
        h1 = Hand([d1, d2])
        maya = NaivePlayer('maya', 23, h1)
        self.assertEqual(maya.__repr__(), 'Name: maya, Age: 23, Hand: ' + f'[{4}|{3}][{3}|{3}]' + ', ' + 'Score: 13')

    # play absract method in player class
