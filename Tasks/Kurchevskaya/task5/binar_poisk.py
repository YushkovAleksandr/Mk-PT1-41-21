
def valid():
    while True:
        try:
            list_binary = sorted(set([int(num) for num in input('Enter a list of numbers, for example "1, 6, 9":\n').strip(' ').split(',')]))
            return list_binary
        except (TypeError, ValueError):
            print('Incorrect input, please try again!!')
            continue

list_binary = valid()
print("Sorted list:", list_binary)

def valid2():
    while True:
        try:
            search_value = int(input('Input search_number: '))
            assert search_value in list_binary, 'The value is not in list'
            return search_value
        except (TypeError, ValueError):
            print('Incorrect input, please try again!')
            continue
        except AssertionError as error:
            print(error)
            continue
value = valid2()

def binar_search(list_binary,index0,indexn, s_value):
    
    if (indexn < index0):
       return None
    else:
        mid = index0+(indexn - index0) // 2
        #print(mid)
        if list_binary[mid] > s_value:
            return binar_search(list_binary, index0, mid-1,s_value)
        elif list_binary[mid] < s_value:
            return binar_search(list_binary, mid+1, indexn, s_value)
        else:
            return mid

index0=0
indexn=len(list_binary)-1
print(binar_search(list_binary, index0,indexn,value))