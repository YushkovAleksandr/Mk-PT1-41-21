def search(l, low, high, value):
    midle = low + ((high - low) // 2)
    if value == l[midle]:
        return midle
    if l[midle] > value:
        return search(l, low, midle - 1, value)
    elif value > l[midle]:
        return search(l, midle + 1, high, value)

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if __name__ == '__main__':
    while True:
        val = int(input(f"What do you want looking for on the {l} \n"))
        try:
            if val in l:
                print("Index of searching element =",search(l, 0, len(l) - 1, val))
                break
            else:
                raise RuntimeError
        except RuntimeError:
            print("This value isn't in list")