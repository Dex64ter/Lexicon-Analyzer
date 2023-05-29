from antlr4 import *

from gen.GramaticaLexer import GramaticaLexer
from gen.GramaticaParser import GramaticaParser

if __name__ == '__main__':
    dados = FileStream('input.txt')
    #dados = InputStream("hello Raimundo, Santos, Moura.")
    lexer = GramaticaLexer(dados)
    for tok in lexer.getAllTokens():
        print(tok.text, tok.type)
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = GramaticaParser(stream)
    tree = parser.ini()
    print(tree.toStringTree())
