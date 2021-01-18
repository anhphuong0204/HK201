# list comprehension
def lessThan_compre(n, lst):
    return [i for i in lst if i < n]

def lessThan_high(n, lst):
    return list(filter(lambda x: x < n, lst))

def lessThan_recursive(n, lst):
    if len(lst) > 0:
        ele = lst.pop(0)
        if ele < n:
            return [ele] + lessThan_recursive(n, lst)
        return lessThan_recursive(n, lst)
    return []

k = [1, 2, 3, 4, 5, 6]
print(lessThan_compre(4, k))