class Random:
    """
    Генератор рандомных чисел, представленный классом Random.
    Интерфейс объекта включает в себя три функции:
    конструктор - принимает на вход seed, начальное число генератора псевдослучайных чисел
    get_next - метод, возвращающий новое случайное число
    reset - метод, сбрасывающий генератор на начальное значение
    """
    def __init__(self, seed: int = 36):
        self.seed = seed

    def get_next(self):
        return (self.seed * 3) % 19

    def reset(self, seed: int = 36):
        self.seed = seed
        return self.seed


seq = Random(100)
result1 = seq.get_next()
print(result1)
result2 = seq.get_next()
print(result2)

print(result1 != result2)
# true

seq.reset()
print(seq.reset())

result21 = seq.get_next()
print(result21)
result22 = seq.get_next()
print(result22)

print(type(result1) == type(result21))
print(type(result2) == type(result22))
