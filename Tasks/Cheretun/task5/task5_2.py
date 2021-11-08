def sum_list(l):
    total = 0
    for value in l:
        if isinstance(value, list):
            total += sum_list(value)
        else:
            total += value
    return total

if __name__ == '__main__':
    print("Count value =", sum_list([1, 2, [2, 4, [[7, 8], 4, 6]]]))