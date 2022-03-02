from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered_players = [player for player in players if player.nationality==nationality]
        filtered_players.sort(key=Player.points, reverse=True)

        return filtered_players

