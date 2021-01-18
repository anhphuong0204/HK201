from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

""" class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):

        return Program(ctx.vardecls().accept(self))

    def visitVardecls(self,ctx:BKITParser.VardeclsContext):

        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self,ctx:BKITParser.VardecltailContext): 

        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecl(self,ctx:BKITParser.VardeclContext): 

        type = ctx.mptype().accept(self)
        ids = ctx.ids().accept(self)
        return list(map(lambda x: VarDecl(x,type), ids))
        
    def visitMptype(self,ctx:BKITParser.MptypeContext):

        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    def visitIds(self,ctx:BKITParser.IdsContext):

        if ctx.getChildCount() == 1:
            return [ID(ctx.ID().getText())]
        return [ID(ctx.ID().getText())] + ctx.ids().accept(self) """

#"a := b := 4" Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))

class ASTGeneration(BKITVisitor):

    def visitProgram(self,ctx:BKITParser.ProgramContext):

        return self.visit(ctx.exp())

    def visitExp(self,ctx:BKITParser.ExpContext):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        return Binary(ctx.ASSIGN().getText(), ctx.term().accept(self), ctx.exp().accept(self))
        

    def visitTerm(self,ctx:BKITParser.TermContext): 

        if ctx.getChildCount() == 1:    
            return self.visit(ctx.factor(0))
        return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self))
        

    def visitFactor(self,ctx:BKITParser.FactorContext):

        if ctx.getChildCount() == 1:    
            return self.visit(ctx.operand())
        return Binary(ctx.ANDOR().getText(), ctx.factor().accept(self), self.visit(ctx.operand()))
        

    def visitOperand(self,ctx:BKITParser.OperandContext):

        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        if ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        return self.visit(ctx.exp())

