"""
 * @author nhphung
"""
# from AST import *
# from Visitor import *
# from StaticError import *
# from SymbolTable import *
# from TypeInferrence import *
from StaticError import *
from functools import *
# from TypeInference import *
from MultiVisitor import *
        
class WrongChildSymbolTable(Exception):
    def __init__(self, s):
        self.message = "Invalid Visit Order With Key: " + s

class SymbolTable:
    # define symbol table for referencing
    def __init__(self, table: dict, parent: 'SymbolTable'=None):
        self.table = table 
        self.parent = parent
        self.children = {}

    def items(self):
        return self.table.items()
    
    def keys(self):
        return self.table.keys()
    
    def values(self):
        return self.table.values()
    
    def get(self, key: str, getAllScope: bool=False):
        # return type for the var/func with scope 
        # depending on getAllScope
        res = self.table.get(key)
        if getAllScope is     True and\
           res         is     None and\
           self.parent is not None:
            return self.parent.get(key, True)
        return res
    
    def add(self, key: str, value):
        # add a pair of key/value
        self.table[key] = value

    # hook the child symboltable for later visit
    def addChild(self, key: str, value: 'SymbolTable'):
        self.children[key] = value

    def getChild(self, key: str):
        res = self.children.get(key)
        if res is None:
            raise WrongChildSymbolTable(key)
        return res
    
    def __str__(self) -> str:
        temp = list(map(lambda x: x[0]+': '+str(x[1]), self.table.items()))
        val = ',\n '.join(temp)
        res = f"{{{val}}}\n"
        for dic in self.children.values():
            res += str(dic)
        return res
    
class Checker(MultipassVisitor):
    def __init__(self, ast):
        super().__init__(ast)
        self.table = None
        self.subst = {}
        self.type_eqs = []

    ############################################################
    #                         some utils                       #
    ############################################################
    def printTypeEqs(self):
        print("Type Equations[\n\t{}\n]".format("\n\t".join([str(eq) for eq in self.type_eqs])))
    def printSubst(self):
        print("Type Substitution[\n\t{}\n]"
              .format("\n\t".join([str(key)+': '+str(val) for key, val in self.subst.items()])))
        
    def apply_subst(self, typ):
        """Applies the unifier subst to typ.
        Returns a type where all occurrences of variables bound in subst
        were replaced (recursively); on failure returns None.
        """
        if self.subst is None:
            return None
        elif len(self.subst) == 0:
            return typ
        # elif isinstance(typ, (BoolType, IntType)):
        #     return typ
        elif isinstance(typ, TypeVar):
            if typ.name in self.subst:
                return self.apply_subst(self.subst[typ.name])
            else:
                return typ
        elif isinstance(typ, FuncType):
            newargtypes = [self.apply_subst(arg) for arg in typ.partype]
            return FuncType(newargtypes,
                            self.apply_subst(typ.rettype))
        elif isinstance(typ, ArrayType):
            newtyp = self.apply_subst(typ.typ)
            return ArrayType(typ.dimensions, newtyp)
        elif isinstance(typ, ParamType):
            return self.apply_subst(typ.partype)
        elif isinstance(typ, StrictType):
            return self.apply_subst(typ.typ)
        return typ
    
    def unify(self, eq):
        self.type_eqs.append(eq)
        subst = unify(eq.left, eq.right, self.subst)
        if subst is None:
            throwError(eq.orig_node)
        self.subst = subst
        # return the subst-ed left hand side
        return self.apply_subst(eq.left)

    ############################################################
    #                                                          #
    #                  preVisit: add type vars and             #
    #                  generate type constraints               #
    #                                                          # 
    ############################################################
    ############################################################
    #                         decl visit                       #
    ############################################################

    # name: str, typ: Type, init: Expr
    def visitVarDecl(self, ast: VarDecl, c: 'SymbolTable'):
        typ = self.apply_subst(ast.init.typ)
        self.unify(TypeEq(ast._typ, typ, ast))
            
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast: FuncDecl, master):
        self.curr = ast.name # mark the function name for return call

        # inherit case
        body = ast.body.body # stmt list from body blockstmt
        sym_tab = self.table.getChild(ast.name)     
        # partype: List[Type], rettype: Type, inherit: str=None
        parent = self.table.get(ast.inherit) # the parent function prototyp
        
        if len(parent.partype) == 0:
            # implicit case
            list(map(lambda x: master.visit(x, sym_tab), body))
            return

        # explicit case
        if len(body) == 0 or isinstance(body[0], CallStmt) and body[0].name == 'super':
            self.visitInherit(parent, sym_tab)

        if  len(body) == 0 or\
            not isinstance(body[0], CallStmt) or\
            (body[0].name != 'preventDefault' and\
             body[0].name != 'super'):
            raise InvalidStatementInFunction(ast.name)
        
        num_args, num_params = len(body[0].args), len(parent.partype) if body[0].name == 'super' else 0
        if num_params > num_args:
            raise TypeMismatchInExpression()
        if num_params < num_args:
            raise TypeMismatchInExpression(body[0].args[num_params])

        for par, arg in zip(parent.partype, body[0].args):
            master.visit(arg, sym_tab)
            self.unify(TypeEq(par, arg.typ, arg))
        
        list(map(lambda x: master.visit(x, sym_tab), body[1:]))

    def visitInherit(self, parent, sym_stack):
        # add the inherit params to symtable
        def isInheritParam(par):
            # so far only params are stored in sym_stack
            if par.inherit is False:
                return False
            if par_visit.get(par.name) is True:
                raise Redeclared(Parameter(), par.name)
            
            par_visit[par.name] = True
            return True
        
        par_visit = {}
        inheritParams = filter(isInheritParam, parent.partype)

        for par in inheritParams:
            if sym_stack.get(par.name) is not None:
                raise Invalid(Parameter(), par.name)
            
            sym_stack.add(par.name, par)

    ############################################################
    #                         stmt visit                       #
    ############################################################

    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast: IfStmt, c: 'SymbolTable'):
        self.unify(TypeEq(ast.cond.typ, BooleanType(), ast))

    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast: AssignStmt, t: tuple):
        master, c = t # untuple t

        master.visit(ast.lhs, c)

        typ = ast.lhs.typ
        if isinstance(typ, ArrayType):
           raise TypeMismatchInStatement(ast)
        
        master.visit(ast.rhs, c)
        self.unify(TypeEq(ast.lhs.typ, ast.rhs.typ, ast))
        
    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast: ForStmt, t: tuple):
        master, c = t # untuple t

        master.visit(ast.init, c)
        self.unify(TypeEq(ast.init.lhs.typ, StrictType(IntegerType()), ast))

        master.visit(ast.cond, c)
        self.unify(TypeEq(ast.cond.typ, BooleanType(), ast))

        master.visit(ast.upd, c)
        self.unify(TypeEq(ast.upd.typ, StrictType(IntegerType()), ast))

        master.visitLoopStmt(ast, c)

    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast: WhileStmt, c: 'SymbolTable'):
        self.unify(TypeEq(ast.cond.typ, BooleanType(), ast))

    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast: DoWhileStmt, c: 'SymbolTable'):
        self.unify(TypeEq(ast.cond.typ, BooleanType(), ast))

    # expr: Expr or None = None
    def visitReturnStmt(self, ast: ReturnStmt, t: tuple):
        master, c = t # untuple t

        if ast.expr is None:
            typ = VoidType()
        else:
            master.visit(ast.expr, c)
            typ = ast.expr.typ
        
        curr_func = self.table.get(self.curr)
        if master.inStmt == 0:
            if master.retOutSide is True:
                return
            master.retOutSide = True
        
        self.unify(TypeEq(curr_func.rettype, typ, ast))

    # name: str, args: List[Expr]
    def visitCallStmt(self, ast: CallStmt, t: tuple):
        # be very careful here, there maybe super n bullshit
        # temporarily skip super n preventDefault n out param bs
        master, c = t # untuple
        func = c.get(ast.name, True)

        if len(func.partype) != len(ast.args):
            raise TypeMismatchInStatement(ast)
        
        for param, arg in zip(func.partype, ast.args):
            master.visit(arg, c)
            self.unify(TypeEq(param, arg.typ, ast))
        
    ############################################################
    #                         expr visit                       #
    ############################################################
    # op: str, left: Expr, right: Expr
    def visitBinExpr(self, ast, c): 
        def widen(ltyp, rtyp, typ):
            if not isinstance(typ, Numeric):
                return typ 
            if isinstance(ltyp, FloatType) or\
               isinstance(rtyp, FloatType):
                return FloatType()
            if isinstance(ltyp, IntegerType) and\
               isinstance(rtyp, IntegerType):
                return IntegerType()
            # cases where both are auto will be error when unify with float
            return ltyp
        
        if ast.op == '::':
            optyp = typ = StringType()
        elif ast.op == '%':
            optyp = typ = StrictType(IntegerType())
        elif ast.op in ['&&', '||']:
            optyp = typ = BooleanType()
        elif ast.op in ['+', '-', '*', '/']:
            optyp = typ = Numeric()
        elif ast.op in ['==', '!=']:
            optyp, typ = Comparable(), BooleanType()
        elif ast.op in ['<', '>', '<=', '>=']:
            optyp, typ = Numeric(), BooleanType()
        
        ltyp = self.unify(TypeEq(ast.left.typ, optyp, ast))
        rtyp = self.unify(TypeEq(ast.right.typ, optyp, ast))

        if isinstance(ltyp, TypeVar) or isinstance(rtyp, TypeVar):
            ltyp = rtyp = self.unify(TypeEq(ltyp, rtyp, ast))
        
        ast.typ = widen(ltyp, rtyp, typ)
        
    # op: str, val: Expr
    def visitUnExpr(self, ast, c: 'SymbolTable'):
        def widen(etyp, typ):
            if not isinstance(typ, Numeric):
                return typ 
            return etyp
        
        if ast.op == '-':
            optyp = typ = Numeric()
        elif ast.op == '!':
            optyp = typ = BooleanType()
        
        etyp = self.unify(TypeEq(ast.val.typ, optyp, ast))
        ast.typ = widen(etyp, typ)

    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast, t: tuple): 
        master, c = t # untuple      
        for ind in ast.cell:
            master.visit(ind, c)
            self.unify(TypeEq(ind.typ, StrictType(IntegerType()), ind))
        
        typ = self.apply_subst(c.get(ast.name, True))
        rows, dims = len(ast.cell), len(typ.dimensions) 
        if rows == dims:
            ast.typ = typ.typ
        elif rows > dims:
            raise TypeMismatchInExpression(ast)
        else:
            ast.typ = ArrayType(typ.dimensions[rows:], typ.typ)

    # explist: List[Expr]
    def visitArrayLit(self, ast, master): 
        def transform(typ):
            # to make sure no coercion happens in type inference
            typ = self.apply_subst(typ)

            if isinstance(typ, TypeVar):
                return typ
            if isinstance(typ, ArrayType):
                return ArrayType(typ.dimensions, transform(typ.typ))
            if isinstance(typ, ParamType):
                return transform(typ.partype)
            return StrictType(typ)
        
        # assumption: no empty arrlit
        var = TypeVar(get_fresh_typename())
        list(map( # this gives a whole different kind of error
                lambda x: self.unify(TypeEq(var, 
                                            transform(x.typ), 
                                            master.parentArrlit)), 
                ast.explist
            ))
        
        typ, exp_dim = self.apply_subst(var), [len(ast.explist)]
        if isinstance(typ, TypeVar):
            dim, new_typ = exp_dim, TypeVar(get_fresh_typename())
        elif not isinstance(typ, ArrayType):
            # typ: raw type
            dim, new_typ = exp_dim, typ
        else:
            # typ: ArrayType(dim, typ)
            dim, new_typ = exp_dim+typ.dimensions, typ.typ
        ast.typ = ArrayType(dim, new_typ)

    # name: str, args: List[Expr]
    def visitFuncCall(self, ast, t: tuple): 
        master, c = t # untuple
        func = c.get(ast.name, True)

        if len(func.partype) != len(ast.args):
            raise TypeMismatchInExpression(ast)
        
        for param, arg in zip(func.partype, ast.args):
            master.visit(arg, c)
            self.unify(TypeEq(param, arg.typ, ast))
        
        ast.typ = func.rettype
        typ = self.apply_subst(ast.typ)
        if isinstance(typ, VoidType):
            raise TypeMismatchInExpression(ast)