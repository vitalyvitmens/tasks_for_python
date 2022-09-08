def summary_ranges(array: list):
    """
    Функция summary_ranges() принимает на вход массив чисел, находит в нём непрерывные возрастающие
    последовательности чисел и возвращает массив строк с их перечислением.
    """
    result = []
    start_index = 0

    for i in range(len(array)):
        if i + 1 < len(array) and array[i] + 1 == array[i + 1]:
            continue

        if start_index == i:
            # TODO: для вывода одиночных чисел не входящих в непрерывную возрастающую последовательность:
            # result.append(str(arr[start_index]))
            pass
        else:
            result.append(f'{str(array[start_index])} -> {str(array[i])}')

        start_index = i + 1

    return result


print(summary_ranges([]))
print(summary_ranges([1]))
print(summary_ranges([1, 2, 3]))
print(summary_ranges([0, 1, 2, 4, 5, 7]))
print(summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5]))
