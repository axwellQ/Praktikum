from random import randint

# Начальная температура чая
current_temperature = 85

# Объявите цикл while
while current_temperature > 60:
    # Получаем случайное значение остывания от 1 до 3
    cooled = randint(1, 3)
    # Уменьшаем температуру
    current_temperature -= cooled
    # Печатаем информацию
    print("Прошла минута.")
    print(f"Чай остыл ещё на {cooled} °C. Текущая температура: {current_temperature} °C")

print("Время пить чай!")