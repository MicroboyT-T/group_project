#Algorithm for the game#
class Game:
    def __init__(self, id):  #determine the player ID#
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):  #function for player move#
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1                     #"P" for Pistol, "B" for Burung "A" for Air
        if p1 == "P" and p2 == "B":
            winner = 0
        elif p1 == "B" and p2 == "P":
            winner = 1
        elif p1 == "A" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "A":
            winner = 1
        elif p1 == "B" and p2 == "A":
            winner = 0
        elif p1 == "A" and p2 == "B":
            winner = 1

        return winner                  #return the value of winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
