grammar Expr;

root : expr EOF;

expr : EOF;

IDT : [a-zA-Z]+;
MAYOR_IGUAL : '>=';
NUMBER : [0-9]+;
WS : [ \t\r\n]+ -> skip;