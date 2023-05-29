# Generated from C:/Users/davij/PycharmProjects/ExemploAntlr\Gramatica.g4 by ANTLR 4.12.0
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
        4,1,6,34,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,28,8,2,1,
        3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,30,0,10,1,0,0,0,2,12,1,0,0,
        0,4,27,1,0,0,0,6,29,1,0,0,0,8,31,1,0,0,0,10,11,3,2,1,0,11,1,1,0,
        0,0,12,13,3,4,2,0,13,3,1,0,0,0,14,15,5,1,0,0,15,16,3,6,3,0,16,17,
        5,2,0,0,17,18,3,4,2,0,18,28,1,0,0,0,19,20,5,1,0,0,20,21,3,6,3,0,
        21,22,5,2,0,0,22,23,3,4,2,0,23,24,5,3,0,0,24,25,3,4,2,0,25,28,1,
        0,0,0,26,28,3,8,4,0,27,14,1,0,0,0,27,19,1,0,0,0,27,26,1,0,0,0,28,
        5,1,0,0,0,29,30,5,5,0,0,30,7,1,0,0,0,31,32,5,6,0,0,32,9,1,0,0,0,
        1,27
    ]

class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'then'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS", "EXP", "PAL" ]

    RULE_ini = 0
    RULE_nomes = 1
    RULE_stmt = 2
    RULE_expr = 3
    RULE_other = 4

    ruleNames =  [ "ini", "nomes", "stmt", "expr", "other" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WS=4
    EXP=5
    PAL=6

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

        def nomes(self):
            return self.getTypedRuleContext(GramaticaParser.NomesContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_ini

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

        localctx = GramaticaParser.IniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ini)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.nomes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NomesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(GramaticaParser.StmtContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_nomes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNomes" ):
                listener.enterNomes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNomes" ):
                listener.exitNomes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNomes" ):
                return visitor.visitNomes(self)
            else:
                return visitor.visitChildren(self)




    def nomes(self):

        localctx = GramaticaParser.NomesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nomes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.StmtContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.StmtContext,i)


        def other(self):
            return self.getTypedRuleContext(GramaticaParser.OtherContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = GramaticaParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(GramaticaParser.T__0)
                self.state = 15
                self.expr()
                self.state = 16
                self.match(GramaticaParser.T__1)
                self.state = 17
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(GramaticaParser.T__0)
                self.state = 20
                self.expr()
                self.state = 21
                self.match(GramaticaParser.T__1)
                self.state = 22
                self.stmt()
                self.state = 23
                self.match(GramaticaParser.T__2)
                self.state = 24
                self.stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.other()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXP(self):
            return self.getToken(GramaticaParser.EXP, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = GramaticaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(GramaticaParser.EXP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAL(self):
            return self.getToken(GramaticaParser.PAL, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_other

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOther" ):
                listener.enterOther(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOther" ):
                listener.exitOther(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther" ):
                return visitor.visitOther(self)
            else:
                return visitor.visitChildren(self)




    def other(self):

        localctx = GramaticaParser.OtherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_other)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(GramaticaParser.PAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





