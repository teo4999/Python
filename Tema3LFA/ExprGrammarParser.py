from antlr4 import *
from io import StringIO
import sys
from typing import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\5\2\22\n\2\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4\3\4")
        buf.write("\3\4\5\4\35\n\4\3\4\3\4\7\4!\n\4\f\4\16\4$\13\4\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\2\3\6\7\2\4\6\b\n\2\2\2*\2\21\3")
        buf.write("\2\2\2\4\27\3\2\2\2\6\34\3\2\2\2\b%\3\2\2\2\n\'\3\2\2")
        buf.write("\2\f\22\5\4\3\2\r\16\5\4\3\2\16\17\7\4\2\2\17\20\5\2\2")
        buf.write("\2\20\22\3\2\2\2\21\f\3\2\2\2\21\r\3\2\2\2\22\3\3\2\2")
        buf.write("\2\23\30\5\6\4\2\24\25\5\6\4\2\25\26\5\4\3\2\26\30\3\2")
        buf.write("\2\2\27\23\3\2\2\2\27\24\3\2\2\2\30\5\3\2\2\2\31\32\b")
        buf.write("\4\1\2\32\35\5\b\5\2\33\35\5\n\6\2\34\31\3\2\2\2\34\33")
        buf.write("\3\2\2\2\35\"\3\2\2\2\36\37\f\3\2\2\37!\7\5\2\2 \36\3")
        buf.write("\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\7\3\2\2\2$\"\3")
        buf.write("\2\2\2%&\7\3\2\2&\t\3\2\2\2\'(\7\6\2\2()\5\2\2\2)*\7\7")
        buf.write("\2\2*\13\3\2\2\2\6\21\27\34\"")
        return buf.getvalue()


class ExprGrammarParser(Parser):
    grammarFileName = "ExprGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "<INVALID>", "'|'", "'*'", "'('", "')'"]

    symbolicNames = ["<INVALID>", "VAR", "UNION", "KLEENE", "LEFT", "RIGHT"]

    RULE_reg_expr = 0
    RULE_add = 1
    RULE_atom = 2
    RULE_variable = 3
    RULE_group = 4

    ruleNames = ["reg_expr", "add", "atom", "variable", "group"]

    EOF = Token.EOF
    VAR = 1
    UNION = 2
    KLEENE = 3
    LEFT = 4
    RIGHT = 5

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class Reg_exprContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add(self):
            return self.getTypedRuleContext(ExprGrammarParser.AddContext, 0)

        def UNION(self):
            return self.getToken(ExprGrammarParser.UNION, 0)

        def reg_expr(self):
            return self.getTypedRuleContext(ExprGrammarParser.Reg_exprContext, 0)

        def getRuleIndex(self):
            return ExprGrammarParser.RULE_reg_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterReg_expr"):
                listener.enterReg_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitReg_expr"):
                listener.exitReg_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitReg_expr"):
                return visitor.visitReg_expr(self)
            else:
                return visitor.visitChildren(self)

    def reg_expr(self):

        localctx = ExprGrammarParser.Reg_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_reg_expr)
        try:
            self.state = 15
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 0, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.add()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.add()
                self.state = 12
                self.match(ExprGrammarParser.UNION)
                self.state = 13
                self.reg_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AddContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(ExprGrammarParser.AtomContext, 0)

        def add(self):
            return self.getTypedRuleContext(ExprGrammarParser.AddContext, 0)

        def getRuleIndex(self):
            return ExprGrammarParser.RULE_add

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAdd"):
                listener.enterAdd(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAdd"):
                listener.exitAdd(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAdd"):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)

    def add(self):

        localctx = ExprGrammarParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_add)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.atom(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.atom(0)
                self.state = 19
                self.add()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(ExprGrammarParser.VariableContext, 0)

        def group(self):
            return self.getTypedRuleContext(ExprGrammarParser.GroupContext, 0)

        def atom(self):
            return self.getTypedRuleContext(ExprGrammarParser.AtomContext, 0)

        def KLEENE(self):
            return self.getToken(ExprGrammarParser.KLEENE, 0)

        def getRuleIndex(self):
            return ExprGrammarParser.RULE_atom

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAtom"):
                listener.enterAtom(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAtom"):
                listener.exitAtom(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAtom"):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)

    def atom(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprGrammarParser.AtomContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_atom, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprGrammarParser.VAR]:
                self.state = 24
                self.variable()
                pass
            elif token in [ExprGrammarParser.LEFT]:
                self.state = 25
                self.group()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 3, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprGrammarParser.AtomContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_atom)
                    self.state = 28
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 29
                    self.match(ExprGrammarParser.KLEENE)
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 3, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ExprGrammarParser.VAR, 0)

        def getRuleIndex(self):
            return ExprGrammarParser.RULE_variable

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVariable"):
                listener.enterVariable(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVariable"):
                listener.exitVariable(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVariable"):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)

    def variable(self):

        localctx = ExprGrammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(ExprGrammarParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT(self):
            return self.getToken(ExprGrammarParser.LEFT, 0)

        def reg_expr(self):
            return self.getTypedRuleContext(ExprGrammarParser.Reg_exprContext, 0)

        def RIGHT(self):
            return self.getToken(ExprGrammarParser.RIGHT, 0)

        def getRuleIndex(self):
            return ExprGrammarParser.RULE_group

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterGroup"):
                listener.enterGroup(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitGroup"):
                listener.exitGroup(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitGroup"):
                return visitor.visitGroup(self)
            else:
                return visitor.visitChildren(self)

    def group(self):

        localctx = ExprGrammarParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ExprGrammarParser.LEFT)
            self.state = 38
            self.reg_expr()
            self.state = 39
            self.match(ExprGrammarParser.RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.atom_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def atom_sempred(self, localctx: AtomContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 1)
