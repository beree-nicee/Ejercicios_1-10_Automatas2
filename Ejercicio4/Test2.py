# importa ANTLR4 para funciones, aquí activamos el enviroment 
from antlr4 import *
# importarlo para obtener sus metodos 
from ExprLexer import ExprLexer

import sys 

# lo que obtiene es la entrada 
input_stream = FileStream(sys.argv[1])
# obtiene la entraada de datos, lo analiza y lo separa en tokens
lexer = ExprLexer(input_stream)

tokens = CommonTokenStream(lexer)
# lo llenamos 
tokens.fill()

print(tokens)

# contiene el arreglo de tokens, los recorre y los imprime
for token in tokens.tokens:
    print("Texto: " + token.text)
    print("Línea: " + str(token.line))
    print("Columna: " + str(token.column))
    nombre_token = lexer.symbolicNames[token.type]

    print("Tipo : " + nombre_token)

    print("==========")