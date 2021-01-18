from functools import reduce

def compose_recursive(*func):
    if(len(func) > 2):
        func_recent_last = compose_recursive(*func[:-1])
    else:
        func_recent_last = func[0]
    return lambda arg: func_recent_last(func[-1](arg))

def compose_high_order(*func):
    return reduce(lambda x, y: lambda arg: y(x(arg)), reversed(func))

def double(x):
    return 2*x
def increase(x):
    return x+1
def square(x):
    return x*x

t1 = compose_high_order(square, increase, double)
print(t1(5))
t2 = compose_recursive(square, increase, double)
print(t2(5))