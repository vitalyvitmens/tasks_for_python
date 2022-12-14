def fringe(array: list, direction: str = 'left'):
    """
    Функция fringe() принимает на вход в качестве аргумента дерево (представленное в виде списка)
    и возвращает список, элементы которого - все листья дерева, по умолчанию упорядоченные слева направо,
    но так же возможно упорядочить элементы списка и справа налево.
    Группировка элементов последовательности count осуществляется по двум элементам.
    """
    count = 2
    if direction == 'left':
        return list(zip(*[iter(array)] * count))
    else:
        right = reversed(array)
        return list(zip(*[iter(right)] * count))


print(fringe([1, 2, 3, 4, 5, 6, 7, 8]))
print(fringe([1, 2, 3, 4, 5, 6, 7, 8], 'right'))
