import sys
from antlr4 import *
from ExprGrammarLexer import ExprGrammarLexer
from ExprGrammarParser import ExprGrammarParser
from ExprGrammarEvalVisitor import ExprGrammarEvalVisitor

if __name__ == "__main__":
    input_data = FileStream(sys.argv[1])
    lexer = ExprGrammarLexer(input_data)
    stream = CommonTokenStream(lexer)
    parser = ExprGrammarParser(stream)

    tree = parser.reg_expr()

    showVisitor = ExprGrammarEvalVisitor()

    output_nfa = sys.argv[2]
    output_dfa = sys.argv[3]
    nfa = showVisitor.visit(tree)
    nfa.print_nfa(output_nfa)

