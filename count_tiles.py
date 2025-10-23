def count_tiles(depth, length, width=None):
    if width is None:
        width = length

    bottom = length * width
    walls = 2 * depth * length + 2 * depth * width
    total = bottom + walls

    return total

total_tiles = count_tiles(2, 2, 2)
print('Общее количество плиток для строительства бассейна:', total_tiles)