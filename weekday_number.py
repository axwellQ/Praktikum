from datetime import datetime, timedelta

def get_weekday_name(weekday_number):
    if weekday_number == 0:
        return 'понедельник'
    elif weekday_number == 1:
        return 'вторник'
    elif weekday_number == 2:
        return 'среда'
    elif weekday_number == 3:
        return 'четверг'
    elif weekday_number == 4:
        return 'пятница'
    elif weekday_number == 5:
        return 'суббота'
    elif weekday_number == 6:
        return 'воскресенье'


def get_day_after_tomorrow(date_string):
    today = datetime.strptime(date_string, '%Y-%m-%d')

    weekday_today = today.weekday()

    day_after_tomorrow = today + timedelta(days=2)
    weekday_after_tomorrow = day_after_tomorrow.weekday()

    today_formatted = today.strftime('%Y-%m-%d')

    name_today = get_weekday_name(weekday_today)
    name_after_tomorrow = get_weekday_name(weekday_after_tomorrow)

    print(f'Сегодня {today_formatted}, {name_today}, а послезавтра будет {name_after_tomorrow}')


# Проверьте работу программы, можете подставить свои значения.
get_day_after_tomorrow('2024-01-01')
get_day_after_tomorrow('2024-01-02')
get_day_after_tomorrow('2024-01-03')
get_day_after_tomorrow('2024-01-04')
get_day_after_tomorrow('2024-01-05')
get_day_after_tomorrow('2024-01-06')