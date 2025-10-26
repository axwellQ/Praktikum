from datetime import datetime


def get_results(leader, participant):
    if leader == participant:
        print(f'Вы пробежали за {leader} и победили!')
        return

    fmt = '%H:%M:%S'
    leader_time = datetime.strptime(leader, fmt)
    participant_time = datetime.strptime(participant, fmt)

    diff_seconds = (participant_time - leader_time).total_seconds()

    hours = int(diff_seconds // 3600)
    minutes = int((diff_seconds % 3600) // 60)
    seconds = int(diff_seconds % 60)

    lag = f'{hours}:{minutes:02}:{seconds:02}'
    print(f'Вы пробежали за {participant} с отставанием от лидера {lag}')


# Проверка
get_results('02:02:02', '02:02:02')
get_results('02:02:02', '03:04:05')