from Exceptions import InvalidNumberException


class Domino:
    def __init__(self, left, right):
        """
defining the fields of the domino and checks its input.
        :param left: the left element in the domino object - int
        :param right:  the right element in the domino object - int
        """
        # checking range input for left number
        if left < 0 or left > 6:
            raise InvalidNumberException('left number out of range between 0-6')
        self.__left = left
        # checking range input for left number
        if right < 0 or right > 6:
            raise InvalidNumberException('right number out of range between 0-6')
        self.__right = right

    # creating a getter for private
    def get_left(self):
        """
gets the left element in the domino object - int
        :return: the left element in the domino object - int
        """
        return self.__left

    # creating a getter for private
    def get_right(self):
        """
gets the right element in the domino object - int
        :return: the right element in the domino object - int
        """
        return self.__right

    def __str__(self):
        """
the method create the str method for a Domino item
        :return: a form of a domino, [left element | right element]
        """
        return f'[{self.__left}|{self.__right}]'

    def __repr__(self):
        """
the method returns the str method's output which is identical to the repr method.

        :return: a form of a domino, [left element | right element]
        """
        return self.__str__()

    def __eq__(self, other):
        """
checks if two Domino element are equal by same element in the same index,
two dominoes are equal if the are identical, or if they have the same numbers in right/left with no importance to the order.
        :param other: the second element we want to check if equals to the certain element.
        :return: boolean value if equals or not.
        """
        # check if we can use this method- only with two objects from Domino class
        if not isinstance(other, Domino):
            return False
        # conditions for equality between objects
        if self.__right == other.__right and self.__left == other.__left or self.__right == other.__left and self.__left == other.__right:
            return True
        else:
            return False

    def __ne__(self, other):
        """
    the function returns true if two Domino items are different from each other, else, false.
        :param other: the second element we want to check if equals to the certain element.
        :return: boolean value if not equals or not
        """
        if not self.__eq__(other):
            return True
        else:
            return False

    def __gt__(self, other):
        """
the method checks if a domino object is greater than the another domino object by calculating the sum of its left and right.
        :param other:the second element we want to check if equals to the certain element.
        :return:boolean value if not equals or not
        """
        # check if we can use this method- only with two objects from Domino class
        if not isinstance(other, Domino):
            return False
        # return boolean if sum of self > sum of other
        return self.__right + self.__left > other.__right + other.__left

    def __contains__(self, key):
        """
    the method checks if a specific value is in the domino (left or right side).
        :param key: int - a number we want to check if is the self.right or self.left
        :return:boolean value if the key is in the domino
        """
        return self.__right == key or self.__left == key

    def flip(self):
        """
the method will create a new object which its attributes is opposite to the certain element.
        :return: a flipped domino type from the form of (self.right, self.left)
        """
        flip = Domino(self.__right, self.__left)
        return flip

