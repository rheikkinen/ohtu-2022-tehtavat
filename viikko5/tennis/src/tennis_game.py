class TennisGame:
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player
        self.first_player_score = 0
        self.second_player_score = 0

    def won_point(self, player_name):
        if player_name == self.first_player:
            self.first_player_score += 1
        else:
            self.second_player_score += 1

    def get_score(self):
        if self.score_is_tied():
            return self.tied_score()

        elif self.either_of_players_has_won_at_least_four_points():
            return self.endgame_score()
        
        return self.current_scores()

    def endgame_score(self):
        if self.first_player_has_advantage():
            return f"Advantage {self.first_player}"
        elif self.second_player_has_advantage():
            return f"Advantage {self.second_player}"
        elif self.first_player_is_ahead_by_two_or_more_points():
            return f"Win for {self.first_player}"
        else:
            return f"Win for {self.second_player}"

    def tied_score(self):
        if self.first_player_score == 0:
            return "Love-All"
        elif self.first_player_score == 1:
            return "Fifteen-All"
        elif self.first_player_score == 2:
            return "Thirty-All"
        elif self.first_player_score == 3:
            return "Forty-All"
        else:
            return "Deuce"
    
    def get_score_call(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"

    def score_is_tied(self):
        return self.first_player_score == self.second_player_score

    def current_scores(self):
        return f"{self.get_score_call(self.first_player_score)}-{self.get_score_call(self.second_player_score)}"

    def either_of_players_has_won_at_least_four_points(self):
        return self.first_player_score >= 4 or self.second_player_score >= 4

    def first_player_is_ahead_by_two_or_more_points(self):
        return self.first_player_score - self.second_player_score >= 2

    def first_player_has_advantage(self):
        return self.first_player_score - self.second_player_score == 1

    def second_player_has_advantage(self):
        return self.first_player_score - self.second_player_score == -1