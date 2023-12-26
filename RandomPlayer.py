import copy
import random
from Player import Player


class RandomPlayer(Player):

    def __init__(self, name, age, hand):
        """
defining the fields of the RandomPlayer class.
        :param name: string - the player name
        :param age: int- the player age
        :param hand: Hand type - list with dominoes (Dominoes)
        """
        Player.__init__(self, name, age, hand)

    def play(self, board):
        """
this play method of the Random player does a shuffle on a copy hand and checks possibility to add each domino in the shuffled
hand to the board(first to the right,than left). if it can be added, the method remove this domino from the copied&original
hand , and if not it is removed only from the copied one in order to not check it again.
        :param board:  the board[Board] that the player plays by.
        :return:  boolean value if the player did play or cant play.
        """
        # Don't change this line and don't move it!
        random.seed(12)  # You can read about seed here: https://en.wikipedia.org/wiki/Random_seed
        # TODO: write your code after this line
        # getting an iterable copied object in order to not change the hand
        copied_hand = copy.deepcopy(self.hand.array)
        # shuffle the copied list
        random.shuffle(copied_hand)
        for domino_ind in range(len(copied_hand)):
            # if true- removing from original hand, right side-
            if board.add_right(copied_hand[domino_ind]):
                self.hand.remove_domino(copied_hand[domino_ind])
                return True
            # if true- removing from original hand, left side-
            if board.add_left(copied_hand[domino_ind]):
                self.hand.remove_domino(copied_hand[domino_ind])
                return True
        return False

    # def score is identical tpo player - no need to define again
    # def has_dominoes is identical tpo player - no need to define again
    # def __str__ is identical to player - no need to define again
    # def __repr__ is identical to player - no need to define again
