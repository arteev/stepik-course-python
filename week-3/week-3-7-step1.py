count = int(input())

games = [input().split(";") for x in range(count)]
scores = dict()
for game in games:
    team1, team2 = game[0], game[2]
    goal1, goal2 = int(game[1]), int(game[3])

    if goal1 < goal2:
        team1, team2 = team2, team1
        goal1, goal2 = goal2, goal1

    scores[team1] = scores.setdefault(team1, [0, 0, 0, 0, 0])
    scores[team2] = scores.setdefault(team2, [0, 0, 0, 0, 0])

    score_team1, score_team2 = scores[team1], scores[team2]
    score_team1[0] += 1
    score_team2[0] += 1

    if goal1 > goal2:
        score_team1[1] += 1
        score_team2[3] += 1
        score_team1[4] += 3
    else:
        score_team1[2] += 1
        score_team2[2] += 1
        score_team1[4] += 1
        score_team2[4] += 1

for team, sc in scores.items():
    print(team + ":", end="")
    for i in sc:
        print(i,end=" ")
    print()
