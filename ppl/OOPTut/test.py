# Question 2
class Rational:
    def __init__(self, *nAndD):
        self.n = 0
        self.d = 1
        if nAndD:
            self.n = nAndD[0]
            self.d = nAndD[1]
        self.g = self.gcd(abs(self.n), abs(self.d))
        self.numer = self.n / self.g
        self.denom = self.d / self.g
    
    def gcd(self, a, b):
        if (b == 0):
            return a
        else:
            return self.gcd(b, a % b)

    # override '+' method
    def __add__(self, o):
        if isinstance(o, Rational):
            return Rational(self.numer * o.denom + o.numer * self.denom , self.denom * o.denom)
        else:
            return Rational(self.numer * 1 + o * self.denom , self.denom * 1)
    # override print method
    def __str__(self):
        return str(self.n) + ' / ' + str(self.d)

# Question 3
class Expr:
    pass
class Var(Expr):
    def __init__(self, name):
        self.expr = name
    def __str__(self):
        return str(self.expr)
class Number(Expr):
    def __init__(self, num):
        self.expr = str(num)
    def printNum(self):
        print(self.expr)
    def __str__(self):
        return str(self.expr)
    def print(self):
        print(self)
class BinOP(Expr):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __str__(self):
        return '(' + str(self.left) + str(self.op) + str(self.right) + ')'
    def evalExpr(self):
        # return a Number obj
        numStr = eval(str(self))
        return Number(int(numStr))



# (x + 0.2) * 3
x = 1
t = BinOP(BinOP(Var('x'), '+', Number(3)), '*', Number(3))
t.evalExpr().print()

#test something
class A: 
    def foo(self,i): print (i) 

class B(A): 
    def foo(self,i): super().foo(i * 2) 

class C(A): 
    def foo(self,i): super().foo(i + 1) 

class D(A): 
    def foo(self,i): super().foo(i * i) 

class E(B, D, C): pass 

x = E() 
x.foo(1)