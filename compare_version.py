def compare_version(version1: str, version2: str):
    """
    Функция compare_version() сравнивает переданные версии version1 и version2.
    Если version1 > version2, то функция вернет 1, если version1 < version2, то функция вернет -1,
    если же version1 = version2, то функция вернет 0.
    Версия - это строка, в которой два числа (мажорная и минорные версии) разделены точкой,
    например: 12.11. Важно понимать, что версия - это не число с плавающей точкой, а несколько чисел
    не связанных между собой. Проверка на больше/меньше производится сравнением каждого числа независимо,
    поэтому версия 0.12 больше версии 0.2.
    """
    version1, version2 = version1.split('.'), version2.split('.')
    print(version1, version2)

    try:
        while len(version1) or len(version2):
            if len(version1) == 0:
                version1 = [0]
            elif len(version2) == 0:
                version2 = [0]
            else:
                tmp1, tmp2 = int(version1[0]), int(version2[0])
                if tmp1 > tmp2:
                    return 1
                elif tmp1 < tmp2:
                    return -1
                else:
                    version1 = version1[1:]
                    version2 = version2[1:]
        return 0
    except ValueError:
        '!!! Это не числа с точкой !!!'


print(compare_version("0.1", "0.2"))
# → -1
print(compare_version("0.2", "0.1"))
# → 1
print(compare_version("4.2", "4.2"))
# → 0
