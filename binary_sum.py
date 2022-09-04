def binarySum(a: str, b: str):
    """
    функция binarySum принимает на вход два бинарных числа (в виде строк) и возвращает их сумму.
    Результат (вычисленная сумма) также является бинарным числом в виде строки.
    """
    if not isinstance(a, str):
        return print('Первое число должно быть типа string')
    elif not isinstance(b, str):
        return print('Второе число должно быть типа string')
    else:
        len_a = len(a)
        dec_a = 0
        for i in range(0, len_a):
            dec_a = dec_a + int(a[i]) * (2 ** (len_a - i - 1))

        len_b = len(b)
        dec_b = 0
        for i in range(0, len_b):
            dec_b = dec_b + int(b[i]) * (2 ** (len_b - i - 1))
        return print(dec_a + dec_b)


binarySum('110011', '111')
