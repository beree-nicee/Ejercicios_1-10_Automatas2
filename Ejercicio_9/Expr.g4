grammar Expr;

root : expr EOF;

expr: EOF;

IF : 'if';
IDT : [a-zA-Z]+;
MAYOR_IGUAL : '>';
NUM : [0-9]+;
PAREND_IZQ : '(';
PAREND_DER : ')';
WS : [ \t\r\n]+ -> skip;