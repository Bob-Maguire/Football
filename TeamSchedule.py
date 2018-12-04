from game import *
from week import *

class TeamSchedule:
    def __init__(self, team):
        self.team = team
        self.weeks = {}

    def newGame(self, game, win):
        if (win == self.team):
            team_win = "Win"
        elif (win == "tie"):
            team_win = "Tie"
        elif (win == None):
            team_win = "Unplayed"
        else:
            team_win = "Loss"
        if (game.home == self.team):
            opp = game.away
            score = game.homeScore
            opp_score = game.awayScore
            venue = "home"
        else:
            opp = game.home
            score = game.awayScore
            opp_score = game.homeScore
            venue = "away"
        new_week = week(game.s_week, team_win, opp, score, opp_score, venue)
        self.weeks[game.s_week] = new_week