import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test00(self):
        input = Program([
            VarDecl(Id('x'), [], None),
            VarDecl(Id('y'), [], None),
            VarDecl(Id('x'), [], None)
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test01(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],
                ([],[])
            )
        ])
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test02(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],[])
            )
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test03(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None)],[])
            ),
            FuncDecl(
                Id('func'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 'func'))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test04(self):
        input = Program([
            VarDecl(Id('x'), [], IntLiteral(3)),
            VarDecl(Id('y'), [], FloatLiteral(1.3)),
            VarDecl(Id('z'), [], StringLiteral('abc')),
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
        ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,404))

    def test05(self):
        input = Program([
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('t'), [], IntLiteral(3))
        ])
        expect = str(Redeclared(Variable(), 't'))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test06(self):
        input = Program([
            VarDecl(Id('t'), [], IntLiteral(3)),
            FuncDecl(
                Id('t'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 't'))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test07(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), Id('b'))
                ])
            )
        ])
        expect = str(Undeclared(Identifier(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,407))    
    
    def test08(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,408))    

    def test09(self):
        input = Program([
            VarDecl(Id('a'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%.', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%.', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,409))     

#1
    def test10(self):
        input = Program([
            VarDecl(Id('x'), [], None),
            VarDecl(Id('y'), [], None),
            VarDecl(Id('x'), [], None)
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test11(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],
                ([],[])
            )
        ])
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test12(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],[])
            )
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test13(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None)],[])
            ),
            FuncDecl(
                Id('func'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 'func'))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test14(self):
        input = Program([
            VarDecl(Id('x'), [], IntLiteral(3)),
            VarDecl(Id('y'), [], FloatLiteral(1.3)),
            VarDecl(Id('z'), [], StringLiteral('abc')),
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
        ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,414))

    def test15(self):
        input = Program([
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('t'), [], IntLiteral(3))
        ])
        expect = str(Redeclared(Variable(), 't'))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test16(self):
        input = Program([
            VarDecl(Id('t'), [], IntLiteral(3)),
            FuncDecl(
                Id('t'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 't'))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test17(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), Id('b'))
                ])
            )
        ])
        expect = str(Undeclared(Identifier(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,417))    
    
    def test18(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,418))    

    def test19(self):
        input = Program([
            VarDecl(Id('a'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%.', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%.', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,419))       

#2
    def test20(self):
        input = Program([
            VarDecl(Id('x'), [], None),
            VarDecl(Id('y'), [], None),
            VarDecl(Id('x'), [], None)
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test21(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],
                ([],[])
            )
        ])
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test22(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],[])
            )
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test23(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None)],[])
            ),
            FuncDecl(
                Id('func'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 'func'))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test24(self):
        input = Program([
            VarDecl(Id('x'), [], IntLiteral(3)),
            VarDecl(Id('y'), [], FloatLiteral(1.3)),
            VarDecl(Id('z'), [], StringLiteral('abc')),
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
        ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,424))

    def test25(self):
        input = Program([
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('t'), [], IntLiteral(3))
        ])
        expect = str(Redeclared(Variable(), 't'))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test26(self):
        input = Program([
            VarDecl(Id('t'), [], IntLiteral(3)),
            FuncDecl(
                Id('t'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 't'))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test27(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), Id('b'))
                ])
            )
        ])
        expect = str(Undeclared(Identifier(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,427))    
    
    def test28(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,428))    

    def test29(self):
        input = Program([
            VarDecl(Id('a'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%.', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%.', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,429))       

#3
    def test30(self):
        input = Program([
            VarDecl(Id('x'), [], None),
            VarDecl(Id('y'), [], None),
            VarDecl(Id('x'), [], None)
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,430))
    
    def test31(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],
                ([],[])
            )
        ])
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test32(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],[])
            )
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test33(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None)],[])
            ),
            FuncDecl(
                Id('func'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 'func'))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test34(self):
        input = Program([
            VarDecl(Id('x'), [], IntLiteral(3)),
            VarDecl(Id('y'), [], FloatLiteral(1.3)),
            VarDecl(Id('z'), [], StringLiteral('abc')),
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
        ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,434))

    def test35(self):
        input = Program([
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('t'), [], IntLiteral(3))
        ])
        expect = str(Redeclared(Variable(), 't'))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test36(self):
        input = Program([
            VarDecl(Id('t'), [], IntLiteral(3)),
            FuncDecl(
                Id('t'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 't'))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test37(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), Id('b'))
                ])
            )
        ])
        expect = str(Undeclared(Identifier(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,437))    
    
    def test38(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,438))    

    def test39(self):
        input = Program([
            VarDecl(Id('a'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%.', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%.', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,439))       
#4
    def test40(self):
        input = Program([
            VarDecl(Id('x'), [], None),
            VarDecl(Id('y'), [], None),
            VarDecl(Id('x'), [], None)
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test41(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],
                ([],[])
            )
        ])
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test42(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],[])
            )
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,442))

    def test43(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None)],[])
            ),
            FuncDecl(
                Id('func'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 'func'))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test44(self):
        input = Program([
            VarDecl(Id('x'), [], IntLiteral(3)),
            VarDecl(Id('y'), [], FloatLiteral(1.3)),
            VarDecl(Id('z'), [], StringLiteral('abc')),
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
        ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,444))

    def test45(self):
        input = Program([
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('t'), [], IntLiteral(3))
        ])
        expect = str(Redeclared(Variable(), 't'))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test46(self):
        input = Program([
            VarDecl(Id('t'), [], IntLiteral(3)),
            FuncDecl(
                Id('t'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 't'))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test47(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), Id('b'))
                ])
            )
        ])
        expect = str(Undeclared(Identifier(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,447))    
    
    def test48(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,448))    

    def test49(self):
        input = Program([
            VarDecl(Id('a'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%.', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%.', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,449))       

#5
    def test50(self):
        input = Program([
            VarDecl(Id('x'), [], None),
            VarDecl(Id('y'), [], None),
            VarDecl(Id('x'), [], None)
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,450))
    
    def test51(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],
                ([],[])
            )
        ])
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test52(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],[])
            )
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,452))

    def test53(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None)],[])
            ),
            FuncDecl(
                Id('func'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 'func'))
        self.assertTrue(TestChecker.test(input,expect,453))

    def test54(self):
        input = Program([
            VarDecl(Id('x'), [], IntLiteral(3)),
            VarDecl(Id('y'), [], FloatLiteral(1.3)),
            VarDecl(Id('z'), [], StringLiteral('abc')),
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
        ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,454))

    def test55(self):
        input = Program([
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('t'), [], IntLiteral(3))
        ])
        expect = str(Redeclared(Variable(), 't'))
        self.assertTrue(TestChecker.test(input,expect,455))

    def test56(self):
        input = Program([
            VarDecl(Id('t'), [], IntLiteral(3)),
            FuncDecl(
                Id('t'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 't'))
        self.assertTrue(TestChecker.test(input,expect,456))

    def test57(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), Id('b'))
                ])
            )
        ])
        expect = str(Undeclared(Identifier(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,457))    
    
    def test58(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,458))    

    def test59(self):
        input = Program([
            VarDecl(Id('a'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%.', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%.', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,459))       

#6
    def test60(self):
        input = Program([
            VarDecl(Id('x'), [], None),
            VarDecl(Id('y'), [], None),
            VarDecl(Id('x'), [], None)
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,460))
    
    def test61(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],
                ([],[])
            )
        ])
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test62(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],[])
            )
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,462))

    def test63(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None)],[])
            ),
            FuncDecl(
                Id('func'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 'func'))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test64(self):
        input = Program([
            VarDecl(Id('x'), [], IntLiteral(3)),
            VarDecl(Id('y'), [], FloatLiteral(1.3)),
            VarDecl(Id('z'), [], StringLiteral('abc')),
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
        ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,464))

    def test65(self):
        input = Program([
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('t'), [], IntLiteral(3))
        ])
        expect = str(Redeclared(Variable(), 't'))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test66(self):
        input = Program([
            VarDecl(Id('t'), [], IntLiteral(3)),
            FuncDecl(
                Id('t'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 't'))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test67(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), Id('b'))
                ])
            )
        ])
        expect = str(Undeclared(Identifier(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,467))    
    
    def test68(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,468))    

    def test69(self):
        input = Program([
            VarDecl(Id('a'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%.', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%.', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,469))       

#7
    def test70(self):
        input = Program([
            VarDecl(Id('x'), [], None),
            VarDecl(Id('y'), [], None),
            VarDecl(Id('x'), [], None)
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,470))
    
    def test71(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],
                ([],[])
            )
        ])
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,471))
    
    def test72(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],[])
            )
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test73(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None)],[])
            ),
            FuncDecl(
                Id('func'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 'func'))
        self.assertTrue(TestChecker.test(input,expect,473))

    def test74(self):
        input = Program([
            VarDecl(Id('x'), [], IntLiteral(3)),
            VarDecl(Id('y'), [], FloatLiteral(1.3)),
            VarDecl(Id('z'), [], StringLiteral('abc')),
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
        ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,474))

    def test75(self):
        input = Program([
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('t'), [], IntLiteral(3))
        ])
        expect = str(Redeclared(Variable(), 't'))
        self.assertTrue(TestChecker.test(input,expect,475))

    def test76(self):
        input = Program([
            VarDecl(Id('t'), [], IntLiteral(3)),
            FuncDecl(
                Id('t'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 't'))
        self.assertTrue(TestChecker.test(input,expect,476))

    def test77(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), Id('b'))
                ])
            )
        ])
        expect = str(Undeclared(Identifier(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,477))    
    
    def test78(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,478))    

    def test79(self):
        input = Program([
            VarDecl(Id('a'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%.', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%.', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,479))       

#8
    def test80(self):
        input = Program([
            VarDecl(Id('x'), [], None),
            VarDecl(Id('y'), [], None),
            VarDecl(Id('x'), [], None)
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,480))
    
    def test81(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],
                ([],[])
            )
        ])
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test82(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],[])
            )
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,482))

    def test83(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None)],[])
            ),
            FuncDecl(
                Id('func'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 'func'))
        self.assertTrue(TestChecker.test(input,expect,483))

    def test84(self):
        input = Program([
            VarDecl(Id('x'), [], IntLiteral(3)),
            VarDecl(Id('y'), [], FloatLiteral(1.3)),
            VarDecl(Id('z'), [], StringLiteral('abc')),
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
        ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,484))

    def test85(self):
        input = Program([
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('t'), [], IntLiteral(3))
        ])
        expect = str(Redeclared(Variable(), 't'))
        self.assertTrue(TestChecker.test(input,expect,485))

    def test86(self):
        input = Program([
            VarDecl(Id('t'), [], IntLiteral(3)),
            FuncDecl(
                Id('t'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 't'))
        self.assertTrue(TestChecker.test(input,expect,486))

    def test87(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), Id('b'))
                ])
            )
        ])
        expect = str(Undeclared(Identifier(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,487))    
    
    def test88(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,488))    

    def test89(self):
        input = Program([
            VarDecl(Id('a'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%.', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%.', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,489))       

#9
    def test90(self):
        input = Program([
            VarDecl(Id('x'), [], None),
            VarDecl(Id('y'), [], None),
            VarDecl(Id('x'), [], None)
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test91(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],
                ([],[])
            )
        ])
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,491))
    
    def test92(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None),
                VarDecl(Id('x'), [], None)],[])
            )
        ])
        expect = str(Redeclared(Variable(), 'x'))
        self.assertTrue(TestChecker.test(input,expect,492))

    def test93(self):
        input = Program([
            FuncDecl(
                Id('func'),
                [],
                ([VarDecl(Id('x'), [], None),
                VarDecl(Id('y'), [], None)],[])
            ),
            FuncDecl(
                Id('func'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 'func'))
        self.assertTrue(TestChecker.test(input,expect,493))

    def test94(self):
        input = Program([
            VarDecl(Id('x'), [], IntLiteral(3)),
            VarDecl(Id('y'), [], FloatLiteral(1.3)),
            VarDecl(Id('z'), [], StringLiteral('abc')),
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))
        ])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,494))

    def test95(self):
        input = Program([
            VarDecl(Id('t'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('t'), [], IntLiteral(3))
        ])
        expect = str(Redeclared(Variable(), 't'))
        self.assertTrue(TestChecker.test(input,expect,495))

    def test96(self):
        input = Program([
            VarDecl(Id('t'), [], IntLiteral(3)),
            FuncDecl(
                Id('t'),
                [],
                ([], [])
            )
        ])
        expect = str(Redeclared(Function(), 't'))
        self.assertTrue(TestChecker.test(input,expect,496))

    def test97(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), Id('b'))
                ])
            )
        ])
        expect = str(Undeclared(Identifier(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,497))    
    
    def test98(self):
        input = Program([
            VarDecl(Id('a'), [], IntLiteral(3)),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,498))    

    def test99(self):
        input = Program([
            VarDecl(Id('a'), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])),
            VarDecl(Id('b'), [], IntLiteral(5)),
            FuncDecl(
                Id('fooleanse'),
                [],
                ([], [
                    Assign(Id('a'), BinaryOp('%.', FloatLiteral(6), Id('b')))
                ])
            )
        ])
        expect = str(TypeMismatchInExpression(BinaryOp('%.', FloatLiteral(6), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,499))         
    