# Пропишите нужные импорты.
from decimal import Decimal, getcontext

# Устанавливаем точность вычислений: 3 значащие цифры
getcontext().prec = 3


# Напишите код функции.
def get_monthly_payment(loan_amount, months, interest_percent):
    # Преобразуем всё в Decimal для точности
    amount = Decimal(str(loan_amount))
    months = Decimal(str(months))
    rate = Decimal(str(interest_percent))

    # Считаем базовый платёж без процента
    base_payment = amount / months

    # Добавляем процент: увеличиваем на (1 + процент/100)
    monthly_payment = base_payment * (1 + rate / 100)

    return monthly_payment


# Вызовите функцию get_monthly_payment()
# с указанными в задании аргументами
# и распечатайте нужное сообщение.
payment = get_monthly_payment(54, 24, 9)
print(f'Ежемесячный платёж: {payment} ВтК')