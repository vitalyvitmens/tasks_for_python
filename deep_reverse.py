def deep_reverse(array: list):
    """
    Функция deep_reverse() принимает список в качестве
    аргумента и возвращает в качестве значения список,
    где порядок элементов обратный и подсписки также обращены.
    """
    try:
        if len(array) > 1:
            return list(deep_reverse(i) for i in reversed(array))
        return array
    except TypeError:
        return array


print(deep_reverse([10, 9, 8, 7, 6, 5, [4, 3, [2, 1]], 'f', 0.0]))
print(deep_reverse([3, 9, 0]))
print(deep_reverse([[4, 3], [2, 1]]))
