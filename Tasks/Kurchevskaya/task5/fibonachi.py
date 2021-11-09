def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ =="__main__":
    while True:
        try:
            n = int(input('Input non-negative number: '))
            assert n >= 0, 'The number must not be negative'
            break
        except ValueError:
            print('Wrong input, please try again')
            continue
        except AssertionError as error:
            print(error)
            continue

    print([fib(i) for i in range(n)])
