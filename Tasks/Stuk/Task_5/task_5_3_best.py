from task_5_3 import entry_number_int, print_numbers_fib


def fib(n: int) -> list:
    """Формирование списка из n чисел Фибоначчи

    Args:
        n (int): кол-во чисел Фибоначчи (положительное целое число)

    Returns:
        list: списка из n чисел Фибоначчи
    """
    if n == 1:
        return [0]

    numbers = [0, 1] + [0]*(n-2)
    for i in range(2, n):
        numbers[i] = numbers[i-1] + numbers[i-2]
    return numbers


def main():
    n = entry_number_int(min_value = 1, text = "Введите кол-во чисел Фибоначчи")
    
    numbers = fib(n)
    print_numbers_fib(numbers)

if __name__ == "__main__":
    main()