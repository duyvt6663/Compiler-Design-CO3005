import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    #########################################################################
    #                           TEST DECLARATION                            #
    #########################################################################
    def test_300_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_301_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))
    #########################################################################
    #                         TEST COMPLEX PROGRAM                          #
    #########################################################################
    def test_303_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304_complex_program(self):
        """More complex program"""
        input = """
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
     printInteger(4);
}"""
        expect = """Program([
\tFuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_306_complex_program(self):
        input = """rJ  : auto  = - B    :: eH   + X     < wfvN   && X    * ! Dv0       ;   t  : auto  = - N0jPYFF    :: ""       ;   mr , l , m7  : array [ 46 , 0 , 0 , 0 ] of integer    ;   l2U : function auto   ( ) { break ;   c , gSuc , Xh  : integer   ;  }    WW , t  : array [ 17 , 4 , 6822_1 , 0 ] of string    ;   B_ : function auto   ( ) inherit IC { continue ;   Gue , BtP_nZ  : integer   ;  }    P : function auto   ( j1 : auto    ) inherit F6KUr { }    W : function auto   ( inherit c : auto    ) inherit jn { }    """
        expect = """Program([
	VarDecl(rJ, AutoType, BinExpr(::, UnExpr(-, B), BinExpr(<, BinExpr(+, eH, X), BinExpr(&&, wfvN, BinExpr(*, X, UnExpr(!, Dv0))))))
	VarDecl(t, AutoType, BinExpr(::, UnExpr(-, N0jPYFF), StringLit()))
	VarDecl(mr, ArrayType([46, 0, 0, 0], IntegerType))
	VarDecl(l, ArrayType([46, 0, 0, 0], IntegerType))
	VarDecl(m7, ArrayType([46, 0, 0, 0], IntegerType))
	FuncDecl(l2U, AutoType, [], None, BlockStmt([BreakStmt(), VarDecl(c, IntegerType), VarDecl(gSuc, IntegerType), VarDecl(Xh, IntegerType)]))
	VarDecl(WW, ArrayType([17, 4, 68221, 0], StringType))
	VarDecl(t, ArrayType([17, 4, 68221, 0], StringType))
	FuncDecl(B_, AutoType, [], IC, BlockStmt([ContinueStmt(), VarDecl(Gue, IntegerType), VarDecl(BtP_nZ, IntegerType)]))
	FuncDecl(P, AutoType, [Param(j1, AutoType)], F6KUr, BlockStmt([]))
	FuncDecl(W, AutoType, [InheritParam(c, AutoType)], jn, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
    #########################################################################
    #                           TEST STATEMENT                              #
    #########################################################################
    def test_305_complex_expr(self):
        """Expression"""
        input = """x:integer = -1+2||"ditmemay"*x&&44::rrow-3-4--2;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(::, BinExpr(&&, BinExpr(||, BinExpr(+, UnExpr(-, IntegerLit(1)), IntegerLit(2)), BinExpr(*, StringLit(ditmemay), x)), IntegerLit(44)), BinExpr(-, BinExpr(-, BinExpr(-, rrow, IntegerLit(3)), IntegerLit(4)), UnExpr(-, IntegerLit(2)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
    def test_307_operands(self):
        """Expression"""
        input = """x:integer = (213+_djw::kew(ditmemay))*(srr::kek);"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, BinExpr(::, BinExpr(+, IntegerLit(213), _djw), FuncCall(kew, [ditmemay])), BinExpr(::, srr, kek)))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
    def test_308_scalar_var(self):
        """scalar variable and for loop"""
        input = """K6y : function void  ( ) inherit sz { wc  : array [ 43781 ] of integer     = gB0   && Rn     :: u5n ( )       ;  }    d4 , wl  : integer   ;   g3D  : array [ 2_0 ] of string    ;   a : function void  ( inherit out g : auto    ) inherit Z { for ( j = Mji   * P      , ""     :: - f    != lgw   || T      , J   + d     :: t   || k9    < _     ) return ;     oz , p  : auto  = s ( )    < - s      , Sg   % B    == - IZ       ;  }"""
        expect = """Program([
	FuncDecl(K6y, VoidType, [], sz, BlockStmt([VarDecl(wc, ArrayType([43781], IntegerType), BinExpr(::, BinExpr(&&, gB0, Rn), FuncCall(u5n, [])))]))
	VarDecl(d4, IntegerType)
	VarDecl(wl, IntegerType)
	VarDecl(g3D, ArrayType([20], StringType))
	FuncDecl(a, VoidType, [InheritOutParam(g, AutoType)], Z, BlockStmt([ForStmt(AssignStmt(j, BinExpr(*, Mji, P)), BinExpr(::, StringLit(), BinExpr(!=, UnExpr(-, f), BinExpr(||, lgw, T))), BinExpr(::, BinExpr(+, J, d), BinExpr(<, BinExpr(||, t, k9), _)), ReturnStmt()), VarDecl(oz, AutoType, BinExpr(<, FuncCall(s, []), UnExpr(-, s))), VarDecl(p, AutoType, BinExpr(==, BinExpr(%, Sg, B), UnExpr(-, IZ)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    def test_309_scalar_var(self):
        """scalar variable and assign statement"""
        input = """jZ : function auto   ( ) inherit ho { iq = jG   - E     :: ! H    == s3Mc ( )      ;   for ( AA = ! bJkg    == l   - vk      , ! x      , - AS     :: ht6pi ( )    < ! o      ) _H ( )  ; keke[423,2+jj::boo]=_329(duca);     }"""
        expect = """Program([
	FuncDecl(jZ, AutoType, [], ho, BlockStmt([AssignStmt(iq, BinExpr(::, BinExpr(-, jG, E), BinExpr(==, UnExpr(!, H), FuncCall(s3Mc, [])))), ForStmt(AssignStmt(AA, BinExpr(==, UnExpr(!, bJkg), BinExpr(-, l, vk))), UnExpr(!, x), BinExpr(::, UnExpr(-, AS), BinExpr(<, FuncCall(ht6pi, []), UnExpr(!, o))), CallStmt(_H, )), AssignStmt(ArrayCell(keke, [IntegerLit(423), BinExpr(::, BinExpr(+, IntegerLit(2), jj), boo)]), FuncCall(_329, [duca]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
    def test_310_funcall_callstmt(self):
        """scalar variable and assign statement"""
        input = """jZ : function auto   ( ) inherit ho { calm(dem, as::3928<_dw,_bitch(_dun(sun,!hux--m))); x:string=lemw(bu,tu,9,_0(_0));}"""
        expect = """Program([
	FuncDecl(jZ, AutoType, [], ho, BlockStmt([CallStmt(calm, dem, BinExpr(::, as, BinExpr(<, IntegerLit(3928), _dw)), FuncCall(_bitch, [FuncCall(_dun, [sun, BinExpr(-, UnExpr(!, hux), UnExpr(-, m))])])), VarDecl(x, StringType, FuncCall(lemw, [bu, tu, IntegerLit(9), FuncCall(_0, [_0])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
    def test_311_ifstmt(self):
        """if statement"""
        input = """kw: function auto (){
            if ( GP ( )     :: Wd   + E    != x   + d4      ) 
                if (x > 23/meme)
                    if (dumm != dummew(dumew_(3)))
                        calm(stem);
            else bN ( )  ;
        }"""
        expect = """Program([
	FuncDecl(kw, AutoType, [], None, BlockStmt([IfStmt(BinExpr(::, FuncCall(GP, []), BinExpr(!=, BinExpr(+, Wd, E), BinExpr(+, x, d4))), IfStmt(BinExpr(>, x, BinExpr(/, IntegerLit(23), meme)), IfStmt(BinExpr(!=, dumm, FuncCall(dummew, [FuncCall(dumew_, [IntegerLit(3)])])), CallStmt(calm, stem), CallStmt(bN, ))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
    def test_312_whilestmt(self):
        """while/do while statement"""
        input = """aa: function void(){
            do { 
                j , y  : string   ; 
                while( yolov == mum*32.1e9)
                    return 922;
            }  
            while ( yy   / s    >= U   / IAliRy      ) ;
        }"""
        expect = """Program([
	FuncDecl(aa, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(>=, BinExpr(/, yy, s), BinExpr(/, U, IAliRy)), BlockStmt([VarDecl(j, StringType), VarDecl(y, StringType), WhileStmt(BinExpr(==, yolov, BinExpr(*, mum, FloatLit(32100000000.0))), ReturnStmt(IntegerLit(922)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    #########################################################################
    #                           TEST CONVERT LITERAL                        #
    #########################################################################
    def test_313_literal(self):
        """Literal"""
        input = """
        dd:string= 1.e3;
        d:string= .1e2;
        fl:float=1_1.1e1;
        ed:float=.e4;
        stri:string="11";
        boo:boolean=true;
        arr:array[2,3] of integer ={2,d/4,9};
        """
        expect = """Program([
	VarDecl(dd, StringType, FloatLit(1000.0))
	VarDecl(d, StringType, FloatLit(10.0))
	VarDecl(fl, FloatType, FloatLit(111.0))
	VarDecl(ed, FloatType, FloatLit(0))
	VarDecl(stri, StringType, StringLit(11))
	VarDecl(boo, BooleanType, BooleanLit(True))
	VarDecl(arr, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(2), BinExpr(/, d, IntegerLit(4)), IntegerLit(9)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))