/* ID: 2052003 */
grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

/* program rule */
program: decl+ EOF;

/******************************************************************
 *                            DECLARATION                         *
 ******************************************************************/
/* combined declaration rule */
decl: vardecl | funcdecl;

/* Variable declaration */
vardecl: 
    idlist COLON typ // variable list
    (
        ASSIGN param // with initializer
{
if $idlist.iSize > $param.pSize:
    raise NoViableAltException(self)
elif $idlist.iSize < $param.pSize:
    raise NoViableAltException(self, offendingToken=$param.ctx.COMMA($idlist.iSize-1).getPayload())
}
    )? SEMI; 
idlist returns [iSize = 1]: 
    ID (COMMA ID{$iSize += 1})*;

/* Function declaration */
funcdecl: ID COLON Function (typ | VOID) LB paramlist? RB (Inherit ID)? blockstmt;
paramlist: paramdecl (COMMA paramdecl)*;
paramdecl: Inherit? Out? ID COLON typ;

/******************************************************************
 *                            STATEMENT                           *
 ******************************************************************/
/* combined statement rule */
stmt: 
    assignstmt   
    | ifstmt 
    | forstmt
    | whilestmt
    | dowhilestmt
    | breakstmt 
    | continuestmt 
    | returnstmt 
    | callstmt
    | blockstmt;

/* assignment statement */
assignstmt: scalarVar ASSIGN expr SEMI; 

/* if statement */
ifstmt: If LB expr RB stmt (Else stmt)?; 

/* for statement */
forstmt: For LB scalarVar ASSIGN expr COMMA expr COMMA expr RB stmt; 
scalarVar: index_expr | ID;

/* while statement */
whilestmt: While LB expr RB stmt;

/* do while statement */
dowhilestmt: Do blockstmt While LB expr RB SEMI;

/* break statement */
breakstmt: Break SEMI; 

/* continue statement */
continuestmt: Continue SEMI; 

/* return statement */
returnstmt: Return expr? SEMI;

/* call statement */
callstmt: funcall SEMI;

/* block statement */
blockstmt: LP (stmt | vardecl)* RP;

/******************************************************************
 *                              TYPE                              *
 ******************************************************************/
/* Var type */
typ: atomic | arrtype | AUTO;

atomic: BOOLEAN | INTEGER | FLOAT | STRING; // atomic type
arrtype: ARRAY LS INTLIT (COMMA INTLIT)* RS Of atomic;

/*data type */
INTEGER: 'integer';
FLOAT: 'float';
BOOLEAN: 'boolean';
STRING: 'string';
ARRAY: 'array';
AUTO: 'auto';
VOID: 'void';

/******************************************************************
 *                             LITERALS                           *
 ******************************************************************/
/* combined Type */
literal: INTLIT | FLOATLIT | BOOLLIT | STRLIT | index_arrlit;

/* Integer literal */
INTLIT: '0' | [1-9]DEC* ('_' DEC+)* {self.text = self.text.replace("_","")}; // trim off _

/* Float literal */
FLOATLIT: 
	(INTLIT DECPART EXPOPART?
	| INTLIT EXPOPART 
	| DECPART EXPOPART) {self.text = self.text.replace("_","")};
fragment DECPART: DOT DEC*;
fragment EXPOPART: [eE][+-]? DEC+;
fragment DEC: [0-9];

/* Boolean literal */
BOOLLIT: TRue | FAlse;

/* String literal */
STRLIT:
	'"' (STR_CHAR | ESCSEQ)* '"' {
	content = str(self.text) 
	self.text = content[1:-1]
};

/* array literal */
index_arrlit: LP (expr (COMMA expr)*)? RP;

/******************************************************************
 *                             EXPRESSION                         *
 ******************************************************************/
/* Operands for expression */
operands: 
    literal 
    | index_expr 
    | ID 
    | funcall
    | LB expr RB;
funcall: ID LB param? RB; // function call

/* Index expression for array: arr[k], [] is index_operator */
index_expr: ID LS param RS;
param returns [pSize = 1]: 
    expr (COMMA expr{$pSize += 1})* ; // list of indices/param, can be used for function call

/* Expression */
expr:
	string_expr
    | string_expr CONCAT string_expr; // string_concat
string_expr: 
    num_expr
    | num_expr (NEQ | EQUAL | GRE | GEQ | LES | LEQ) num_expr; // relational_expr
num_expr:
	SUB num_expr
	| LNOT num_expr
	| num_expr (MUL | MOD | DIV) num_expr
	| num_expr (SUB | ADD) num_expr
	| num_expr (LAND | LOR) num_expr
	| operands;

/******************************************************************
 *                              UTILS                             *
 ******************************************************************/
/* Comment */
BlockComment: '/*' .*? '*/' -> skip;
LineComment: '//' .*? '\n' -> skip;

/* Keywords */
Function: 'function';
Break: 'break';
Continue: 'continue';
If: 'if';
Else: 'else';
For: 'for';
While: 'while';
Return: 'return';
Of: 'of';
Do: 'do';
Out: 'out';
Inherit: 'inherit';
TRue: 'true';
FAlse: 'false';

/* Operators */
LNOT: '!';
LAND: '&&';
LOR: '||';
EQUAL: '==';

NEQ: '!=';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
GRE: '>';
GEQ: '>=';
LES: '<';
LEQ: '<=';
CONCAT: '::';

/* Delimiters/Separators */
ASSIGN: '=';
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LS: '[';
RS: ']';
SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';

fragment STR_CHAR: ~[\\"\n];
fragment ESCSEQ:
	'\\b'
	| '\\f'
	| '\\r'
	| '\\n'
	| '\\t'
	| '\\\''
	| '\\\\'
	| '\\"';
fragment ESCERROR: '\\' ~[bfrnt'\\"];

/* Identifiers */
ID: [a-zA-Z_][a-zA-Z0-9_]*; // check keywords already done by placing them ahead of this rule

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING:
	'"' (STR_CHAR | ESCSEQ)* (EOF | '\n') {
	content = str(self.text)
	esc = '\n'
	if content[-1] in esc:
		raise UncloseString(content[1:-1])
	else:
		raise UncloseString(content[1:])
};

ILLEGAL_ESCAPE:
	'"' (STR_CHAR | ESCSEQ)* ESCERROR {
	content = str(self.text) 
	raise IllegalEscape(content[1:])
};