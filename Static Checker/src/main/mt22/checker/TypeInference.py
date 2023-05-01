import itertools
import sys
import os
if not '../utils/' in sys.path:
    sys.path.append('../utils/')
from AST import *
from StaticError import *

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

if __name__ == "__main__":
    f = FloatType()
    i = IntegerType()
    p = ParamType(IntegerType(), False, False)
    p2 = ParamType(FloatType(), False, False)
    s = StringType()
    st = BooleanLit(True)
    im = IntegerLit(2)
    print(p2 == i)