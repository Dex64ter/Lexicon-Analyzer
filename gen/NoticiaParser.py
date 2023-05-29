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
        4,1,6,31,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,3,0,13,
        8,0,1,1,1,1,3,1,17,8,1,1,2,1,2,1,2,5,2,22,8,2,10,2,12,2,25,9,2,3,
        2,27,8,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,31,0,12,1,0,0,0,2,14,1,0,
        0,0,4,18,1,0,0,0,6,28,1,0,0,0,8,9,5,1,0,0,9,13,3,2,1,0,10,13,3,4,
        2,0,11,13,3,6,3,0,12,8,1,0,0,0,12,10,1,0,0,0,12,11,1,0,0,0,13,1,
        1,0,0,0,14,16,5,3,0,0,15,17,5,5,0,0,16,15,1,0,0,0,16,17,1,0,0,0,
        17,3,1,0,0,0,18,26,5,4,0,0,19,23,5,5,0,0,20,22,5,4,0,0,21,20,1,0,
        0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,27,1,0,0,0,25,23,
        1,0,0,0,26,19,1,0,0,0,26,27,1,0,0,0,27,5,1,0,0,0,28,29,5,2,0,0,29,
        7,1,0,0,0,4,12,16,23,26
    ]

class NoticiaParser ( Parser ):

    grammarFileName = "Noticia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "EMAIL", "WOR", "NUM", "PONTUACAO", 
                      "WS" ]

    RULE_ini = 0
    RULE_nomes = 1
    RULE_numeros = 2
    RULE_endereco = 3

    ruleNames =  [ "ini", "nomes", "numeros", "endereco" ]

    EOF = Token.EOF
    T__0=1
    EMAIL=2
    WOR=3
    NUM=4
    PONTUACAO=5
    WS=6

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
            return self.getTypedRuleContext(NoticiaParser.NomesContext,0)


        def numeros(self):
            return self.getTypedRuleContext(NoticiaParser.NumerosContext,0)


        def endereco(self):
            return self.getTypedRuleContext(NoticiaParser.EnderecoContext,0)


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
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(NoticiaParser.T__0)
                self.state = 9
                self.nomes()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 10
                self.numeros()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 11
                self.endereco()
                pass
            else:
                raise NoViableAltException(self)

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

        def WOR(self):
            return self.getToken(NoticiaParser.WOR, 0)

        def PONTUACAO(self):
            return self.getToken(NoticiaParser.PONTUACAO, 0)

        def getRuleIndex(self):
            return NoticiaParser.RULE_nomes

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

        localctx = NoticiaParser.NomesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nomes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(NoticiaParser.WOR)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 15
                self.match(NoticiaParser.PONTUACAO)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumerosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(NoticiaParser.NUM)
            else:
                return self.getToken(NoticiaParser.NUM, i)

        def PONTUACAO(self):
            return self.getToken(NoticiaParser.PONTUACAO, 0)

        def getRuleIndex(self):
            return NoticiaParser.RULE_numeros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeros" ):
                listener.enterNumeros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeros" ):
                listener.exitNumeros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeros" ):
                return visitor.visitNumeros(self)
            else:
                return visitor.visitChildren(self)




    def numeros(self):

        localctx = NoticiaParser.NumerosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_numeros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(NoticiaParser.NUM)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 19
                self.match(NoticiaParser.PONTUACAO)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 20
                    self.match(NoticiaParser.NUM)
                    self.state = 25
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnderecoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMAIL(self):
            return self.getToken(NoticiaParser.EMAIL, 0)

        def getRuleIndex(self):
            return NoticiaParser.RULE_endereco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndereco" ):
                listener.enterEndereco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndereco" ):
                listener.exitEndereco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndereco" ):
                return visitor.visitEndereco(self)
            else:
                return visitor.visitChildren(self)




    def endereco(self):

        localctx = NoticiaParser.EnderecoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_endereco)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(NoticiaParser.EMAIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





