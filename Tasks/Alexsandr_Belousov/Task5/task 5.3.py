def fib(n, x=[0]):
    """
    Функция для вычисления n первых чисел Фибоначчи
    """
    if n == 0:
        return x
    elif  len(x) < 2:
        return fib(n - 1, x + [1])
    return fib(n - 1, x + [x[-1] + x[-2]])

def main():
    print(fib(4))
    print(fib(9))

if __name__ == '__main__':
    main()