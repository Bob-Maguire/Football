from game import *

class TeamSchedule:
    def __init__(self, team):
        self.team = team
        self.week1 = None
        self.week2 = None
        self.week3 = None
        self.week4 = None
        self.week5 = None
        self.week6 = None
        self.week7 = None
        self.week8 = None
        self.week9 = None
        self.week10 = None
        self.week11 = None
        self.week12 = None
        self.week13 = None
        self.week14 = None
        self.week15 = None
        self.week16 = None
        self.week17 = None

    def newGame(self, game, win):
        if win:
