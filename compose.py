def compose(array):
    """
    Функция compose() реализует композицию.
    Принимает на вход массив одноаргументных функций,
    возвращает сумму значений переданных в массив функций.
    """
    def inner(arg):
        for f in reversed(array):
            arg = f(arg)
        return arg

    return inner


def square(num):
    return num ** 2


def half(num):
    return num / 2


func1 = compose([square, half])
print(func1(10))

func2 = compose([])
print(func2(3))
