def fizz_buzz(begin: int, end: int):
    """
    Функция fizz_buzz(), возвращает строку с числами (через пробел) в диапазоне от begin до end включительно.
    При этом:
        Если число делится без остатка на 3, то вместо него выводится слово Fizz
        Если число делится без остатка на 5, то вместо него выводится слово Buzz
        Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово FizzBuzz
        В остальных случаях в строку добавляется само число
    Функция принимает два параметра (begin и end), определяющих начало и конец диапазона (включительно).
    Если диапазон пуст (в случае, когда begin > end), то функция возвращает пустую строку.
    """
    a = []
    if not isinstance(begin, int):
        return 'Начальное число должно быть типа integer'
    elif not isinstance(end, int):
        return 'Конечное число должно быть типа integer'
    elif begin < end:
        for i in range(begin, end + 1):
            if i % 3 == 0 and i % 5 == 0:
                i = 'FizzBuzz'
                a.append(i)
            elif i % 3 == 0 and i % 5 != 0:
                i = 'Fizz'
                a.append(i)
            elif i % 5 == 0 and i % 3 != 0:
                i = 'Buzz'
                a.append(i)
            else:
                i = i
                a.append(i)
    else:
        return 'пустая строка'
    return [*a]


print(fizz_buzz(1, 22))
