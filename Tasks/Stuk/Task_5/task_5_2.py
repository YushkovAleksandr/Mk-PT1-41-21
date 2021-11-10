# def sum_numbers(A):
#     sum_num = 0
#     for el in A:
#         if type(el) == list:
#             sum_num += sum_numbers(el)
#             continue
#         sum_num += el
#     return sum_num


def sum_numbers_tree(numbers):
    sum_num = 0
    for el in numbers:
        try:
            sum_num += int(el) # защита от зацикливания, если вдруг какой косяк
        except TypeError:
            sum_num += sum_numbers_tree(el)
        except ValueError:
            raise RuntimeError("Попался элемент, который не является числом!")
    return sum_num


if __name__ == "__main__":
    numbers = [1, 2, [2, 4, [[7, 8], 4, 6]]]
    try:
        print(sum_numbers_tree(numbers))
    except RuntimeError as error:
        print(error)
