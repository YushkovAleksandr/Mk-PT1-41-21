def binary_search(element, my_list):
    def _binary_search(element, first, last, my_list):
        if last < first:
            return False
        if last == first:
            return my_list[last] == element
        mid = (first + last) // 2
        if my_list[mid] > element:
            last = mid
            return _binary_search(element, first, last, my_list)
        elif my_list[mid] < element:
            first = mid + 1
            return _binary_search(element, first, last, my_list)
        else:
            index = mid
            return index

    return _binary_search(element, 0, len(my_list) - 1, my_list)


print(binary_search(0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
