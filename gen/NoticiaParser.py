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
        4,1,3,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,1,1,1,1,1,1,2,
        1,2,1,2,5,2,17,8,2,10,2,12,2,20,9,2,1,3,1,3,1,3,5,3,25,8,3,10,3,
        12,3,28,9,3,5,3,30,8,3,10,3,12,3,33,9,3,1,3,0,0,4,0,2,4,6,0,0,33,
        0,8,1,0,0,0,2,10,1,0,0,0,4,13,1,0,0,0,6,31,1,0,0,0,8,9,3,2,1,0,9,
        1,1,0,0,0,10,11,3,4,2,0,11,12,3,6,3,0,12,3,1,0,0,0,13,18,5,2,0,0,
        14,15,5,1,0,0,15,17,5,2,0,0,16,14,1,0,0,0,17,20,1,0,0,0,18,16,1,
        0,0,0,18,19,1,0,0,0,19,5,1,0,0,0,20,18,1,0,0,0,21,26,5,2,0,0,22,
        23,5,1,0,0,23,25,5,2,0,0,24,22,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,
        0,26,27,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,29,21,1,0,0,0,30,33,
        1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,7,1,0,0,0,33,31,1,0,0,0,3,
        18,26,31
    ]

class NoticiaParser ( Parser ):

    grammarFileName = "Noticia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WORD", "WS" ]

    RULE_ini = 0
    RULE_article = 1
    RULE_title_content = 2
    RULE_body_content = 3

    ruleNames =  [ "ini", "article", "title_content", "body_content" ]

    EOF = Token.EOF
    T__0=1
    WORD=2
    WS=3

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

        def article(self):
            return self.getTypedRuleContext(NoticiaParser.ArticleContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.article()
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


        def body_content(self):
            return self.getTypedRuleContext(NoticiaParser.Body_contentContext,0)


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
            self.state = 10
            self.title_content()
            self.state = 11
            self.body_content()
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

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(NoticiaParser.WORD)
            else:
                return self.getToken(NoticiaParser.WORD, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(NoticiaParser.WORD)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 14
                self.match(NoticiaParser.T__0)
                self.state = 15
                self.match(NoticiaParser.WORD)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(NoticiaParser.WORD)
            else:
                return self.getToken(NoticiaParser.WORD, i)

        def getRuleIndex(self):
            return NoticiaParser.RULE_body_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody_content" ):
                listener.enterBody_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody_content" ):
                listener.exitBody_content(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_content" ):
                return visitor.visitBody_content(self)
            else:
                return visitor.visitChildren(self)




    def body_content(self):

        localctx = NoticiaParser.Body_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 21
                self.match(NoticiaParser.WORD)
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 22
                    self.match(NoticiaParser.T__0)
                    self.state = 23
                    self.match(NoticiaParser.WORD)
                    self.state = 28
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





