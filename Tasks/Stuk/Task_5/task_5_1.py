def input_list_numbers() -> list:
    """Ввод списка целых чисел

    Returns:
        list: список целых чисел
    """
    while True:
        values = input(f"Введите список целых чисел через запятую:\n")
        try:
            values = [int(value) for value in values.split(",")]
            break
        except ValueError:
            print("Входные данные не являются целыми числами. Повторите попытку.")
    return values


def entry_number_int(text: str) -> int:
    """Ввод целого числа 

    Args:
        text (str): текст сообщения перед вводом данных

    Returns:
        int: вводимое целое число
    """
    while True:
        value = input(f"{text} (целое число):\n")
        try:
            value = int(value)
            break
        except ValueError:
            print("Входные данные не являются целым число. Повторите попытку.")
    return value


def binary_search(numbers: list, left: int, right: int, key: int) -> int:
    """Алгоритм бинарного поиска

    Args:
        numbers (list): отсортированный непустой список чисел
        left (int): левая граница поиска
        right (int): правая граница поиска
        key (int): искомое число

    Returns:
        int: индекс искомого числа в списке либо None, если
             такого числа нет
    """
    if (right - left) == 0:
        if numbers[left] == key:
            return left
        return None

    midle = (right + left) // 2
    if numbers[midle] == key:
        return midle
    if numbers[midle] < key:
        return binary_search(numbers, midle+1, right, key)
    else:
        return binary_search(numbers, left, midle-1, key)


def print_result(numbers, index):
    if index is None:
        print("Числа нет в списке.")
    else:
        print(f"Число {numbers[index]} присутствует в списке.")


def main():
    numbers = sorted(list(set(input_list_numbers())))
    sea_number = entry_number_int("Введите искомое число")
    index = binary_search(numbers, 0, len(numbers), key = sea_number)
    print_result(numbers, index)

if __name__ == "__main__":
    main()
