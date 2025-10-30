def get_stickers_comparison(collection_1, collection_2):
    set_1 = set(collection_1)
    set_2 = set(collection_2)

    only_in_1 = sorted(set_1 - set_2)

    only_in_2 = sorted(set_2 - set_1)

    common = sorted(set_1 & set_2)

    return (only_in_1, only_in_2, common)


stas_collection = ['Тим Бернерс-Ли', 'Линус Торвальдс', 'Ада Лавлейс', 'Линус Торвальдс', 'Маргарет Гамильтон',
                   'Бьярн Страуструп']
anton_collection = ['Тим Бернерс-Ли', 'Гвидо ван Россум', 'Линус Торвальдс', 'Бьярн Страуструп', 'Бьярн Страуструп',
                    'Кен Томпсон', 'Деннис Ричи']

stas_stickers, anton_stickers, common_stickers = get_stickers_comparison(stas_collection, anton_collection)

print('Стикеры, которые есть только у Стаса:', stas_stickers)
print('Стикеры, которые есть только у Антона:', anton_stickers)
print('Стикеры, которые есть и у Стаса, и у Антона:', common_stickers)