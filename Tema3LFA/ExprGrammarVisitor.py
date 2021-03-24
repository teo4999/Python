from antlr4 import *
from ExprGrammarParser import ExprGrammarParser


# This class defines a complete generic visitor for a parse tree produced by ExprGrammarParser.

class ExprGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprGrammarParser#reg_expr.
    def visitReg_expr(self, ctx: ExprGrammarParser.Reg_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprGrammarParser#add.
    def visitAdd(self, ctx: ExprGrammarParser.AddContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprGrammarParser#atom.
    def visitAtom(self, ctx: ExprGrammarParser.AtomContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprGrammarParser#variable.
    def visitVariable(self, ctx: ExprGrammarParser.VariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprGrammarParser#group.
    def visitGroup(self, ctx: ExprGrammarParser.GroupContext):
        return self.visitChildren(ctx)


del ExprGrammarParser
