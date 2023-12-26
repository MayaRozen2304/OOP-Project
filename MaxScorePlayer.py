import copy

from Player import Player


class MaxScorePlayer(Player):
    def __init__(self, name, age, hand):
        """
defining the fields of the MaxScorePlayer class.
        :param name: string - the player name
        :param age: int- the player age
        :param hand: Hand type - list with dominoes (Dominoes)
        """
        Player.__init__(self, name, age, hand)

    # def score is identical to player - no need to define again
    # def has_dominoes is identical to player - no need to define again

    def play(self, board):
        """
this play method of the Maxscoreplayer calling the help function of highest_index and finds the domino with the highest value
of left and right. then, it checks if it can be added to the right side, if it is the method remove this domino from
the copied&original hand. then, it checks if the domino can be added to the left side, and does the same action.
if not fits both, it is removed only from the copied one in order to not check it again and finds the next highest domino.
        :param board: the board[Board] that the player plays by.
        :return: boolean value if the player did play or cant play.
        """
        if len(self.hand) == 0:
            return False
        # copied to the hand
        new = copy.deepcopy(self.hand)
        # finding the index with the highest sum
        index_to_add = self.find_highest(new)
        for item in range(len(new)):
            # checking if fits the board, right side
            if board.add_right(new[index_to_add]):
                # removing from hand & copied hand
                self.hand.remove_domino(new[index_to_add])
                new.remove_domino(new[index_to_add])
                return True
                # checking left side
            if board.add_left(new[index_to_add]):
                # removing from hand & copied hand
                self.hand.remove_domino(new[index_to_add])
                new.remove_domino(new[index_to_add])
                return True
            # not fits to both right and left side do removed from copied hand
            # find the next high index
            new.remove_domino(new[index_to_add])
            index_to_add = self.find_highest(new)
            # if the new is empty, no domino fits to the board, returns false
            if len(new) == 0:
                return False

    def find_highest(self, new):
        """
the methos finds the index of the domino in the hand which its sum of left+right is the highest.
        :param new: copied hand [Hand]
        :return: the index of the domino in the hand which its sum of left+right is the highest.
        """
        sum = 0
        max_index = 0
        # for each domino in hand by index
        # finding the highest sum and index  for domino object in board
        for index in range(len(new)):
            temp = new[index].get_left() + new[index].get_right()
            if temp > sum:
                sum = temp
                max_index = index
        return max_index

    def __str__(self):
        """
the method create the str method for a MaxScorePlayer by combining all fields and adds them to an empty string with additional string.
        :return: a string with all the player details - return value of the str method.
        """
        player = ''
        player += 'Name: ' + self.name + ', Age: ' + str(self.age) + ', Hand: ' + str(self.hand) + ', Score: ' + str(self.score()) + ', I can win the game!'
        return player

    # def repr is identical to player - no need to define again

