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
        4,0,4,36,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,1,4,1,13,
        8,1,11,1,12,1,14,1,2,4,2,18,8,2,11,2,12,2,19,1,2,3,2,23,8,2,1,2,
        1,2,3,2,27,8,2,1,3,1,3,4,3,31,8,3,11,3,12,3,32,1,3,1,3,0,0,4,1,1,
        3,2,5,3,7,4,1,0,3,2,0,10,10,13,13,3,0,32,32,48,57,192,252,3,0,48,
        57,65,90,97,122,41,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,
        0,1,9,1,0,0,0,3,12,1,0,0,0,5,26,1,0,0,0,7,28,1,0,0,0,9,10,7,0,0,
        0,10,2,1,0,0,0,11,13,7,1,0,0,12,11,1,0,0,0,13,14,1,0,0,0,14,12,1,
        0,0,0,14,15,1,0,0,0,15,4,1,0,0,0,16,18,7,1,0,0,17,16,1,0,0,0,18,
        19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,23,3,1,0,
        0,22,21,1,0,0,0,22,23,1,0,0,0,23,27,1,0,0,0,24,27,3,7,3,0,25,27,
        1,0,0,0,26,17,1,0,0,0,26,24,1,0,0,0,26,25,1,0,0,0,27,6,1,0,0,0,28,
        30,5,40,0,0,29,31,7,2,0,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,
        0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,35,5,41,0,0,35,8,1,0,0,0,6,0,
        14,19,22,26,32,0
    ]

class NoticiaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NEWLINE = 1
    TITLE_TEXT = 2
    BODY_TEXT = 3
    INFO = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "TITLE_TEXT", "BODY_TEXT", "INFO" ]

    ruleNames = [ "NEWLINE", "TITLE_TEXT", "BODY_TEXT", "INFO" ]

    grammarFileName = "Noticia.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


