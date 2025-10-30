import random

# 1. создание списка списков:
harvest = [[random.randint(5, 20) for _ in range(5)] for _ in range(4)]

# 2. функция для подсчёта общего урожая:
def total_harvest(harvest_data):
    return sum(sum(plot) for plot in harvest_data)

# 3. функция для подсчёта среднего урожая с каждого участка:
def average_harvest_per_plot(harvest_data):
    return [sum(plot) / len(plot) for plot in harvest_data]

# вывод результатов
print('Урожай с каждой грядки на каждом участке:', harvest)
print('Общий урожай со всех участков:', total_harvest(harvest))
print('Средний урожай с каждого участка:', average_harvest_per_plot(harvest))