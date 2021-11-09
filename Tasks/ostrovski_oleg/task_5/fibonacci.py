def validation():
    while True:  
        try:
            fib_number = int(input("введите число для последовательности Фибоначчи (число должно быть больше ноля): ")) 
            if fib_number < 0:
                raise RuntimeError('произошла ошибка, будьте внимательны вы ввели число меньше ноля') 
            return fib_number
        except ValueError:
            print('произошла ошибка, повторите ввод')
        except RuntimeError as error:
            print(error)
            continue


def fibonacci(number, new_list = [0]):
    if number == 0:
        return new_list
    if len(new_list) < 2:
        return fibonacci(number - 1, new_list + [1])
    return fibonacci(number - 1, new_list + [new_list[-1] + new_list[-2]])


def fizz_buzz(new_list):
    return ["Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0) or i for i in new_list]


def fib_fizz_buzz(number):
    return fizz_buzz(fibonacci(number))


if __name__ == "__main__":        
    print(fibonacci(validation()))
    print(fibonacci(9))
    print(fib_fizz_buzz(13))


