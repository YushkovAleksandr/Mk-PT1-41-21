"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Binary Search (рекурсивный, в идеале без слайсов)
"""

def binary_search(arr, val):
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2

    if val == arr[mid]:
        return mid

    if val > arr[mid]:
        return binary_search(arr[mid + 1:], val) + (mid + 1)

    return binary_search(arr[:mid], val)


if __name__ == '__main__':
    assert binary_search([1, 2, 1, 1, 5, 8, 9], 5) == 4
    print('Решено!')


