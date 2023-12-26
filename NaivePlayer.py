from Player import Player


class NaivePlayer(Player):
    def __init__(self, name, age, hand):
        """
defining the fields of the NaivePlayer class.
        :param name: string - the player name
        :param age: int- the player age
        :param hand: Hand type - list with dominoes (Dominoes)
        """
        Player.__init__(self, name, age, hand)

    # def score is identical tpo player - no need to define again
    # def has_dominoes is identical tpo player - no need to define again

    def play(self, board):
        """
the method is checks if an Naive Player can play on a board with his given hand dominoes.
at first it checks the right side and returns if it possible for this player to add a card to this side, than it checks
the left side by the games rules and checks if a valid action can be done. if there is no such domino that fits, returns
False.
        :param board: the board[Board] that the player plays by.
        :return: boolean value if the player did play or cant play.
        """
        if len(board) == 0:
            board.add(self.hand[0])
            self.hand.remove_domino(self.hand[0])
            return True
        for index in range(len(self.hand)):
            # adding the first possible domino to the board and break
            # checking possibility to the right side of the board first:
            if board.add_right(self.hand[index]):
                # removed from player's hand:
                self.hand.remove_domino(self.hand[index])
                return True
            # checking possibility to the left side of the board:
            if board.add_left(self.hand[index]):
                # removed from player's hand:
                self.hand.remove_domino(self.hand[index])
                return True
        return False


    # def __str__ is identical to player - no need to define again
    # def __repr__ is identical to player - no need to define again

