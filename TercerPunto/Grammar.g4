grammar Grammar;

list : '[' element (',' element)* ']' ;
element : NUMBER ;

NUMBER : ('0'..'9')+ ('.' ('0'..'9')+)?;

WS : [ \t\r\n]+ -> skip;
