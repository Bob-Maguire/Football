from game import *
from TeamSchedule import *

class Team:
    
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.homePlayed = 0
        self.awayPlayed = 0
        self.schedule = TeamSchedule(self.name)

    def addAwayGame(self, game):
        self.awayPlayed += 1
        if (game.win == self.name):
            self.wins += 1
            self.
        elif (game.win == "tie"):
            self.ties += 1
        else:
            self.losses += 1

    def addHomeGame(self, game):
        self.homePlayed += 1
        if (game.win == self.name):
            self.wins += 1
        elif (game.win == "tie"):
            self.ties += 1
        else:
            self.losses += 1