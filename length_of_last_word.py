def lengthOfLastWord(string):
    """
    функция lengthOfLastWord, возвращает длину последнего слова переданной на вход строки.
    Словом считается любая последовательность, не содержащая пробелов.
    Функция принимает на вход параметр (string) - строку в которой необходимо посчитать длину последнего слова.
    Если длина строки равна нулю (пустая строка) функция вернет ноль.
        используем функцию нарезки split ("").
        Иногда в конце строки бывает много лишних пробелов, что бы их удалить используем функцию strip ()
    """
    if len(string) == 0:
        return 0
    t = string.strip().split(" ")
    return f'Количество букв в последнем слове строки: {len(t[-1])}', f'Искомое слово: {t[-1]}'


a = 'Вставай, страна огромная, вставай на смертный бой. С фашистской силой темною, с проклятою ордой!'
b = ' '
c = '   p   y   t   h   o   n   '
d = 'СССР'

print(lengthOfLastWord(a))
print(lengthOfLastWord(b))
print(lengthOfLastWord(c))
print(lengthOfLastWord(d))
print(lengthOfLastWord(''))
print(lengthOfLastWord('man in BlacK'))
print(lengthOfLastWord('hello, world!  '))
