class Player:
    def __init__(self, name, nationality, assists, goals, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team
        self.games = games
    
    def points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {self.goals + self.assists}"
