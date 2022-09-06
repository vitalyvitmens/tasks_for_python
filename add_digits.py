def add_digits(a: int):
    """
    Функция add_digits() принимает на вход неотрицательное целое число и
    возвращает другое число, полученное из первого следующим преобразованием:
    Итеративно слаживает все входящие в него цифры до тех пор пока, не останется одна цифра.
    """
    if not isinstance(a, int):
        return 'Число должно быть типа integer'
    elif a > 0:
        if a < 10:
            return a
        elif a >= 10:
            b = (a // 10) + (a % 10)
            while b > 9:
                b = (b // 10) + (b % 10)
            return b
    elif a == 0:
        return 0
    elif a < 0:
        return 'Вы ввели отрицательное число'
    else:
        return 'Введите число!'


print(add_digits(226))
