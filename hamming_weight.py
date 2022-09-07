def hamming_weight(num: int):
    """
    Функция hamming_weight() принимает на вход положительное, целое число (типа int)
    в десятичной системе исчисления, преобразует его в двоичную систему исчисления (base = 2)
    и возвращает посчитанное количество единиц в десятичном представлении числа.
    """
    if not isinstance(num, int):
        raise TypeError("Hamming Weight function can work only with <class 'int'> type.")
    if num < 0:
        raise ValueError("Hamming Weight can't work with negative numbers.")
    if num == 0:
        print(0, end='')
    assert num >= 0
    base = 2
    sum_1 = []
    while num > 0:
        digit = num % base
        print(digit, end='')
        num //= base
        if digit == 0:
            continue
        if digit == 1:
            sum_1.append(1)
    return print(f'\nКоличество единиц = {len(sum_1)}')


hamming_weight(0)
hamming_weight(4)
hamming_weight(101)
