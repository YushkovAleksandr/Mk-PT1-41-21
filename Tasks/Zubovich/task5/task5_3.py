
n = int(input('Введите количество первых чисел Фибоначчи: '))
n = 7
def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        list_fib = fib(n-1)
        list_fib.append(list_fib[-1] + list_fib[-2])
        return list_fib

#a = (fib(n-1))

print(", ".join(str(x) for x in (fib(n-1))))
