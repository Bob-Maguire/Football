class week:
    def __init__(self, season_week, win, opponent, score, opScore, venue):
        self.season_week = season_week
        self.win = win
        self.opponent = opponent
        self.score = score
        self.opScore = opScore
        self.venue = venue

    def printScore(self):
        print(self.score)
