from game import *
from TeamSchedule import *

class Team:
    
    def __init__(self, name, id, stadium, location, full_name):
        self.name = name
        self.id = id
        self.stadium = stadium
        self.location = location
        self.full_name = full_name
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.homePlayed = 0
        self.awayPlayed = 0
        self.homeRemaining = 0
        self.awayRemaining = 0
        self.schedule = TeamSchedule(self.name)

    def addAwayGame(self, game):
        if game.completed:
            self.awayPlayed += 1
            if (game.win == self.name):
                self.wins += 1
            elif (game.win == "tie"):
                self.ties += 1
            else:
                self.losses += 1
            self.schedule.newGame(game, game.win)
        else:
            self.awayRemaining += 1
            self.schedule.newGame(game, game.win)

    def addHomeGame(self, game):
        if game.completed:
            self.homePlayed += 1
            if (game.win == self.name):
                self.wins += 1
            elif (game.win == "tie"):
                self.ties += 1
            else:
                self.losses += 1
            self.schedule.newGame(game, game.win)
        else:
            self.homeRemaining += 1
            self.schedule.newGame(game, game.win)