def count_tiles(depth, length, width=None):
    if width is None:
        width = length

    width_side = 2 * width * depth
    length_side = 2 * length * depth
    bottom_tiles = length * width
    total = width_side + length_side + bottom_tiles

    return total


def make_phrase(total_tiles):
    if total_tiles % 100 in (11, 12, 13, 14):
        word = 'плиток'
    else:
        remainder = total_tiles % 10
        if remainder == 1:
            word = 'плитку'
        elif remainder in (2, 3, 4):
            word = 'плитки'
        else:
            word = 'плиток'

    return f'{total_tiles} {word}'


total_tiles = count_tiles(2, 2, 2)
print('Для строительства бассейна нужно заготовить', make_phrase(total_tiles))