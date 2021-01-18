from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):

    def visitProgram(self,ctx:BKITParser.ProgramContext):
        varDeclList = []
        funcDeclList = []
        for i in range(ctx.getChildCount()):
            if ctx.global_varideclare(i) is not None:
                varDeclList += self.visit(ctx.global_varideclare(i))
        for i in range(ctx.getChildCount()):
            if ctx.function_declare(i) is not None:
                funcDeclList += [self.visit(ctx.function_declare(i))]
        #after this step, varDeclList will hold all func_decl and pass them to Program
        for funcDecl in funcDeclList:
            varDeclList += [funcDecl]
        return Program(varDeclList)

#variable declaration 
#begin

    def visitGlobal_varideclare(self,ctx:BKITParser.Global_varideclareContext):
        #variable : Id
        #varDimen : List[int] # empty list for scalar variable
        #varInit  : Literal   # null if no initial
        varItemList = self.visit(ctx.var_list())
        declList = []
        for varItem in varItemList:
            #varItem: (ID, [#list of int that're dime], initial_value)
            declList += [VarDecl(varItem[0], varItem[1], varItem[2])]
        return declList

    def visitVar_list(self,ctx:BKITParser.Var_listContext):
        varItemList = []
        i = ctx.getChildCount()
        i = i - int(i/2) # number of var_item
        for j in range(i):
            #varItem = (ID, [#list of integers that are dimensions])
            varItem = self.visit(ctx.var_item(j))
            varItemList += [varItem]
        return varItemList

    def visitVar_item(self,ctx:BKITParser.Var_itemContext):
        dimeList = []
        for i in range(ctx.getChildCount()):
            if ctx.INTEGER(i) is None:
                break
            else:
                dimeList += [ctx.INTEGER(i).getText()]
        if ctx.initial_value() is None:
            return (Id(ctx.ID().getText()), dimeList, None)
        return (Id(ctx.ID().getText()), dimeList, self.visit(ctx.initial_value()))

    def visitInitial_value(self,ctx:BKITParser.Initial_valueContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTEGER():
            return IntLiteral(ctx.INTEGER().getText())
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        elif ctx.BOOLEAN():
            return BooleanLiteral(ctx.BOOLEAN().getText())
        elif ctx.FLOAT():
            return FloatLiteral(ctx.FLOAT().getText())
        return self.visit(ctx.arraylit())
    
    def visitArraylit(self,ctx:BKITParser.ArraylitContext):
        if ctx.simple_array():
            return self.visit(ctx.simple_array())

        return ArrayLiteral([self.visit(ctx.arraylit(i)) for i in range(ctx.getChildCount()) if ctx.arraylit(i) is not None])
    
    def visitSimple_array(self,ctx:BKITParser.Simple_arrayContext):
        #drawback: just one type , or else can render only one type in order
        literalList = []
        if ctx.ID():
            for i in range(ctx.getChildCount()):
                if ctx.ID(i) is None:
                    break
                literalList += [Id(ctx.ID(i).getText())]
        elif ctx.INTEGER():
            for i in range(ctx.getChildCount()):
                if ctx.INTEGER(i) is None:
                    break
                literalList += [IntLiteral(ctx.INTEGER(i).getText())]
        elif ctx.STRING():
            for i in range(ctx.getChildCount()):
                if ctx.STRING(i) is None:
                    break
                literalList += [StringLiteral(ctx.STRING(i).getText())]
        elif ctx.BOOLEAN():
            for i in range(ctx.getChildCount()):
                if ctx.BOOLEAN(i) is None:
                    break
                literalList += [BooleanLiteral(ctx.BOOLEAN(i).getText())]
        elif ctx.FLOAT():
            for i in range(ctx.getChildCount()):
                if ctx.FLOAT(i) is None:
                    break
                literalList += [FloatLiteral(ctx.FLOAT(i).getText())]
        return ArrayLiteral(literalList)
#end

#function declaration
    def visitFunction_declare(self,ctx:BKITParser.Function_declareContext):
        #name: Id
        #param: List[VarDecl]
        #body: Tuple[List[VarDecl],List[Stmt]]
        id = Id(ctx.ID().getText())
        param = self.visit(ctx.para_list()) if ctx.para_list() else []
        
        varDecl =[]
        stmt = []
        if ctx.global_varideclare():
            for i in range(ctx.getChildCount()):
                if ctx.global_varideclare(i) is not None:
                    varDecl += self.visit(ctx.global_varideclare(i))
        if ctx.statement():
            for i in range(ctx.getChildCount()):
                if ctx.statement(i) is not None:
                    stmt += [self.visit(ctx.statement(i))]
        body = (varDecl, stmt)

        return FuncDecl(id, param, body)

    def visitPara_list(self,ctx:BKITParser.Para_listContext):

        #number of para items
        i = ctx.getChildCount()
        i = i - int(i/2)
        return [self.visit(ctx.para_item(j)) for j in range(i)]
    
    def visitPara_item(self,ctx:BKITParser.Para_itemContext):

        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTEGER():
            return IntLiteral(ctx.INTEGER().getText())
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        elif ctx.BOOLEAN():
            return BooleanLiteral(ctx.BOOLEAN().getText())
        elif ctx.FLOAT():
            return FloatLiteral(ctx.FLOAT().getText())

    def visitStatement(self,ctx:BKITParser.StatementContext):
        if ctx.assign_statement():
            return self.visit(ctx.assign_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.while_statement():
            return self.visit(ctx.while_statement())
        elif ctx.dowhile_statement():
            return self.visit(ctx.dowhile_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.call_statement():
            return self.visit(ctx.call_statement())
        return self.visit(ctx.return_statement())
    
    def visitAssign_statement(self,ctx:BKITParser.Assign_statementContext):
        #lhs: LHS -> ID or ArrayCell
        #rhs: Expr
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expression())
        return Assign(lhs, rhs)

    def visitLhs(self,ctx:BKITParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.array_cell())
    
    def visitArray_cell(self,ctx:BKITParser.Array_cellContext):
        #arr:Expr
        #idx:List[Expr]
        arr = self.visit(ctx.expression(0))
        idx = []
        if ctx.getChildCount() > 1:
            for i in range(ctx.getChildCount()):
                if i > 0:
                    if ctx.expression(i) is not None:
                        idx += [self.visit(ctx.expression(i))]
        return ArrayCell(arr, idx)

    def visitExpression(self,ctx:BKITParser.ExpressionContext):
        #op:str
        #left:Expr
        #right:Expr
        if ctx.getChildCount() == 1:
            return self.visit(ctx.rela())
        return BinaryOp(
            ctx.BIN_INFIX_NONE().getText(),
            self.visit(ctx.expression(0)),
            self.visit(ctx.expression(1))
        )

    def visitRela(self,ctx:BKITParser.RelaContext):
        #op:str
        #left:Expr
        #right:Expr
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logi())
        return BinaryOp(
            ctx.BIN_INFIX_LEFT3().getText(),
            self.visit(ctx.rela()),
            self.visit(ctx.logi())
        )

    def visitLogi(self,ctx:BKITParser.LogiContext):
        #op:str
        #left:Expr
        #right:Expr
        if ctx.getChildCount() == 1:
            return self.visit(ctx.adding())
        logiOp = ctx.BIN_INFIX_LEFT2().getText() if ctx.BIN_INFIX_LEFT2() else ctx.SIGN_BOTH().getText()
        return BinaryOp(
            logiOp,
            self.visit(ctx.logi()),
            self.visit(ctx.adding())
        )

    def visitAdding(self,ctx:BKITParser.AddingContext):
        #op:str
        #left:Expr
        #right:Expr
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multi())
        return BinaryOp(
            ctx.BIN_INFIX_LEFT1().getText(),
            self.visit(ctx.adding()),
            self.visit(ctx.multi())
        )

    def visitMulti(self,ctx:BKITParser.MultiContext):
        #op:str
        #body:Expr
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logih())
        return UnaryOp(ctx.UN_PRE2().getText(), self.visit(ctx.multi()))

    def visitLogih(self,ctx:BKITParser.LogihContext):
        #op:str
        #body:Expr
        if ctx.getChildCount() == 1:
            return self.visit(ctx.signn())
        return UnaryOp(ctx.SIGN_BOTH().getText(), self.visit(ctx.logih()))
    
    def visitSignn(self,ctx:BKITParser.SignnContext):
        #op:str
        #body:Expr
        if ctx.getChildCount() == 1:
            return self.visit(ctx.endofex())
        return UnaryOp(
            ctx.LSB().getText() if ctx.LSB() else ctx.RSB().getText(),
            self.visit(ctx.signn())
        )
        
    def visitEndofex(self,ctx:BKITParser.EndofexContext):
        if ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.para_item():
            return self.visit(ctx.para_item())
        return self.visit(ctx.call_statement())


    def visitIf_statement(self,ctx:BKITParser.If_statementContext):
        """Expr is the condition, 
        List[VarDecl] is the list of declaration in the beginning of Then branch, 
            empty list if no declaration
        List[Stmt] is the list of statement after the declaration in Then branch, 
            empty list if no statement
        """
        #ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        #elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
        ifthenStmt = []
        ifthenStmt += [self.visit(ctx.if_then_stmt())]
        if ctx.else_if_stmt():
            for i in range(ctx.getChildCount()):
                if ctx.else_if_stmt(i) is not None:
                    ifthenStmt += [self.visit(ctx.else_if_stmt(i))]
        elseStmt = self.visit(ctx.else_stmt()) if ctx.else_stmt() is not None else ([],[])
        return If(ifthenStmt, elseStmt)
    
    def visitIf_then_stmt(self,ctx:BKITParser.If_then_stmtContext):
        #Tuple[Expr,List[VarDecl],List[Stmt]]
        expr = self.visit(ctx.expression())
        varDecl = []
        stmt = []
        if ctx.global_varideclare():
            for i in range(ctx.getChildCount()):
                if ctx.global_varideclare(i) is not None:
                    varDecl += self.visit(ctx.global_varideclare(i))
        if ctx.statement():
            for i in range(ctx.getChildCount()):
                if ctx.statement(i) is not None:
                    stmt += [self.visit(ctx.statement(i))]
        return (expr, varDecl, stmt)

    def visitElse_if_stmt(self,ctx:BKITParser.Else_if_stmtContext):
        expr = self.visit(ctx.expression())
        varDecl = []
        stmt = []
        if ctx.global_varideclare():
            for i in range(ctx.getChildCount()):
                if ctx.global_varideclare(i) is not None:
                    varDecl += self.visit(ctx.global_varideclare(i))
        if ctx.statement():
            for i in range(ctx.getChildCount()):
                if ctx.statement(i) is not None:
                    stmt += [self.visit(ctx.statement(i))]
        return (expr, varDecl, stmt)
    
    def visitElse_stmt(self,ctx:BKITParser.Else_stmtContext):
        varDecl = []
        stmt = []
        if ctx.global_varideclare():
            for i in range(ctx.getChildCount()):
                if ctx.global_varideclare(i) is not None:
                    varDecl += self.visit(ctx.global_varideclare(i))
        if ctx.statement():
            for i in range(ctx.getChildCount()):
                if ctx.statement(i) is not None:
                    stmt += [self.visit(ctx.statement(i))]
        return (varDecl, stmt)

    def visitFor_statement(self,ctx:BKITParser.For_statementContext):
        #idx1: Id
        #expr1:Expr
        #expr2:Expr
        #expr3:Expr
        #loop: Tuple[List[VarDecl],List[Stmt]]
        varDecl = []
        stmt = []
        if ctx.global_varideclare():
            for i in range(ctx.getChildCount()):
                if ctx.global_varideclare(i) is not None:
                    varDecl += self.visit(ctx.global_varideclare(i))
        if ctx.statement():
            for i in range(ctx.getChildCount()):
                if ctx.statement(i) is not None:
                    stmt += [self.visit(ctx.statement(i))]
        return For(
            Id(ctx.ID().getText()),
            self.visit(ctx.expression(0)),
            self.visit(ctx.expression(1)),
            self.visit(ctx.expression(2)),
            (varDecl, stmt)
        )

    def visitWhile_statement(self,ctx:BKITParser.While_statementContext):
        #exp: Expr
        #sl:Tuple[List[VarDecl],List[Stmt]]
        varDecl = []
        stmt = []
        if ctx.global_varideclare():
            for i in range(ctx.getChildCount()):
                if ctx.global_varideclare(i) is not None:
                    varDecl += self.visit(ctx.global_varideclare(i))
        if ctx.statement():
            for i in range(ctx.getChildCount()):
                if ctx.statement(i) is not None:
                    stmt += [self.visit(ctx.statement(i))]
        return While(
            self.visit(ctx.expression()),
            (varDecl, stmt)
        )
    
    def visitDowhile_statement(self,ctx:BKITParser.Dowhile_statementContext):
        #sl:Tuple[List[VarDecl],List[Stmt]]
        #exp: Expr
        varDecl = []
        stmt = []
        if ctx.global_varideclare():
            for i in range(ctx.getChildCount()):
                if ctx.global_varideclare(i) is not None:
                    varDecl += self.visit(ctx.global_varideclare(i))
        if ctx.statement():
            for i in range(ctx.getChildCount()):
                if ctx.statement(i) is not None:
                    stmt += [self.visit(ctx.statement(i))]
        return Dowhile(
            (varDecl,stmt),
            self.visit(ctx.expression())
        )

    def visitBreak_statement(self,ctx:BKITParser.Break_statementContext):
        return Break()

    def visitContinue_statement(self,ctx:BKITParser.Continue_statementContext):
        return Continue()

    def visitCall_statement(self,ctx:BKITParser.Call_statementContext):
        #method:Id
        #param:List[Expr]
        param = []
        for i in range(ctx.getChildCount()):
            if ctx.expression(i) is not None:
                param += [self.visit(ctx.expression(i))]
        return CallStmt(
            Id(ctx.ID().getText()),
            param
        )

    def visitReturn_statement(self,ctx:BKITParser.Return_statementContext):
        #expr:Expr # None if no expression
        if ctx.expression() is None:
            return Return(None)
        return Return(self.visit(ctx.expression()))