import time


# Декоратор объявляется до декорируемой функции.
def time_of_function(func):
    # В декораторе есть вложенная функция.
    def wrapper():
        start_time = time.time()
        result = func()
        execution_time = round(time.time() - start_time, 3)
        print(f'Время выполнения: {execution_time} сек.')
        return result
    # Декоратор возвращает вызываемый объект (callable object),
    # в нашем случае - функцию.
    return wrapper


# Имя функции-декоратора (с символом @)
# ставится перед объявлением декорируемой функции.
@time_of_function
def sleep_one_sec():
    time.sleep(1)
    return 'Функция sleep_one_sec() завершила вычисления.'


# После декорирования любой вызов функции sleep_one_sec()
# будет автоматически сопровождаться измерением времени её выполнения.
sleep_one_sec()
