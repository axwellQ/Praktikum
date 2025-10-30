def is_palindrome(s):
    # Приводим строку к нижнему регистру и удаляем все пробелы
    cleaned = s.lower().replace(' ', '')
    # Проверяем, равна ли строка своему обратному срезу
    return cleaned == cleaned[::-1]


# Должно быть напечатано True:
print(is_palindrome('А роза упала на лапу Азора'))
# Должно быть напечатано False:
print(is_palindrome('Не палиндром'))