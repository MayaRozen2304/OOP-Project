from unittest import TestCase

from Board import Board
from Domino import Domino
from Hand import Hand
from MaxScorePlayer import MaxScorePlayer
from NaivePlayer import NaivePlayer
from RandomPlayer import RandomPlayer
from Team import Team


class TestTeam(TestCase):
    def test_get_team(self):
        hand1 = Hand([])
        hand2 = Hand([Domino(4, 4)])
        nitsan = RandomPlayer('nitsan', 23, hand1)
        maya = NaivePlayer('Maya', 22, hand2)
        myteam = Team('mn', [maya, nitsan])
        self.assertEqual(myteam.get_team(), [maya, nitsan])


    def test_has_dominoes_team(self):
        hand1 = Hand([])
        hand2 = Hand([Domino(4, 4)])
        nitsan = RandomPlayer('nitsan', 23, hand1)
        maya = NaivePlayer('Maya', 22, hand2)
        myteam = Team('mn', [maya, nitsan])
        self.assertEqual(myteam.has_dominoes_team(), True)
        # false - no domino
        hand1 = Hand([])
        hand2 = Hand([])
        noa = NaivePlayer('noa', 22, hand2)
        shahar = NaivePlayer('shahar', 22, hand1)
        myteam = Team('mn', [noa, shahar])
        self.assertEqual(myteam.has_dominoes_team(), False)

    #
    def test_score_team(self):
        hand1 = Hand([])
        hand2 = Hand([Domino(4, 4)])
        nitsan = RandomPlayer('nitsan', 23, hand1)
        maya = NaivePlayer('Maya', 22, hand2)
        myteam = Team('mn', [maya, nitsan])
        self.assertEqual(myteam.score_team(), 8)
        hand1 = Hand([Domino(4, 4),Domino(2, 3)])
        hand2 = Hand([Domino(4, 4)])
        nitsan = RandomPlayer('nitsan', 23, hand1)
        maya = NaivePlayer('Maya', 22, hand2)
        myteam = Team('mn', [maya, nitsan])
        self.assertEqual(myteam.score_team(), 21)
        #epmpty lists score 0:
        hand1 = Hand([])
        hand2 = Hand([])
        nitsan = RandomPlayer('nitsan', 23, hand1)
        maya = NaivePlayer('Maya', 22, hand2)
        myteam = Team('mn', [maya, nitsan])
        self.assertEqual(myteam.score_team(), 0)


    def test_team_str_repr(self):
        board = Board(20)
        board.add(Domino(1, 2))
        b = Hand([Domino(2, 3)])
        a = Hand([Domino(4, 4)])
        maya = NaivePlayer('Maya', 22, a)
        nitsan = RandomPlayer('nitsan', 23, b)
        team = Team('mn', [maya, nitsan])
        self.assertEqual(team.__str__(), 'Name mn, Score team: 13, Players: Name: Maya, Age: 22, Hand: [4|4], Score: 8 Name: nitsan, Age: 23, Hand: [2|3], Score: 5')
        self.assertEqual(team.__repr__(), 'Name mn, Score team: 13, Players: Name: Maya, Age: 22, Hand: [4|4], Score: 8 Name: nitsan, Age: 23, Hand: [2|3], Score: 5')

    def test_play(self):
        board = Board(20)
        board.add(Domino(1, 2))
        b = Hand([Domino(3, 3)])
        a = Hand([Domino(4, 4),Domino(6, 2)])
        maya = MaxScorePlayer('Maya', 22, a)
        nitsan = RandomPlayer('nitsan', 23, b)
        team = Team('mn', [maya, nitsan])
        self.assertEqual(team.play(board), True)
        self.assertEqual(team.play(board), False)

