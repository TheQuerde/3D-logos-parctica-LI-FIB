grammar Logos3D;
root : statement* EOF ;

statement : assigna_variable
         | crea_procediment 
         | bucle_for
         | bucle_while
         | condicional 
         | expr
         ;

assigna_variable : ID ':=' expr ;

bucle_for: 'FOR' variable  'FROM' expr 'TO' expr 'DO' statement+ 'END';

crea_procediment: 'PROC'  ID '('(parametre',')*parametre*')' 'IS' statement+ 'END';

bucle_while: 'WHILE' eqexpr 'DO' statement+ 'END';
        
condicional: 'IF' eqexpr 'THEN' statement+ ('ELSE' statement+)? 'END';

procediment : ID '('(parametre',')*parametre*')';

variable : ID;

parametre : variable
          | expr
          ;

expr: variable
    | procediment
    | eqexpr
    | opexpr
    | '<<' expr
    | '>>' variable
    ;



eqexpr :  (variable|opexpr) '=' (variable|opexpr)
       | (variable|opexpr) '>' (variable|opexpr)
       | (variable|opexpr) '<' (variable|opexpr)
       | (variable|opexpr) '>=' (variable|opexpr)
       | (variable|opexpr) '<=' (variable|opexpr)
       | (variable|opexpr) '!=' (variable|opexpr) 
      ;

opexpr : variable|opexpr '+' opexpr
     | opexpr '-' opexpr
     | opexpr '*' opexpr
     | opexpr '/' opexpr
     | <assoc=right> opexpr '^' opexpr
     | numerical
     | variable
     ;

numerical: NUM;
NUM : ('-'*)(([0-9]+'.'[0-9]*)|([0-9]*'.'[0-9]+)|([0-9]+)) ; //numeros reals
 


ID : [a-z][a-zA-Z0-9_]*;//els identidicadors de les varibles han de comencar en minuscula 

COMENTARIS : '//' ~[\r\n]* -> skip; //comentaris al codi 

WS : [ \t\n]+ -> skip ;

