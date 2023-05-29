# Generated from C:/Users/davij/PycharmProjects/ExemploAntlr\Noticia.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NoticiaParser import NoticiaParser
else:
    from NoticiaParser import NoticiaParser

# This class defines a complete generic visitor for a parse tree produced by NoticiaParser.

class NoticiaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NoticiaParser#ini.
    def visitIni(self, ctx:NoticiaParser.IniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoticiaParser#nomes.
    def visitNomes(self, ctx:NoticiaParser.NomesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoticiaParser#numeros.
    def visitNumeros(self, ctx:NoticiaParser.NumerosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoticiaParser#endereco.
    def visitEndereco(self, ctx:NoticiaParser.EnderecoContext):
        return self.visitChildren(ctx)



del NoticiaParser