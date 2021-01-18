#f = compose(increase,square)
#print(f(3)) #increase(square(3)) = 10
#10

def compose(*funcList):
    if len(funcList) <= 2:
        funcToCompose = funcList[0]
    else:
        funcToCompose = compose(*funcList[:-1])
    return lambda func: funcToCompose(funcList[-1](func))



def increase(n):
    return n + 1
def square(n):
    return n * n
def double(n):
    return n * 2

f = compose(increase)
print(f(3)) #increase(square(3)) = 10

