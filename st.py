# Допишите нужные импорты.
from datetime import datetime

def timedelta_days(datetime_str_1, datetime_str_2):
    # Напишите тело функции.
    format_str = '%Y/%m/%d %H:%M:%S'
    dt1 = datetime.strptime(datetime_str_1, format_str)
    dt2 = datetime.strptime(datetime_str_2, format_str)
    delta = dt2 - dt1
    return delta.days

difference = timedelta_days('2019/05/10 00:00:00', '2019/10/04 00:00:00')

print('От начала посевной до начала сбора урожая прошло', difference, 'дней.')