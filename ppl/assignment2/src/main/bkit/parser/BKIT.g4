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

//----------

program: vardecls EOF;

vardecls: vardecl vardecltail;

vardecltail: vardecl vardecltail | ;

vardecl: mptype ids ';' ;

mptype: INTTYPE | FLOATTYPE;

ids: ID ',' ids | ID; 

INTTYPE: 'int';

FLOATTYPE: 'float';

ID: [a-z]+ ;

//----------

COMMENT: '**'.*?'**' -> skip;
WSPP: [ \t]+ -> skip;
NL: ('\r' '\n'? | '\n') -> skip;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;