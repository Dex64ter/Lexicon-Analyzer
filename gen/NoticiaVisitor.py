# Generated from C:/Users/ryant/OneDrive/Área de Trabalho/2023.1/COMPILADORES/LexiconAnalyzer\Noticia.g4 by ANTLR 4.12.0
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


    # Visit a parse tree produced by NoticiaParser#article.
    def visitArticle(self, ctx:NoticiaParser.ArticleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoticiaParser#title_content.
    def visitTitle_content(self, ctx:NoticiaParser.Title_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoticiaParser#body_content.
    def visitBody_content(self, ctx:NoticiaParser.Body_contentContext):
        return self.visitChildren(ctx)



del NoticiaParser