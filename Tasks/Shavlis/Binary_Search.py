# 1. Binary Search (рекурсивный, в идеале без слайсов)

def input_1():
    while True:
        try:
            c = int(input('Ведите число для поиска: '))
            d = int(input('Введите начало списка: '))
            e = int(input('Введите конец списка: ')) + 1
            break  
        except:
            print('Данные введены неккоректно')
            continue
    l = []
    for i in range(d,e):
        l.append(i)
    if c not in l:
        print('Данные введены неккоректно')
        return input_1()
    print('Введенный список: ', l)
    return l, c

q = input_1()

def bin(x, y):
    a = 0 
    b = len(x)-1
    mid = (a + b)//2
    if (y == x[mid]):
        return mid
    elif (y > x[mid]):
        return bin(x[mid+1:], y) + (mid + 1)
    else:
        return bin(x[:mid], y)

print('Позиция в списке: ', bin(q[0], q[1]))