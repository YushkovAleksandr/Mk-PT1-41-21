def fib(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib(num-2) + fib(num-1)

if __name__ == '__main__':
    while True:
        n = input("Input the integer range of numbers:\n")
        try:
            if n:
                if int(n):
                    n = int(n)
                    break
                else:
                    raise ValueError
            else:
                raise RuntimeError
        except (ValueError, RuntimeError):
            print("Input correct value")

    result = []
    for num in range(n):
        result.append(fib(num))
    print(*result, sep=', ')