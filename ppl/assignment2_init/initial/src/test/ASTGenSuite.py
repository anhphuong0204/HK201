import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x=5;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_variable_decla1(self):
        """Simple program: int main() {} """
        input = """Var:x[10][20]=5;"""
        expect = Program([VarDecl(Id("x"),[10,20],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_variable_decla2(self):
        """Simple program: int main() {} """
        input = """Var:x[10][20]=5, a={1,2};"""
        expect = Program([
            VarDecl(Id("x"),[10,20],IntLiteral(5)),
            VarDecl(Id("a"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_variable_decla3(self):
        """Simple program: int main() {} """
        input = """Var:a={{1,2},{3,4}};"""
        expect = Program([VarDecl(Id("a"),[],
        ArrayLiteral([
            ArrayLiteral([IntLiteral(1),IntLiteral(2)]),
            ArrayLiteral([IntLiteral(3),IntLiteral(4)])
        ])
        )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_variable_decla4(self):
        """Simple program: int main() {} """
        input = """Var:a={1,2};"""
        expect = Program([VarDecl(Id("a"),[],
        ArrayLiteral([
            IntLiteral(1),
            IntLiteral(2)
        ])
        )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_variable_decla5(self):
        """Simple program: int main() {} """
        input = """Var:a[10][20][30][40]={{5.4,7.8},{5.5},{5.6,5.7,5.8},{9.0}};"""
        expect = Program([VarDecl(Id("a"),[10,20,30,40],
        ArrayLiteral([
            ArrayLiteral([FloatLiteral(5.4),FloatLiteral(7.8)]),
            ArrayLiteral([FloatLiteral(5.5)]),
            ArrayLiteral([FloatLiteral(5.6),FloatLiteral(5.7),FloatLiteral(5.8)]),
            ArrayLiteral([FloatLiteral(9.0)])
        ])
        )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_multi_var_decl1(self):
        """Simple program: int main() {} """
        input = """Var:x="abc"; Var:y=True;"""
        expect = Program([
            VarDecl(Id("x"),[],StringLiteral("abc")),
            VarDecl(Id("y"),[],BooleanLiteral(True))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    def test_multi_var_decl2(self):
        """Simple program: int main() {} """
        input = """Var:x="abc"; Var:z[10]=5.4,y=True;"""
        expect = Program([
            VarDecl(Id("x"),[],StringLiteral("abc")),
            VarDecl(Id("z"),[10],FloatLiteral(5.4)),
            VarDecl(Id("y"),[],BooleanLiteral(True))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_simple_function1(self):
        """Simple program: int main() {} """
        input = """Var:x=5;
                    Function: ma
                    Parameter: n, k, ff
                    Body:
                    Var:x=5;
                    x = 10;
                    EndBody."""
        expect = Program([
                VarDecl(Id("x"),[],IntLiteral(5)),
                FuncDecl(
                    Id("ma"),
                    [Id("n"),Id("k"),Id("ff")],
                    (
                        [VarDecl(Id("x"),[],IntLiteral(5))],
                        [Assign(Id("x"),IntLiteral(10))]
                    )
                )
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_function2(self):
        """Simple program: int main() {} """
        input = """Function: f
                    Body:
                        If n == 0 Then
                            Return 1;
                        ElseIf n > 6 Then
                            Break;
                        EndIf.
                    EndBody.
                    """
        expect = Program([
            FuncDecl(
                Id("f"),
                [],
                (
                    [],
                    [
                        If(
                            [
                                (
                                    BinaryOp("==", Id("n"), IntLiteral(0)),
                                    [],
                                    [Return(IntLiteral(1))]
                                ),
                                (
                                    BinaryOp(">", Id("n"), IntLiteral(6)),
                                    [],
                                    [Break()]
                                )
                            ],
                            ([],[])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_function3(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_function4(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                Parameter: n
                Body:
                    While n > 3 Do
                        n = n + 1;
                        Continue;
                        Break;
                    EndWhile.

                    Do n = n * 8 - 7;
                    While n * 6 < 9
                    EndDo.

                    For (i = 1, i < i + 1, i < 8) Do
                        Var: k;
                        k = k + 1;
                    EndFor.
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"),
                [Id("n")],
                (
                    [],
                    [
                        While(
                            BinaryOp(">", Id("n"), IntLiteral(3)), 
                            (
                                [],
                                [
                                    Assign(Id("n"), BinaryOp("+", Id("n"), IntLiteral(1))),
                                    Continue(),
                                    Break()
                                ]
                            )
                        ),
                        Dowhile(
                            (
                                [],
                                [
                                    Assign(Id("n"), BinaryOp("-", BinaryOp("*", Id("n"), IntLiteral(8)), IntLiteral(7)))
                                ]
                            ),
                            BinaryOp("<", BinaryOp("*", Id("n"), IntLiteral(6)), IntLiteral(9))
                        ),
                        For(
                            Id("i"),
                            IntLiteral(1),
                            BinaryOp("<", Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                            BinaryOp("<", Id("i"), IntLiteral(8)),
                            (
                                [VarDecl(Id("k"), [], None)],
                                [Assign(Id("k"), BinaryOp("+", Id("k"), IntLiteral(1)))]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_function5(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_function13(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_function14(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_function15(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_function16(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_function17(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_function18(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_function19(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_function20(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_function21(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_function22(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_function23(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_function24(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_function25(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_function26(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_function27(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_function28(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_function29(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_function30(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_function31(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_function32(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_function33(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_function34(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_function35(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_function36(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_function37(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_function38(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_function39(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_function40(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_function41(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_function42(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_function43(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_function44(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_function45(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_function46(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_function47(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_function48(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_function49(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_function50(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_function51(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_function52(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_function53(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_function54(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_function55(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_function56(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_function57(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_function58(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_function59(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_function60(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_function61(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_function62(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_function63(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_function64(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_function65(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_function66(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_function67(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_function68(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_function69(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_function70(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_function71(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_function72(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_function73(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_function74(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_function75(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_function76(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_function77(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_function78(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_function79(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_function80(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_function81(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_function82(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_function83(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_function84(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_function85(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_function86(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_functio87(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_function88(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_function89(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_function90(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_function91(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_function92(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_function93(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_function94(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_function95(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_function96(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_function97(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_function98(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    
    def test_function99(self):
        """Simple program: int main() {} """
        input = """
                Function: kak
                Parameter: n, k10n_123
                Body:
                    Var: j = 10, a[1][0] = {{1,2}, {2,3}};
                    k = "abc" + "def";
                    print(k);
                    Return "abc";
                    a[1 + 3][k + 9 + j] = 6;
                    **cmt**
                EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("kak"),
                [Id("n"), Id("k10n_123")],
                (
                    [
                        VarDecl(Id("j"), [], IntLiteral(10)),
                        VarDecl(Id("a"), [1, 0], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(2), IntLiteral(3)])]))
                    ],
                    [
                        Assign(Id("k"), BinaryOp("+", StringLiteral("abc"), StringLiteral("def"))),
                        CallStmt(Id("print"), [Id("k")]),
                        Return(StringLiteral("abc")),
                        Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", BinaryOp("+", Id("k"), IntLiteral(9)), Id("j"))]), IntLiteral(6))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))