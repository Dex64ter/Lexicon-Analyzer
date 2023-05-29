# Generated from C:/Users/davij/PycharmProjects/ExemploAntlr\Noticia.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NoticiaParser import NoticiaParser
else:
    from NoticiaParser import NoticiaParser

# This class defines a complete listener for a parse tree produced by NoticiaParser.
class NoticiaListener(ParseTreeListener):

    # Enter a parse tree produced by NoticiaParser#ini.
    def enterIni(self, ctx:NoticiaParser.IniContext):
        pass

    # Exit a parse tree produced by NoticiaParser#ini.
    def exitIni(self, ctx:NoticiaParser.IniContext):
        pass


    # Enter a parse tree produced by NoticiaParser#nomes.
    def enterNomes(self, ctx:NoticiaParser.NomesContext):
        pass

    # Exit a parse tree produced by NoticiaParser#nomes.
    def exitNomes(self, ctx:NoticiaParser.NomesContext):
        pass


    # Enter a parse tree produced by NoticiaParser#numeros.
    def enterNumeros(self, ctx:NoticiaParser.NumerosContext):
        pass

    # Exit a parse tree produced by NoticiaParser#numeros.
    def exitNumeros(self, ctx:NoticiaParser.NumerosContext):
        pass


    # Enter a parse tree produced by NoticiaParser#endereco.
    def enterEndereco(self, ctx:NoticiaParser.EnderecoContext):
        pass

    # Exit a parse tree produced by NoticiaParser#endereco.
    def exitEndereco(self, ctx:NoticiaParser.EnderecoContext):
        pass



del NoticiaParser