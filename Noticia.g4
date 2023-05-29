grammar Noticia;
ini: citacao |FONT | nomes | numeros ;
nomes: (WOR (PONTUACAO)?);
numeros: NUM (PONTUACAO (NUM)*)?;
endereco: EMAIL;
citacao: CIT;

FONT: 'Fonte:';
WOR: [a-zãàáíêôâéóúçA-ZÇÃÂ];
EMAIL: '[' WOR (('@')? WOR '.com')?']' | '[' WOR ']';
CIT: '"' WOR '"';
NUM: [0-9];

INFO: '('WOR')';

PONTUACAO: [.;,/];
WS: [ \t\r\n] -> skip;
