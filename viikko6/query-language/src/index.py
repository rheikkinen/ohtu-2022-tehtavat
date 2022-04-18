from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, Or, HasAtLeast, HasFewerThan, Not, PlaysIn, All

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)


    matcher = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )

    matcher2 = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher):
        print(player)
    print("----------------")
    for player in stats.matches(matcher2):
        print(player)


if __name__ == "__main__":
    main()
