# 1. Binary Search (рекурсивный, в идеале без слайсов) с использованием функции 

a = [0, 1, 2, 3, 4, 5, 7, 8, 9]
b = int(input('Введите элемент для поиска:\n'))

def b_search(a, first_el, final_el, b):
	if final_el >= first_el:
		mid_el = (final_el + first_el) // 2
		if a[mid_el] == b:
			return mid_el
		elif a[mid_el] > b:
			return b_search(a, first_el, mid_el - 1, b)
		else:
			return b_search(a, mid_el + 1, final_el, b)
	else:
		return -1

c = b_search(a, 0, len(a)-1, b)

if c != -1:
    print(f'Индекс элемента: {c}')
else:
    print("Такого элемента в списке нет.")
    
