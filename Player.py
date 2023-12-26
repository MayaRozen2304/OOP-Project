from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, age, hand):
        """
defining the fields of the player class.
        :param name: string - the player name
        :param age: int- the player age
        :param hand: Hand type - list with dominoes (Dominoes)
        """
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):
        """
the method calculates the score of the player by the sum of each domino values in the player's hand.
        :return: the sum value for the right element + left element in the domino for each domino in the player's hand.
        """
        sum = 0
        for i in range(len(self.hand)):
            # each item in hand is from Domino class, using its methods - get_right,get_left to sum its values
            sum += self.hand[i].get_right() + self.hand[i].get_left()
        return sum

    def has_dominoes(self):
        """
the method returns a boolean value if the player still has dominoes in his hand, if its empty returns false.
        :return: a boolean value if the player still has dominoes in his hand
        """
        return len(self.hand) > 0

    # play  - abstract, changed between players
    @abstractmethod
    def play(self, board):
        """
this is an abstract method which wont be used in this class and changes between each player type.
        :param board: the board that the player plays by.
        """
        pass

    def __str__(self):
        """
the method create the str method for a player by combining all fields and adds them to an empty string.
        :return: a string with all the player details.
        """
        return f'Name: {self.name}, Age: {self.age}, Hand: {self.hand}, Score: {self.score()}'

    def __repr__(self):
        """
the method returns the str method's output which is identical to the repr method.
        :return: a string with all the player details - return value of the str method.
        """
        return self.__str__()
