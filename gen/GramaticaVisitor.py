# Generated from C:/Users/davij/PycharmProjects/ExemploAntlr\Gramatica.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.

class GramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaParser#ini.
    def visitIni(self, ctx:GramaticaParser.IniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#nomes.
    def visitNomes(self, ctx:GramaticaParser.NomesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#stmt.
    def visitStmt(self, ctx:GramaticaParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#expr.
    def visitExpr(self, ctx:GramaticaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#other.
    def visitOther(self, ctx:GramaticaParser.OtherContext):
        return self.visitChildren(ctx)



del GramaticaParser