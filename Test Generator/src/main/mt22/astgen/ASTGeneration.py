from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
import sys

from AST import *


class ASTGeneration(MT22Visitor):
    # program: decl+ EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        res = []
        for x in ctx.decl():
            res += self.visitDecl(x)
        return Program(res)

    # vardecl: idlist COLON typ (ASSIGN param)? SEMI;
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        # break the idlist + param down to single chunks of vardecl in AST.py
        namelist = self.visitIdlist(ctx.idlist()) # return the variable name list
        typ = self.visitTyp(ctx.typ())
        initlist = self.visitParam(ctx.param()) if ctx.param() else [None]*len(namelist)

        return [VarDecl(name, typ, init) for name, init in zip(namelist, initlist)]
        
    # idlist: ID (COMMA ID)*;
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        return [x.getText() for x in ctx.ID()]

    # funcdecl: ID COLON Function (typ | VOID) LB paramlist? RB (Inherit ID)? blockstmt;
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        name = ctx.ID(0).getText()
        typ = self.visitTyp(ctx.typ()) if ctx.typ() else VoidType()
        params = self.visitParamlist(ctx.paramlist()) if ctx.paramlist() else []
        inherit = ctx.ID(1).getText() if ctx.Inherit() else None
        body = self.visitBlockstmt(ctx.blockstmt())
        # return list
        return [FuncDecl(name, typ, params, inherit, body)]

    # paramlist: paramdecl (COMMA paramdecl)*;
    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        return [self.visitParamdecl(x) for x in ctx.paramdecl()]

    # paramdecl: Inherit? Out? ID COLON typ;
    def visitParamdecl(self, ctx: MT22Parser.ParamdeclContext):
        name = ctx.ID().getText()
        typ = self.visitTyp(ctx.typ())
        out = True if ctx.Out() else False
        inherit = True if ctx.Inherit() else False
        return ParamDecl(name, typ, out, inherit)

    # assignstmt: scalarVar ASSIGN expr SEMI; 
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        lhs = self.visitScalarVar(ctx.scalarVar())
        rhs = self.visitExpr(ctx.expr())
        return AssignStmt(lhs, rhs)

    # ifstmt: If LB expr RB stmt (Else stmt)?;
    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        cond = self.visitExpr(ctx.expr())
        tstmt = self.visitStmt(ctx.stmt(0)) # stmt return list
        fstmt = self.visitStmt(ctx.stmt(1)) if ctx.Else() else None
        return IfStmt(cond, tstmt, fstmt)

    # forstmt: For LB scalarVar ASSIGN expr COMMA expr COMMA expr RB stmt; 
    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        var = self.visitScalarVar(ctx.scalarVar())
        init_expr = self.visitExpr(ctx.expr(0))
        init = AssignStmt(var, init_expr)
        cond = self.visitExpr(ctx.expr(1))
        upd = self.visitExpr(ctx.expr(2))
        stmt = self.visitStmt(ctx.stmt())
        return ForStmt(init, cond, upd, stmt)
    
    # scalarVar: index_expr | ID;
    def visitScalarVar(self, ctx:MT22Parser.ScalarVarContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visitChildren(ctx)

    # whilestmt: While LB expr RB stmt;
    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        cond = self.visitExpr(ctx.expr())
        stmt = self.visitStmt(ctx.stmt())
        return WhileStmt(cond, stmt) 

    # dowhilestmt: Do blockstmt While LB expr RB SEMI;
    def visitDowhilestmt(self, ctx: MT22Parser.DowhilestmtContext):
        cond = self.visitExpr(ctx.expr())
        stmt = self.visitBlockstmt(ctx.blockstmt())
        return DoWhileStmt(cond, stmt)

    # breakstmt: Break SEMI;
    def visitBreakstmt(self, ctx: MT22Parser.BreakstmtContext):
        return BreakStmt()

    # continuestmt: Continue SEMI;
    def visitContinuestmt(self, ctx: MT22Parser.ContinuestmtContext):
        return ContinueStmt()

    # returnstmt: Return expr? SEMI;
    def visitReturnstmt(self, ctx: MT22Parser.ReturnstmtContext):
        expr = self.visitExpr(ctx.expr()) if ctx.expr() else None
        return ReturnStmt(expr)

    # callstmt: funcall SEMI;
    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        funcall = ctx.funcall()
        name = funcall.ID().getText()
        args = self.visitParam(funcall.param()) if funcall.param() else []
        return CallStmt(name, args)
        
    # blockstmt: LP (stmt | vardecl)* RP;
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        body = []
        for i in range(1,ctx.getChildCount()-1):
            tem = ctx.getChild(i).accept(self)
            if isinstance(tem, list):
                body += tem
            else:
                body.append(tem)
        return BlockStmt(body)

    # typ: atomic | arrtype | AUTO;
    def visitTyp(self, ctx: MT22Parser.TypContext):
        return AutoType() if ctx.AUTO() else self.visit(ctx.getChild(0))

    # atomic: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitAtomic(self, ctx: MT22Parser.AtomicContext):
        import AST
        typ = ctx.getChild(0).getText()
        method_name = typ[0].upper() + typ[1:] + 'Type'
        visit = getattr(AST, method_name)   
        return visit()

    # arrtype: ARRAY LS INTLIT (COMMA INTLIT)* RS Of atomic;
    def visitArrtype(self, ctx: MT22Parser.ArrtypeContext):
        dimensions = [int(x.getText()) for x in ctx.INTLIT()]
        typ = self.visitAtomic(ctx.atomic())
        return ArrayType(dimensions, typ)

    # literal: INTLIT | FLOATLIT | BOOLLIT | STRLIT | index_arrlit;
    def visitLiteral(self, ctx: MT22Parser.LiteralContext):
        lit = ctx.getChild(0).getText()
        if ctx.INTLIT():
            return IntegerLit(int(lit))
        elif ctx.FLOATLIT():
            # edge case: .e
            if lit[:2] == ".e" or lit[:2] == ".E":
                return FloatLit(float(0))
            return FloatLit(float(lit))
        elif ctx.BOOLLIT():
            return BooleanLit(lit == "true")
        elif ctx.STRLIT():
            return StringLit(lit)
        else:
            return self.visitIndex_arrlit(ctx.index_arrlit())

    # index_arrlit: LP (expr (COMMA expr)*)? RP;
    def visitIndex_arrlit(self, ctx: MT22Parser.Index_arrlitContext):
        explist = [self.visitExpr(x) for x in ctx.expr()]
        return ArrayLit(explist)


    # operands: literal | index_expr | ID | funcall | LB expr RB;
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return self.visitExpr(ctx.expr())

    # funcall: ID LB param? RB;
    def visitFuncall(self, ctx: MT22Parser.FuncallContext):
        name = ctx.ID().getText()
        args = self.visitParam(ctx.param()) if ctx.param() else []
        return FuncCall(name, args)

    # index_expr: ID LS param RS;
    def visitIndex_expr(self, ctx: MT22Parser.Index_exprContext):
        name = ctx.ID().getText()
        cell = self.visitParam(ctx.param())
        return ArrayCell(name, cell)

    # param: expr (COMMA expr)* ;
    def visitParam(self, ctx: MT22Parser.ParamContext):
        return [self.visitExpr(x) for x in ctx.expr()]

    # expr: string_expr | string_expr CONCAT string_expr;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visitString_expr(ctx.string_expr(0))
        op = ctx.getChild(1).getText()
        left = self.visitString_expr(ctx.string_expr(0))
        right = self.visitString_expr(ctx.string_expr(1))
        return BinExpr(op, left, right)

    # string_expr: num_expr | num_expr (NEQ | EQUAL | GRE | GEQ | LES | LEQ) num_expr;
    def visitString_expr(self, ctx: MT22Parser.String_exprContext):
        if ctx.getChildCount() == 1:
            return self.visitNum_expr(ctx.num_expr(0))
        op = ctx.getChild(1).getText()
        left = self.visitNum_expr(ctx.num_expr(0))
        right = self.visitNum_expr(ctx.num_expr(1))
        return BinExpr(op, left, right)


    # num_expr: SUB num_expr | LNOT num_expr
	#   | num_expr (MUL | MOD | DIV) num_expr
	#   | num_expr (SUB | ADD) num_expr
	#   | num_expr (LAND | LOR) num_expr
	#   | operands;
    def visitNum_expr(self, ctx: MT22Parser.Num_exprContext):
        if ctx.getChildCount() == 1:
            return self.visitOperands(ctx.operands())
        elif ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            val = self.visitNum_expr(ctx.num_expr(0))
            return UnExpr(op, val)
        op = ctx.getChild(1).getText()
        left = self.visitNum_expr(ctx.num_expr(0))
        right = self.visitNum_expr(ctx.num_expr(1))
        return BinExpr(op, left, right)