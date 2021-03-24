grammar ExprGrammar;

VAR : [a-z] ;
UNION : '|' ;
KLEENE : '*' ;
LEFT : '(' ;
RIGHT : ')' ;


reg_expr : add | add UNION reg_expr ;
add : atom | atom add ;
atom : variable | group | atom KLEENE ;
variable: VAR ;
group : LEFT reg_expr RIGHT ;
