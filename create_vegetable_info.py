
def create_vegetable_info(vegetables, varieties, yields):
    variety_yield_pairs = zip(varieties, yields)
    vegetable_info = dict(zip(vegetables, variety_yield_pairs))
    return vegetable_info

vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
varieties = ['Красный куб', 'Аллигатор', 'Василёк', 'Тропический закат', 'Арктик']
yields = [6.5, 4.3, 2.8, 2.2, 3.5]

print(create_vegetable_info(vegetables, varieties, yields))