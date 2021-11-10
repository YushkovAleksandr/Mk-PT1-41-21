l=[4,5,6,7,8,9,10,11,12,13,14,15]
def binary_search_rec(some_list,x): 
    if len(some_list)==0: 
        return 0 
    else: 
        mid=len(some_list)//2 
    if (x==some_list[mid]): 
        return l.index(x) 
    else: 
        if x>some_list[mid]: 
            return binary_search_rec(some_list[mid+1:],x) 
        else: 
            return binary_search_rec(some_list[:mid],x)
print(binary_search_rec(l,3))
