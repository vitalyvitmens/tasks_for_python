from itertools import permutations


def arrange_biggest_number(array: list):
    """
    Функция arrange_biggest_number(), составляет самое большое число из
    переданного массива чисел и возвращает его строковое представление.
    """
    big_num_list = []
    for i in permutations(array, len(array)):
        big_num_list.append("".join(map(str, i)))
    return max(big_num_list)


print(arrange_biggest_number([1, 34, 3, 98, 9, 76, 45, 4]))
