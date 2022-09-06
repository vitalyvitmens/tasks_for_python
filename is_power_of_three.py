def is_power_of_three(a: int):
    """
    Функция is_power_of_three() которая определяет, является ли переданное число натуральной степенью тройки.
    Например, число 27 – это третья степень (3**3), а 81 – четвёртая (3**4).
    """
    if not isinstance(a, int):
        return 'Число должно быть типа integer, положительное и больше нуля!'
    elif a == 1:
        return 'True'
    elif a < 1 or a % 3 != 0:
        return 'False'
    return is_power_of_three(a // 3)


print(is_power_of_three(243))
