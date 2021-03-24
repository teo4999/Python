import sys
from antlr4 import *
from ExprGrammarVisitor import ExprGrammarVisitor
from ExprGrammarParser import ExprGrammarParser
from RegexToNFA import RegexToNFA


class ExprGrammarEvalVisitor(ExprGrammarVisitor):

    def visitReg_expr(self, ctx: ExprGrammarParser.Reg_exprContext):
        add = ctx.add()
        UNION = ctx.UNION()
        reg_ex = ctx.reg_expr()

        fa1 = self.visitAdd(add)
        if UNION:
            fa2 = self.visitReg_expr(reg_ex)
            construct = RegexToNFA.union(fa1, fa2)
            return construct
        else:
            return fa1

    # Visit a parse tree produced by ExprGrammarParser#concat.
    def visitAdd(self, ctx: ExprGrammarParser.AddContext):
        atom = ctx.atom()
        add = ctx.add()

        fa1 = self.visitAtom(atom)
        if add:
            fa2 = self.visitAdd(add)
            construct = RegexToNFA.concatenation(fa1, fa2)
            return construct
        else:
            return self.visitAtom(atom)

    # Visit a parse tree produced by ExprGrammarParser#atom.
    def visitAtom(self, ctx: ExprGrammarParser.AtomContext):
        atom = ctx.atom()
        group = ctx.group()
        var = ctx.variable()
        KLEENE = ctx.KLEENE()

        if atom and KLEENE:
            construct = RegexToNFA.kleene_star(self.visitAtom(atom))
            return construct

        if group:
            return self.visitGroup(group)

        if var:
            return self.visitVariable(var)

    # Visit a parse tree produced by ExprGrammarParser#variable.
    def visitVariable(self, ctx: ExprGrammarParser.VariableContext):
        var = str(ctx.VAR())
        construct = RegexToNFA.add_variable(var)
        return construct

    # Visit a parse tree produced by ExprGrammarParser#inner_expr.
    def visitGroup(self, ctx: ExprGrammarParser.GroupContext):
        return self.visit(ctx.reg_expr())

