#importa para funciones 
from antlr4 import *
from ExprLexer import ExprLexer
#obtiene la entrada de datos, analiza el texto y lo separa en tokens
lexer = ExprLexer(InputStream(input("? ")))
#tooma los token y los guarda de una lista 
tokens=CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for token in tokens.tokens:
    if token.type == Token.EOF:
        continue
    nombre_token = lexer.symbolicNames[token.type]
    print(f"{token.text:<15} {nombre_token:<15} {token.type:<6} {token.line:<6} {token.column:<8}")
