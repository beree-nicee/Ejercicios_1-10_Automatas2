grammar Expr;

root : expr EOF;

expr: EOF;

PRINT : 'print';
CAD : '"' ~["\t\n]* '"';
PAREND_IZQ : '(';
PAREND_DER : ')';
PUNTO_COMA : ';';
WS : [ \t\r\n]+ -> skip;