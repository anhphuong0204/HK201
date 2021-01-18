import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_first(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",100))
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_lower_identifier1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc)df","abc,),df,<EOF>",102))
    def test_lower_identifier2(self):
        """test identifiers"""        
        self.assertTrue(TestLexer.checkLexeme("ags_383jaahs h_____ahshs","ags_383jaahs,h_____ahshs,<EOF>",103))
    def test_lower_identifier3(self):
        """test identifiers"""        
        self.assertTrue(TestLexer.checkLexeme("Do While wHile EndDo","Do,While,wHile,EndDo,<EOF>",104))
    def test_lower_identifier4(self):
        """test identifiers"""        
        self.assertTrue(TestLexer.checkLexeme("tutorial","tutorial,<EOF>",105))
    def test_lower_identifier5(self):
        """test identifiers"""        
        self.assertTrue(TestLexer.checkLexeme("tu23torial program","tu23torial,program,<EOF>",106))
    def test_lower_identifier6(self):
        """test identifiers"""       
        self.assertTrue(TestLexer.checkLexeme("tutorial PPL","tutorial,Error Token P",107))
    def test_lower_identifier7(self):
        """test identifiers"""        
        self.assertTrue(TestLexer.checkLexeme("0tutorial","0,tutorial,<EOF>",108))
    def test_lower_identifier8(self):
        """test identifiers"""        
        self.assertTrue(TestLexer.checkLexeme("**ahs*","Unterminated Comment",109))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("0 199 0xFF 0XABC 0o567 0o77","0,199,0xFF,0XABC,0o567,0o77,<EOF>",110))
        self.assertTrue(TestLexer.checkLexeme("0xff","0,xff,<EOF>",111))

    def test_floats(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12e3 12.e5 12.0e3 12000. 120000e-1", "12.0e3,12e3,12.e5,12.0e3,12000.,120000e-1,<EOF>",112))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",113))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,114))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def" abc1gs ""","""ab'"c\\n def,abc1gs,<EOF>""",115))
    
    # test id
    def test_2_make1(self):
        self.assertTrue(TestLexer.checkLexeme(""" ajsjsj123 ssaas2 kjs___ ""","""ajsjsj123,ssaas2,kjs___,<EOF>""",116))
    def test_2_make2(self):
        self.assertTrue(TestLexer.checkLexeme(""" g3389EEEgs ""","""g3389EEEgs,<EOF>""",117))
    def test_2_make3(self):
        self.assertTrue(TestLexer.checkLexeme(""" Edshs ""","""Error Token E""",118))
    def test_2_make4(self):
        self.assertTrue(TestLexer.checkLexeme(""" _as ""","""Error Token _""",119))
    def test_2_make5(self):
        self.assertTrue(TestLexer.checkLexeme(""" abc   def ""","""abc,def,<EOF>""",120))

    # test keywords
    def test_2_make6(self):
        self.assertTrue(TestLexer.checkLexeme(""" Body ""","""Body,<EOF>""",121))
    def test_2_make7(self):
        self.assertTrue(TestLexer.checkLexeme(""" Break Continue Do Else ElseIf ""","""Break,Continue,Do,Else,ElseIf,<EOF>""",122))
    def test_2_make8(self):
        self.assertTrue(TestLexer.checkLexeme(""" EndBody EndIf EndFor EndWhile For ""","""EndBody,EndIf,EndFor,EndWhile,For,<EOF>""",123))
    def test_2_make9(self):
        self.assertTrue(TestLexer.checkLexeme(""" Function If Parameter Return Then ""","""Function,If,Parameter,Return,Then,<EOF>""",124))
    def test_2_make10(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var While True False EndDo ""","""Var,While,True,False,EndDo,<EOF>""",125))

    # test integers
    def test_2_make11(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0 123 0123 ""","""0,123,0,123,<EOF>""",126))
    def test_2_make12(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0x3 0o7554 ""","""0x3,0o7554,<EOF>""",127))
    def test_2_make13(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0XFFF2 0O1012 ""","""0XFFF2,0O1012,<EOF>""",128))
    def test_2_make14(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0x0 0o0 ""","""0,x0,0,o0,<EOF>""",129))
    def test_2_make15(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1 ""","""1,<EOF>""",130))

    # test floats
    def test_2_make16(self):
        self.assertTrue(TestLexer.checkLexeme(""" 00.E+12 ""","""00.E+12,<EOF>""",131))
    def test_2_make17(self):
        self.assertTrue(TestLexer.checkLexeme(""" 10.2342 ""","""10.2342,<EOF>""",132))
    def test_2_make18(self):
        self.assertTrue(TestLexer.checkLexeme(""" 1.0E0 ""","""1.0E0,<EOF>""",133))
    def test_2_make19(self):
        self.assertTrue(TestLexer.checkLexeme(""" 234. ""","""234.,<EOF>""",134))
    def test_2_make20(self):
        self.assertTrue(TestLexer.checkLexeme(""" 5.e-0 ""","""5.e-0,<EOF>""",135))

    # test boolean
    def test_2_make21(self):
        self.assertTrue(TestLexer.checkLexeme(""" True ""","""True,<EOF>""",136))
    def test_2_make22(self):
        self.assertTrue(TestLexer.checkLexeme(""" False ""","""False,<EOF>""",137))
    def test_2_make23(self):
        self.assertTrue(TestLexer.checkLexeme(""" False ""","""False,<EOF>""",138))
    def test_2_make24(self):
        self.assertTrue(TestLexer.checkLexeme(""" False ""","""False,<EOF>""",139))
    def test_2_make25(self):
        self.assertTrue(TestLexer.checkLexeme(""" True ""","""True,<EOF>""",140))

    # test strings
    def test_2_make26(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t" ""","""This is a string containing tab \\t,<EOF>""",141))
    def test_2_make27(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab" ""","""ab,<EOF>""",142))
    def test_2_make28(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'k" ""","""Illegal Escape In String: 'k""",143))
    def test_2_make29(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'"" ""","""'",<EOF>""",144))
    def test_2_make30(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hshs'" ""","""Unclosed String: hshs'" """,145))

    # test array lit
    def test_2_make31(self):
        self.assertTrue(TestLexer.checkLexeme(""" {a} ""","""{,a,},<EOF>""",146))
    def test_2_make32(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Hey: '"?'"" ""","""Hey: '"?'",<EOF>""",147))
    def test_2_make33(self):
        self.assertTrue(TestLexer.checkLexeme(""" {}}} ""","""{,},},},<EOF>""",148))
    def test_2_make34(self):
        self.assertTrue(TestLexer.checkLexeme(""" ({[]}) ""","""(,{,[,],},),<EOF>""",149))
    def test_2_make35(self):
        self.assertTrue(TestLexer.checkLexeme(""" {{a, b},   {c, d}} ""","""{,{,a,,,b,},,,{,c,,,d,},},<EOF>""",150))

    # test '['  and ']'
    def test_2_make36(self):
        self.assertTrue(TestLexer.checkLexeme(""" b[2]; ""","""b,[,2,],;,<EOF>""",151))
    def test_2_make37(self):
        self.assertTrue(TestLexer.checkLexeme(""" k][5] ""","""k,],[,5,],<EOF>""",152))
    def test_2_make38(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123d[h2] ""","""123,d,[,h2,],<EOF>""",153))
    def test_2_make39(self):
        self.assertTrue(TestLexer.checkLexeme(""" [[]]]]] ""","""[,[,],],],],],<EOF>""",154))
    def test_2_make40(self):
        self.assertTrue(TestLexer.checkLexeme(""" asds__[**asd**] ""","""asds__,[,],<EOF>""",155))

    # test comment
    def test_2_make41(self):
        self.assertTrue(TestLexer.checkLexeme(""" **This is a comment** ""","""<EOF>""",156))
    def test_2_make42(self):
        self.assertTrue(TestLexer.checkLexeme(""" ***** ""","""*,<EOF>""",157))
    def test_2_make43(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** *** ""","""*,<EOF>""",158))
    def test_2_make44(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** ?? * ""","""Unterminated Comment""",159))
    def test_2_make45(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** ""","""Unterminated Comment""",160))

    # test program
    def test_2_make46(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var: int k 12.e+31 ""","""Var,:,int,k,12.e+31,<EOF>""",161))
    def test_2_make47(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var str "my oh my"; ""","""Var,str,my oh my,;,<EOF>""",162))
    def test_2_make48(self):
        self.assertTrue(TestLexer.checkLexeme(""" Parameter var Var ""","""Parameter,var,Var,<EOF>""",163))
    def test_2_make49(self):
        self.assertTrue(TestLexer.checkLexeme(""" string ""","""string,<EOF>""",164))
    def test_2_make50(self):
        self.assertTrue(TestLexer.checkLexeme(""" P ""","""Error Token P""",165))

    # test league of legends
    def test_2_make51(self):
        self.assertTrue(TestLexer.checkLexeme(""" poppy is a champ__12 ""","""poppy,is,a,champ__12,<EOF>""",166))
    def test_2_make52(self):
        self.assertTrue(TestLexer.checkLexeme(""" dame:123 ""","""dame,:,123,<EOF>""",167))
    def test_2_make53(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'"seraphine'"" ""","""'"seraphine'",<EOF>""",168))
    def test_2_make54(self):
        self.assertTrue(TestLexer.checkLexeme(""" stop,him ""","""stop,,,him,<EOF>""",169))
    def test_2_make55(self):
        self.assertTrue(TestLexer.checkLexeme(""" ,,, """,""",,,,,,<EOF>""",170))

    # test some enter
    def test_2_make56(self):
        self.assertTrue(TestLexer.checkLexeme(""" me
        the
        boy ""","""me,the,boy,<EOF>""",171))
    def test_2_make57(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var
        
        
        
        : 
        ; ""","""Var,:,;,<EOF>""",172))
    def test_2_make58(self):
        self.assertTrue(TestLexer.checkLexeme(""" 
        
        
        
        
        
        
        
        
        
         ""","""<EOF>""",173))
    def test_2_make59(self):
        self.assertTrue(TestLexer.checkLexeme(""" error ""","""error,<EOF>""",174))
    def test_2_make60(self):
        self.assertTrue(TestLexer.checkLexeme(""" f 1 0 a _ ""","""f,1,0,a,Error Token _""",175))

    # test computer
    def test_2_make61(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0000 ""","""0,0,0,0,<EOF>""",176))
    def test_2_make62(self):
        self.assertTrue(TestLexer.checkLexeme(""" 00123 ""","""0,0,123,<EOF>""",177))
    def test_2_make63(self):
        self.assertTrue(TestLexer.checkLexeme(""" d+4==3 ""","""d,+,4,==,3,<EOF>""",178))
    def test_2_make64(self):
        self.assertTrue(TestLexer.checkLexeme(""" char ""","""char,<EOF>""",179))
    def test_2_make65(self):
        self.assertTrue(TestLexer.checkLexeme(""" sucks ""","""sucks,<EOF>""",180))

    # ???
    def test_2_make66(self):
        self.assertTrue(TestLexer.checkLexeme(""" ? ""","""Error Token ?""",181))
    def test_2_make67(self):
        self.assertTrue(TestLexer.checkLexeme(""" ?? ""","""Error Token ?""",182))
    def test_2_make68(self):
        self.assertTrue(TestLexer.checkLexeme(""" ??? ""","""Error Token ?""",183))
    def test_2_make69(self):
        self.assertTrue(TestLexer.checkLexeme(""" ???? ""","""Error Token ?""",184))
    def test_2_make70(self):
        self.assertTrue(TestLexer.checkLexeme(""" ????? ""","""Error Token ?""",185))

    # test some strings
    def test_2_make71(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """,""",<EOF>""",186))
    def test_2_make72(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\f" ""","""\\f,<EOF>""",187))
    def test_2_make73(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\y" ""","""Illegal Escape In String: \y""",188))
    def test_2_make74(self):
        self.assertTrue(TestLexer.checkLexeme(""" """" ""","""<EOF>""",189))
    def test_2_make75(self):
        self.assertTrue(TestLexer.checkLexeme(""" " ""","""Unclosed String:  """,190))

    # Finally I found the bug. F you b*tch. 2 hours 
    def test_2_make76(self):
        self.assertTrue(TestLexer.checkLexeme(""" bugs ""","""bugs,<EOF>""",191))
    def test_2_make77(self):
        self.assertTrue(TestLexer.checkLexeme(""" bugs bugs ""","""bugs,bugs,<EOF>""",192))
    def test_2_make78(self):
        self.assertTrue(TestLexer.checkLexeme(""" bugs bugs bgus ""","""bugs,bugs,bgus,<EOF>""",193))
    def test_2_make79(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'0" ""","""Illegal Escape In String: '0""",194))
    def test_2_make80(self):
        self.assertTrue(TestLexer.checkLexeme(""" {""} ""","""{,,},<EOF>""",195))

    # The more suffering, the more you understand the pain 
    # it brings to you. 
    # You can only know the true peace 
    # after you understand fully what pain is
    def test_2_make81(self):
        self.assertTrue(TestLexer.checkLexeme(""" Yeah that's right ""","""Error Token Y""",196))
    def test_2_make82(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'a" ""","""Illegal Escape In String: 'a""",197))
    def test_2_make83(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'" ""","""Unclosed String: '" """,198))
    def test_2_make84(self):
        self.assertTrue(TestLexer.checkLexeme(""" end==) ""","""end,==,),<EOF>""",199))
    def test_2_make85(self):
        self.assertTrue(TestLexer.checkLexeme(""" ==)========> ""","""==,),==,==,==,==,>,<EOF>""",200))
    