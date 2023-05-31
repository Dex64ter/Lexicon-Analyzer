grammar Noticia;
ini: article;

article: title_content  body_content;

title_content: WORD ( ' ' WORD )*;

body_content: (WORD ( ' ' WORD )*)*;

// Lexer rules

WORD: '[' | ']' | ' '| '"' | '$' | '”' | '“' | [A-ZÂÃÀÁÉÊÍÎÔÓÛÚÇa-zâãàáéêíîóõôüúûç0-9,.:;(){}/-]+;
WS: [\n\t\r]+ -> skip;