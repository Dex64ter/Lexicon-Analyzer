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


    # Enter a parse tree produced by NoticiaParser#article.
    def enterArticle(self, ctx:NoticiaParser.ArticleContext):
        pass

    # Exit a parse tree produced by NoticiaParser#article.
    def exitArticle(self, ctx:NoticiaParser.ArticleContext):
        pass


    # Enter a parse tree produced by NoticiaParser#title_content.
    def enterTitle_content(self, ctx:NoticiaParser.Title_contentContext):
        pass

    # Exit a parse tree produced by NoticiaParser#title_content.
    def exitTitle_content(self, ctx:NoticiaParser.Title_contentContext):
        pass


    # Enter a parse tree produced by NoticiaParser#title.
    def enterTitle(self, ctx:NoticiaParser.TitleContext):
        pass

    # Exit a parse tree produced by NoticiaParser#title.
    def exitTitle(self, ctx:NoticiaParser.TitleContext):
        pass


    # Enter a parse tree produced by NoticiaParser#body.
    def enterBody(self, ctx:NoticiaParser.BodyContext):
        pass

    # Exit a parse tree produced by NoticiaParser#body.
    def exitBody(self, ctx:NoticiaParser.BodyContext):
        pass



del NoticiaParser