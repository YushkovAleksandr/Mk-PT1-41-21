# 3. Написать функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34 


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

if __name__ ==  "__main__":
    
    a = int(input("Введите количество первых чисел Фибоначчи: "))

    result = []
    for i in range(0, a):
        result.append(fibonacci(i))
    print(', '.join(str(x) for x in result))
