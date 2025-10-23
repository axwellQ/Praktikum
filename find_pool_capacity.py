def find_pool_capacity(num_of_people, length, width=None):
    if length < 0:
        length = -length


    if num_of_people < 0:
        num_of_people = -num_of_people


    if width is None:
        width = length
    elif width < 0:
        width = -width

    pool_area = length * width

    max_people = pool_area * 2

    if num_of_people <= max_people:
        print(f'Бассейн площадью {pool_area} кв. м. вмещает {num_of_people} чел.')
    else:
        print(f'Бассейн площадью {pool_area} кв. м. не вмещает {num_of_people} чел.')

find_pool_capacity(4, 2)
find_pool_capacity(4, 5, 10)
find_pool_capacity(-10, -5, -2)