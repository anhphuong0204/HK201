import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test3(self):
        input = """Function: fact
    Parameter: n 
    Body: 
        If n == 0 Then 
            Return 1; 
        Else  
            Return n * fact (n - 1);  
        EndIf. 
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test4(self):
        input = """Var: x, d = 9, o , a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test5(self):
        input = """Var: x = {1, 2, 3, 4, 5};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test6(self):
        input = """Var: x = "this is a string";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
        
    def test7(self):
        input = """Var: x = 0O123, d, e;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
        
    def test8(self):
        input = """Var: e = 12e3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
        
    def test9(self):
        input = """Var: x = 123;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
        
    def test10(self):
        input = """Var: x = 0X123, y = 0x123;"""
        expect = "Error on line 1 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test11(self):
        input = """Var: bad_d, ddfs;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    
    def test12(self):
        input = """Var: x = 0O123;
        Var: y = 0o123;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    
    def test13(self):
        input = """Var: x = "this is unclosed string;"""
        expect = "this is unclosed string;"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    
    def test14(self):
        input = """Var: x = 0e3; **this is a comment**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    
    def test15(self):
        input = """Var: x = "this is a string contain \\t";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    
    def test16(self):
        input = """Var: x = "this is illegal escape \\h";"""
        expect = "this is illegal escape \\h"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    
    def test17(self):
        input = """Var: x = "this is '"string'" having '"";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    
    def test18(self):
        input = """Var: x = y = 0x123;"""
        expect = "Error on line 1 col 11: ="
        self.assertTrue(TestParser.checkParser(input,expect,218))
    
    def test19(self):
        input = """Var x = 0X123, y = 0x123;"""
        expect = "Error on line 1 col 4: x"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    
    def test20(self):
        input = """Var: x, 0X123, y = 0x123;"""
        expect = "Error on line 1 col 8: 0X123"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    
    def test21(self):
        input = """Var: x, y = 0x123"""
        expect = "Error on line 1 col 17: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    
    def test22(self):
        input = """var: x, y = 0x123;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    
    def test23(self):
        input = """Var: x, y = 0x123;
        Var a, b,c;"""
        expect = "Error on line 2 col 12: a"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    
    def test24(self):
        input = """Var: x; **this is unclosed comment** """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    
    def test25(self):
        input = """Var: x = a + b - 9;"""
        expect = "Error on line 1 col 11: +"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    
    def test26(self):
        input = """Var: xyz = 12.e-3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    
    def test27(self):
        input = """Var: array = { {1, 2, 3}, {4, 5, 6} };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    
    def test28(self):
        input = """Var: x1, x2, x3X = 123;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    
    def test29(self):
        input = """Var: x_1, x_2, x_X_3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    
    def test30(self):
        input = """Var: x, x_X-123;"""
        expect = "Error on line 1 col 11: -"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test31(self):
        input = """Function: fact
        Parameter: n
        Body:
        If n==0 Then Return 0;
        Else Return 1;
        EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test32(self):
        input = """Function fact
        Parameter: n
        Body:
        If n==0 Then Return 0;
        Else Return 1;
        EndIf.
        EndBody."""
        expect = "Error on line 1 col 9: fact"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test33(self):
        input = """Function: fact
        Parameter: n
        Body:
        If n==0 Then Return 0;
        Else Return 1;
        EndIf.
        EndBody"""
        expect = "Error on line 7 col 15: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test34(self):
        input = """Function: fact
        
        Body:
        If True Then Return 0;
        Else Return 1;
        EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test35(self):
        input = """Function: fact
        Parameter: n
        Body:
        If  Then Return 0;
        Else Return 1;
        EndIf.
        EndBody."""
        expect = "Error on line 4 col 12: Then"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test36(self):
        input = """Function: fact
        Parameter: n
        Body:
        If n==0 Then Return 0;
        Else Return 1
        EndIf.
        EndBody."""
        expect = "Error on line 6 col 8: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test37(self):
        input = """Function: fact
        Parameter: n
        Body:
        If n==0 Then Return 0;
        Else Return 1;
        
        EndBody."""
        expect = "Error on line 7 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test38(self):
        input = """Function: fact
        Parameter: n
        
        If n==0 Then Return 0;
        Else Return 1;
        EndIf.
        """
        expect = "Error on line 4 col 8: If"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test39(self):
        input = """Function: fact
        Parameter: n
        Body:
        If n==0 Then Return 0;
        ElseIf n == 2 Then Return 2;
        Else Return 1;
        EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test40(self):
        input = """Function: fact
        Parameter: n
        Body:
        If n==0 Then Return 0;
        ElseIf n==10 Then Return 10;
        
        EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test41(self):
        input = """Function: fact
        Parameter: n
        Body:
        For (n = 1, n < 10, 1) Do
            n = n + 1;
            n = 10 + 5 * 12;
        EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test42(self):
        input = """Function: fact
        Parameter: n
        Body:
        For (n = 1, n < 10) Do
            n = n + 1;
            n = 10 + 5 * 12;
        EndFor.
        EndBody."""
        expect = "Error on line 4 col 26: )"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test43(self):
        input = """Function: fact
        Parameter: n
        Body:
        For (n == 1, n < 10, 1) Do
            n = n + 1;
            n = 10 + 5 * 12;
        EndFor.
        EndBody."""
        expect = "Error on line 4 col 15: =="
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test44(self):
        input = """Function: fact
        Parameter: n
        Body:
        For (n = 1, n < 10, 1) 
            n = n + 1;
            n = 10 + 5 * 12;
        EndFor.
        EndBody."""
        expect = "Error on line 5 col 12: n"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test45(self):
        input = """Function: fact
        Parameter: n
        Body:
        For (n = 1, n < 10, 1) Do
            n = n + 1;
            n = 10 + 5 * 12;
        
        EndBody."""
        expect = "Error on line 8 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test46(self):
        input = """Function: fact
        Parameter: n
        Body:
        For (n = 1, n < 10, 1) Do
            n = n + 1;
            n = 10 + 5 * 12;
        EndFor
        EndBody."""
        expect = "Error on line 8 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test47(self):
        input = """Function: fact
        Parameter: n
        Body:
        For n = 1, n < 10, 1 Do
            n = n + 1;
            n = 10 + 5 * 12;
        EndFor.
        EndBody."""
        expect = "Error on line 4 col 12: n"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test48(self):
        input = """Function: fact
        Parameter: n
        Body:
        For (n = 1, n <= 10, 1) Do
            n = n + 1;
            n = 10 + 5 * 12;
        EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test49(self):
        input = """Function: fact
        Parameter: n, k, d_g
        Body:
        For (n = 1, n < 10, 10e3) Do
            n = n + 1;
            n = 10 + 5 * 12;
        EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test50(self):
        input = """Function: fact
        Parameter: n
        Body:
        For (n = 1, n < 10, 1) Do
            Var: v;
            v = n;
            n = n + 1;
            v = 10 + 5 * 12;
        EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test51(self):
        input = """Function: fact
        Parameter: n
        Body:
        While n == 10 Do
            n = n + 10;
            Var: v = 9;
            n = n + v;
        EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test52(self):
        input = """Function: fact
        Parameter: n
        Body:
        While n == 10 Do
            n = n + 10;
            var: v = 9;
            n = n + v;
        EndWhile.
        EndBody."""
        expect = "Error on line 6 col 15: :"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test53(self):
        input = """Function: fact
        Parameter: n
        Body:
        While n == 10 Do
            n = n + 10;
            Var: v = 9;
        EndBody."""
        expect = "Error on line 7 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test54(self):
        input = """Function: fact
        Parameter: n
        Body:
        While n == 10 Do
            n = n + 10;
        EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test55(self):
        input = """Function: fact
        Parameter: n
        Body:
        While n == 10
            n = n + 10;
            Var: v = 9;
            n = n + v;
        EndWhile.
        EndBody."""
        expect = "Error on line 5 col 12: n"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test56(self):
        input = """Function: fact
        Parameter: n
        Body:
        While n == 10 Do
            n = n + 10;
            Var: v = 9;
            n = n + v;
        
        EndBody."""
        expect = "Error on line 9 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test57(self):
        input = """Function: fact
        Parameter: n
        Body:
        While (n == 10) Do
            n = n + 10;
            Var: v = 9;
            n = n + v;
        EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test58(self):
        input = """Function: fact
        Parameter: n
        Body:
        While Do
            n = n + 10;
            Var: v = 9;
            n = n + v;
        EndWhile.
        EndBody."""
        expect = "Error on line 4 col 14: Do"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test59(self):
        input = """Function: fact
        Parameter: n
        Body:
        While False Do
            n = n + 10;
            Var: v = 9;
            n = n + v;
        EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test60(self):
        input = """Function: fact
        Parameter: n
        Body:
        While n == 10 Do
            
        EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test61(self):
        input = """Function: fact
        Parameter: n
        Body:
        Do
            n = n + 10;
            Var: v, e, m;
            v = n + m * e - v;
        While n < 100
        EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test62(self):
        input = """Function: fact
        Parameter: n
        Body:
        Do
            n = n + 10;
            Var: v, e, m;
            v = n + m * e - v;
        While n < 100;
        EndDo.
        EndBody."""
        expect = "Error on line 8 col 21: ;"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test63(self):
        input = """Function: fact
        Parameter: n
        Body:
        
            n = n + 10;
            Var: v, e, m;
            v = n + m * e - v;
        While n < 100
        EndDo.
        EndBody."""
        expect = "Error on line 9 col 8: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test64(self):
        input = """Function: fact
        Parameter: n
        Body:
        Do
            n = n + 10;
            Var: v, e, m;
            v = n + m * e - v;
        n < 100
        EndDo.
        EndBody."""
        expect = "Error on line 8 col 10: <"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test65(self):
        input = """Function: fact
        Parameter: n
        Body:
        Do
            n = n + 10;
            Var: v, e, m;
            v = n + m * e - v;
        While n < 100
        
        EndBody."""
        expect = "Error on line 10 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test66(self):
        input = """Function: fact
        Parameter: n
        Body:
        Do
            n = n + 10;
            Var: v, e, m;
            v = n + m * e - v;
        While True
        EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test67(self):
        input = """Function: fact
        Parameter: n
        Body:
        Do
            n = n + 10;
            Var: v, e, m;
            v = n + m * e - v;
        While 
        EndDo.
        EndBody."""
        expect = "Error on line 9 col 8: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test68(self):
        input = """Function: fact
        Parameter: n
        Body:
        Do
            n = n + 10;
        While n < 100
        EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test69(self):
        input = """Function: fact
        Parameter: n
        Body:
        Do:
            n = n + 10;
            Var: v, e, m;
            v = n + m * e - v;
        While n < 100
        EndDo.
        EndBody."""
        expect = "Error on line 4 col 10: :"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test70(self):
        input = """Function: fact
        Parameter: n
        Body:
        Do
            
        While n < 100
        EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test71(self):
        input = """Function: fact
        Parameter: n
        Body:
            Return;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test72(self):
        input = """Function: fact
        Parameter: n
        Body:
            Continue;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test73(self):
        input = """Function: fact
        Parameter: n
        Body:
            Break;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test74(self):
        input = """Function: fact
        Parameter: n
        Body:
            foo();
            foo(2 + n, 4 \\ n);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test75(self):
        input = """Function: fact
        Parameter: n
        Body:
            Return fact(n + 1);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test76(self):
        input = """Function: fact
        Parameter: n
        Body:
            If n == 0 Then
                Return fact(10);
            EndIf;
        EndBody."""
        expect = "Error on line 6 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test77(self):
        input = """Function: fact
        Parameter: n
        Body:
            If n == 0 Then
                Continue;
            Else
                Return n + 10;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test78(self):
        input = """Function: fact
        Parameter: n
        Body:
            Do
                n = n + 10;
                Break;
            While n < 100
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test79(self):
        input = """Function: fact
        Parameter: n
        Body:
            Do
                n = n + 10;
                Return n;
            While n < 100
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test80(self):
        input = """Function: fact
        Parameter: n
        Body:
            Continue;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test81(self):
        input = """Function: fact
        Parameter: n
        Body:
            While n == 10 Do
                If n == 11 Then 
                    Break;
                Else
                    Return 10;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test82(self):
        input = """Function: fact
        Parameter: n
        Body:
            While n == 10 Do
                If n == 11 Then 
                    Break;
                Else
                    Continue;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test83(self):
        input = """Function: fact
        Parameter: n
        Body:
            While n == 10 Do
                If n == 11 Then 
                    Break;
                Else
                    Return fact(n + 1);
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test84(self):
        input = """Function: fact
        Parameter: n
        Body:
            While n == 10 Do
                If n == 11 Then 
                    Return 11;
                Else
                    Return 10;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test85(self):
        input = """Function: fact
        Parameter: n
        Body:
            While n == 10 Do
                If n == 11 Then 
                    foo();
                    Break;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test86(self):
        input = """Function: fact
        Parameter: n
        Body:
            While n == 10 Do
                If n == 11 Then 
                    Break;
                Else
                    printLn();
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test87(self):
        input = """Function: fact
        Parameter: n
        Body:
            While n == 10 Do
                If n == 11 Then 
                    read();
                Else
                    Return 10;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test88(self):
        input = """Function: fact
        Parameter: n
        Body:
            While n == 10 Do
                If n == 11 Then 
                    Var: k = 10;
                Else
                    Return n + 0x123;
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test89(self):
        input = """Function: fact
        Parameter: n
        Body:
            While n == 10 Do
                If n == 11 Then 
                    print(arg);
                Else
                    Return printLn();
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test90(self):
        input = """Function: fact
        Parameter: n
        Body:
            While n == 10 Do
                If n == 11 Then 
                    writeln(n);
                Else
                    write(n);
                EndIf.
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test91(self):
        input = """Function: fact
        Parameter: n
        Body:
            For (n = 1, n <= 10, 1) Do
                n = n + 1;
                n = 10 + 5 * 12;
                Return n;
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test92(self):
        input = """Function: fact
        Parameter: n
        Body:
            For (n = 1, n < 10, 1) Do
                For (m = n, m < 10, 1) Do
                    writeln(m);
                    writeln(n);
                EndFor.
                If (False) Then Break;
                EndIf.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test93(self):
        input = """Function: fact
        Parameter: n
        Body:
            For (n = 1, n < 10, 1) Do
                If n == v + 1 Then 
                    foo();
                    Continue;
                Else 
                    Return foo(n + 10029);
                EndIf.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test94(self):
        input = """Function: fact
        Parameter: n
        Body:
            For (n = 1, n < 10, 1) Do
                If n == v + 1 Then 
                    Var: k = 10;
                    If (k == v) || (k == n) Then 
                        Break;
                    EndIf.
                Else 
                    Return n + 100 \\ 10 + 1;
                EndIf.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test95(self):
        input = """Function: fact
        Parameter: n
        Body:
            For (n = 1, n < 10, 1) Do
                If n == v + 1 Then 
                    If True Then 
                        Return v;
                        Continue;
                    Else 
                        Return n + 100 \\ 10 + 1;
                    EndIf.
                EndIf.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test96(self):
        input = """Function: fact
        Parameter: n
        Body:
            For (n = 1, n <= 10, 1) Do
                If n == v + 1 Then 
                    Var: k;
                    k = n + v;
                    Continue;
                Else 
                    Return n + 100 \\ 10 + 1;
                EndIf.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test97(self):
        input = """Function: fact
        Parameter: n
        Body:
            For (n = 1, n <= 10, 1) Do
                If n == v + 1 Then 
                    foo();
                    Continue;
                Else 
                    Return n + 100 \\ 10 + 1;
                EndIf.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test98(self):
        input = """Function: fact
        Parameter: n
        Body:
            For (n = 1, n <= 10, 1) Do
                n = n + 1;
                foo(10 + 5 * 12);
                
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test99(self):
        input = """Function: fact
        Parameter: n
        Body:
            For (n = 1, n <= 10, 1) Do
                If n == 11 Then 
                    n = 10 + 5 * 12;
                    Return n;
                EndIf.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test100(self):
        input = """Function: fact
        Parameter: n
        Body:
            For (n = 1, n >= 10, 1) Do
                writeln(n);
                Continue;
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    

