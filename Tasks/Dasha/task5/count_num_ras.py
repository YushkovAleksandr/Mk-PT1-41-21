"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать рекурсивную функцию sum_unpack,которая на вход получает список c вложенными списками,а возвращает
сумму всех элементов списка.
"""


def sum_unpack(arr):
    sum_p = 0
    for i in arr:
        if not isinstance(i, list):
            sum_p = sum_p + i
        else:
            sum_p = sum_p + sum_unpack(i)
    return sum_p


if __name__ == '__main__':
    assert sum_unpack([1, [2, [1, 1], 5, 8], 9]) == 27
    print('Решено!')
