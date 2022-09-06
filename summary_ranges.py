def summary_ranges(arr: list):
    """
    функция summary_ranges() принимает на вход массив чисел, находит в нём непрерывные возрастающие
    последовательности чисел и возвращает массив строк с их перечислением.
    """
    result = []
    start_index = 0

    for i in range(len(arr)):
        if i + 1 < len(arr) and arr[i] + 1 == arr[i + 1]:
            continue

        if start_index == i:
            # TODO: для вывода одиночных чисел не входящих в непрерывную возрастающую последовательность:
            # result.append(str(arr[start_index]))
            pass
        else:
            result.append(f'{str(arr[start_index])} -> {str(arr[i])}')

        start_index = i + 1

    return print(result)


summary_ranges([])
summary_ranges([1])
summary_ranges([1, 2, 3])
summary_ranges([0, 1, 2, 4, 5, 7])
summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5])
