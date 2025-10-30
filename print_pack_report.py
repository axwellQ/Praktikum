def print_pack_report(starting_value):
    for num in range(starting_value, 0, -1):
        divisible_by_3 = (num % 3 == 0)
        divisible_by_5 = (num % 5 == 0)

        if divisible_by_3 and divisible_by_5:
            print(f"{num} - расфасуем по 3 или по 5")
        elif divisible_by_5:
            print(f"{num} - расфасуем по 5")
        elif divisible_by_3:
            print(f"{num} - расфасуем по 3")
        else:
            print(f"{num} - не заказываем!")


print_pack_report(31)