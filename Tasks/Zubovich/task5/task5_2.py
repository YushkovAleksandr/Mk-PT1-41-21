my_list = [1, 2, [2, 4, [[7, 8], 4, 6]]]


def sum1(my_list):
    new_list = 0
    for element in my_list:
        if type(element) == type([]):
            new_list = new_list + sum1(element)
        else:
            new_list = new_list + element
    return new_list


print("Сумма элементов: ", sum1(my_list))
