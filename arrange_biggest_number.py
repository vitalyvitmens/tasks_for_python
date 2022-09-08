def arrange_biggest_number(array: list):
    """
    Функция arrange_biggest_number(), составляет самое большое число из
    переданного массива чисел и возвращает его строковое представление.
    """
    if len(array) == 1:
        return str(array[0])
    for i in range(len(array)):
        array[i] = str(array[i])
    for i in range(len(array)):
        for j in range(1 + i, len(array)):
            if array[j] + array[i] > array[i] + array[j]:
                array[i], array[j] = array[j], array[i]
    result = ''.join(array)
    if result == '0' * len(result):
        return '0'
    else:
        return result


if __name__ == "__main__":
    print(arrange_biggest_number([1, 34, 3, 98, 9, 76, 45, 4]))
    print(arrange_biggest_number([1]))
    print(arrange_biggest_number([0]))
    print(arrange_biggest_number([1, 2]))
    print(arrange_biggest_number([0, 0]))
