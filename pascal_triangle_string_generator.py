def pascal_triangle_string_generator(rows):
    """
    функция pascal_triangle_string_generator (генератор строк треугольника Паскаля),
    возвращает строки треугольника паскаля в виде массива
    На вход, принимает следующий параметр:
    - rows, количество массива строк треугольника паскаля
    """
    start_num = [1]
    count = 0
    while rows > count:
        count = count + 1
        yield start_num
        start_num.append(0)
        start_num = [start_num[i - 1] + start_num[i] for i in range(len(start_num))]


for n in pascal_triangle_string_generator(5):
    print(n)
