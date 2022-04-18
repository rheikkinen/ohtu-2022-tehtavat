from statistics import Statistics
from player_reader import PlayerReader
from querybuilder import QueryBuilder


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (
        query
        .hasAtLeast(10, "goals")
        .hasFewerThan(20, "assists")
        .playsIn("BOS")
        .build()
    )
    
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
