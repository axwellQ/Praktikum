def get_season(month):
    if month == 'январь' or month == 'февраль' or month == 'декабрь':
        return 'зима'
    elif month == 'март' or month == 'апрель' or month == 'май':
        return 'весна'
    elif month == 'июнь' or month == 'июль' or month == 'август':
        return 'лето'
    elif month == 'сентябрь' or month == 'октябрь' or month == 'ноябрь':
        return 'осень'
    else:
        return 'Ошибка в написании месяца!'

print(get_season('июнь'))
print(get_season('мартобрь'))