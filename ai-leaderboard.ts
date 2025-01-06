const results = [
    {
        winner: "Tom",
        players: [
            "Tom",
            "Taylor"
        ]
    },
    {
        winner: "Taylor",
        players: [
            "Tom",
            "Taylor"
        ]
    },
    {
        winner: "Alice",
        players: [
            "Alice",
            "Bob"
        ]
    },
    {
        winner: "Bob",
        players: [
            "Alice",
            "Bob"
        ]
    },
    {
        winner: "Alice",
        players: [
            "Alice",
            "Bob"
        ]
    },
    {
        winner: "Bob",
        players: [
            "Alice",
            "Bob"
        ]
    },
    {
        winner: "Alice",
        players: [
            "Alice",
            "Bob"
        ]
    },
    {
        winner: "Bob",
        players: [
            "Alice",
            "Bob"
        ]
    },
    {
        winner: "Alice",
        players: [
            "Alice",
            "Bob"
        ]
    },
    {
        winner: "Bob",
        players: [
            "Alice",
            "Bob"
        ]
    },
    {
        winner: "Charlie",
        players: [
            "Charlie",
            "Dave"
        ]
    },
    {
        winner: "Dave",
        players: [
            "Charlie",
            "Dave"
        ]
    },
    {
        winner: "Frank",
        players: [
            "Eve",
            "Frank"
        ]
    },
    {
        winner: "Frank",
        players: [
            "Eve",
            "Frank"
        ]
    },
    {
        winner: "Frank",
        players: [
            "Joe",
            "Frank"
        ]
    }
];

function generateLeaderboard(results) {
    const leaderboard = {};

    results.forEach(result => {
        const winner = result.winner;
        const players = result.players;

        players.forEach(player => {
            if (!leaderboard[player]) {
                leaderboard[player] = { name: player, wins: 0, losses: 0, average: 0 };
            }
            if (player === winner) {
                leaderboard[player].wins++;
            } else {
                leaderboard[player].losses++;
            }
            leaderboard[player].average = leaderboard[player].wins / (leaderboard[player].wins + leaderboard[player].losses);
        });
    });

    const leaderboardArray = Object.values(leaderboard);
    leaderboardArray.sort((a, b) => {
        if (b.average === a.average) {
            if (b.wins === 0 && a.wins === 0) {
                return (a.wins + a.losses) - (b.wins + b.losses);
            }
            return (b.wins + b.losses) - (a.wins + a.losses);
        }
        return b.average - a.average;
    });

    return leaderboardArray;
}

const leaderboard = generateLeaderboard(results);
console.log(leaderboard);