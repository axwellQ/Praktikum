vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
vegetable_yields = [6.5, 4.3, 2.8, 2.2, 3.5]

for index in range(len(vegetable_yields)):
    yield_kg_per_ha = vegetable_yields[index] * 10000  # Переводим т/га в кг/га
    print(f"{vegetables[index]}: урожайность - {int(yield_kg_per_ha)} кг на гектар.")