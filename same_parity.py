def same_parity(array: list):
    """
    Функция same_parity() принимает список чисел и возвращает
    отфильтрованный список у которого четность ближайшего элемента
    совпадает с четностью первого элемента этого списка.
    """
    new_list = []
    if len(array) == 1:
        return f'В списке только одно число {array[0]}, его четность не с чем сравнивать'
    if len(array) == 0:
        return f'Список пуст'
    for i in range(1, len(array)):
        if array[0] % 2 == array[i] % 2:
            new_list.append(array[0])
            new_list.append(array[i])
            return new_list
    else:
        return f'В списке нет чисел с такой же четностью как у числа {array[0]}'


print(same_parity([2, 3, 13, 1, 15, 9, 11, 13, 1, 0]))
