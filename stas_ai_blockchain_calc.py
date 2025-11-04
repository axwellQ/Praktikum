def stas_ai_blockchain_calc(operation, first, second):
    if operation == '+':
        result = first + second
    elif operation == '-':
        result = first - second
    elif operation == '*':
        result = first * second
    elif operation == '/':
        result = first / second
    elif operation == '**':
        result = first ** second
    else:
        return f'Не могу вычислить, операция {operation} не предусмотрена!'
    return result


print(stas_ai_blockchain_calc('+', 5, 10))   # Складываем.
print(stas_ai_blockchain_calc('*', 30, 10))  # Умножаем.
print(stas_ai_blockchain_calc('**', 30, 2))  # Возводим в степень.
# Ломаем, передав неизвестный указатель.
print(stas_ai_blockchain_calc('¯\_(ツ)_/¯', 10, 2))