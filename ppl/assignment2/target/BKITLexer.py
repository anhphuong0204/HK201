# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("T\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\6\6+\n\6\r\6\16\6,\3\7\3\7\3\7\3\7\7\7\63\n\7\f\7\16")
        buf.write("\7\66\13\7\3\7\3\7\3\7\3\7\3\7\3\b\6\b>\n\b\r\b\16\b?")
        buf.write("\3\b\3\b\3\t\3\t\5\tF\n\t\3\t\5\tI\n\t\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\64\2\16\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\4\3\2c|\4\2")
        buf.write("\13\13\"\"\2X\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t#\3\2\2\2")
        buf.write("\13*\3\2\2\2\r.\3\2\2\2\17=\3\2\2\2\21H\3\2\2\2\23L\3")
        buf.write("\2\2\2\25N\3\2\2\2\27P\3\2\2\2\31R\3\2\2\2\33\34\7=\2")
        buf.write("\2\34\4\3\2\2\2\35\36\7.\2\2\36\6\3\2\2\2\37 \7k\2\2 ")
        buf.write("!\7p\2\2!\"\7v\2\2\"\b\3\2\2\2#$\7h\2\2$%\7n\2\2%&\7q")
        buf.write("\2\2&\'\7c\2\2\'(\7v\2\2(\n\3\2\2\2)+\t\2\2\2*)\3\2\2")
        buf.write("\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\f\3\2\2\2./\7,\2\2/")
        buf.write("\60\7,\2\2\60\64\3\2\2\2\61\63\13\2\2\2\62\61\3\2\2\2")
        buf.write("\63\66\3\2\2\2\64\65\3\2\2\2\64\62\3\2\2\2\65\67\3\2\2")
        buf.write("\2\66\64\3\2\2\2\678\7,\2\289\7,\2\29:\3\2\2\2:;\b\7\2")
        buf.write("\2;\16\3\2\2\2<>\t\3\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2")
        buf.write("?@\3\2\2\2@A\3\2\2\2AB\b\b\2\2B\20\3\2\2\2CE\7\17\2\2")
        buf.write("DF\7\f\2\2ED\3\2\2\2EF\3\2\2\2FI\3\2\2\2GI\7\f\2\2HC\3")
        buf.write("\2\2\2HG\3\2\2\2IJ\3\2\2\2JK\b\t\2\2K\22\3\2\2\2LM\13")
        buf.write("\2\2\2M\24\3\2\2\2NO\13\2\2\2O\26\3\2\2\2PQ\13\2\2\2Q")
        buf.write("\30\3\2\2\2RS\13\2\2\2S\32\3\2\2\2\b\2,\64?EH\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTTYPE = 3
    FLOATTYPE = 4
    ID = 5
    COMMENT = 6
    WSPP = 7
    NL = 8
    ERROR_CHAR = 9
    UNCLOSE_STRING = 10
    ILLEGAL_ESCAPE = 11
    UNTERMINATED_COMMENT = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "ID", "COMMENT", "WSPP", "NL", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "INTTYPE", "FLOATTYPE", "ID", "COMMENT", 
                  "WSPP", "NL", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text[1:(len(result.text))])
        elif tk == self.ILLEGAL_ESCAPE:
            k = result.text.find("\\")
            if (k == -1):
                k = result.text.find("\'")
            result.text = result.text[1:(k+2)]
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            if (result.text.find("\"") != -1):
                result.text = result.text[1:-1]
            return result;


