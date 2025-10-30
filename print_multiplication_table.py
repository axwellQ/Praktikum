def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i, "*", j, "=", i * j)
        print("-" * 10)


print_multiplication_table()