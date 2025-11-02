from math import sqrt
from typing import Optional


def add_numbers(first_number: float, second_number: float) -> float:
    return first_number + second_number


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return None

    root_value = calculate_square_root(your_number)
    return (
        f'Мы вычислили квадратный корень из введённого вами числа. '
        f'Это будет: {root_value}'
    )


first_number = 10
second_number = 5

print('Сумма чисел:', add_numbers(first_number, second_number))
print(calc(25.5))