while True:
    try:
        some_number=int(input('введите число==>>'))+1
        break  
    except ValueError:
        print('неверный ввод')
        continue
def fib(some_number):
    if some_number==1:
        return 0
    if some_number==2:
        return 1
    return fib(some_number-1)+fib(some_number-2)
def fib_list(some_number):
    l =[]
    for i in range(1,some_number):
        element=fib(i)
        l.append(element)
    return (', '.join(map(str,l)))
print(fib_list(some_number))