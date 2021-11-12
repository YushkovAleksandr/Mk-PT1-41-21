l=[8,9,7,[7,[5,7],4],8]
def sum_elements(some_list):
    element_sum=0
    for element in some_list:
        if (type(element) == type([])):
            element_sum = element_sum + sum_elements(element)
        else:
            element_sum = element_sum + element
    return element_sum
print("сумма элементов:", sum_elements(l))