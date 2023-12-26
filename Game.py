class Game:
    def __init__(self, board, team1, team2):
        """
defining the fields of the Game class.
        :param board: the game board[Board] that the game goes by.
        :param team1: object from Team type
        :param team2: object from Team type
        """
        self.board = board
        self.team1 = team1
        self.team2 = team2

    def play(self):
        """
the method runs the game by turns of the two teams. it checks for each turn if the team can play and if the game can continue,
if it is , the team plays and the game continue (starts from team1)
in case one of the stop conditions is true, the game is overs and the win function returns the string with the game results.
        :return: a string with the game results
        """
        # stop condition
        if self.stop():
            return self.win()
        # team 1 play first
        if self.team1.play(self.board):
            # dont need to stop
            if self.stop() is False:
                # team 2 play
                if self.team2.play(self.board):
                    # no need to stop
                    if self.stop() is False:
                        # another turn
                        self.play()
                    return self.win()
                self.play()
            return self.win()
        # team 2 play if team 1 cant
        if self.team2.play(self.board):
            # no need to stop
            if self.stop() is False:
                # another turn
                self.play()
            return self.win()
        # no team can play
        return self.win()

    def win(self):
        """
this function returns a string with the games results by the score of the team. the team with the lowest score will win.
        :return:  a string with the game results
        """
        if self.team1.score_team() == self.team2.score_team():
            return 'Draw!'
        # team 1 won:
        elif self.team1.score_team() < self.team2.score_team():
            return str('Team' + " " + str(self.team1.name) + " " + 'wins Team' + " " + str(self.team2.name))
        # team 2 won:
        else:
            return str('Team' + " " + str(self.team2.name) + " " + 'wins Team' + " " + str(self.team1.name))

    def stop(self):
        """
the function checks a few conditions and returns a true/false value that stops/not stops the game.
conditions for stop:
* no more dominoes to one team
*full board
        :return: a boolean value if the game need to be stopped or not.
        """
        if self.team1.has_dominoes_team() is False:
            return True
        if self.team2.has_dominoes_team() is False:
            return True
        if len(self.board) == self.board.max_capacity:
            return True
        else:
            return False


