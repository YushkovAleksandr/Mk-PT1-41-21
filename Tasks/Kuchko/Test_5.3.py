# 3. Написать функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34 


def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        x = fibonacci(n-1)
        x.append(sum(x[:-3:-1]))
        return x

if __name__ ==  "__main__":

    a = int(input("Введите количество первых чисел Фибоначчи: "))
    print(', '.join(str(x) for x in fibonacci(a)))