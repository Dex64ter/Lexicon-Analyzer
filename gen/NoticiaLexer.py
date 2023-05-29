# Generated from C:/Users/davij/PycharmProjects/ExemploAntlr\Noticia.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,40,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,1,1,3,1,19,8,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,8,1,
        1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,0,0,6,1,1,3,2,5,
        3,7,4,9,5,11,6,1,0,4,5,0,65,90,97,122,163,163,173,173,195,195,1,
        0,48,57,3,0,44,44,46,47,59,59,3,0,9,10,13,13,32,32,41,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,
        13,1,0,0,0,3,15,1,0,0,0,5,30,1,0,0,0,7,32,1,0,0,0,9,34,1,0,0,0,11,
        36,1,0,0,0,13,14,5,10,0,0,14,2,1,0,0,0,15,16,5,91,0,0,16,26,3,5,
        2,0,17,19,5,64,0,0,18,17,1,0,0,0,18,19,1,0,0,0,19,20,1,0,0,0,20,
        21,3,5,2,0,21,22,5,46,0,0,22,23,5,99,0,0,23,24,5,111,0,0,24,25,5,
        109,0,0,25,27,1,0,0,0,26,18,1,0,0,0,26,27,1,0,0,0,27,28,1,0,0,0,
        28,29,5,93,0,0,29,4,1,0,0,0,30,31,7,0,0,0,31,6,1,0,0,0,32,33,7,1,
        0,0,33,8,1,0,0,0,34,35,7,2,0,0,35,10,1,0,0,0,36,37,7,3,0,0,37,38,
        1,0,0,0,38,39,6,5,0,0,39,12,1,0,0,0,3,0,18,26,1,6,0,0
    ]

class NoticiaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    EMAIL = 2
    WOR = 3
    NUM = 4
    PONTUACAO = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "EMAIL", "WOR", "NUM", "PONTUACAO", "WS" ]

    ruleNames = [ "T__0", "EMAIL", "WOR", "NUM", "PONTUACAO", "WS" ]

    grammarFileName = "Noticia.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


