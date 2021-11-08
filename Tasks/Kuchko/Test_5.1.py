# 1. Binary Search (рекурсивный, в идеале без слайсов)

a = [0, 1, 2, 3, 4, 5, 7, 8, 9]
b = int(input('Введите элемент для поиска:\n'))

first_el = 0
mid_el = len(a) // 2
final_el = len(a) - 1
 
while a[mid_el] != b and first_el <= final_el:
    if b > a[mid_el]:
        first_el = mid_el + 1
    else:
        final_el = mid_el - 1
    mid_el = (first_el + final_el) // 2
 
if first_el > final_el:
    print("Такого элемента в списке нет.")
else:
    print("Индекс элемента: ", mid_el)

    