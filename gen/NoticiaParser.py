# Generated from C:/Users/davij/PycharmProjects/ExemploAntlr\Noticia.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,4,28,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,4,0,13,
        8,0,11,0,12,0,14,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,
        0,0,5,0,2,4,6,8,0,0,23,0,10,1,0,0,0,2,16,1,0,0,0,4,20,1,0,0,0,6,
        23,1,0,0,0,8,25,1,0,0,0,10,12,5,1,0,0,11,13,3,2,1,0,12,11,1,0,0,
        0,13,14,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,1,1,0,0,0,16,17,3,
        4,2,0,17,18,5,1,0,0,18,19,3,8,4,0,19,3,1,0,0,0,20,21,5,2,0,0,21,
        22,5,1,0,0,22,5,1,0,0,0,23,24,5,2,0,0,24,7,1,0,0,0,25,26,5,3,0,0,
        26,9,1,0,0,0,1,14
    ]

class NoticiaParser ( Parser ):

    grammarFileName = "Noticia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "TITLE_TEXT", "BODY_TEXT", 
                      "INFO" ]

    RULE_ini = 0
    RULE_article = 1
    RULE_title_content = 2
    RULE_title = 3
    RULE_body = 4

    ruleNames =  [ "ini", "article", "title_content", "title", "body" ]

    EOF = Token.EOF
    NEWLINE=1
    TITLE_TEXT=2
    BODY_TEXT=3
    INFO=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class IniContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(NoticiaParser.NEWLINE, 0)

        def article(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NoticiaParser.ArticleContext)
            else:
                return self.getTypedRuleContext(NoticiaParser.ArticleContext,i)


        def getRuleIndex(self):
            return NoticiaParser.RULE_ini

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIni" ):
                listener.enterIni(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIni" ):
                listener.exitIni(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIni" ):
                return visitor.visitIni(self)
            else:
                return visitor.visitChildren(self)




    def ini(self):

        localctx = NoticiaParser.IniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ini)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(NoticiaParser.NEWLINE)
            self.state = 12 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 11
                self.article()
                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArticleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def title_content(self):
            return self.getTypedRuleContext(NoticiaParser.Title_contentContext,0)


        def NEWLINE(self):
            return self.getToken(NoticiaParser.NEWLINE, 0)

        def body(self):
            return self.getTypedRuleContext(NoticiaParser.BodyContext,0)


        def getRuleIndex(self):
            return NoticiaParser.RULE_article

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArticle" ):
                listener.enterArticle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArticle" ):
                listener.exitArticle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArticle" ):
                return visitor.visitArticle(self)
            else:
                return visitor.visitChildren(self)




    def article(self):

        localctx = NoticiaParser.ArticleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_article)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.title_content()
            self.state = 17
            self.match(NoticiaParser.NEWLINE)
            self.state = 18
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Title_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TITLE_TEXT(self):
            return self.getToken(NoticiaParser.TITLE_TEXT, 0)

        def NEWLINE(self):
            return self.getToken(NoticiaParser.NEWLINE, 0)

        def getRuleIndex(self):
            return NoticiaParser.RULE_title_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitle_content" ):
                listener.enterTitle_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitle_content" ):
                listener.exitTitle_content(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTitle_content" ):
                return visitor.visitTitle_content(self)
            else:
                return visitor.visitChildren(self)




    def title_content(self):

        localctx = NoticiaParser.Title_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_title_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(NoticiaParser.TITLE_TEXT)
            self.state = 21
            self.match(NoticiaParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TITLE_TEXT(self):
            return self.getToken(NoticiaParser.TITLE_TEXT, 0)

        def getRuleIndex(self):
            return NoticiaParser.RULE_title

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitle" ):
                listener.enterTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitle" ):
                listener.exitTitle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTitle" ):
                return visitor.visitTitle(self)
            else:
                return visitor.visitChildren(self)




    def title(self):

        localctx = NoticiaParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(NoticiaParser.TITLE_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY_TEXT(self):
            return self.getToken(NoticiaParser.BODY_TEXT, 0)

        def getRuleIndex(self):
            return NoticiaParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = NoticiaParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(NoticiaParser.BODY_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





