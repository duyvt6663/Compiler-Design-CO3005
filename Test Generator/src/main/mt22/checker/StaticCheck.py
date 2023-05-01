# from AST import *
from Visitor import *
from StaticError import *
import copy
from functools import *
# from TypeInference import *
from MultiVisitor import *
from TypeCheck import *

class StaticChecker(MultipassVisitor):
    # global built-in methods
    global_envi = {
        "readInteger": FuncType([], IntegerType()),
        "printInteger": FuncType([ParamType(IntegerType())], VoidType()),
        "readFloat": FuncType([], FloatType()),
        "printFloat": FuncType([ParamType(FloatType())], VoidType()),
        "readBoolean": FuncType([], BooleanType()),
        "printBoolean": FuncType([ParamType(BooleanType())], VoidType()),
        "readString": FuncType([], StringType()),
        "printString": FuncType([ParamType(StringType())], VoidType()),
        "super": FuncType([], VoidType()),
        "preventDefault": FuncType([], VoidType()),
    }

    def __init__(self, ast):
        super().__init__(ast)
        self.inLoop = False
        self.inStmt = 0
        self.retOutSide = False
        self.table = None
        self.parentArrlit = None
        self.checker = Checker(ast)

    def printTable(self):
        print(str(self.table))
    
    def check(self, ast=None, param=None):
        if ast is not None:
            # when there is ast, it's type checking
            self.checker.visit(ast, param)
            return
        
        self.visit(self.ast, self.checker)
        reset_type_counter()
        return []
    
    def returnControl(fn):
        def control_fn(obj, *args, **kwargs):
            obj.inStmt += 1
            fn(obj, *args, **kwargs)
            obj.inStmt -= 1

        control_fn.__name__ = fn.__name__
        return control_fn

    def apply_subst(self, typ):
        return self.checker.apply_subst(typ)
    ############################################################
    #                         decl visit                       #
    ############################################################
    # decls: List[Decl] // only FuncDecl and VarDecl
    def visitProgram(self, ast: Program, checker):
        # construct global symbol table and pass it to master, 
        # deep copy to avoid altering class attribute
        self.table = checker.table = SymbolTable(copy.deepcopy(StaticChecker.global_envi))
        flag = False # no entry flag

        # previsit to collect global prototypes
        for x in ast.decls:
            self.preVisit(x, self.table)

        self.visited = {
            "readInteger": True, "printInteger": True, "readFloat": True, "printFloat": True, 
            "readBoolean": True, "printBoolean": True, "readString": True, "printString": True,
            "super": True, "preventDefault": True,
        } # global tab check

        # in visit to collect local envs
        for x in ast.decls: # x: Decl
            # set flag for main function entry
            flag = flag or\
                (isinstance(x, FuncDecl) and
                 x.name == "main" and
                 len(x.params) == 0 and 
                 isinstance(x.return_type, VoidType))
            
            # depth-first-search for symbols
            param = self.table if isinstance(x, VarDecl) else self.visited
            self.visit(x, param)

        # check for no entry exception after building the table
        if flag == False:
            raise NoEntryPoint()

    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast: VarDecl, c: 'SymbolTable'):
        ctyp = c.get(ast.name) # get the variable from the table out
        if   ctyp is not None and\
            (not isinstance(ctyp, FuncType) or\
             self.visited.get(ast.name) is True):
            raise Redeclared(Variable(), ast.name)
        
        if c.parent is None: # global scope
            self.visited[ast.name] = True

        typ = ast.typ   
        if isinstance(typ, AutoType): # replace auto type with typevar
            if ast.init is None:
                raise Invalid(Variable(), ast.name)
            typ = TypeVar(get_fresh_typename())
        ast._typ = typ

        if ctyp is None:
            c.add(ast.name, ast._typ) 

        if ast.init is None:
            return 
        self.visit(ast.init, c)
        self.check(ast, c)
        
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def preVisitFuncDecl(self, ast: FuncDecl, c: 'SymbolTable'):
        if c.get(ast.name) is not None:
            return
        
        # symbol stack has access to function visible names
        sym_stack = SymbolTable({}, c)
        c.addChild(ast.name, sym_stack) # add symbol stack child to c

        # add params
        paramtyps = []
        for param in ast.params:
            # name: str, typ: Type, out: bool = False, inherit: bool = False            
            partype = TypeVar(get_fresh_typename())\
                        if isinstance(param.typ, AutoType) else param.typ
            typ = ParamType(partype, param.out, param.inherit, param.name)

            if sym_stack.get(param.name) is None:
                sym_stack.add(param.name, typ)
            paramtyps.append(typ)

        # add function to global scope
        rettype = TypeVar(get_fresh_typename())\
                    if isinstance(ast.return_type, AutoType) else ast.return_type
        functyp = FuncType(paramtyps, rettype, ast.inherit)

        c.add(ast.name, functyp)

    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast: FuncDecl, visited: dict):   
        def checkParams(parlist):
            par_visit = {}
            for param in parlist:
                # name: str, typ: Type, out: bool = False, inherit: bool = False
                if par_visit.get(param.name) is True:
                    raise Redeclared(Parameter(), param.name)
                par_visit[param.name] = True

        # check redeclared function
        if visited.get(ast.name) is True:
            raise Redeclared(Function(), ast.name)
        visited[ast.name] = True

        body = ast.body.body # stmt list from body blockstmt
        sym_tab = self.table.getChild(ast.name)   

        if ast.inherit is None:
            # normal case
            checkParams(ast.params)
            
            if len(body) != 0 and\
               isinstance(body[0], CallStmt) and\
              (body[0].name == 'preventDefault' or\
               body[0].name == 'super'):
                raise InvalidStatementInFunction(ast.name)

            self.checker.curr = ast.name # mark the function name for return call
            list(map(lambda x: self.visit(x, sym_tab), body))
            return
        
        # inherit case 
        # partype: List[Type], rettype: Type, inherit: str
        parent = self.table.get(ast.inherit) # the parent function prototyp
        if parent is None:
            raise Undeclared(Function(), ast.inherit)
        
        checkParams(ast.params)

        # find symbols in body
        self.check(ast, self)

    ############################################################
    #                         stmt visit                       #
    ############################################################
    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast: BlockStmt, c: 'SymbolTable'):
        key = self.setState()
        # symbol stacks init
        sym_stack = SymbolTable({}, c)
        c.addChild(key, sym_stack)

        self.enterScope()
        list(map(lambda x: self.visit(x, sym_stack), ast.body))
        self.exitScope()

    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    @returnControl
    def visitIfStmt(self, ast: IfStmt, c: 'SymbolTable'):
        self.visit(ast.cond, c)
        # cond must be bool
        self.check(ast, c)

        # visit if scope
        self.visit(ast.tstmt, c)
        # visit else scope
        if ast.fstmt is None:
            return
        
        self.visit(ast.fstmt, c)

    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    @returnControl
    def visitForStmt(self, ast: ForStmt, c: 'SymbolTable'):
        self.check(ast, (self, c))

    # cond: Expr, stmt: Stmt
    @returnControl
    def visitWhileStmt(self, ast: WhileStmt, c: 'SymbolTable'):
        self.visit(ast.cond, c)
        self.check(ast, c)

        self.visitLoopStmt(ast, c)

    # cond: Expr, stmt: BlockStmt
    @returnControl
    def visitDoWhileStmt(self, ast: DoWhileStmt, c: 'SymbolTable'):
        # do first while second
        self.visitLoopStmt(ast, c)

        self.visit(ast.cond, c)
        self.check(ast, c)

    def visitLoopStmt(self, ast, c: 'SymbolTable'):
        state = self.inLoop
        if state is False:
            self.inLoop = True

        self.visit(ast.stmt, c)

        if state is False:
            # reset only if it is the first loop
            self.inLoop = False

    def visitBreakStmt(self, ast: BreakStmt, c: 'SymbolTable'):
        if self.inLoop is False:
            raise MustInLoop(ast)
    def visitContinueStmt(self, ast: ContinueStmt, c: 'SymbolTable'):
        if self.inLoop is False:
            raise MustInLoop(ast)   

    # name: str, args: List[Expr]    
    def visitCallStmt(self, ast: CallStmt, c: 'SymbolTable'): 
        func = c.get(ast.name, True)
        if func is None:
            raise Undeclared(Function(), ast.name)
        if not isinstance(func, FuncType): 
            raise TypeMismatchInStatement(ast)
        
        # list(map(lambda x: self.visit(x, c), ast.args))
        self.check(ast, (self, c))
    
    # expr: Expr or None = None
    def visitReturnStmt(self, ast: ReturnStmt, c): 
        self.check(ast, (self, c))

    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast: AssignStmt, c): 
        self.check(ast, (self, c))

    ############################################################
    #                         expr visit                       #
    ############################################################
    # op: str, left: Expr, right: Expr
    def visitBinExpr(self, ast: BinExpr, c): 
        self.visit(ast.left, c)
        self.visit(ast.right, c)

        self.check(ast, c)

    # op: str, val: Expr
    def visitUnExpr(self, ast: UnExpr, c): 
        self.visit(ast.val, c)

        self.check(ast, c)
    
    # name: str
    def visitId(self, ast: Id, c): 
        typ = c.get(ast.name, True)
        if typ is None:
            raise Undeclared(Identifier(), ast.name)
        # Identifier nodes are treated specially, as they have to refer to
        # previously defined identifiers in the symbol table.
        ast.typ = typ

    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast: ArrayCell, c): 
        typ = self.apply_subst(c.get(ast.name, True))
        if typ is None:
            raise Undeclared(Identifier(), ast.name)
        if not isinstance(typ, ArrayType):
            raise TypeMismatchInExpression(ast)

        self.check(ast, (self, c))
        
    # explist: List[Expr]
    def visitArrayLit(self, ast: ArrayLit, c): 
        state = self.parentArrlit
        if state is None:
            self.parentArrlit = ast

        list(map(lambda x: self.visit(x, c), ast.explist))

        self.check(ast, self)

        if state is None:
            # reset only if it is the parent arrlit
            self.parentArrlit = None

    # name: str, args: List[Expr]
    def visitFuncCall(self, ast: FuncCall, c): 
        func = c.get(ast.name, True)
        if func is None:
            raise Undeclared(Function(), ast.name)
        if not isinstance(func, FuncType):
            raise TypeMismatchInExpression(ast)
        
        # list(map(lambda x: self.visit(x, c), ast.args))
        self.check(ast, (self, c))
    
    def visitIntegerLit(self, ast, c: 'SymbolTable'):
        ast.typ = IntegerType()
    def visitFloatLit(self, ast, c: 'SymbolTable'): 
        ast.typ = FloatType()
    def visitStringLit(self, ast, c: 'SymbolTable'): 
        ast.typ = StringType()
    def visitBooleanLit(self, ast, c: 'SymbolTable'): 
        ast.typ = BooleanType()
        