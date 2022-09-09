def flatten(array):
    """
    Функция flatten() принимает на вход массив любой вложенности и делает его плоским.
    """
    new_list = []
    new_list.extend([array]) if (type(array) is not list) else [new_list.extend(flatten(e)) for e in array]
    return new_list


print(flatten([[1, 2], [3, 4], [5, 6]]))
print(flatten([]))
print(flatten([77]))
print(flatten([[1], ['key => value', [4]]]))
