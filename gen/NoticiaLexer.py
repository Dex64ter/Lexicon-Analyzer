# Generated from C:/Users/ryant/OneDrive/Área de Trabalho/2023.1/COMPILADORES/LexiconAnalyzer\Noticia.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,24,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,4,1,12,8,1,
        11,1,12,1,13,3,1,16,8,1,1,2,4,2,19,8,2,11,2,12,2,20,1,2,1,2,0,0,
        3,1,1,3,2,5,3,1,0,3,5,0,34,34,36,36,91,91,93,93,160,160,17,0,40,
        41,44,59,65,90,97,123,125,125,192,195,199,199,201,202,205,206,211,
        212,218,219,224,227,231,231,233,234,237,238,243,244,250,251,2,0,
        9,10,13,13,26,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,1,7,1,0,0,0,3,
        15,1,0,0,0,5,18,1,0,0,0,7,8,5,32,0,0,8,2,1,0,0,0,9,16,7,0,0,0,10,
        12,7,1,0,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,
        0,14,16,1,0,0,0,15,9,1,0,0,0,15,11,1,0,0,0,16,4,1,0,0,0,17,19,7,
        2,0,0,18,17,1,0,0,0,19,20,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,
        22,1,0,0,0,22,23,6,2,0,0,23,6,1,0,0,0,4,0,13,15,20,1,6,0,0
    ]

class NoticiaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WORD = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' '" ]

    symbolicNames = [ "<INVALID>",
            "WORD", "WS" ]

    ruleNames = [ "T__0", "WORD", "WS" ]

    grammarFileName = "Noticia.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


