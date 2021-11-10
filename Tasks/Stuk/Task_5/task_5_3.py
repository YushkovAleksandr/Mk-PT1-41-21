def entry_number_int(min_value: int, text: str) -> int:
    """Ввод целого числа 

    Args:
        min_value (int): минимальное значение целого числа
        text (str): текст сообщения перед вводом данных

    Raises:
        RuntimeError: ошибка, если вводимое число меньше минимального значения

    Returns:
        int: вводимое целое число
    """
    while True:
        value = input(f"{text} (целое число):\n")
        
        try:
            value = int(value)
            if value < min_value:
                raise RuntimeError(f"Введенное число меньше минимально допустимого значения: {min_value}. Повторите попытку.")
            break
        except ValueError:
            print("Входные данные не являются целым число. Повторите попытку.")
        except RuntimeError as error:
            print(error)
    return value


def print_numbers_fib(numbers_fib):
    for i in numbers_fib:
        print(i, end=" ")


def fib(n, numbers_fib=[0, 1, 1]):
    if n <= 1:
        return 1

    value = fib(n-1, numbers_fib) + fib(n-2, numbers_fib)    
    if value > numbers_fib[-1]:
        numbers_fib.append(value)
    return value


def main():
    numbers_fib = [0, 1, 1]
    n = entry_number_int(min_value = 1, text = "Введите кол-во чисел Фибоначчи")

    if n <= len(numbers_fib):
        print_numbers_fib(numbers_fib[:n])
    else:
        fib(n-2, numbers_fib)
        print_numbers_fib(numbers_fib)

if __name__ == "__main__":
    main()