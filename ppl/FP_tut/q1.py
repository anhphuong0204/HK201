def double(lst):
    return list(map(lambda x: x*2, lst))

def double_recursive(lst):
    if (len(lst) == 1):
        return [lst[0] * 2]
    return  [lst.pop(0) * 2] + double_recursive(lst)


k = [1, 4, 5, 7]
print(double_recursive(k))