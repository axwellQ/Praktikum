people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']


def say_to_all(func, sequence):
    for item in sequence:
        func(item)


say_to_all(lambda name: print(f'Здравствуй, {name}!') if name.startswith('С') else print(f'Привет, {name}!'), people)
