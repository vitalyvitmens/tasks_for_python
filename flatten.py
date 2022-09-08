def flatten(array):
    result = [y for x in array for y in x]
    if len(array) == 0:
        return print([])
    if len(array) == 1:
        return print(str(array[0]))
    for i in range(len(array) > 1):
        array[i] = str(array[i])
        return print(result)


flatten([[1, 2], [3, 4], [5, 6]])
flatten([])
flatten([[77]])
flatten([[1], ['key', 'value', [4]]])

# flatten([[1], ['key' => 'value', [4]]])
a = [[1, 3], [2, 4], [3, 5], ["abc", "def", [4]]]
a1 = [y for x in a for y in x]
print(a1)
