from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, HasFewerThan, Not, PlaysIn, All

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)


    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )

    matcher2 = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher):
        print(player)
    print("----------------")
    for player in stats.matches(matcher2):
        print(player)


if __name__ == "__main__":
    main()
