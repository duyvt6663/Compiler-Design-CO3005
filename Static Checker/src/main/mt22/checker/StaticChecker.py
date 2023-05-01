from Visitor import *
from StaticError import *
import itertools
from AST import *
import copy
from functools import *

############################################################
#                                                          #
#                        TYPE INFERENCE                    #
#                        TYPE INFERENCE                    #
#                                                          # 
############################################################
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
    
############################################################
#                        TYPE VAR GEN                      #
############################################################
# Global counter to produce unique type names.
_typecounter = itertools.count(start=0)

def get_fresh_typename():
    """Creates a fresh typename that will be unique throughout the program."""
    return 't{}'.format(next(_typecounter))

# This function is useful for determinism in tests.
def reset_type_counter():
    global _typecounter
    _typecounter = itertools.count(start=0)
############################################################
#                         NEW TYPES                        #
############################################################
# define func type for symbol table
class FuncType(Type):
    def __init__(self, partype: List[Type], rettype: Type, inherit: str=None):
        self.partype = partype # param types
        self.rettype = rettype # return type
        self.inherit = inherit
    def __str__(self):
        return self.__class__.__name__
    
# define param type for symbol table
class ParamType(Type):
    def __init__(self, partype: Type, out: bool=False, inherit: bool=False, name: str=None):
        self.partype = partype # param type
        self.out = out
        self.inherit = inherit
        self.name = name
    def __str__(self):
        return self.__class__.__name__
    def __eq__(self, other) -> bool:
        return self.partype == other.partype\
                if isinstance(other, ParamType) else\
                (isinstance(other, Numeric) and self.partype == Numeric()) or\
                (isinstance(other, Comparable) and self.partype == Comparable()) or\
                self.partype == other
class StrictType(Type):
    # type with no coercion
    def __init__(self, typ: Type):
        self.typ = typ
    def __str__(self):
        return self.__class__.__name__
    def __eq__(self, other) -> bool:
        return type(self.typ) == type(other.typ)\
                if isinstance(other, StrictType) else\
                (isinstance(other, Numeric) and self.typ == Numeric()) or\
                (isinstance(other, Comparable) and self.typ == Comparable()) or\
                (isinstance(other, ParamType) and type(self.typ) == type(other.partype)) or\
                (type(self.typ) == type(other))
    
class Numeric(Type):
    def __eq__(self, other) -> bool:
        return isinstance(other, FloatType) or isinstance(other, IntegerType)
    def __str__(self):
        return self.__class__.__name__
    
class Comparable(Type):
    # !=, ==
    def __eq__(self, other) -> bool:
        return isinstance(other, FloatType) or isinstance(other, IntegerType) or isinstance(other, BooleanType)
    def __str__(self):
        return self.__class__.__name__
    
class TypeVar(Type):
    """A type variable."""
    def __init__(self, name, isNum=False, isComp=False):
        self.name = name
        self.isNum = isNum 
        self.isComp = isComp

    def __str__(self):
        return self.name

    __repr__ = __str__

    def __eq__(self, other):
        return (self.isNum and isinstance(other, Numeric)) or\
            (self.isComp and isinstance(other, Comparable)) or\
            (type(self) == type(other) and self.name == other.name)
    
class TypeEq:
    """A type equation between two types: left and right.
    orig_node is the original AST node from which this equation was derived, for
    debugging.
    """
    def __init__(self, left, right, orig_node):
        self.left = left
        self.right = right
        self.orig_node = orig_node
    def __reduce_orig__(self):
        res = str(self.orig_node)
        return res if len(res) <= 50 else res[:50]+'...'
    def __str__(self):
        return '{} :: {} [from {}]'.format(self.left,
                                           self.right, self.__reduce_orig__())

    __repr__ = __str__
############################################################
#                         __eq__ method                    #
############################################################
def equalNum(self, other):
    if isinstance(other, ParamType):
        return self == other.partype
    elif isinstance(other, Numeric) or\
        (isinstance(other, Comparable) and isinstance(self, IntegerType)):
        return True
    elif isinstance(other, StrictType):
        return type(self) is type(other.typ)
    return type(self) is type(other) or (isinstance(self, FloatType) and isinstance(other, IntegerType))
def equalComp(self, other):
    if isinstance(other, ParamType):
        return self == other.partype
    elif isinstance(other, Comparable):
        return True
    return type(self) is type(other)
def equal(self, other):
    return self == other.partype if isinstance(other, ParamType) else type(self) is type(other)
VoidType.__eq__ = StringType.__eq__ = equal
FloatType.__eq__ = IntegerType.__eq__ = equalNum
BooleanType.__eq__ = equalComp

############################################################
#                      unification algo                    #
############################################################
def unify(typ_x, typ_y, subst):
    """Unify two types typ_x and typ_y, with initial subst.
    Returns a subst (map of name->Type) that unifies typ_x and typ_y, or None if
    they can't be unified. Pass subst={} if no subst are initially
    known. Note that {} means valid (but empty) subst.
    """
    # to maintain inference position due to type coercion
    # need to apply_subst to typ_y first
    typ_y = apply_subst(typ_y, subst)
    if subst is None:
        return None
    elif typ_x == typ_y:
        return subst
    elif isinstance(typ_x, ParamType) and isinstance(typ_x.partype, TypeVar):
        return unify_variable(typ_x.partype, typ_y, subst)
    elif isinstance(typ_y, ParamType) and isinstance(typ_y.partype, TypeVar):
        return unify_variable(typ_y.partype, typ_x, subst)
    elif isinstance(typ_x, TypeVar):
        return unify_variable(typ_x, typ_y, subst)
    elif isinstance(typ_y, TypeVar):
        return unify_variable(typ_y, typ_x, subst)
    # typ_y is funcCall with arguments
    elif isinstance(typ_x, FuncType) and isinstance(typ_y, FuncType):
        if len(typ_x.partype) != len(typ_y.partype):
            return None
        
        # subst = unify(typ_x.rettype, typ_y.rettype, subst)
        for i in range(len(typ_x.partype)):
            subst = unify(typ_x.partype[i], typ_y.partype[i], subst)
            if subst is None:
                return None
        return subst
    
    elif isinstance(typ_x, ArrayType) and isinstance(typ_y, ArrayType):
        if len(typ_x.dimensions) != len(typ_y.dimensions) or\
            any(x != y for x, y in zip(typ_x.dimensions, typ_y.dimensions)):
            return None 
        
        subst = unify(typ_x.typ, typ_y.typ, subst)
        return subst
    
    return None

def occurs_check(v, typ, subst):
    """Does the variable v occur anywhere inside typ?
    Variables in typ are looked up in subst and the check is applied
    recursively.
    """
    assert isinstance(v, TypeVar)
    if v == typ:
        return True
    elif isinstance(typ, TypeVar) and typ.name in subst:
        return occurs_check(v, subst[typ.name], subst)
    elif isinstance(typ, FuncType):
        return (occurs_check(v, typ.rettype, subst) or
                any(occurs_check(v, arg, subst) for arg in typ.partype))
    elif isinstance(typ, ArrayType):
        return occurs_check(v, typ.typ, subst)
    else:
        return False
    
def unify_variable(v, typ, subst):
    """Unifies variable v with type typ, using subst.
    Returns updated subst or None on failure.
    """
    assert isinstance(v, TypeVar)
    if v.name in subst:
        return unify(subst[v.name], typ, subst)
    if isinstance(typ, TypeVar) and typ.name in subst:
        return unify(v, subst[typ.name], subst)
    if occurs_check(v, typ, subst):
        return None
    # v is not yet in subst and can't simplify x. Extend subst.
    if isinstance(typ, Numeric):
        v.isNum = True
        return subst
    if isinstance(typ, Comparable):
        v.isComp = True 
        return subst
    # the following check requires skillful comparisons
    if v.isNum is True and not(typ == Numeric()):
        return None
    if v.isComp is True and not(typ == Comparable()):
        return None
    return {**subst, v.name: typ}

def unify_all_equations(eqs):
    """Unifies all type equations in the sequence eqs.
    Returns a substitution (most general unifier).
    """
    subst = {}
    for eq in eqs:
        subst = unify(eq.left, eq.right, subst)
        if subst is None:
            throwError(eq.orig_node)
    return subst

def throwError(node):
    if isinstance(node, ArrayLit):
        raise IllegalArrayLiteral(node)
    elif isinstance(node, Expr):
        raise TypeMismatchInExpression(node)
    elif isinstance(node, Stmt):
        raise TypeMismatchInStatement(node)
    elif isinstance(node, Decl):
        raise TypeMismatchInVarDecl(node)

def apply_subst(typ, subst):
    """Applies the unifier subst to typ.
    Returns a type where all occurrences of variables bound in subst
    were replaced (recursively); on failure returns None. On StrictType does not 
    strip the outer layer, thus this method differs from one in TypeCheck.py
    """
    if subst is None:
        return None
    elif len(subst) == 0:
        return typ
    # elif isinstance(typ, (BoolType, IntType)):
    #     return typ
    elif isinstance(typ, TypeVar):
        if typ.name in subst:
            return apply_subst(subst[typ.name], subst)
        else:
            return typ
    elif isinstance(typ, FuncType):
        newargtypes = [apply_subst(arg, subst) for arg in typ.partype]
        return FuncType(newargtypes, apply_subst(typ.rettype, subst))
    elif isinstance(typ, ArrayType):
        newtyp = apply_subst(typ.typ, subst)
        return ArrayType(typ.dimensions, newtyp)
    elif isinstance(typ, ParamType):
        return apply_subst(typ.partype, subst)
    return typ

############################################################
#                                                          #
#                          SYMBOL TABLE                    #
#                          SYMBOL TABLE                    #
#                                                          # 
############################################################

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
    
############################################################
#                                                          #
#                        STATIC CHECKER                    #
#                        STATIC CHECKER                    #
#                                                          # 
############################################################

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
        return 
    
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
        if typ is None or isinstance(typ, FuncType):
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
            if self.table.get(ast.name) is not None:
                raise TypeMismatchInExpression(ast)
            raise Undeclared(Function(), ast.name)
        
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