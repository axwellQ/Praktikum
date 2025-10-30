def get_competition_data(data):
    # Шаг 1: собрать все названия команд и подсчитать суммарные баллы
    teams = set()
    scores = {}

    for race in data:
        for team, score in race.items():
            teams.add(team)
            if team not in scores:
                scores[team] = 0
            scores[team] += score

    # Сортируем список команд по алфавиту
    sorted_teams = sorted(teams)
    teams_str = ', '.join(sorted_teams)
    print(f"Команды, участвовавшие в гонке: {teams_str}")

    # Шаг 2: найти победителя
    winner_team = None
    winner_score = 0
    for team, score in scores.items():
        if score > winner_score:
            winner_score = score
            winner_team = team

    print(f"В гонке победила команда {winner_team} с результатом {winner_score} баллов")


races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]

get_competition_data(races_data)