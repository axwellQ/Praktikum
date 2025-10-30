def get_competition_data(data):
    # Собираем все названия команд из всех заездов
    teams = set()
    for race in data:
        teams.update(race.keys())

    # Сортируем по алфавиту
    sorted_teams = sorted(teams)

    # Формируем строку с командами через запятую
    teams_str = ', '.join(sorted_teams)

    print(f"Команды, участвовавшие в гонке: {teams_str}")


races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]

get_competition_data(races_data)