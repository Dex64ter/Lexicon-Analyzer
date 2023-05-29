# Generated from C:/Users/davij/PycharmProjects/ExemploAntlr\Gramatica.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete listener for a parse tree produced by GramaticaParser.
class GramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by GramaticaParser#ini.
    def enterIni(self, ctx:GramaticaParser.IniContext):
        pass

    # Exit a parse tree produced by GramaticaParser#ini.
    def exitIni(self, ctx:GramaticaParser.IniContext):
        pass


    # Enter a parse tree produced by GramaticaParser#nomes.
    def enterNomes(self, ctx:GramaticaParser.NomesContext):
        pass

    # Exit a parse tree produced by GramaticaParser#nomes.
    def exitNomes(self, ctx:GramaticaParser.NomesContext):
        pass


    # Enter a parse tree produced by GramaticaParser#stmt.
    def enterStmt(self, ctx:GramaticaParser.StmtContext):
        pass

    # Exit a parse tree produced by GramaticaParser#stmt.
    def exitStmt(self, ctx:GramaticaParser.StmtContext):
        pass


    # Enter a parse tree produced by GramaticaParser#expr.
    def enterExpr(self, ctx:GramaticaParser.ExprContext):
        pass

    # Exit a parse tree produced by GramaticaParser#expr.
    def exitExpr(self, ctx:GramaticaParser.ExprContext):
        pass


    # Enter a parse tree produced by GramaticaParser#other.
    def enterOther(self, ctx:GramaticaParser.OtherContext):
        pass

    # Exit a parse tree produced by GramaticaParser#other.
    def exitOther(self, ctx:GramaticaParser.OtherContext):
        pass



del GramaticaParser