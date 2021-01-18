//1813621
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

program: exp EOF;

exp: term ASSIGN exp | term;

term: factor COMPARE factor | factor;

factor: factor ANDOR operand | operand; 

operand: ID | INTLIT | BOOLIT | '(' exp ')';

INTLIT: [0-9]+ ;

BOOLIT: 'True' | 'False' ;

ANDOR: 'and' | 'or' ;

ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

ID: [a-z]+ ;



COMMENT: '**'.*?'**' -> skip;
WSPP: [ \t]+ -> skip;
NL: ('\r' '\n'? | '\n') -> skip;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;