class game:
    def __init__(self, id, week, away, home, completion, awayScore, homeScore):
        self.id = id
        self.week = week

        self.away = away
        self.home = home
        if completion != "COMPLETED":
            self.completed = False
        else:
            self.completed = True
        if self.completed:
            self.awayScore = awayScore
            self.homeScore = homeScore
            if (self.awayScore > homeScore):
                self.win = self.away
            elif (self.awayScore < self.homeScore):
                self.win = self.home
            else:
                self.win = "tie"
        else:
            self.awayScore = None
            self.homeScore = None
            self.win = None
    

