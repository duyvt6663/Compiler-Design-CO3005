from Visitor import *
from StaticError import *
from TypeInference import *

class MultipassVisitor(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.states = []
    ############################################################
    #            util functions for scope management           #
    ############################################################
    def enterScope(self):
        self.states.append(-1)
            
    def setState(self) -> str:
        if len(self.states) == 0:
            return ""
        self.states[-1] += 1
        return str(self.states[-1])
    def exitScope(self):
        self.states.pop()
    def kind(self, id):
        return Parameter() if type(id) is ParamType else\
            Function() if  type(id) is FuncType else Variable()
    
    ############################################################
    #                preVisit and postVisit method             #
    ############################################################
    def preVisit(self, ast, param):
        method_name = 'preVisit{}'.format(ast.__class__.__name__)
        visit = getattr(self, method_name)
        return visit(ast, param)
    def postVisit(self, ast, param):
        method_name = 'postVisit{}'.format(ast.__class__.__name__)
        visit = getattr(self, method_name)
        return visit(ast, param)
    ############################################################
    def preVisitIntegerType(self, ast, param): pass
    def preVisitFloatType(self, ast, param): pass
    def preVisitBooleanType(self, ast, param): pass
    def preVisitStringType(self, ast, param): pass
    def preVisitArrayType(self, ast, param): pass
    def preVisitAutoType(self, ast, param): pass
    def preVisitVoidType(self, ast, param): pass

    def preVisitBinExpr(self, ast, param): pass
    def preVisitUnExpr(self, ast, param): pass
    def preVisitId(self, ast, param): pass
    def preVisitArrayCell(self, ast, param): pass
    def preVisitIntegerLit(self, ast, param): pass
    def preVisitFloatLit(self, ast, param): pass
    def preVisitStringLit(self, ast, param): pass
    def preVisitBooleanLit(self, ast, param): pass
    def preVisitArrayLit(self, ast, param): pass
    def preVisitFuncCall(self, ast, param): pass

    def preVisitAssignStmt(self, ast, param): pass
    def preVisitBlockStmt(self, ast, param): pass
    def preVisitIfStmt(self, ast, param): pass
    def preVisitForStmt(self, ast, param): pass
    def preVisitWhileStmt(self, ast, param): pass
    def preVisitDoWhileStmt(self, ast, param): pass
    def preVisitBreakStmt(self, ast, param): pass
    def preVisitContinueStmt(self, ast, param): pass
    def preVisitReturnStmt(self, ast, param): pass
    def preVisitCallStmt(self, ast, param): pass

    def preVisitVarDecl(self, ast, param): pass
    def preVisitParamDecl(self, ast, param): pass
    def preVisitFuncDecl(self, ast, param): pass

    def preVisitProgram(self, ast, param): pass
    ############################################################
    def postVisitIntegerType(self, ast, param): pass
    def postVisitFloatType(self, ast, param): pass
    def postVisitBooleanType(self, ast, param): pass
    def postVisitStringType(self, ast, param): pass
    def postVisitArrayType(self, ast, param): pass
    def postVisitAutoType(self, ast, param): pass
    def postVisitVoidType(self, ast, param): pass

    def postVisitBinExpr(self, ast, param): pass
    def postVisitUnExpr(self, ast, param): pass
    def postVisitId(self, ast, param): pass
    def postVisitArrayCell(self, ast, param): pass
    def postVisitIntegerLit(self, ast, param): pass
    def postVisitFloatLit(self, ast, param): pass
    def postVisitStringLit(self, ast, param): pass
    def postVisitBooleanLit(self, ast, param): pass
    def postVisitArrayLit(self, ast, param): pass
    def postVisitFuncCall(self, ast, param): pass

    def postVisitAssignStmt(self, ast, param): pass
    def postVisitBlockStmt(self, ast, param): pass
    def postVisitIfStmt(self, ast, param): pass
    def postVisitForStmt(self, ast, param): pass
    def postVisitWhileStmt(self, ast, param): pass
    def postVisitDoWhileStmt(self, ast, param): pass
    def postVisitBreakStmt(self, ast, param): pass
    def postVisitContinueStmt(self, ast, param): pass
    def postVisitReturnStmt(self, ast, param): pass
    def postVisitCallStmt(self, ast, param): pass

    def postVisitVarDecl(self, ast, param): pass
    def postVisitParamDecl(self, ast, param): pass
    def postVisitFuncDecl(self, ast, param): pass

    def postVisitProgram(self, ast, param): pass
    