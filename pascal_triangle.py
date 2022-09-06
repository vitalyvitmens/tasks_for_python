def pascal_triangle(rows):
    """
    функция pascal_triangle() (треугольник Паскаля),
    возвращает строки треугольника паскаля в виде массива
    На вход, принимает следующий параметр:
    - rows, количество массива строк треугольника паскаля
    """
    row = [1]
    for i in range(rows):
        print(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]


pascal_triangle(5)
