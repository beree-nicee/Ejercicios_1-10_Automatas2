grammar Expr;

root : expr EOF;

expr : EOF;

INT:'int';
ASIG:'=';
NUM:[0-9]+;
ID:[a-zA-Z]+;
WS : [ \t\r\n]+ -> skip;