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

program  :  global_varideclare* function_declare*;


// Global declare
// It's for global part, but it can be used for function part also
global_varideclare: VAR CL var_list ('=' initial_value)? SM;
var_list: var_item (CM var_item)*;
var_item: 
        ID 
        | (ID (LSB INTEGER RSB)+);

initial_value: assign_item (CM assign_item)*;
assign_item:
        ID
        | INTEGER
        | STRING
        | BOOLEAN
        | FLOAT
        | arraylit;
arraylit: 
        LCB arraylit (CM arraylit)* RCB
        | simple_array;
simple_array: ( LCB
    (ID | INTEGER | STRING | BOOLEAN | FLOAT) (CM (ID | INTEGER | STRING | BOOLEAN | FLOAT))*
    RCB
    );

// Function part
function_declare: FUNCTION CL ID (PARAMETER CL para_list)? BODY CL global_varideclare* statement* ENDBODY DOT;
para_list: para_item (CM para_item)*;
para_item: ID
        | INTEGER
        | STRING
        | BOOLEAN
        | FLOAT;

statement: 
        global_varideclare
        | assign_statement
        | if_statement
        | for_statement
        | while_statement
        | dowhile_statement
        | break_statement
        | continue_statement
        | call_statement SM
        | return_statement;
// For assign statement and expression
assign_statement: ID '=' expression SM;
expression: expression BIN_INFIX_NONE expression | rela;
rela: rela BIN_INFIX_LEFT3 logi | logi;
logi: logi op=(BIN_INFIX_LEFT2 | SIGN_BOTH) adding | adding;
adding: adding BIN_INFIX_LEFT1 multi | multi;
multi: UN_PRE2 multi | logih;
logih: SIGN_BOTH logih | signn;
signn: signn ',' | endofex;
endofex: LP expression RP | para_item | call_statement;

// If statement
if_statement: 
    IF expression THEN statement*
    (ELSEIF expression THEN statement*)*
    (ELSE statement*)?
    ENDIF DOT;

// For statement
for_statement: FOR LP ID (',' ID)* '=' expression CM expression CM expression RP DO
                statement*
                ENDFOR DOT;

// While statement
while_statement: WHILE expression DO statement* ENDWHILE DOT;

// Do-while statement
dowhile_statement: DO statement* WHILE expression ENDDO DOT;

// Break statement
break_statement: BREAK SM;

// Continue statement
continue_statement: CONTINUE SM;

// For call statement
call_statement: ID LP (expression (',' expression)*)? RP;

// Return statement
return_statement: RETURN_KEY expression? SM;

// For GRAMMAR RULES



// For TOKEN define

fragment LOWER_LETTER: [a-z];
fragment UPPER_LETTER: [A-Z];
fragment DIGIT: [0-9];

// *-------* Identifiers
ID: LOWER_LETTER(LOWER_LETTER|UPPER_LETTER|'_'|DIGIT)*;

// *-------* Key words (21)
BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue'; 
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf'; 
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If'; 
PARAMETER: 'Parameter'; 
RETURN_KEY: 'Return'; 
THEN: 'Then';
VAR: 'Var'; 
WHILE: 'While'; 
fragment TRUE: 'True'; 
fragment FALSE: 'False';
ENDDO: 'EndDo';

// *-------* Operators
// *Note: -, -. : can be SIGN or SUB, but SUB for both this time
    // Arithmetic Ops
fragment SUBINT: '-';
fragment SUBFLOAT: '-.';
fragment ADDINT: '+';
fragment ADDFLOAT: '+.';
fragment MULINT: '*';
fragment MULFLOAT: '*.';
fragment DIVINT: '\\';
fragment DIVFLOAT: '\\.';
fragment REDIV: '%';
    // Boolean Ops
fragment NOT: '!';
fragment AND: '&&';
fragment OR: '||';
    // Relational Ops
fragment EQUAL: '==';
fragment NOTEQUALINT: '!=';
fragment LTINT: '<';
fragment GTINT: '>';
fragment LOREINT: '<=';
fragment GOREINT: '>=';
fragment NOTEQUALFLOAT: '=//=';
fragment LTFLOAT: '<.';
fragment GTFLOAT: '>.';
fragment LOREFLOAT: '<=.';
fragment GOREFLOAT: '>=.';
// Sumary operator types: Binary and Unary
UN_PRE2: NOT;
BIN_INFIX_LEFT1: 
            MULINT
        | MULFLOAT
        | DIVINT
        | DIVFLOAT
        | REDIV;
BIN_INFIX_LEFT2:
        ADDINT
        | ADDFLOAT;
SIGN_BOTH:         
        SUBINT
        | SUBFLOAT;
BIN_INFIX_LEFT3:
        AND
        | OR;
BIN_INFIX_NONE: 
    EQUAL
    | NOTEQUALINT
    | LTINT
    | GTINT
    | LOREINT
    | GOREINT
    | NOTEQUALFLOAT
    | LTFLOAT
    | GTFLOAT
    | LOREFLOAT
    | GOREFLOAT;


// *-------* Separators
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
CL: ':';
DOT: '.';
CM: ',';
SM: ';';
LCB: '{';
RCB: '}';

// *==========================*

// Literals Section //
fragment SIGN: '+' | '-';

// *-------* Integers
INTEGER: INTLIT | HEXA | OCT;
fragment INTLIT: '0' | ([1-9] DIGIT*);
fragment HEXA: ('0x' | '0X')([1-9] | [A-F])(DIGIT|[A-F])*;
fragment OCT: ('0o' | '0O')[1-7][0-7]*;

// *-------* Floats = interger + decimal + exponent
fragment EXPONENT: ('e' | 'E') SIGN? DIGIT+;
fragment DECIMAL_FOR_F: [0-9]+;
fragment DECIMAL_PART: '.' DIGIT*;
FLOAT: (DECIMAL_FOR_F DECIMAL_PART EXPONENT) | (DECIMAL_FOR_F DECIMAL_PART) | (DECIMAL_FOR_F EXPONENT);

// *--------* Boolean 
BOOLEAN: TRUE | FALSE;

// *------* String
fragment ESCAPE_SEQUENCE: '\\\'' | '\\\\' | '\\b' | '\\f' | '\\n' | '\\t' | '\\r' | ('\'' '"');
fragment SCHAR: ~ ["'\\\r\n] | ESCAPE_SEQUENCE;
STRING: '"' SCHAR* '"';

// *-------* Array (should be in grammar rules)




COMMENT: '**'.*?'**' -> skip;
WSPP: [ \t]+ -> skip;
NL: ('\r' '\n'? | '\n') -> skip;

ERROR_CHAR: .;
UNCLOSE_STRING: '"' SCHAR*;
ILLEGAL_ESCAPE: '"' (('\\' ~[btnfr"'\\]) | ~'\\' | ~'\'' | ('\'' ~["] ))* '"';
UNTERMINATED_COMMENT: ('**' .*?) | ('**' .*? '*');