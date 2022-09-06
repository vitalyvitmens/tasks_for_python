def arithmetic_progression_generator(start, step, end):
    """
    функция arithmetic_progression_generator() (генератор арифметической прогрессии), возвращает числа
    арифметической прогрессии в диапазоне от start до end включительно с шагом step между числами.
    На вход, принимает три параметра:
    - start, начальное число арифметической прогрессии равное первому числу вывода
    - step, шаг между числами в арифметической прогрессии
    - end, общее количество чисел в арифметической прогрессии
    """

    count = 1
    while count <= end:
        yield start
        start += step
        count += 1


arithmetic_progression_list = []
for i in arithmetic_progression_generator(0, 5, 10):
    arithmetic_progression_list.append(i)
print(arithmetic_progression_list)
