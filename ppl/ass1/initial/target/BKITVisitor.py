# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#global_varideclare.
    def visitGlobal_varideclare(self, ctx:BKITParser.Global_varideclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_item.
    def visitVar_item(self, ctx:BKITParser.Var_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#initial_value.
    def visitInitial_value(self, ctx:BKITParser.Initial_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arraylit.
    def visitArraylit(self, ctx:BKITParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#simple_array.
    def visitSimple_array(self, ctx:BKITParser.Simple_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_declare.
    def visitFunction_declare(self, ctx:BKITParser.Function_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_list.
    def visitPara_list(self, ctx:BKITParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_item.
    def visitPara_item(self, ctx:BKITParser.Para_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_statement.
    def visitAssign_statement(self, ctx:BKITParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#rela.
    def visitRela(self, ctx:BKITParser.RelaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logi.
    def visitLogi(self, ctx:BKITParser.LogiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#adding.
    def visitAdding(self, ctx:BKITParser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multi.
    def visitMulti(self, ctx:BKITParser.MultiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logih.
    def visitLogih(self, ctx:BKITParser.LogihContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#signn.
    def visitSignn(self, ctx:BKITParser.SignnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#endofex.
    def visitEndofex(self, ctx:BKITParser.EndofexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#lhs.
    def visitLhs(self, ctx:BKITParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_cell.
    def visitArray_cell(self, ctx:BKITParser.Array_cellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_then_stmt.
    def visitIf_then_stmt(self, ctx:BKITParser.If_then_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_if_stmt.
    def visitElse_if_stmt(self, ctx:BKITParser.Else_if_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_stmt.
    def visitElse_stmt(self, ctx:BKITParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_statement.
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhile_statement.
    def visitDowhile_statement(self, ctx:BKITParser.Dowhile_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_statement.
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)



del BKITParser