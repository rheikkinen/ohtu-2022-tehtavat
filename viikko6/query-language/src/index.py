from statistics import Statistics
from player_reader import PlayerReader
from querybuilder import QueryBuilder


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    q1 = (
       query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    q2 = (
        query
        .playsIn("EDM")
        .hasAtLeast(40, "points")
        .build()
    )

    matcher = query.oneOf(q1, q2).build()
    
    matcher2 = (
        query
        .oneOf(
        query.playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build(),
        query.playsIn("EDM")
            .hasAtLeast(40, "points")
            .build()
        )
        .build()
    )

    for player in stats.matches(matcher):
        print(player)
    print("---------------")
    for player in stats.matches(matcher2):
        print(player)

if __name__ == "__main__":
    main()
