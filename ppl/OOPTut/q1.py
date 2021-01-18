class Exp:
    pass

class IntLit(Exp):
    def __init__(self, num):
        self.expr = str(num)
    def print(self):
        print(self.expr)
    def __str__(self):
        return str(self.expr)
    def eval(self):
        return eval(str(self))
    def printPrefix(self):
        return str(self) + ' '
    def printPostfix(self):
        return str(self) + ' '
    def accept(self, visitor):
        return visitor.visit(self)

class FloatLit(Exp):
    def __init__(self, num):
        self.expr = str(num)
    def print(self):
        print(self.expr)
    def __str__(self):
        return str(self.expr)
    def eval(self):
        return eval(str(self))
    def printPrefix(self):
        return str(self) + ' '
    def printPostfix(self):
        return str(self) + ' '
    def accept(self, visitor):
        return visitor.visit(self)

class UnExp(Exp):
    def __init__(self, op, exp):
        self.op = op
        self.exp = exp
    def __str__(self):
        return str(self.op) + '(' + str(self.exp) + ')'
    def eval(self):
        return eval(str(self))
    def printPrefix(self):
        return self.op + '. ' + str(self.exp.printPrefix())
    def printPostfix(self):
        return str(self.exp.printPostfix()) + self.op + '. '
    def accept(self, visitor):
        return visitor.visit(self)
        
class BinExp(Exp):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __str__(self):
        return '(' + str(self.left) + str(self.op) + str(self.right) + ')'
    def eval(self):
        return eval(str(self))
    def printPrefix(self):
        return self.op + ' ' + str(self.left.printPrefix()) + str(self.right.printPrefix())
    def printPostfix(self):
        return str(self.left.printPostfix()) + str(self.right.printPostfix()) + self.op + ' '
    def accept(self, visitor):
        return visitor.visit(self)


#test the expression
x1 = UnExp('-', IntLit(4))
x2 = IntLit(3)
x3 = IntLit(2)
x4 = BinExp(x1, '+', BinExp(x2, '*', x3))
print(x4.printPostfix())

# Q3 
# x.accept(Eval())
# x.accept(PrintPrefix())
# x.accept(PrintPostfix())
# Eval, PrintPrefix and PrintPostfix are classes (Visitors)

# Visitors define
class Visitor:
    def visit(self, deriv_element):
        pass
class Eval(Visitor):
    def visit(self, deriv_element):
        return deriv_element.eval()
class PrintPrefix(Visitor):
    def visit(self, deriv_element):
        return deriv_element.printPrefix()
class PrintPostfix(Visitor):
    def visit(self, deriv_element):
        return deriv_element.printPostfix()

v_eval = Eval()
v_pPre = PrintPrefix()
v_pPost = PrintPostfix()


print(x4.accept(v_pPost))
