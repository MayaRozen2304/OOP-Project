from unittest import TestCase
from Board import Board
from Domino import Domino
from Game import Game
from Hand import Hand
from NaivePlayer import NaivePlayer
from Team import Team


class TestGame(TestCase):
    def test_play(self):
        # team 1 plays first
        board1 = Board(20)
        board1.add(Domino(1, 2))
        a = Hand([Domino(4, 4), Domino(3,3)])
        b = Hand([Domino(5, 4), Domino(2,4)])
        c = Hand([Domino(2, 4)])
        shahar = NaivePlayer('shahar', 22, c)
        maya = NaivePlayer('Maya', 22, a)
        nitsan = NaivePlayer('nitsan', 23, b)
        team1 = Team('mn', [maya, nitsan])
        team2 = Team('s', [shahar])
        game = Game(board1, team1, team2)
        self.assertEqual(game.play(), 'Team s wins Team mn')


        # team 2 plays first
        board1 = Board(10)
        board1.add(Domino(4, 4))
        a = Hand([Domino(5, 5)])
        b = Hand([Domino(2, 1)])
        c = Hand([Domino(4, 5), Domino(5, 5)])
        shahar = NaivePlayer('shahar', 22, c)
        maya = NaivePlayer('Maya', 22, a)
        nitsan = NaivePlayer('nitsan', 23, b)
        team1 = Team('mn', [maya, nitsan])
        team2 = Team('s', [shahar])
        game = Game(board1, team1, team2)
        self.assertEqual(game.play(), 'Team s wins Team mn')


        # one team has no dominoes
        board1 = Board(20)
        board1.add(Domino(1, 2))
        a = Hand([Domino(2,1)])
        b = Hand([])
        c = Hand([Domino(4, 4)])
        shahar = NaivePlayer('shahar', 22, c)
        maya = NaivePlayer('Maya', 22, a)
        nitsan = NaivePlayer('nitsan', 23, b)
        team1 = Team('mn', [maya, nitsan])
        team2 = Team('s', [shahar])
        game = Game(board1, team1, team2)
        self.assertEqual(game.play(), 'Team mn wins Team s')

        # draw - same score & max capacity
        board1 = Board(1)
        a = Hand([Domino(2, 1)])
        b = Hand([Domino(2, 1), Domino(4, 5)])
        c = Hand([Domino(4, 5), Domino(2, 1)])
        shahar = NaivePlayer('shahar', 22, c)
        maya = NaivePlayer('Maya', 22, a)
        nitsan = NaivePlayer('nitsan', 23, b)
        team1 = Team('mn', [maya, nitsan])
        team2 = Team('s', [shahar])
        game = Game(board1, team1, team2)
        self.assertEqual(game.play(), 'Draw!')

        board1 = Board(3)
        a = Hand([Domino(2, 1),Domino(2,2)])
        b = Hand([])
        c = Hand([Domino(2, 1), Domino(2, 2), Domino(5, 5),Domino(4, 5)])
        shahar = NaivePlayer('shahar', 22, c)
        maya = NaivePlayer('Maya', 22, a)
        nitsan = NaivePlayer('nitsan', 23, b)
        team1 = Team('mn', [maya, nitsan])
        team2 = Team('s', [shahar])
        game = Game(board1, team1, team2)
        self.assertEqual(game.play(), 'Team mn wins Team s')

        board1 = Board(6)
        a = Hand([Domino(2, 1),Domino(2,2),Domino(2,3),Domino(1,1)])
        c = Hand([Domino(2, 1), Domino(2, 2), Domino(5, 5),Domino(2, 2),Domino(3,3)])
        shahar = NaivePlayer('shahar', 22, c)
        maya = NaivePlayer('Maya', 22, a)
        team1 = Team('m', [maya])
        team2 = Team('s', [shahar])
        game = Game(board1, team1, team2)
        self.assertEqual(game.play(), 'Team m wins Team s')
