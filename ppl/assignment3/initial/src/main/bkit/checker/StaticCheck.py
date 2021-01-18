
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        #decl : List[Decl]
        c = [[]]
        [self.visit(x,c) for x in ast.decl]
        checkMain = False
        for env in c:
            for decl in env:
                if decl.name == 'main' and type(decl.mtype) == MType:
                    checkMain = True
        if checkMain == False:
            raise NoEntryPoint()

    def visitVarDecl(self,ast,c):
        #variable : Id
        #varDimen : List[int] # empty list for scalar variable
        #varInit  : Literal   # null if no initial
        for dec in c[0]:
            if dec.name == ast.variable.name:
                raise Redeclared(Variable(), dec.name)

        if len(ast.varDimen) == 0:
            if ast.varInit is None:
                c[0].append(Symbol(ast.variable.name, Unknown()))
            else:
                c[0].append(Symbol(ast.variable.name, self.visit(ast.varInit, c)))
        else:
            if ast.varInit is None:
                c[0].append(Symbol(ast.variable.name, ArrayType(ast.varDimen, Unknown())))
            else:
                c[0].append(Symbol(ast.variable.name, ArrayType(ast.varDimen, self.visit(ast.varInit, c))))
        #print(c[0][-1])
        

## Check blocks

    def visitFuncDecl(self,ast,c):
        #name: Id(name(string)) , if you wanna take name of function, you have to take name of its Id
        #param: List[VarDecl]
        #body: Tuple[List[VarDecl],List[Stmt]]
        for decl in c[0]:
            if decl.name == ast.name.name:      
                raise Redeclared(Function(), ast.name.name)

        funcEnv = [[]]
        for paraDecl in ast.param:
            for decl in funcEnv[0]:
                if decl.name == paraDecl.variable.name:
                    raise Redeclared(Parameter(), decl.name)
            funcEnv[0].append(Symbol(paraDecl.variable.name, Unknown())) #para has to be Unknown type
        
        for varDeclInFunc in ast.body[0]:
            self.visit(varDeclInFunc, funcEnv + c)

        #visit stmts to inferred type of param decl

        for stmt in ast.body[1]:
            self.visit(stmt, funcEnv + c)

        # function has Symbol : 1. name of string, 2. MType([list of type's paras], return type)
        paramList = []
        for i in range(len(ast.param)):
            paramList.append(funcEnv[0][i].mtype)
        c[0].append(Symbol(ast.name.name, MType(paramList, Unknown())))


    def visitIf(self,ast,c):
        """Expr is the condition, 
        List[VarDecl] is the list of declaration in the beginning of Then branch, empty list if no declaration
        List[Stmt] is the list of statement after the declaration in Then branch, empty list if no statement
    """
        #ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        #elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
        for block in ast.ifthenStmt:
            # block is Tuple[Expr,List[VarDecl],List[Stmt]]
            expr = self.visit(block[0], c)
            if type(expr.mtype) != BoolType:
                raise TypeMismatchInStatement(ast)
            ifEnv = [[]]
            for decl in block[1]:
                self.visit(decl, ifEnv)
            for stmt in block[2]:
                self.visit(stmt, ifEnv + c)
        elseEnv = [[]]
        for decl in ast.elseStmt[0]:
            self.visit(decl, elseEnv)
        for stmt in ast.elseStmt[1]:
            self.visit(stmt, elseEnv + c)


    def visitFor(self,ast,c):
        #idx1: Id
        #expr1:Expr
        #expr2:Expr
        #expr3:Expr
        #loop: Tuple[List[VarDecl],List[Stmt]]
        idx = self.visit(ast.idx1, c)
        expr1 = self.visit(ast.expr1, c)
        expr2 = self.visit(ast.expr2, c)
        expr3 = self.visit(ast.expr3, c)
        if type(idx.mtype) != IntType or type(expr1.mtype) != IntType or type(expr3.mtype) != IntType or type(expr2.mtype) != BoolType:
            raise TypeMismatchInStatement(ast)
        forEnv = [[]]
        for decl in ast.loop[0]:
            self.visit(decl, forEnv)
        for stmt in ast.loop[1]:
            self.visit(stmt, forEnv + c)

    def visitDowhile(self,ast,c):
        #sl:Tuple[List[VarDecl],List[Stmt]]
        #exp: Expr
        doEnv = [[]]
        for decl in ast.sl[0]:
            self.visit(decl, doEnv)
        for stmt in ast.sl[1]:
            self.visit(stmt, doEnv + c)
        if type(self.visit(ast.exp, c).mtype) != BoolType:
            raise TypeMismatchInStatement(ast)

    def visitWhile(self,ast,c):
        if type(self.visit(ast.exp, c).mtype) != BoolType:
            raise TypeMismatchInStatement(ast)
        doEnv = [[]]
        for decl in ast.sl[0]:
            self.visit(decl, doEnv)
        for stmt in ast.sl[1]:
            self.visit(stmt, doEnv + c)


## Check expressions, statements

    def visitAssign(self,ast,c):
        #lhs: LHS: Id and ArrayCell
        #rhs: Expr
        lhs = self.visit(ast.lhs, c)
        rhs = self.visit(ast.rhs, c)
        if type(rhs) in [IntType, FloatType, BoolType, StringType, ArrayType]:
            rhs = Symbol('', rhs)
        if type(rhs.mtype) == MType:
            if type(lhs.mtype) == Unknown and type(rhs.mtype.restype) == Unknown:
                raise TypeMismatchInStatement(ast)
            elif type(lhs.mtype) == Unknown and type(rhs.mtype.restype) != Unknown:
                lhs.mtype = rhs.mtype.restype
            elif type(lhs.mtype) != Unknown and type(rhs.mtype.restype) == Unknown:
                rhs.mtype.restype = lhs.mtype
            elif type(lhs.mtype) != type(rhs.mtype.restype):
                raise TypeMismatchInStatement(ast)
        else:
            if type(lhs.mtype) == Unknown and type(rhs.mtype) == Unknown:
                raise TypeMismatchInStatement(ast)
            elif type(lhs.mtype) == Unknown and type(rhs.mtype) != Unknown:
                lhs.mtype = rhs.mtype
            elif type(lhs.mtype) != Unknown and type(rhs.mtype) == Unknown:
                rhs.mtype = lhs.mtype
            elif type(lhs.mtype) != type(rhs.mtype):
                raise TypeMismatchInStatement(ast)


    def visitArrayCell(self,ast,c):
        #arr:Expr
        #idx:List[Expr]
        idx = []
        for idxEle in ast.idx:
            id = self.visit(idxEle, c)
            if type(id) != IntType:
                raise TypeMismatchInExpression(ast)
            else:
                idx.append(id)
        arr = self.visit(ast.arr, c)
        if type(arr.mtype) == MType:
            if type(arr.mtype.restype) != ArrayType:
                raise TypeMismatchInExpression(ast)
            else:
                if len(arr.mtype.restype.dimen) != len(idx):
                    raise TypeMismatchInExpression(ast)
        elif type(arr.mtype) != ArrayType:
            raise TypeMismatchInExpression(ast)
        else:
            if len(arr.mtype.dimen) != len(idx):
                raise TypeMismatchInExpression(ast)
        #return (self.visit(ast.arr, c), idx)
        return arr
    
    def visitBinaryOp(self,ast,c): 
        #op:str
        #left:Expr  # symbol, type can be primitive or MType (function)
        #right:Expr # symbol, type can be primitive or MType (function)
        op = ast.op
        left = self.visit(ast.left, c)
        if type(left) in [IntType, FloatType, BoolType, StringType, ArrayType]:
            left = Symbol('', left)
        right = self.visit(ast.right, c)
        if type(right) in [IntType, FloatType, BoolType, StringType, ArrayType]:
            right = Symbol('', right)
        #op:str
        #left:Expr  # symbol, type can be primitive or MType (function)
        #right:Expr # symbol, type can be primitive or MType (function)

        # return INTEGER TYPE
        if op in ['+', '-', '*', '\\', '%']:
            if type(left.mtype) == MType and type(right.mtype) == MType:
                # both operands are function type
                if type(left.mtype.restype) == Unknown:
                    left.mtype.restype = IntType()
                if type(right.mtype.restype) == Unknown:
                    right.mtype.restype = IntType()
                if type(left.mtype.restype) != type(right.mtype.restype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) == MType and type(right.mtype) != MType:
                # only left is function
                if type(left.mtype.restype) == Unknown:
                    left.mtype.restype = IntType()
                if type(right.mtype) == Unknown:
                    right.mtype = IntType()
                if type(left.mtype.restype) != type(right.mtype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) != MType and type(right.mtype) == MType:
                # only right is function
                if type(left.mtype) == Unknown:
                    left.mtype = IntType()
                if type(right.mtype.restype) == Unknown:
                    right.mtype.restype = IntType()
                if type(left.mtype) != type(right.mtype.restype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) != MType and type(right.mtype) != MType:
                # both are not function
                if type(left.mtype) == Unknown:
                    left.mtype = IntType()
                if type(right.mtype) == Unknown:
                    right.mtype = IntType()
                if type(left.mtype) != type(right.mtype):
                    raise TypeMismatchInExpression(ast)
            return Symbol('', IntType())

        # return FLOAT TYPE
        if op in ['+.', '-.', '*.', '\\.', '%.']:
            if type(left.mtype) == MType and type(right.mtype) == MType:
                # both operands are function type
                if type(left.mtype.restype) == Unknown:
                    left.mtype.restype = FloatType()
                if type(right.mtype.restype) == Unknown:
                    right.mtype.restype = FloatType()
                if type(left.mtype.restype) != type(right.mtype.restype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) == MType and type(right.mtype) != MType:
                # only left is function
                if type(left.mtype.restype) == Unknown:
                    left.mtype.restype = FloatType()
                if type(right.mtype) == Unknown:
                    right.mtype = FloatType()
                if type(left.mtype.restype) != type(right.mtype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) != MType and type(right.mtype) == MType:
                # only right is function
                if type(left.mtype) == Unknown:
                    left.mtype = FloatType()
                if type(right.mtype.restype) == Unknown:
                    right.mtype.restype = FloatType()
                if type(left.mtype) != type(right.mtype.restype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) != MType and type(right.mtype) != MType:
                # both are not function
                if type(left.mtype) == Unknown:
                    left.mtype = FloatType()
                if type(right.mtype) == Unknown:
                    right.mtype = FloatType()
                if type(left.mtype) != type(right.mtype):
                    raise TypeMismatchInExpression(ast)
            return Symbol('', FloatType())

        # return BOOLEAN TYPE, both sides are BOOL
        if op in ['&&', '||']:
            if type(left.mtype) == MType and type(right.mtype) == MType:
                # both operands are function type
                if type(left.mtype.restype) == Unknown:
                    left.mtype.restype = BoolType()
                if type(right.mtype.restype) == Unknown:
                    right.mtype.restype = BoolType()
                if type(left.mtype.restype) != type(right.mtype.restype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) == MType and type(right.mtype) != MType:
                # only left is function
                if type(left.mtype.restype) == Unknown:
                    left.mtype.restype = BoolType()
                if type(right.mtype) == Unknown:
                    right.mtype = BoolType()
                if type(left.mtype.restype) != type(right.mtype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) != MType and type(right.mtype) == MType:
                # only right is function
                if type(left.mtype) == Unknown:
                    left.mtype = BoolType()
                if type(right.mtype.restype) == Unknown:
                    right.mtype.restype = BoolType()
                if type(left.mtype) != type(right.mtype.restype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) != MType and type(right.mtype) != MType:
                # both are not function
                if type(left.mtype) == Unknown:
                    left.mtype = BoolType()
                if type(right.mtype) == Unknown:
                    right.mtype = BoolType()
                if type(left.mtype) != type(right.mtype):
                    raise TypeMismatchInExpression(ast)
            return Symbol('', BoolType())
        
        # return BOOLEAN TYPE, both sides are INTEGER
        if op in ['==', '!=', '<', '>', '<=', '>=']:
            if type(left.mtype) == MType and type(right.mtype) == MType:
                # both operands are function type
                if type(left.mtype.restype) == Unknown:
                    left.mtype.restype = IntType()
                if type(right.mtype.restype) == Unknown:
                    right.mtype.restype = IntType()
                if type(left.mtype.restype) != type(right.mtype.restype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) == MType and type(right.mtype) != MType:
                # only left is function
                if type(left.mtype.restype) == Unknown:
                    left.mtype.restype = IntType()
                if type(right.mtype) == Unknown:
                    right.mtype = IntType()
                if type(left.mtype.restype) != type(right.mtype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) != MType and type(right.mtype) == MType:
                # only right is function
                if type(left.mtype) == Unknown:
                    left.mtype = IntType()
                if type(right.mtype.restype) == Unknown:
                    right.mtype.restype = IntType()
                if type(left.mtype) != type(right.mtype.restype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) != MType and type(right.mtype) != MType:
                # both are not function
                if type(left.mtype) == Unknown:
                    left.mtype = IntType()
                if type(right.mtype) == Unknown:
                    right.mtype = IntType()
                if type(left.mtype) != type(right.mtype):
                    raise TypeMismatchInExpression(ast)
            return Symbol('', BoolType())

        # return BOOLEAN TYPE, both sides are FLOAT
        if op in ['=/=', '<.', '>.', '<=.', '>=.']:
            if type(left.mtype) == MType and type(right.mtype) == MType:
                # both operands are function type
                if type(left.mtype.restype) == Unknown:
                    left.mtype.restype = FloatType()
                if type(right.mtype.restype) == Unknown:
                    right.mtype.restype = FloatType()
                if type(left.mtype.restype) != type(right.mtype.restype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) == MType and type(right.mtype) != MType:
                # only left is function
                if type(left.mtype.restype) == Unknown:
                    left.mtype.restype = FloatType()
                if type(right.mtype) == Unknown:
                    right.mtype = FloatType()
                if type(left.mtype.restype) != type(right.mtype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) != MType and type(right.mtype) == MType:
                # only right is function
                if type(left.mtype) == Unknown:
                    left.mtype = FloatType()
                if type(right.mtype.restype) == Unknown:
                    right.mtype.restype = FloatType()
                if type(left.mtype) != type(right.mtype.restype):
                    raise TypeMismatchInExpression(ast)
            elif type(left.mtype) != MType and type(right.mtype) != MType:
                # both are not function
                if type(left.mtype) == Unknown:
                    left.mtype = FloatType()
                if type(right.mtype) == Unknown:
                    right.mtype = FloatType()
                if type(left.mtype) != type(right.mtype):
                    raise TypeMismatchInExpression(ast)
            return Symbol('', BoolType())
                    

    def visitUnaryOp(self,ast,c):
        op = ast.op
        expr = self.visit(ast.body, c)
        if type(expr) in [IntType, FloatType, BoolType, StringType, ArrayType]:
            expr = Symbol('', expr)
        # return INTEGER
        if op in ['-']:
            if type(expr.mtype) == MType:
                if type(expr.mtype.restype) == Unknown:
                    expr.mtype.restype = IntType()
                elif type(expr.mtype.restype) != IntType:
                    raise TypeMismatchInExpression(ast)
            else:
                if type(expr.mtype) == Unknown:
                    expr.mtype = IntType()
                elif type(expr.mtype) != IntType:
                    raise TypeMismatchInExpression(ast)
            return Symbol('', IntType())

        # return FLOAT
        if op in ['-.']:
            if type(expr.mtype) == MType:
                if type(expr.mtype.restype) == Unknown:
                    expr.mtype.restype = FloatType()
                elif type(expr.mtype.restype) != FloatType:
                    raise TypeMismatchInExpression(ast)
            else:
                if type(expr.mtype) == Unknown:
                    expr.mtype = FloatType()
                elif type(expr.mtype) != FloatType:
                    raise TypeMismatchInExpression(ast)
            return Symbol('', FloatType())
        
        # return BOOLEAN
        if op in ['!']:
            if type(expr.mtype) == MType:
                if type(expr.mtype.restype) == Unknown:
                    expr.mtype.restype = BoolType()
                elif type(expr.mtype.restype) != BoolType:
                    raise TypeMismatchInExpression(ast)
            else:
                if type(expr.mtype) == Unknown:
                    expr.mtype = BoolType()
                elif type(expr.mtype) != BoolType:
                    raise TypeMismatchInExpression(ast)
            return Symbol('', BoolType())   
    
    def visitCallExpr(self,ast,c):
        #method:Id
        #param:List[Expr]
        try:
            self.visit(ast.method, c)
        except:
            raise Undeclared(Function(), ast.method.name)
        fDecl = self.visit(ast.method, c)
        args = [self.visit(x, c) for x in ast.param]
        params = fDecl.mtype.intype
        if len(args) != len(params):
            raise TypeMismatchInExpression(ast)
        for i in range(len(params)):
            if type(args[i]) == Unknown:
                raise TypeMismatchInExpression(ast)
            if type(params[i]) == Unknown:
                params[i] = args[i]
                break
            if type(args[i]) != type(params[i]):
                raise TypeMismatchInExpression(ast)
        return Symbol('', fDecl.mtype.restype)

    def visitCallStmt(self,ast,c):
        #method:Id
        #param:List[Expr]
        try:
            self.visit(ast.method, c)
        except:
            raise Undeclared(Function(), ast.method.name)
        fDecl = self.visit(ast.method, c)
        args = [self.visit(x, c) for x in ast.param]
        params = fDecl.mtype.intype
        if len(args) != len(params):
            raise TypeMismatchInStatement(ast)
        for i in range(len(params)):
            if type(args[i]) == Unknown:
                raise TypeMismatchInStatement(ast)
            if type(params[i]) == Unknown:
                params[i] = args[i]
                break
            if type(args[i]) != type(params[i]):
                raise TypeMismatchInStatement(ast)
        if type(fDecl.mtype.restype) == Unknown:
            fDecl.mtype.restype = VoidType
        else:
            if type(fDecl.mtype.restype) != VoidType:
                raise TypeMismatchInStatement(ast)
    

## I don't know what I'm to say but say it anyways ~~
    
    def visitBreak(self,ast,c): pass
    
    def visitContinue(self,ast,c): pass

    def visitReturn(self,ast,c):
        #expr:Expr # None if no expression
        pass

    def visitId(self,ast,c):
        for decls in c:
            for decl in decls:
                if ast.name == decl.name:
                    return decl
        raise Undeclared(Identifier(), ast.name)

## Check Literals

    def visitIntLiteral(self,ast,c):
        return IntType()
    
    def visitFloatLiteral(self,ast,c):
        return FloatType()
    
    def visitStringLiteral(self,ast,c):
        return StringType()
    
    def visitBooleanLiteral(self,ast,c):
        return BoolType()
    
    def visitArrayLiteral(self,ast,c):
        #value:List[Literal]
        if len(ast.value) == 0:
            return Unknown()
        literal = ast.value[0]
        retType = self.visit(literal, c)
        if type(retType) in [IntType, FloatType, BoolType, StringType, Unknown]:
            return retType
        while type(retType) not in [IntType, FloatType, BoolType, StringType, Unknown]:
            retType = self.visit(literal.value[0])
        return retType

    