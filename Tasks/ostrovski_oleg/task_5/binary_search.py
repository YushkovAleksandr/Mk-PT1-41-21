def binary_search(l, value, start = None, end = None):
    start = start if start else 0
    end = len(l) if end is None else end     
    mid_index = (end - start) // 2 + start
    
    if start <= end:
        if l[mid_index] > value:
            return binary_search(l, value, start = start, end = mid_index - 1)
        elif l[mid_index] < value:
            return binary_search(l, value ,start = mid_index + 1, end = end)
        else:
            return mid_index  
    else:
        return None


if __name__ == "__main__":   
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
