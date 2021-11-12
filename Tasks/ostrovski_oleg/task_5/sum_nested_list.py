# вариант 1

nested_list = [1, 2,[2, 4, [[7, 8], 4, 6]]]
rec = lambda x: sum(map(rec, x)) if isinstance(x, list) else x


# вариант 2

def sum_list(list):
    count = 0
    for i in list:
        if type(i) == type([]):
            count += sum_list(i)
        else:
            count += i
    return count


if __name__ == "__main__":
    print(rec(nested_list)) 
    print(sum_list(nested_list))