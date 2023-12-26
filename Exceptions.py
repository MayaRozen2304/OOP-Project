
class EmptyBoardException(Exception):
    # raised when the board is empty
    def __init__(self, message):
        """
an exception we will get if we want to do action on a board but it is empty, therefore we cant do them.
        :param message: a specific message we want to give the user in this exception case.
        """
        self.message = 'ERROR' + " " + str(message)

    def __str__(self):
        """
the method create the str method for this exception case.
        :return:  a specific message we want to give the user in this exception case.
        """
        return self.message


class FullBoardException(Exception):
    # full board
    def __init__(self, message):
        """
an exception we will get if we want to do action on a board but it is full, therefore we cant do them.
        :param message:  a specific message we want to give the user in this exception case.
        """
        self.message = 'ERROR' + " " + str(message)

    def __str__(self):
        """
the method create the str method for this exception case.
        :return:  a specific message we want to give the user in this exception case.
        """
        return self.message


class NoSuchDominoException(Exception):
    # we want to remove a domino that doesnt exist in collection
    def __init__(self, message):
        """
an exception we will get if we want to do action on a domino type object but it is not exists, therefore we cant do it.
        :param message: a specific message we want to give the user in this exception case
        """
        self.message = 'ERROR' + " " + str(message)

    def __str__(self):
        """
the method create the str method for this exception case.
        :return: a specific message we want to give the user in this exception case
        """
        return self.message


class InvalidNumberException(Exception):
    # invalid number
    def __init__(self, message):
        self.message = 'ERROR' + " " + str(message)

    def __str__(self):
        return self.message


