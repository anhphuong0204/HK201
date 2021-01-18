def lstSquare_recursive(n):
    if (n ==0):
        return []
    if (n == 1):
        return [n]
    return lstSquare_recursive(n - 1) + [n * n]

def lstSquare(n):
    return [i * i for i in range(1, n + 1)]


def dist_recursive(lst, n):
    if len(lst) == 1:
        return [(lst[0], n)]
    return [(lst.pop(0), n)] + dist_recursive(lst, n)

def dist_high(lst, n):
    return list(map(lambda x: (x, n), lst))

#############

#square = powGen(2)
#print(square(4))
#16
def powGen(n):
    return lambda i: i**n
square = powGen(2)
print(square(0))

k = (1, 2, 3, 4, 5, 6)
print(k[:-1])