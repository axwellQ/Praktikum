not_uniq_str = 'съешь же ещё этих мягких французских булок да выпей чаю'

unique_chars = set(not_uniq_str.replace(' ', ''))
count_char = len(unique_chars)

print(count_char)