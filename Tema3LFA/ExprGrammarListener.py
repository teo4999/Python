from antlr4 import *

from ExprGrammarParser import ExprGrammarParser


# This class defines a complete listener for a parse tree produced by ExprGrammarParser.
class ExprGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ExprGrammarParser#reg_expr.
    def enterReg_expr(self, ctx: ExprGrammarParser.Reg_exprContext):
        pass

    # Exit a parse tree produced by ExprGrammarParser#reg_expr.
    def exitReg_expr(self, ctx: ExprGrammarParser.Reg_exprContext):
        pass

    # Enter a parse tree produced by ExprGrammarParser#add.
    def enterAdd(self, ctx: ExprGrammarParser.AddContext):
        pass

    # Exit a parse tree produced by ExprGrammarParser#add.
    def exitAdd(self, ctx: ExprGrammarParser.AddContext):
        pass

    # Enter a parse tree produced by ExprGrammarParser#atom.
    def enterAtom(self, ctx: ExprGrammarParser.AtomContext):
        pass

    # Exit a parse tree produced by ExprGrammarParser#atom.
    def exitAtom(self, ctx: ExprGrammarParser.AtomContext):
        pass

    # Enter a parse tree produced by ExprGrammarParser#variable.
    def enterVariable(self, ctx: ExprGrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by ExprGrammarParser#variable.
    def exitVariable(self, ctx: ExprGrammarParser.VariableContext):
        pass

    # Enter a parse tree produced by ExprGrammarParser#group.
    def enterGroup(self, ctx: ExprGrammarParser.GroupContext):
        pass

    # Exit a parse tree produced by ExprGrammarParser#group.
    def exitGroup(self, ctx: ExprGrammarParser.GroupContext):
        pass


del ExprGrammarParser
