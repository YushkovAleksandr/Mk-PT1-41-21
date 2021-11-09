lst=[1, 2, [2, 4, [[7, 8], 4, 6]]] #34
def sum(lst):
    count = 0
    for i in lst:
        if type(i) == type([]):
            count = count + sum(i)
        else:
            count = count + i
    return count

if __name__ =="__main__":
    print('The sum of the list items is: ', sum(lst))