grammar Noticia;
ini: NEWLINE article;

article: title_content (NEWLINE NEWLINE)* body;

title_content: TITLE_TEXT;

title: TITLE_TEXT;

// Lexer rules
body: BODY_TEXT;

// Lexer rules
NEWLINE: '\r' | '\n';
TITLE_TEXT: [À-ü0-9 ]+;
// CONTENT_TEXT: ~[\r\n]+;
BODY_TEXT: [À-ü0-9 ]+ NEWLINE?;

// INFO: '(' [A-Za-z0-9]+ ')';