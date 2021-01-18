from functools import reduce

def flatten_high(lst): 
    if (len(lst) == 0):
        return []
    return reduce(lambda x, y: x + y, lst)
k = [[1], [2, 3], [4, 5, 6]]

def flatten_recursive(lst):
    if (len(lst) == 1):
        return lst[0]
    return lst.pop(0) + flatten_recursive(lst)

print(flatten_high(k))