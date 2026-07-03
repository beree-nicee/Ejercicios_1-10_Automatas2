from antlr4 import *

from ExprLexer import ExprLexer

lexer = ExprLexer(InputStream(input("? ")))

tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for token in tokens.tokens:
        # SI ES EL TOKEN DE FIN DE ARCHIVO, DETENER EL CICLO O MARCARLO CORRECTAMENTE
        if token.type == Token.EOF:
            print("Texto: <EOF>")
            print("Línea: " + str(token.line))
            print("Columna: " + str(token.column))
            print("Nombre del token: EOF")
            print("==========")
            continue
            
        print("Texto: " + token.text)
        print("Línea: " + str(token.line))
        print("Columna: " + str(token.column))
        
        nombre_token = lexer.symbolicNames[token.type]
        print("Nombre del token: " + nombre_token)
        print("==========")