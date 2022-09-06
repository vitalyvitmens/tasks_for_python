def binary_sum(a: str, b: str):
    """
    Функция binary_sum() принимает на вход два бинарных числа (в виде строк) и возвращает их сумму.
    Результат (вычисленная сумма) является десятичным числом в виде строки.
    """
    if not isinstance(a, str):
        return 'Первое число должно быть типа string'
    elif not isinstance(b, str):
        return 'Второе число должно быть типа string'
    else:
        len_a = len(a)
        dec_a = 0
        for i in range(0, len_a):
            dec_a = dec_a + int(a[i]) * (2 ** (len_a - i - 1))

        len_b = len(b)
        dec_b = 0
        for i in range(0, len_b):
            dec_b = dec_b + int(b[i]) * (2 ** (len_b - i - 1))
        return dec_a + dec_b


print(binary_sum('110011', '111'))
print(binary_sum('10', '1'))
print(binary_sum('1101', '101'))
