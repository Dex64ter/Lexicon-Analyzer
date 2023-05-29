grammar Gramatica;
ini: nomes ;
nomes: E;

/*stmt:  ('+' stmt)
    | (stmt '*' stmt)
    | ('-' stmt)
    | ( stmt )
    | 'id'
A:
    ;
*/
WS: [ \t\r\n] -> skip;


/*
E:  (E '*' E)
    | (E '+' E)
    | ('-' E)
    | ( E )
    | 'id'
    ;

*/

E: T R;

R: '+' T R
   | '*' T R
   ;

T: '-' T
   | ( E )
   | 'id'
   ;
/*
stmt: 'if' expr 'then' stmt 'else' stmt
     | 'if' expr 'then' stmt
     | other
     ;

expr: EXP;

EXP: 'E'[0-9];

other: PAL;
PAL: [a-zA-Z]+[0-9]+ ;
*/