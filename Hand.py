from Collection import Collection
from Exceptions import NoSuchDominoException


class Hand(Collection):
    def __init__(self, dominoes):
        """
defining the fields of the Hand class.
        :param dominoes: a list that includes dominoes from Domino type.
        """
        Collection.__init__(self, dominoes)
        self.array = dominoes

    def add(self, domino, index=None):
        """
the method adds a certain domino to board by the index was given , if no index was given it append it to the end of the array.
        :param domino:a domino element which may be added to the index if given or to the end of the array.
        :param index: int - where we want to add our dominoes
        :return:the update array after the adding function.
        """
        if index is None:
            # adding to the end of the array
            self.array.append(domino)
        else:
            # adding to a specific index
            self.array.insert(index, domino)
        return self.array

    def remove_domino(self, domino):
        """
the method will return a domino from the board and returns its index, if there is no such domino in the board the
method will raise an execption .
        :param domino: a domino element which we want to remove from the array.
        :return:the index of the domino that we want to remove
        """
        for i in range(len(self.array)):
            # eq is works also for flipped
            if self.array[i] == domino:
                self.array.remove(self.array[i])
                return i
            else:
                continue
            # no such domino in the board, raise exception
        raise NoSuchDominoException('no such domino in board')

    # __getitem__ method is identical to collection - no need to define again
    # __contains__ method is identical to collection - no need to define again
    # __eq__ method is identical to collection - no need to define again
    # __ne__ method is identical to collection - no need to define again
    # len method is identical to collection - no need to define again
    # __str__ method is identical to collection - no need to define again
    # __repr__ method is identical to collection - no need to define again

