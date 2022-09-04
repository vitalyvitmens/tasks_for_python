def is_power_of_three(a: int):
    """
    функция is_power_of_three() которая определяет, является ли переданное число натуральной степенью тройки.
    Например, число 27 – это третья степень (3**3), а 81 – четвёртая (3**4).
    """
    if not isinstance(a, int):
        return print('Число должно быть типа integer, положительное и больше нуля!')
    elif a == 1:
        return print('True')
    elif a < 1 or a % 3 != 0:
        return print('False')
    return is_power_of_three(a // 3)


is_power_of_three(243)
