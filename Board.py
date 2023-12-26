from Collection import Collection
from Exceptions import InvalidNumberException, EmptyBoardException, FullBoardException


class Board(Collection):
    def __init__(self, max_capacity):
        """
defining the fields of the Board and checks its input( if valid, else exception)
        :param max_capacity: the max number of dominoes that can be in the board - int
        """
        Collection.__init__(self, array=[])
        if max_capacity < 1 or max_capacity > 28:
            raise InvalidNumberException('number out of range between 1-28')
        self.max_capacity = max_capacity

    def in_left(self):
        """
the method returns the most left number in the left domino of the board.
        :return: int- left side element of the most left domino.
        """
        # if the board is empty- raise exception
        if len(self.array) == 0:
            raise EmptyBoardException('empty board')
        first_domino = self.__getitem__(0)
        return first_domino.get_left()

    def in_right(self):
        """
the method returns the most right number in the right domino of the board.
        :return: int- right side element of the most right domino.
        """
        # if the board is empty- raise exception
        if len(self.array) == 0:
            raise EmptyBoardException('empty board')
        last_domino = self.__getitem__(-1)
        return last_domino.get_right()

    def add(self, domino, add_to_right=True):
        """
the method checks if a certain domino can be added to a certian side of the board depending of the value of add_to_true.
if true, it checks if it fits to the right side by calling the help function- add right, than if we can add it, returns true,
else, false (same for checking addition to the left side by value of add_to_right = False.)
        :param domino: a domino type element which may be added to the left/right side.
        :param add_to_right: boolean true/false in order to know to which side of the board to check.
        :return: boolean if the domino can be added to the left/right side of the board by requirement.
        """
        if len(self.array) >= self.max_capacity:
            raise FullBoardException('full board, cant add more domino')
        # if the array is empty, only one add - not from both sides
        if len(self.array) == 0:
            self.array.append(domino)
            return True
        # if we need to add the right side
        if add_to_right is True:
            # checks possibility
            if self.add_right(domino) is True:
                return True
            return False
        # if we need to add the left side
        else:
            # checks possibility
            if self.add_left(domino) is True:
                return True
            return False

    def add_left(self, domino):
        """
the method checks if a certain domino can be added to the left side of the board, by its form or its flipped form.
        :param domino: a domino type element which may be added to the left side if true.
        :return:  boolean if the domino can be added to the left side of the board.
        """
        res = False
        if len(self.array) == 0:
            self.array.append(domino)
            return True
        if len(self.array) < self.max_capacity:
            if self.array[0].get_left() == domino.get_right():
                self.array.insert(0, domino)
                return True
            if self.array[0].get_left() == domino.flip().get_right():
                self.array.insert(0, domino.flip())
                return True
        return res

    def add_right(self, domino):
        """
the method checks if a certain domino can be added to the right side of the board, by its form or its flipped form.
        :param domino: a domino type element which may be added to the right side if true.
        :return: boolean if the domino can be added to the right side of the board.
        """
        res = False
        if len(self.array) == 0:
            self.array.append(domino)
            return True
        if len(self.array) < self.max_capacity:
            if self.array[-1].get_right() == domino.get_left():
                self.array.append(domino)
                return True
            if self.array[-1].get_right() == domino.flip().get_left():
                self.array.append(domino.flip())
                return True
        return res

    # __getitem__ method is identical to collection - no need to define again
    # __contains__ method is identical to collection - no need to define again

    def __eq__(self, other):
        """
checks if two board element are equal by a few conditions - same type, same max capacity and same len.
        :param other: another element we want to check if equals to the certain Board element.
        :return: boolean if the the two elements are equal, else false,
        """
        # check if we can use this method- only with two objects from Board class.
        # check if both with same max capacity parameter and same len - if not- they arent equal.
        res = False
        if not isinstance(other, Board) or self.max_capacity != other.max_capacity or len(self.array) != len(other.array):
            return False
        if len(self.array) == 0 or len(other.array) == 0:
            return True
        for i in range(len(self.array)):
            if self.array[i].get_right() == other.array[i].get_right() and self.array[i].get_left() == other.array[i].get_left():
                res = True
            else:
                res = False
                break
        return res

    # __ne__ method is identical to collection - no need to define again.
    # len() method is identical to collection - no need to define again.

    def __str__(self):
        """
the method create the str method for a board item by combining all the dominoes in the array and adds them to
an empty string by order.
        :return: a string with all the dominoes in th board.
        """
        board = ''
        for domino in self.array:
            # adding the domino to the empty string by using str method of Domino class.
            board += domino.__str__()
        return board

    # __repr__ method is identical to collection - no need to define again.


