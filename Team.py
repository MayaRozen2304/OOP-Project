
class Team:
    def __init__(self, name, players):
        """
defining the fields of the Team class.
        :param name: string- the team name
        :param players: list of players[some player type]
        """
        self.name = name
        # private
        self.__players = players

    def get_team(self):
        """
    the method returns a list with all the players details.
        :return: a list with all the players details
        """
        return self.__players

    def score_team(self):
        """
the method calculates the score of each player in the team by calling the player.score()
and sums all the team score together.
        :return: int - the total score of the team.
        """
        total_score = 0
        for player in self.__players:
            # do score method on each player in the list and sums all results
            total_score += player.score()
        return total_score

    def has_dominoes_team(self):
        """
the method checks if the team still has dominoes by check each players.has_dominoes(), if even one player has , it returns
true. if none of the players in the team has dominoes, returns False.
        :return: boolean if the team still has dominoes.
        """
        for player in self.__players:
            # if true to one player, the team have dominoes
            if player.has_dominoes():
                return True
        return False

    def play(self, board):
        """
the method going over the players in the team and checks if one player can play with his dominoes.
        :param board:  the board[Board] that the player plays by.
        :return: boolean value if the team can play or not.
        """
        for player in self.__players:
            # if the play method returns true
            if player.play(board):
                return True
        # if no player played
        return False

    def __str__(self):
        """
creates a string with all the team details
        :return:  a string with all the team details
        """
        team = ''
        players = ''
        for i in self.__players:
            # adding a space between players
            players += i.__str__() + " "
        # removing the last space
        players = players[:-1]
        team += str('Name ' + self.name + ', Score team: ' + str(self.score_team()) + ', Players: ' + str(players))
        return team

    def __repr__(self):
        """
a string with all the team details - return value of the str method.
        :return: a string with all the team details - return value of the str method.
        """
        return self.__str__()

