# from dataclasses import dataclass
from typing import List, TypedDict, Dict


class ResultItem(TypedDict):
    winner: str
    players: List[str]


# @dataclass
# class ResultItem:
#     winner: str
#     players: List[str]


class LeaderboardItem(TypedDict):
    name: str
    wins: int
    losses: int
    average: float


foo: dict[str, int | str] = {
    "foo": 0,
    "bar": "cat",
}

results: List[ResultItem] = [
    {
        # "foo": 0,
        "winner": "Tom",
        "players": [
            "Tom",
            "Taylor",
            # 0,
        ],
    },
    {
        "winner": "Taylor",
        "players": [
            "Tom",
            "Taylor",
        ],
    },
    {
        "winner": "Alice",
        "players": [
            "Alice",
            "Bob",
        ],
    },
    {
        "winner": "Bob",
        "players": [
            "Alice",
            "Bob",
        ],
    },
    {
        "winner": "Alice",
        "players": [
            "Alice",
            "Bob",
        ],
    },
    {
        "winner": "Bob",
        "players": [
            "Alice",
            "Bob",
        ],
    },
    {
        "winner": "Charlie",
        "players": [
            "Charlie",
            "Dave",
        ],
    },
    {
        "winner": "Dave",
        "players": [
            "Charlie",
            "Dave",
        ],
    },
    {
        "winner": "Frank",
        "players": [
            "Eve",
            "Frank",
        ],
    },
    {
        "winner": "Frank",
        "players": [
            "Eve",
            "Frank",
        ],
    },
    {
        "winner": "Frank",
        "players": [
            "Joe",
            "Frank",
        ],
    },
]


def generate_leaderboard(
    results: List[ResultItem],
) -> List[LeaderboardItem]:
    leaderboard: Dict[str, LeaderboardItem] = {}
    # leaderboard = {}

    for result in results:
        winner = result["winner"]
        players = result["players"]

        for player in players:
            if player not in leaderboard:
                leaderboard[player] = {
                    "name": player,
                    "wins": 0,
                    "losses": 0,
                    "average": 0,
                }
            if player == winner:
                leaderboard[player]["wins"] += 1
            else:
                leaderboard[player]["losses"] += 1
            total_games = leaderboard[player]["wins"] + leaderboard[player]["losses"]
            leaderboard[player]["average"] = (
                leaderboard[player]["wins"] / total_games if total_games > 0 else 0
            )

    leaderboard_array = list(
        leaderboard.values(),
    )
    leaderboard_array.sort(
        key=lambda x: (
            -x["average"],
            -(x["wins"] + x["losses"]) if x["wins"] > 0 else (x["wins"] + x["losses"]),
        ),
    )

    return leaderboard_array


leaderboard = generate_leaderboard(
    results,
)
print(
    leaderboard,
)

# Used Copilot chat to get traling commas everywhere,
# then Ctrl + s to save with Prettier and Black
# : - ))
