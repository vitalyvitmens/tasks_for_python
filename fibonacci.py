def fibonacci(n: int):
    """
    Функция fibonacci(), находит положительные числа Фибоначчи.
    Аргументом функции является порядковый номер числа.
    Вычисляет числа Фибоначчи n. Выбрасывает исключение TypeError,
    если вызвана не для целочисленного типа. Выбрасывает исключение ValueError,
    если число отрицательное или больше допустимого по контракту.
    :param n: целое число от 0 до 100000
    :return: целое число от 0 до ...
    """
    if not isinstance(n, int):
        raise TypeError("Fibonacci function can work only with <class 'int'> type.")
    if n < 0:
        raise ValueError("Fibonacci can't work with negative numbers.")
    if n >= 100001:
        raise ValueError("Fibonacci can't work with numbers larger than 100000.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    assert n >= 0
    F = [0, 1] + [0] * n
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    assert F[n] >= 0 and F[n] == F[n - 1] + F[n - 2]
    return F[n]


print(fibonacci(0))
# 0
print(fibonacci(1))
# 1
print(fibonacci(2))
# 1
print(fibonacci(3))
# 2
print(fibonacci(5))
# 5
print(fibonacci(10))
# 55
