x = [1, 2, [2, 4, [[7, 8], 4, 6]]]

def summ(x):

    """
    Функция для вычисления суммы всех элементов вложенных (любая глубина) списков
    """

    suma=0
    for i in x:
        if isinstance(i, list):
            suma += summ(i)
        else:
            suma += i
    return suma

if __name__ == '__main__':
    print(summ(x))
       