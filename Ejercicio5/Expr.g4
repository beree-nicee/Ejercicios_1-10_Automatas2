grammar Expr;

root : expr EOF;

//expr : EOF| expr MAS expr| NUM;
expr : EOF;

PRINT:'print';
CADENA: '"' ~["\r\n]* '"' ;
WS : [ \t\r\n]+ -> skip;