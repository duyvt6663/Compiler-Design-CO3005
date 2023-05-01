import unittest
from TestUtils import TestAST

class ASTGenSuite(unittest.TestCase):
	def test_301(self):
		input = """q , k , Hv , BrQa  : auto  ;   """
		expect = """Program([
	VarDecl(q, AutoType)
	VarDecl(k, AutoType)
	VarDecl(Hv, AutoType)
	VarDecl(BrQa, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 301))

	def test_302(self):
		input = """A : function auto  ( inherit out LW : array [ 0 ] of string     , out Ob : float    , OTr : auto   , out X : auto    ) { WX  : auto  = ""     :: T   || i       ;  }    """
		expect = """Program([
	FuncDecl(A, AutoType, [InheritOutParam(LW, ArrayType([0], StringType)), OutParam(Ob, FloatType), Param(OTr, AutoType), OutParam(X, AutoType)], None, BlockStmt([VarDecl(WX, AutoType, BinExpr(::, StringLit(), BinExpr(||, Id(T), Id(i))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 302))

	def test_303(self):
		input = """z , S , D , HG , VN  : auto  = - ! ! F      != { }       , ! O04kp   || f     + N   && WzJ0    * ! Sma      < pAJi   * ZS    + - c     - - K    % ! scX        , ! - 0      > 0      , Clp    :: ! - zg     && - TY   && MC      == 0    + L   % ux     * - lZ ( )        , - H   * wIz    - R   + iE      > ! SE4       ;   U : function auto  ( ) { do { t , ZM , s  : array [ 0 , 0 , 4 , 0 ] of float    ;  { }   }  while ( ""    >= My     ) ;   while ( k   % MPK     :: CG   - qQ    <= ay   + v      ) continue ;     }    fkHsG  : float   = 0    < ! ! y    && j        ;   E  : integer   ;   """
		expect = """Program([
	VarDecl(z, AutoType, BinExpr(!=, UnExpr(-, UnExpr(!, UnExpr(!, Id(F)))), ArrayLit([])))
	VarDecl(S, AutoType, BinExpr(<, BinExpr(&&, BinExpr(||, UnExpr(!, Id(O04kp)), BinExpr(+, Id(f), Id(N))), BinExpr(*, Id(WzJ0), UnExpr(!, Id(Sma)))), BinExpr(-, BinExpr(+, BinExpr(*, Id(pAJi), Id(ZS)), UnExpr(-, Id(c))), BinExpr(%, UnExpr(-, Id(K)), UnExpr(!, Id(scX))))))
	VarDecl(D, AutoType, BinExpr(>, UnExpr(!, UnExpr(-, IntegerLit(0))), IntegerLit(0)))
	VarDecl(HG, AutoType, BinExpr(::, Id(Clp), BinExpr(==, BinExpr(&&, BinExpr(&&, UnExpr(!, UnExpr(-, Id(zg))), UnExpr(-, Id(TY))), Id(MC)), BinExpr(+, IntegerLit(0), BinExpr(*, BinExpr(%, Id(L), Id(ux)), UnExpr(-, FuncCall(lZ, [])))))))
	VarDecl(VN, AutoType, BinExpr(>, BinExpr(+, BinExpr(-, BinExpr(*, UnExpr(-, Id(H)), Id(wIz)), Id(R)), Id(iE)), UnExpr(!, Id(SE4))))
	FuncDecl(U, AutoType, [], None, BlockStmt([DoWhileStmt(BinExpr(>=, StringLit(), Id(My)), BlockStmt([VarDecl(t, ArrayType([0, 0, 4, 0], FloatType)), VarDecl(ZM, ArrayType([0, 0, 4, 0], FloatType)), VarDecl(s, ArrayType([0, 0, 4, 0], FloatType)), BlockStmt([])])), WhileStmt(BinExpr(::, BinExpr(%, Id(k), Id(MPK)), BinExpr(<=, BinExpr(-, Id(CG), Id(qQ)), BinExpr(+, Id(ay), Id(v)))), ContinueStmt())]))
	VarDecl(fkHsG, FloatType, BinExpr(<, IntegerLit(0), BinExpr(&&, UnExpr(!, UnExpr(!, Id(y))), Id(j))))
	VarDecl(E, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 303))

	def test_304(self):
		input = """T6  : array [ 3 ] of boolean    = z   >= - ! Bj   || R         ;   """
		expect = """Program([
	VarDecl(T6, ArrayType([3], BooleanType), BinExpr(>=, Id(z), BinExpr(||, UnExpr(-, UnExpr(!, Id(Bj))), Id(R))))
])"""
		self.assertTrue(TestAST.test(input, expect, 304))

	def test_305(self):
		input = """h : function void ( q : array [ 0 ] of integer     , inherit iAD : boolean     ) inherit o { for ( p  = Do   * bU     :: ""    != Y   - r_      , S    :: dP   * I      , ! jH8tX    < H    :: kPmZ   % C      ) continue ;     }    wd : function auto  ( wgY3u : float    , out y_ola : auto    ) inherit h5T { }    Gn4O , B , g , gK  : auto  = ! r   * y7    * - Xp      == ! - bzQV   - UG        , Dp33    :: Z   + eG    || ! Je     - ! ! h        , - dH ( )     > ! ! h    + _   || w       :: - ""    + syeOK   % DI        , b3   + E    - - Apj     / ! ut71S   + J_      < cEYFojXbZO   || M    + RZ    - FLM   % oR1    && ! g       :: ! t       ;   KOVG7 : function void ( inherit r : array [ 0 , 0 ] of integer     , out M : array [ 56_6_2 , 18 ] of float      ) { }    n : function void ( ) inherit H { m  : auto  ;  }    t3H , qS , A  : boolean   ;   K : function void ( out L : auto    ) inherit N { }    """
		expect = """Program([
	FuncDecl(h, VoidType, [Param(q, ArrayType([0], IntegerType)), InheritParam(iAD, BooleanType)], o, BlockStmt([ForStmt(AssignStmt(Id(p), BinExpr(::, BinExpr(*, Id(Do), Id(bU)), BinExpr(!=, StringLit(), BinExpr(-, Id(Y), Id(r_))))), BinExpr(::, Id(S), BinExpr(*, Id(dP), Id(I))), BinExpr(::, BinExpr(<, UnExpr(!, Id(jH8tX)), Id(H)), BinExpr(%, Id(kPmZ), Id(C))), ContinueStmt())]))
	FuncDecl(wd, AutoType, [Param(wgY3u, FloatType), OutParam(y_ola, AutoType)], h5T, BlockStmt([]))
	VarDecl(Gn4O, AutoType, BinExpr(==, BinExpr(*, BinExpr(*, UnExpr(!, Id(r)), Id(y7)), UnExpr(-, Id(Xp))), BinExpr(-, UnExpr(!, UnExpr(-, Id(bzQV))), Id(UG))))
	VarDecl(B, AutoType, BinExpr(::, Id(Dp33), BinExpr(||, BinExpr(+, Id(Z), Id(eG)), BinExpr(-, UnExpr(!, Id(Je)), UnExpr(!, UnExpr(!, Id(h)))))))
	VarDecl(g, AutoType, BinExpr(::, BinExpr(>, UnExpr(-, FuncCall(dH, [])), BinExpr(||, BinExpr(+, UnExpr(!, UnExpr(!, Id(h))), Id(_)), Id(w))), BinExpr(+, UnExpr(-, StringLit()), BinExpr(%, Id(syeOK), Id(DI)))))
	VarDecl(gK, AutoType, BinExpr(::, BinExpr(<, BinExpr(+, BinExpr(-, BinExpr(+, Id(b3), Id(E)), BinExpr(/, UnExpr(-, Id(Apj)), UnExpr(!, Id(ut71S)))), Id(J_)), BinExpr(&&, BinExpr(||, Id(cEYFojXbZO), BinExpr(-, BinExpr(+, Id(M), Id(RZ)), BinExpr(%, Id(FLM), Id(oR1)))), UnExpr(!, Id(g)))), UnExpr(!, Id(t))))
	FuncDecl(KOVG7, VoidType, [InheritParam(r, ArrayType([0, 0], IntegerType)), OutParam(M, ArrayType([5662, 18], FloatType))], None, BlockStmt([]))
	FuncDecl(n, VoidType, [], H, BlockStmt([VarDecl(m, AutoType)]))
	VarDecl(t3H, BooleanType)
	VarDecl(qS, BooleanType)
	VarDecl(A, BooleanType)
	FuncDecl(K, VoidType, [OutParam(L, AutoType)], N, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 305))

	def test_306(self):
		input = """O , t  : array [ 0 , 3 , 8_3 ] of string    ;   H8j2k : function void ( ) { p3 ( )  ;   a  = n ( )    != em ( )      ;   break ;   return X   * H    <= - C     :: ""      ;   }    """
		expect = """Program([
	VarDecl(O, ArrayType([0, 3, 83], StringType))
	VarDecl(t, ArrayType([0, 3, 83], StringType))
	FuncDecl(H8j2k, VoidType, [], None, BlockStmt([CallStmt(p3, ), AssignStmt(Id(a), BinExpr(!=, FuncCall(n, []), FuncCall(em, []))), BreakStmt(), ReturnStmt(BinExpr(::, BinExpr(<=, BinExpr(*, Id(X), Id(H)), UnExpr(-, Id(C))), StringLit()))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 306))

	def test_307(self):
		input = """U  : auto  ;   W  : float   = K      ;   """
		expect = """Program([
	VarDecl(U, AutoType)
	VarDecl(W, FloatType, Id(K))
])"""
		self.assertTrue(TestAST.test(input, expect, 307))

	def test_308(self):
		input = """VJguc , lT , p  : integer   ;   """
		expect = """Program([
	VarDecl(VJguc, IntegerType)
	VarDecl(lT, IntegerType)
	VarDecl(p, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 308))

	def test_309(self):
		input = """t2Q8 : function void ( ) { }    """
		expect = """Program([
	FuncDecl(t2Q8, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 309))

	def test_310(self):
		input = """cU  : auto  = ! ! - B      >= - ! Kc    && q5   + BWzbe4         ;   """
		expect = """Program([
	VarDecl(cU, AutoType, BinExpr(>=, UnExpr(!, UnExpr(!, UnExpr(-, Id(B)))), BinExpr(&&, UnExpr(-, UnExpr(!, Id(Kc))), BinExpr(+, Id(q5), Id(BWzbe4)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 310))

	def test_311(self):
		input = """K : function integer   ( inherit out B : array [ 6 , 0 , 0 ] of integer      ) { while ( N_   % k     :: eF   * y9Pe8GW      ) break ;     p , q  : auto  ;  }    """
		expect = """Program([
	FuncDecl(K, IntegerType, [InheritOutParam(B, ArrayType([6, 0, 0], IntegerType))], None, BlockStmt([WhileStmt(BinExpr(::, BinExpr(%, Id(N_), Id(k)), BinExpr(*, Id(eF), Id(y9Pe8GW))), BreakStmt()), VarDecl(p, AutoType), VarDecl(q, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 311))

	def test_312(self):
		input = """q6S , M3l  : array [ 0 ] of float    = O   && Nl    * NNGV   && M     * tyvQ5d   - KKiW    || _   % Wv       :: ! CciSK    + iid   + rKZ     && ! Osic_C5    + Vh   / kS8        , - - L3d   % IAQ       :: ! ! t   * r         ;   Yt : function string   ( ) inherit hGUmE { oUjE  : integer   = d ( )     :: K   || S    > nK   + F       ;  }    ot : function void ( eM5mZiW : array [ 0 ] of integer      ) { }    L1 : function void ( inherit at : integer    , inherit mV : float    , inherit U : auto   , out L7Q : auto   , inherit Ch : array [ 5725 ] of integer     , out o4 : float    , V2 : auto    ) { }    X9 : function auto  ( ) { }    j  : array [ 0 ] of integer    ;   N : function auto  ( ) { I , G9  : auto  = _Y2Q_   * M    < z9   + EVVa     :: ""      , ! eQG    < ! Oe       ;  if ( ! GCp     :: - h      ) I ( )  ;   else return ;     myNfar ( )  ;   }    OC  : auto  ;   """
		expect = """Program([
	VarDecl(q6S, ArrayType([0], FloatType), BinExpr(::, BinExpr(||, BinExpr(&&, BinExpr(&&, Id(O), BinExpr(*, Id(Nl), Id(NNGV))), BinExpr(-, BinExpr(*, Id(M), Id(tyvQ5d)), Id(KKiW))), BinExpr(%, Id(_), Id(Wv))), BinExpr(&&, BinExpr(+, BinExpr(+, UnExpr(!, Id(CciSK)), Id(iid)), Id(rKZ)), BinExpr(+, UnExpr(!, Id(Osic_C5)), BinExpr(/, Id(Vh), Id(kS8))))))
	VarDecl(M3l, ArrayType([0], FloatType), BinExpr(::, BinExpr(%, UnExpr(-, UnExpr(-, Id(L3d))), Id(IAQ)), BinExpr(*, UnExpr(!, UnExpr(!, Id(t))), Id(r))))
	FuncDecl(Yt, StringType, [], hGUmE, BlockStmt([VarDecl(oUjE, IntegerType, BinExpr(::, FuncCall(d, []), BinExpr(>, BinExpr(||, Id(K), Id(S)), BinExpr(+, Id(nK), Id(F)))))]))
	FuncDecl(ot, VoidType, [Param(eM5mZiW, ArrayType([0], IntegerType))], None, BlockStmt([]))
	FuncDecl(L1, VoidType, [InheritParam(at, IntegerType), InheritParam(mV, FloatType), InheritParam(U, AutoType), OutParam(L7Q, AutoType), InheritParam(Ch, ArrayType([5725], IntegerType)), OutParam(o4, FloatType), Param(V2, AutoType)], None, BlockStmt([]))
	FuncDecl(X9, AutoType, [], None, BlockStmt([]))
	VarDecl(j, ArrayType([0], IntegerType))
	FuncDecl(N, AutoType, [], None, BlockStmt([VarDecl(I, AutoType, BinExpr(::, BinExpr(<, BinExpr(*, Id(_Y2Q_), Id(M)), BinExpr(+, Id(z9), Id(EVVa))), StringLit())), VarDecl(G9, AutoType, BinExpr(<, UnExpr(!, Id(eQG)), UnExpr(!, Id(Oe)))), IfStmt(BinExpr(::, UnExpr(!, Id(GCp)), UnExpr(-, Id(h))), CallStmt(I, ), ReturnStmt()), CallStmt(myNfar, )]))
	VarDecl(OC, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 312))

	def test_313(self):
		input = """FlO , J , p6 , a , bw3  : boolean   = VZ   * o2I    || - zU     || k   && sRc    && ! iM        , ! l   - qX    + CU ( )      == - dn    + Ds   - i     % Uo ( )    * ! u        , Odc   + j    % Y_s   || U     + ! Qh    || X   % X      < ! - tMD   && g       :: YDac ( )      , ! ""     / _   && W   / f      == J   || q    && - _     || LN ( )    + Wge   / Dd       :: - ! r     || lZ      , nL   && y    && ""     + c_   + k4y    - kt   / jQ9       :: XFE3      ;   s : function void ( inherit b : auto    ) inherit ly { sl  : float   = - N       ;  b4  : auto  ;  }    """
		expect = """Program([
	VarDecl(FlO, BooleanType, BinExpr(&&, BinExpr(&&, BinExpr(||, BinExpr(||, BinExpr(*, Id(VZ), Id(o2I)), UnExpr(-, Id(zU))), Id(k)), Id(sRc)), UnExpr(!, Id(iM))))
	VarDecl(J, BooleanType, BinExpr(==, BinExpr(+, BinExpr(-, UnExpr(!, Id(l)), Id(qX)), FuncCall(CU, [])), BinExpr(-, BinExpr(+, UnExpr(-, Id(dn)), Id(Ds)), BinExpr(*, BinExpr(%, Id(i), FuncCall(Uo, [])), UnExpr(!, Id(u))))))
	VarDecl(p6, BooleanType, BinExpr(::, BinExpr(<, BinExpr(||, BinExpr(||, BinExpr(+, Id(Odc), BinExpr(%, Id(j), Id(Y_s))), BinExpr(+, Id(U), UnExpr(!, Id(Qh)))), BinExpr(%, Id(X), Id(X))), BinExpr(&&, UnExpr(!, UnExpr(-, Id(tMD))), Id(g))), FuncCall(YDac, [])))
	VarDecl(a, BooleanType, BinExpr(::, BinExpr(==, BinExpr(&&, BinExpr(/, UnExpr(!, StringLit()), Id(_)), BinExpr(/, Id(W), Id(f))), BinExpr(||, BinExpr(&&, BinExpr(||, Id(J), Id(q)), UnExpr(-, Id(_))), BinExpr(+, FuncCall(LN, []), BinExpr(/, Id(Wge), Id(Dd))))), BinExpr(||, UnExpr(-, UnExpr(!, Id(r))), Id(lZ))))
	VarDecl(bw3, BooleanType, BinExpr(::, BinExpr(&&, BinExpr(&&, Id(nL), Id(y)), BinExpr(-, BinExpr(+, BinExpr(+, StringLit(), Id(c_)), Id(k4y)), BinExpr(/, Id(kt), Id(jQ9)))), Id(XFE3)))
	FuncDecl(s, VoidType, [InheritParam(b, AutoType)], ly, BlockStmt([VarDecl(sl, FloatType, UnExpr(-, Id(N))), VarDecl(b4, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 313))

	def test_314(self):
		input = """EK  : auto  = ! H   || BPU    || _ln   && F__       :: - - wR     * - g   + qWg      == ! sP    && - hKE     || ! li        ;   """
		expect = """Program([
	VarDecl(EK, AutoType, BinExpr(::, BinExpr(&&, BinExpr(||, BinExpr(||, UnExpr(!, Id(H)), Id(BPU)), Id(_ln)), Id(F__)), BinExpr(==, BinExpr(+, BinExpr(*, UnExpr(-, UnExpr(-, Id(wR))), UnExpr(-, Id(g))), Id(qWg)), BinExpr(||, BinExpr(&&, UnExpr(!, Id(sP)), UnExpr(-, Id(hKE))), UnExpr(!, Id(li))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 314))

	def test_315(self):
		input = """h : function boolean   ( ) inherit rp5v { }    l5 , Cw7 , D  : auto  ;   x , H , Cdv7u  : integer   = v ( )    / fc   + v     % fuA   || k    % ! cc      != T   && k    || X   - M     * - ""       :: - ! - n      >= B ( )      , ! b    * d   && r     + ! A    - C1   && Zl4K       :: s ( )    || ZWU5BlM   + y9x    + o   && GX      >= - 5       , ! YN   + v     - D       ;   """
		expect = """Program([
	FuncDecl(h, BooleanType, [], rp5v, BlockStmt([]))
	VarDecl(l5, AutoType)
	VarDecl(Cw7, AutoType)
	VarDecl(D, AutoType)
	VarDecl(x, IntegerType, BinExpr(::, BinExpr(!=, BinExpr(||, BinExpr(+, BinExpr(/, FuncCall(v, []), Id(fc)), BinExpr(%, Id(v), Id(fuA))), BinExpr(%, Id(k), UnExpr(!, Id(cc)))), BinExpr(||, BinExpr(&&, Id(T), Id(k)), BinExpr(-, Id(X), BinExpr(*, Id(M), UnExpr(-, StringLit()))))), BinExpr(>=, UnExpr(-, UnExpr(!, UnExpr(-, Id(n)))), FuncCall(B, []))))
	VarDecl(H, IntegerType, BinExpr(::, BinExpr(&&, BinExpr(&&, BinExpr(*, UnExpr(!, Id(b)), Id(d)), BinExpr(-, BinExpr(+, Id(r), UnExpr(!, Id(A))), Id(C1))), Id(Zl4K)), BinExpr(>=, BinExpr(&&, BinExpr(||, FuncCall(s, []), BinExpr(+, BinExpr(+, Id(ZWU5BlM), Id(y9x)), Id(o))), Id(GX)), UnExpr(-, IntegerLit(5)))))
	VarDecl(Cdv7u, IntegerType, BinExpr(-, BinExpr(+, UnExpr(!, Id(YN)), Id(v)), Id(D)))
])"""
		self.assertTrue(TestAST.test(input, expect, 315))

	def test_316(self):
		input = """_ , H  : boolean   = ! ! _U    * m   - v       :: Z ( )    - ! iyA     || hII ( )     != i   / wF    + d   / Qj     + true       , ! MY ( )     >= ! true      :: - F3   - OT    % - j      < ! V   % SjA    / ! iVHD0o         ;   JX , C  : auto  ;   """
		expect = """Program([
	VarDecl(_, BooleanType, BinExpr(::, BinExpr(-, BinExpr(*, UnExpr(!, UnExpr(!, Id(_U))), Id(m)), Id(v)), BinExpr(!=, BinExpr(||, BinExpr(-, FuncCall(Z, []), UnExpr(!, Id(iyA))), FuncCall(hII, [])), BinExpr(+, BinExpr(+, BinExpr(/, Id(i), Id(wF)), BinExpr(/, Id(d), Id(Qj))), BooleanLit(True)))))
	VarDecl(H, BooleanType, BinExpr(::, BinExpr(>=, UnExpr(!, FuncCall(MY, [])), UnExpr(!, BooleanLit(True))), BinExpr(<, BinExpr(-, UnExpr(-, Id(F3)), BinExpr(%, Id(OT), UnExpr(-, Id(j)))), BinExpr(/, BinExpr(%, UnExpr(!, Id(V)), Id(SjA)), UnExpr(!, Id(iVHD0o))))))
	VarDecl(JX, AutoType)
	VarDecl(C, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 316))

	def test_317(self):
		input = """iy4 : function void ( ) inherit Wev { }    _1y , N , VmOo , a  : auto  = ! I   + s     || LoU   / Ss    || ! DX      < - ! ! E       :: ! NPGp    % t   % B2N     * ! L   * Uf        , ! D ( )    + i ( )      != ! u   + px    / M   / H        , - - K   && Z      < - - TJqh   / d        , tE   && FQ    || t   + x     || KjH   - K    % o   || cFNx2      >= - - ! Zl8d       :: { }     > r      ;   rv : function auto  ( out p : auto   , inherit out n : array [ 9_4_83 , 9 , 1 ] of float     , inherit out oWi : boolean     ) { }    """
		expect = """Program([
	FuncDecl(iy4, VoidType, [], Wev, BlockStmt([]))
	VarDecl(_1y, AutoType, BinExpr(::, BinExpr(<, BinExpr(||, BinExpr(||, BinExpr(+, UnExpr(!, Id(I)), Id(s)), BinExpr(/, Id(LoU), Id(Ss))), UnExpr(!, Id(DX))), UnExpr(-, UnExpr(!, UnExpr(!, Id(E))))), BinExpr(*, BinExpr(*, BinExpr(%, BinExpr(%, UnExpr(!, Id(NPGp)), Id(t)), Id(B2N)), UnExpr(!, Id(L))), Id(Uf))))
	VarDecl(N, AutoType, BinExpr(!=, BinExpr(+, UnExpr(!, FuncCall(D, [])), FuncCall(i, [])), BinExpr(+, UnExpr(!, Id(u)), BinExpr(/, BinExpr(/, Id(px), Id(M)), Id(H)))))
	VarDecl(VmOo, AutoType, BinExpr(<, BinExpr(&&, UnExpr(-, UnExpr(-, Id(K))), Id(Z)), BinExpr(/, UnExpr(-, UnExpr(-, Id(TJqh))), Id(d))))
	VarDecl(a, AutoType, BinExpr(::, BinExpr(>=, BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(&&, Id(tE), Id(FQ)), BinExpr(+, Id(t), Id(x))), BinExpr(-, Id(KjH), BinExpr(%, Id(K), Id(o)))), Id(cFNx2)), UnExpr(-, UnExpr(-, UnExpr(!, Id(Zl8d))))), BinExpr(>, ArrayLit([]), Id(r))))
	FuncDecl(rv, AutoType, [OutParam(p, AutoType), InheritOutParam(n, ArrayType([9483, 9, 1], FloatType)), InheritOutParam(oWi, BooleanType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 317))

	def test_318(self):
		input = """e815acMmzA1w  : array [ 0 ] of boolean    ;   """
		expect = """Program([
	VarDecl(e815acMmzA1w, ArrayType([0], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 318))

	def test_319(self):
		input = """uC  : array [ 242_5 ] of float    ;   """
		expect = """Program([
	VarDecl(uC, ArrayType([2425], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 319))

	def test_320(self):
		input = """EMbg7cN , ji  : auto  = - ek   - Z     && II4 ( )       , ! ! g6   || wn50         ;   Q : function array [ 1_2697 ] of integer    ( out YZ : string    , inherit Qx3 : auto   , out i : array [ 2_72 , 370525 ] of integer     , inherit fM3Qs : array [ 0 ] of string      ) inherit ns { }    g : function auto  ( ) inherit s { R  : array [ 4 , 0 , 618758 ] of string    ;  }    C : function integer   ( ) inherit j { }    """
		expect = """Program([
	VarDecl(EMbg7cN, AutoType, BinExpr(&&, BinExpr(-, UnExpr(-, Id(ek)), Id(Z)), FuncCall(II4, [])))
	VarDecl(ji, AutoType, BinExpr(||, UnExpr(!, UnExpr(!, Id(g6))), Id(wn50)))
	FuncDecl(Q, ArrayType([12697], IntegerType), [OutParam(YZ, StringType), InheritParam(Qx3, AutoType), OutParam(i, ArrayType([272, 370525], IntegerType)), InheritParam(fM3Qs, ArrayType([0], StringType))], ns, BlockStmt([]))
	FuncDecl(g, AutoType, [], s, BlockStmt([VarDecl(R, ArrayType([4, 0, 618758], StringType))]))
	FuncDecl(C, IntegerType, [], j, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 320))

	def test_321(self):
		input = """I , fGprC  : float   ;   """
		expect = """Program([
	VarDecl(I, FloatType)
	VarDecl(fGprC, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 321))

	def test_322(self):
		input = """PK : function void ( inherit o : boolean    , inherit out M : float     ) { h  : auto  ;  e ( )  ;   continue ;   do { }  while ( j   % f     :: E   && ICX      ) ;   { }   U , G , r , Za , jA , l3m  : auto  ;  }    z  : boolean   = B   + I    - fJ   % w     * - C   || L      == ! h ( )        ;   """
		expect = """Program([
	FuncDecl(PK, VoidType, [InheritParam(o, BooleanType), InheritOutParam(M, FloatType)], None, BlockStmt([VarDecl(h, AutoType), CallStmt(e, ), ContinueStmt(), DoWhileStmt(BinExpr(::, BinExpr(%, Id(j), Id(f)), BinExpr(&&, Id(E), Id(ICX))), BlockStmt([])), BlockStmt([]), VarDecl(U, AutoType), VarDecl(G, AutoType), VarDecl(r, AutoType), VarDecl(Za, AutoType), VarDecl(jA, AutoType), VarDecl(l3m, AutoType)]))
	VarDecl(z, BooleanType, BinExpr(==, BinExpr(||, BinExpr(-, BinExpr(+, Id(B), Id(I)), BinExpr(*, BinExpr(%, Id(fJ), Id(w)), UnExpr(-, Id(C)))), Id(L)), UnExpr(!, FuncCall(h, []))))
])"""
		self.assertTrue(TestAST.test(input, expect, 322))

	def test_323(self):
		input = """c0Z0 , H , c9 , w  : string   ;   """
		expect = """Program([
	VarDecl(c0Z0, StringType)
	VarDecl(H, StringType)
	VarDecl(c9, StringType)
	VarDecl(w, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 323))

	def test_324(self):
		input = """fmH : function void ( ) inherit ypx { }    _4EQFx , y , K9 , ICRWgDth , f  : string   ;   F , C , ebgIC , P  : array [ 2_4 , 4 ] of string    ;   """
		expect = """Program([
	FuncDecl(fmH, VoidType, [], ypx, BlockStmt([]))
	VarDecl(_4EQFx, StringType)
	VarDecl(y, StringType)
	VarDecl(K9, StringType)
	VarDecl(ICRWgDth, StringType)
	VarDecl(f, StringType)
	VarDecl(F, ArrayType([24, 4], StringType))
	VarDecl(C, ArrayType([24, 4], StringType))
	VarDecl(ebgIC, ArrayType([24, 4], StringType))
	VarDecl(P, ArrayType([24, 4], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 324))

	def test_325(self):
		input = """KAC : function float   ( ) { }    I : function auto  ( out sIgc : float    , ap4 : auto   , inherit s : array [ 7_68_10_473777_258_56027 ] of float     , inherit out L : auto    ) inherit Ju { bD ( )  ;   { }   }    """
		expect = """Program([
	FuncDecl(KAC, FloatType, [], None, BlockStmt([]))
	FuncDecl(I, AutoType, [OutParam(sIgc, FloatType), Param(ap4, AutoType), InheritParam(s, ArrayType([7681047377725856027], FloatType)), InheritOutParam(L, AutoType)], Ju, BlockStmt([CallStmt(bD, ), BlockStmt([])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 325))

	def test_326(self):
		input = """crA , f , sq , UY , YB , H , j  : float   ;   E , ryO , t  : float   = ! o   * MyaBZ     || ! Lm   + I      < h   * g9    + - s     / Y ( )       , ! ! HeQA   / q9fnOb8        , 0    + A   * SKUGe    - 3      > - - Wu   || Sw9s         ;   L : function void ( ) inherit _ { }    Xe : function void ( ) { }    """
		expect = """Program([
	VarDecl(crA, FloatType)
	VarDecl(f, FloatType)
	VarDecl(sq, FloatType)
	VarDecl(UY, FloatType)
	VarDecl(YB, FloatType)
	VarDecl(H, FloatType)
	VarDecl(j, FloatType)
	VarDecl(E, FloatType, BinExpr(<, BinExpr(||, BinExpr(*, UnExpr(!, Id(o)), Id(MyaBZ)), BinExpr(+, UnExpr(!, Id(Lm)), Id(I))), BinExpr(+, BinExpr(*, Id(h), Id(g9)), BinExpr(/, UnExpr(-, Id(s)), FuncCall(Y, [])))))
	VarDecl(ryO, FloatType, BinExpr(/, UnExpr(!, UnExpr(!, Id(HeQA))), Id(q9fnOb8)))
	VarDecl(t, FloatType, BinExpr(>, BinExpr(-, BinExpr(+, IntegerLit(0), BinExpr(*, Id(A), Id(SKUGe))), IntegerLit(3)), BinExpr(||, UnExpr(-, UnExpr(-, Id(Wu))), Id(Sw9s))))
	FuncDecl(L, VoidType, [], _, BlockStmt([]))
	FuncDecl(Xe, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 326))

	def test_327(self):
		input = """aLj6s5 : function auto  ( __ : auto   , out N : array [ 83 , 52_4_26_6 , 2_2_2_0 ] of string      ) { Bbiw  : float   = K0    :: s   > ! b1M       ;  V  = hL   - K      ;   }    JJ : function auto  ( out WV : auto   , inherit out Zj : integer     ) { diFj ( )  ;   }    """
		expect = """Program([
	FuncDecl(aLj6s5, AutoType, [Param(__, AutoType), OutParam(N, ArrayType([83, 524266, 2220], StringType))], None, BlockStmt([VarDecl(Bbiw, FloatType, BinExpr(::, Id(K0), BinExpr(>, Id(s), UnExpr(!, Id(b1M))))), AssignStmt(Id(V), BinExpr(-, Id(hL), Id(K)))]))
	FuncDecl(JJ, AutoType, [OutParam(WV, AutoType), InheritOutParam(Zj, IntegerType)], None, BlockStmt([CallStmt(diFj, )]))
])"""
		self.assertTrue(TestAST.test(input, expect, 327))

	def test_328(self):
		input = """jOpteT : function auto  ( inherit x : array [ 0 , 89 , 7_98 ] of float      ) inherit T { }    """
		expect = """Program([
	FuncDecl(jOpteT, AutoType, [InheritParam(x, ArrayType([0, 89, 798], FloatType))], T, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 328))

	def test_329(self):
		input = """i : function void ( inherit VD : float     ) inherit K { }    U : function void ( inherit out p : array [ 6_7 ] of float     , inherit out T : array [ 98_2 , 4 ] of boolean     , inherit out V : array [ 0 ] of integer     , inherit s4 : array [ 80 , 4 , 9_4_46_7_34_15 , 2 , 0 , 135 ] of string     , inherit out SB : array [ 0 , 0 ] of boolean     , M : boolean     ) inherit F { }    """
		expect = """Program([
	FuncDecl(i, VoidType, [InheritParam(VD, FloatType)], K, BlockStmt([]))
	FuncDecl(U, VoidType, [InheritOutParam(p, ArrayType([67], FloatType)), InheritOutParam(T, ArrayType([982, 4], BooleanType)), InheritOutParam(V, ArrayType([0], IntegerType)), InheritParam(s4, ArrayType([80, 4, 944673415, 2, 0, 135], StringType)), InheritOutParam(SB, ArrayType([0, 0], BooleanType)), Param(M, BooleanType)], F, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 329))

	def test_330(self):
		input = """C : function void ( ) { U , pJ , Aej , Mr0F  : float   = k ( )    != ! M     :: AE   || kUF      , Vt   / Mz     :: E   * J      , Lr   + o      , v4tpT      ;  do { }  while ( - f    != Tu ( )      ) ;   break ;   while ( Xw   || fzmo    != - r1     :: cHZ     ) X ( )  ;     }    """
		expect = """Program([
	FuncDecl(C, VoidType, [], None, BlockStmt([VarDecl(U, FloatType, BinExpr(::, BinExpr(!=, FuncCall(k, []), UnExpr(!, Id(M))), BinExpr(||, Id(AE), Id(kUF)))), VarDecl(pJ, FloatType, BinExpr(::, BinExpr(/, Id(Vt), Id(Mz)), BinExpr(*, Id(E), Id(J)))), VarDecl(Aej, FloatType, BinExpr(+, Id(Lr), Id(o))), VarDecl(Mr0F, FloatType, Id(v4tpT)), DoWhileStmt(BinExpr(!=, UnExpr(-, Id(f)), FuncCall(Tu, [])), BlockStmt([])), BreakStmt(), WhileStmt(BinExpr(::, BinExpr(!=, BinExpr(||, Id(Xw), Id(fzmo)), UnExpr(-, Id(r1))), Id(cHZ)), CallStmt(X, ))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 330))

	def test_331(self):
		input = """M  : boolean   = Z    :: F ( )       ;   """
		expect = """Program([
	VarDecl(M, BooleanType, BinExpr(::, Id(Z), FuncCall(F, [])))
])"""
		self.assertTrue(TestAST.test(input, expect, 331))

	def test_332(self):
		input = """Dykmx : function void ( ) inherit _E { G , lu , QK , r  : auto  = Ju   + eQ    != i   - s      , bR   + t     :: 3      , ! l      , t   || q    != ! h     :: - FZy       ;  while ( ! T    == ! ZR      ) continue ;     }    """
		expect = """Program([
	FuncDecl(Dykmx, VoidType, [], _E, BlockStmt([VarDecl(G, AutoType, BinExpr(!=, BinExpr(+, Id(Ju), Id(eQ)), BinExpr(-, Id(i), Id(s)))), VarDecl(lu, AutoType, BinExpr(::, BinExpr(+, Id(bR), Id(t)), IntegerLit(3))), VarDecl(QK, AutoType, UnExpr(!, Id(l))), VarDecl(r, AutoType, BinExpr(::, BinExpr(!=, BinExpr(||, Id(t), Id(q)), UnExpr(!, Id(h))), UnExpr(-, Id(FZy)))), WhileStmt(BinExpr(==, UnExpr(!, Id(T)), UnExpr(!, Id(ZR))), ContinueStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 332))

	def test_333(self):
		input = """N , uej  : auto  = - F   % AV7P     % cUf   * wT    || _   - U        , - ! I   - aaF         ;   """
		expect = """Program([
	VarDecl(N, AutoType, BinExpr(||, BinExpr(*, BinExpr(%, BinExpr(%, UnExpr(-, Id(F)), Id(AV7P)), Id(cUf)), Id(wT)), BinExpr(-, Id(_), Id(U))))
	VarDecl(uej, AutoType, BinExpr(-, UnExpr(-, UnExpr(!, Id(I))), Id(aaF)))
])"""
		self.assertTrue(TestAST.test(input, expect, 333))

	def test_334(self):
		input = """HC , mQ  : auto  = e ( )    < - ldWx     :: _   && p    + i   - eglM2O2     + ""    / r   / J        , - m   % Z    && w   || WJ         ;   """
		expect = """Program([
	VarDecl(HC, AutoType, BinExpr(::, BinExpr(<, FuncCall(e, []), UnExpr(-, Id(ldWx))), BinExpr(&&, Id(_), BinExpr(+, BinExpr(-, BinExpr(+, Id(p), Id(i)), Id(eglM2O2)), BinExpr(/, BinExpr(/, StringLit(), Id(r)), Id(J))))))
	VarDecl(mQ, AutoType, BinExpr(||, BinExpr(&&, BinExpr(%, UnExpr(-, Id(m)), Id(Z)), Id(w)), Id(WJ)))
])"""
		self.assertTrue(TestAST.test(input, expect, 334))

	def test_335(self):
		input = """Zq : function void ( inherit out a : auto   , M3 : auto    ) { }    """
		expect = """Program([
	FuncDecl(Zq, VoidType, [InheritOutParam(a, AutoType), Param(M3, AutoType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 335))

	def test_336(self):
		input = """r : function void ( ) inherit I { edjMa  : array [ 0 , 7_5_9 , 0 ] of boolean    ;  }    r , n , iZ , HeRAkG , sQF , n  : auto  ;   b : function integer   ( ) inherit a { }    """
		expect = """Program([
	FuncDecl(r, VoidType, [], I, BlockStmt([VarDecl(edjMa, ArrayType([0, 759, 0], BooleanType))]))
	VarDecl(r, AutoType)
	VarDecl(n, AutoType)
	VarDecl(iZ, AutoType)
	VarDecl(HeRAkG, AutoType)
	VarDecl(sQF, AutoType)
	VarDecl(n, AutoType)
	FuncDecl(b, IntegerType, [], a, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 336))

	def test_337(self):
		input = """v8 , kveaI  : auto  ;   """
		expect = """Program([
	VarDecl(v8, AutoType)
	VarDecl(kveaI, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 337))

	def test_338(self):
		input = """eH : function auto  ( inherit f5 : array [ 0 ] of boolean     , out H : array [ 0 , 74873 , 0 , 384_85 ] of string     , tT : boolean    , inherit xck : array [ 0 ] of float     , inherit out gTKO990Xl : array [ 58 ] of float      ) { }    """
		expect = """Program([
	FuncDecl(eH, AutoType, [InheritParam(f5, ArrayType([0], BooleanType)), OutParam(H, ArrayType([0, 74873, 0, 38485], StringType)), Param(tT, BooleanType), InheritParam(xck, ArrayType([0], FloatType)), InheritOutParam(gTKO990Xl, ArrayType([58], FloatType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 338))

	def test_339(self):
		input = """wY : function void ( ) { n  : array [ 21_6 , 0 , 0 ] of integer    ;  }    """
		expect = """Program([
	FuncDecl(wY, VoidType, [], None, BlockStmt([VarDecl(n, ArrayType([216, 0, 0], IntegerType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 339))

	def test_340(self):
		input = """h : function string   ( ) { zK , DXY  : float   = Lw   && J    < Kw   + z     :: ! fkEa      , D3   && qo    >= - MF45Tz     :: ! dL    == x   - Lzs       ;  U  : auto  ;  r , OFp , AJdR2ea , q  : float   ;  while ( - f6    == ! XhH5      ) return ;     }    v , j , O3 , IJ , TGkhe  : float   ;   m : function float   ( ) inherit A5 { ncO , jX , i9  : auto  ;  }    f3 , W , P  : array [ 8 , 0 , 8_2 ] of integer    ;   c : function void ( ) inherit S { }    """
		expect = """Program([
	FuncDecl(h, StringType, [], None, BlockStmt([VarDecl(zK, FloatType, BinExpr(::, BinExpr(<, BinExpr(&&, Id(Lw), Id(J)), BinExpr(+, Id(Kw), Id(z))), UnExpr(!, Id(fkEa)))), VarDecl(DXY, FloatType, BinExpr(::, BinExpr(>=, BinExpr(&&, Id(D3), Id(qo)), UnExpr(-, Id(MF45Tz))), BinExpr(==, UnExpr(!, Id(dL)), BinExpr(-, Id(x), Id(Lzs))))), VarDecl(U, AutoType), VarDecl(r, FloatType), VarDecl(OFp, FloatType), VarDecl(AJdR2ea, FloatType), VarDecl(q, FloatType), WhileStmt(BinExpr(==, UnExpr(-, Id(f6)), UnExpr(!, Id(XhH5))), ReturnStmt())]))
	VarDecl(v, FloatType)
	VarDecl(j, FloatType)
	VarDecl(O3, FloatType)
	VarDecl(IJ, FloatType)
	VarDecl(TGkhe, FloatType)
	FuncDecl(m, FloatType, [], A5, BlockStmt([VarDecl(ncO, AutoType), VarDecl(jX, AutoType), VarDecl(i9, AutoType)]))
	VarDecl(f3, ArrayType([8, 0, 82], IntegerType))
	VarDecl(W, ArrayType([8, 0, 82], IntegerType))
	VarDecl(P, ArrayType([8, 0, 82], IntegerType))
	FuncDecl(c, VoidType, [], S, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 340))

	def test_341(self):
		input = """ONmL : function void ( ) { }    """
		expect = """Program([
	FuncDecl(ONmL, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 341))

	def test_342(self):
		input = """WE : function array [ 0 ] of boolean    ( RT : integer     ) { while ( vUL7KqI9   / YWp     :: eC   || bC    == - _      ) Gq ( )  ;     return ;   }    qfX  : float   ;   gsv , oF , q1C , Df , Vf , q  : auto  = ! ! _1Ui     && - ! J      <= ! oP7   && aAM     * A ( )       , { }     && - e   / T      <= ! N    && Zy   - A     - ! G    + 0       :: n49   / W    - - t6     - - l    + w   - z_      > - W   / yz    + Em       , m99   / K    || c   && b     || j      , - - t    + m_a   / gRA        , ! ! ! k      > ! c   || D    || ! Q        , N   + q    && D   * a_     - C ( )     != ! ! O   + z         ;   """
		expect = """Program([
	FuncDecl(WE, ArrayType([0], BooleanType), [Param(RT, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(::, BinExpr(/, Id(vUL7KqI9), Id(YWp)), BinExpr(==, BinExpr(||, Id(eC), Id(bC)), UnExpr(-, Id(_)))), CallStmt(Gq, )), ReturnStmt()]))
	VarDecl(qfX, FloatType)
	VarDecl(gsv, AutoType, BinExpr(<=, BinExpr(&&, UnExpr(!, UnExpr(!, Id(_1Ui))), UnExpr(-, UnExpr(!, Id(J)))), BinExpr(&&, UnExpr(!, Id(oP7)), BinExpr(*, Id(aAM), FuncCall(A, [])))))
	VarDecl(oF, AutoType, BinExpr(::, BinExpr(<=, BinExpr(&&, ArrayLit([]), BinExpr(/, UnExpr(-, Id(e)), Id(T))), BinExpr(&&, UnExpr(!, Id(N)), BinExpr(+, BinExpr(-, BinExpr(-, Id(Zy), Id(A)), UnExpr(!, Id(G))), IntegerLit(0)))), BinExpr(>, BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(-, BinExpr(/, Id(n49), Id(W)), UnExpr(-, Id(t6))), UnExpr(-, Id(l))), Id(w)), Id(z_)), BinExpr(+, BinExpr(/, UnExpr(-, Id(W)), Id(yz)), Id(Em)))))
	VarDecl(q1C, AutoType, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(/, Id(m99), Id(K)), Id(c)), Id(b)), Id(j)))
	VarDecl(Df, AutoType, BinExpr(+, UnExpr(-, UnExpr(-, Id(t))), BinExpr(/, Id(m_a), Id(gRA))))
	VarDecl(Vf, AutoType, BinExpr(>, UnExpr(!, UnExpr(!, UnExpr(!, Id(k)))), BinExpr(||, BinExpr(||, UnExpr(!, Id(c)), Id(D)), UnExpr(!, Id(Q)))))
	VarDecl(q, AutoType, BinExpr(!=, BinExpr(&&, BinExpr(+, Id(N), Id(q)), BinExpr(-, BinExpr(*, Id(D), Id(a_)), FuncCall(C, []))), BinExpr(+, UnExpr(!, UnExpr(!, Id(O))), Id(z))))
])"""
		self.assertTrue(TestAST.test(input, expect, 342))

	def test_343(self):
		input = """y , p  : boolean   ;   R , iiJ , u8myb5Yhd3 , M , a  : boolean   ;   L  : array [ 5 , 6 , 0 ] of boolean    = ! C    && G   - QPY     + ! ! Y       :: - Yk    <= ! YPmKKu5qJ   + G     / true        ;   e : function array [ 6_7_5 ] of integer    ( ) { P2  : string   ;  break ;   }    """
		expect = """Program([
	VarDecl(y, BooleanType)
	VarDecl(p, BooleanType)
	VarDecl(R, BooleanType)
	VarDecl(iiJ, BooleanType)
	VarDecl(u8myb5Yhd3, BooleanType)
	VarDecl(M, BooleanType)
	VarDecl(a, BooleanType)
	VarDecl(L, ArrayType([5, 6, 0], BooleanType), BinExpr(::, BinExpr(&&, UnExpr(!, Id(C)), BinExpr(+, BinExpr(-, Id(G), Id(QPY)), UnExpr(!, UnExpr(!, Id(Y))))), BinExpr(<=, UnExpr(-, Id(Yk)), BinExpr(+, UnExpr(!, Id(YPmKKu5qJ)), BinExpr(/, Id(G), BooleanLit(True))))))
	FuncDecl(e, ArrayType([675], IntegerType), [], None, BlockStmt([VarDecl(P2, StringType), BreakStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 343))

	def test_344(self):
		input = """mYto : function void ( inherit skAk : auto    ) { }    YIP : function void ( ) inherit mpwa7 { }    """
		expect = """Program([
	FuncDecl(mYto, VoidType, [InheritParam(skAk, AutoType)], None, BlockStmt([]))
	FuncDecl(YIP, VoidType, [], mpwa7, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 344))

	def test_345(self):
		input = """a , Pi3 , N  : auto  ;   """
		expect = """Program([
	VarDecl(a, AutoType)
	VarDecl(Pi3, AutoType)
	VarDecl(N, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 345))

	def test_346(self):
		input = """XX : function void ( ) { do { }  while ( E   + T    != eo   || H      ) ;   }    Y : function void ( inherit uo1c : array [ 0 ] of float      ) { Au , oPOmp  : array [ 0 , 64 ] of boolean    = Ko   * Q    >= ! W      , G      ;  }    """
		expect = """Program([
	FuncDecl(XX, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, BinExpr(+, Id(E), Id(T)), BinExpr(||, Id(eo), Id(H))), BlockStmt([]))]))
	FuncDecl(Y, VoidType, [InheritParam(uo1c, ArrayType([0], FloatType))], None, BlockStmt([VarDecl(Au, ArrayType([0, 64], BooleanType), BinExpr(>=, BinExpr(*, Id(Ko), Id(Q)), UnExpr(!, Id(W)))), VarDecl(oPOmp, ArrayType([0, 64], BooleanType), Id(G))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 346))

	def test_347(self):
		input = """Hv  : array [ 8381 ] of float    = _ ( )    > z ( )     :: - k ( )        ;   D  : boolean   ;   IvlY , A  : array [ 0 ] of float    ;   bPyO : function float   ( sc : array [ 0 , 883693_011_44 , 8 , 66 ] of boolean      ) inherit wU6 { f6  : float   ;  }    """
		expect = """Program([
	VarDecl(Hv, ArrayType([8381], FloatType), BinExpr(::, BinExpr(>, FuncCall(_, []), FuncCall(z, [])), UnExpr(-, FuncCall(k, []))))
	VarDecl(D, BooleanType)
	VarDecl(IvlY, ArrayType([0], FloatType))
	VarDecl(A, ArrayType([0], FloatType))
	FuncDecl(bPyO, FloatType, [Param(sc, ArrayType([0, 88369301144, 8, 66], BooleanType))], wU6, BlockStmt([VarDecl(f6, FloatType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 347))

	def test_348(self):
		input = """nE : function void ( mnho0WR9 : auto    ) inherit rnuQ { }    Ak  : integer   = ! - F     || - i    % _TEP   - J      >= S      ;   SBrwW , p , k , Uwka , FU  : string   = ! - UL    * q3ujDP   + mK0      <= - - vbvB    + - sxg        , ""    || BOnQ   && _     || - x1    - 8       :: ! ! ! k1        , - ! Sgk    || ikn5 ( )      >= - - 0       :: yx   <= ! vA    - - w     / 1    * LQ   || ZA        , - ! - v      < - - d9     % LiS     :: - SB3f    * g   % fUh5     || y   - BJD    && ! w      < l   && H    + s   + F     || ! k6s   - x        , - K   - Z     * M3R ( )     > ! ! - G         ;   """
		expect = """Program([
	FuncDecl(nE, VoidType, [Param(mnho0WR9, AutoType)], rnuQ, BlockStmt([]))
	VarDecl(Ak, IntegerType, BinExpr(>=, BinExpr(||, UnExpr(!, UnExpr(-, Id(F))), BinExpr(-, BinExpr(%, UnExpr(-, Id(i)), Id(_TEP)), Id(J))), Id(S)))
	VarDecl(SBrwW, StringType, BinExpr(<=, BinExpr(+, BinExpr(*, UnExpr(!, UnExpr(-, Id(UL))), Id(q3ujDP)), Id(mK0)), BinExpr(+, UnExpr(-, UnExpr(-, Id(vbvB))), UnExpr(-, Id(sxg)))))
	VarDecl(p, StringType, BinExpr(::, BinExpr(||, BinExpr(&&, BinExpr(||, StringLit(), Id(BOnQ)), Id(_)), BinExpr(-, UnExpr(-, Id(x1)), IntegerLit(8))), UnExpr(!, UnExpr(!, UnExpr(!, Id(k1))))))
	VarDecl(k, StringType, BinExpr(::, BinExpr(>=, BinExpr(||, UnExpr(-, UnExpr(!, Id(Sgk))), FuncCall(ikn5, [])), UnExpr(-, UnExpr(-, IntegerLit(0)))), BinExpr(<=, Id(yx), BinExpr(||, BinExpr(-, UnExpr(!, Id(vA)), BinExpr(*, BinExpr(/, UnExpr(-, Id(w)), IntegerLit(1)), Id(LQ))), Id(ZA)))))
	VarDecl(Uwka, StringType, BinExpr(::, BinExpr(<, UnExpr(-, UnExpr(!, UnExpr(-, Id(v)))), BinExpr(%, UnExpr(-, UnExpr(-, Id(d9))), Id(LiS))), BinExpr(<, BinExpr(&&, BinExpr(||, BinExpr(%, BinExpr(*, UnExpr(-, Id(SB3f)), Id(g)), Id(fUh5)), BinExpr(-, Id(y), Id(BJD))), UnExpr(!, Id(w))), BinExpr(||, BinExpr(&&, Id(l), BinExpr(+, BinExpr(+, Id(H), Id(s)), Id(F))), BinExpr(-, UnExpr(!, Id(k6s)), Id(x))))))
	VarDecl(FU, StringType, BinExpr(>, BinExpr(-, UnExpr(-, Id(K)), BinExpr(*, Id(Z), FuncCall(M3R, []))), UnExpr(!, UnExpr(!, UnExpr(-, Id(G))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 348))

	def test_349(self):
		input = """Oqt : function array [ 0 , 0 ] of float    ( out F : boolean    , inherit q : auto   , inherit G : array [ 1 , 0 , 0 ] of float      ) inherit q { dx  : float   = - i    <= - oF_       ;  Wz , g  : array [ 0 ] of boolean    = I ( )    == 8     :: ! i      , - D     :: s   * E       ;  }    X , lzB , T , Nb , E , jW , Updo  : array [ 1 ] of float    ;   """
		expect = """Program([
	FuncDecl(Oqt, ArrayType([0, 0], FloatType), [OutParam(F, BooleanType), InheritParam(q, AutoType), InheritParam(G, ArrayType([1, 0, 0], FloatType))], q, BlockStmt([VarDecl(dx, FloatType, BinExpr(<=, UnExpr(-, Id(i)), UnExpr(-, Id(oF_)))), VarDecl(Wz, ArrayType([0], BooleanType), BinExpr(::, BinExpr(==, FuncCall(I, []), IntegerLit(8)), UnExpr(!, Id(i)))), VarDecl(g, ArrayType([0], BooleanType), BinExpr(::, UnExpr(-, Id(D)), BinExpr(*, Id(s), Id(E))))]))
	VarDecl(X, ArrayType([1], FloatType))
	VarDecl(lzB, ArrayType([1], FloatType))
	VarDecl(T, ArrayType([1], FloatType))
	VarDecl(Nb, ArrayType([1], FloatType))
	VarDecl(E, ArrayType([1], FloatType))
	VarDecl(jW, ArrayType([1], FloatType))
	VarDecl(Updo, ArrayType([1], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 349))

	def test_350(self):
		input = """DY , E , Ej , wv  : string   ;   """
		expect = """Program([
	VarDecl(DY, StringType)
	VarDecl(E, StringType)
	VarDecl(Ej, StringType)
	VarDecl(wv, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 350))

	def test_351(self):
		input = """ETLZsS , O , v , WTXBSO , xT  : array [ 6 ] of boolean    ;   """
		expect = """Program([
	VarDecl(ETLZsS, ArrayType([6], BooleanType))
	VarDecl(O, ArrayType([6], BooleanType))
	VarDecl(v, ArrayType([6], BooleanType))
	VarDecl(WTXBSO, ArrayType([6], BooleanType))
	VarDecl(xT, ArrayType([6], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 351))

	def test_352(self):
		input = """I , t  : integer   = - Va4w5K8 ( )       , - ! W     / p   + Wny    || ! sF4M         ;   iN : function boolean   ( ) inherit eT_JY0lTgrd7fu { { }   return - X2      ;   }    """
		expect = """Program([
	VarDecl(I, IntegerType, UnExpr(-, FuncCall(Va4w5K8, [])))
	VarDecl(t, IntegerType, BinExpr(||, BinExpr(+, BinExpr(/, UnExpr(-, UnExpr(!, Id(W))), Id(p)), Id(Wny)), UnExpr(!, Id(sF4M))))
	FuncDecl(iN, BooleanType, [], eT_JY0lTgrd7fu, BlockStmt([BlockStmt([]), ReturnStmt(UnExpr(-, Id(X2)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 352))

	def test_353(self):
		input = """O  : array [ 0 , 0 , 0 , 9 ] of string    = - KIlN   && j    && LAD   && d      < ""    - - ! Q       :: - Ae    + uWO   + k    - ! VSG      == i      ;   """
		expect = """Program([
	VarDecl(O, ArrayType([0, 0, 0, 9], StringType), BinExpr(::, BinExpr(<, BinExpr(&&, BinExpr(&&, BinExpr(&&, UnExpr(-, Id(KIlN)), Id(j)), Id(LAD)), Id(d)), BinExpr(-, StringLit(), UnExpr(-, UnExpr(!, Id(Q))))), BinExpr(==, BinExpr(-, BinExpr(+, BinExpr(+, UnExpr(-, Id(Ae)), Id(uWO)), Id(k)), UnExpr(!, Id(VSG))), Id(i))))
])"""
		self.assertTrue(TestAST.test(input, expect, 353))

	def test_354(self):
		input = """Uh : function array [ 34 , 97_39_10 ] of integer    ( ) { }    nU : function void ( ) inherit Gcp { }    m5 : function array [ 0 , 10 ] of boolean    ( ) { Pi ( )  ;   while ( - b6l9a     :: UW ( )    > X   - yvYV      ) return ;     }    o : function string   ( ) { }    """
		expect = """Program([
	FuncDecl(Uh, ArrayType([34, 973910], IntegerType), [], None, BlockStmt([]))
	FuncDecl(nU, VoidType, [], Gcp, BlockStmt([]))
	FuncDecl(m5, ArrayType([0, 10], BooleanType), [], None, BlockStmt([CallStmt(Pi, ), WhileStmt(BinExpr(::, UnExpr(-, Id(b6l9a)), BinExpr(>, FuncCall(UW, []), BinExpr(-, Id(X), Id(yvYV)))), ReturnStmt())]))
	FuncDecl(o, StringType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 354))

	def test_355(self):
		input = """X , F  : auto  ;   """
		expect = """Program([
	VarDecl(X, AutoType)
	VarDecl(F, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 355))

	def test_356(self):
		input = """k  : auto  = ! - C   || TH      == v    :: s   == K9      ;   """
		expect = """Program([
	VarDecl(k, AutoType, BinExpr(::, BinExpr(==, BinExpr(||, UnExpr(!, UnExpr(-, Id(C))), Id(TH)), Id(v)), BinExpr(==, Id(s), Id(K9))))
])"""
		self.assertTrue(TestAST.test(input, expect, 356))

	def test_357(self):
		input = """O  : auto  ;   Z , k  : auto  ;   """
		expect = """Program([
	VarDecl(O, AutoType)
	VarDecl(Z, AutoType)
	VarDecl(k, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 357))

	def test_358(self):
		input = """jSVn07 : function void ( ) inherit mbR { while ( ! kgdEny      ) continue ;     veGK , M  : boolean   = p3O   * Bm    > - F     :: ""      , Ej   * Vk       ;  }    D : function integer   ( ) { }    quwZQu : function void ( ) { }    RW , fQd , ABbA  : boolean   = ! N   / XU8     % q ( )     > ! mV ( )    || ST   % t       :: - ! E    && d     < - ! - N4gb        , ""    >= gnsU ( )    * i   && C     + - qR   % Ci       :: g   + ""     < ! s ( )    * ! y        , - "\\b\\\'"        ;   """
		expect = """Program([
	FuncDecl(jSVn07, VoidType, [], mbR, BlockStmt([WhileStmt(UnExpr(!, Id(kgdEny)), ContinueStmt()), VarDecl(veGK, BooleanType, BinExpr(::, BinExpr(>, BinExpr(*, Id(p3O), Id(Bm)), UnExpr(-, Id(F))), StringLit())), VarDecl(M, BooleanType, BinExpr(*, Id(Ej), Id(Vk)))]))
	FuncDecl(D, IntegerType, [], None, BlockStmt([]))
	FuncDecl(quwZQu, VoidType, [], None, BlockStmt([]))
	VarDecl(RW, BooleanType, BinExpr(::, BinExpr(>, BinExpr(%, BinExpr(/, UnExpr(!, Id(N)), Id(XU8)), FuncCall(q, [])), BinExpr(||, UnExpr(!, FuncCall(mV, [])), BinExpr(%, Id(ST), Id(t)))), BinExpr(<, BinExpr(&&, UnExpr(-, UnExpr(!, Id(E))), Id(d)), UnExpr(-, UnExpr(!, UnExpr(-, Id(N4gb)))))))
	VarDecl(fQd, BooleanType, BinExpr(::, BinExpr(>=, StringLit(), BinExpr(&&, BinExpr(*, FuncCall(gnsU, []), Id(i)), BinExpr(+, Id(C), BinExpr(%, UnExpr(-, Id(qR)), Id(Ci))))), BinExpr(<, BinExpr(+, Id(g), StringLit()), BinExpr(*, UnExpr(!, FuncCall(s, [])), UnExpr(!, Id(y))))))
	VarDecl(ABbA, BooleanType, UnExpr(-, StringLit(\\b\\')))
])"""
		self.assertTrue(TestAST.test(input, expect, 358))

	def test_359(self):
		input = """l : function void ( ) inherit b_ { iRPJYJ , Ug , ZX , FtmZ  : array [ 0 ] of float    ;  reFbqv  : auto  ;  }    """
		expect = """Program([
	FuncDecl(l, VoidType, [], b_, BlockStmt([VarDecl(iRPJYJ, ArrayType([0], FloatType)), VarDecl(Ug, ArrayType([0], FloatType)), VarDecl(ZX, ArrayType([0], FloatType)), VarDecl(FtmZ, ArrayType([0], FloatType)), VarDecl(reFbqv, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 359))

	def test_360(self):
		input = """s0nZ : function boolean   ( ) inherit d { Zm , uFEy  : auto  = ""    > s0   && y      , K   && N7R     :: v8   || M       ;  }    YsG  : string   = ! n    || WNn   / UQ     || - ! L       :: 0e6       ;   Y  : array [ 72 , 0 ] of integer    = - - ! JG         ;   """
		expect = """Program([
	FuncDecl(s0nZ, BooleanType, [], d, BlockStmt([VarDecl(Zm, AutoType, BinExpr(>, StringLit(), BinExpr(&&, Id(s0), Id(y)))), VarDecl(uFEy, AutoType, BinExpr(::, BinExpr(&&, Id(K), Id(N7R)), BinExpr(||, Id(v8), Id(M))))]))
	VarDecl(YsG, StringType, BinExpr(::, BinExpr(||, BinExpr(||, UnExpr(!, Id(n)), BinExpr(/, Id(WNn), Id(UQ))), UnExpr(-, UnExpr(!, Id(L)))), FloatLit(0.0)))
	VarDecl(Y, ArrayType([72, 0], IntegerType), UnExpr(-, UnExpr(-, UnExpr(!, Id(JG)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 360))

	def test_361(self):
		input = """SQmS6 : function void ( inherit out KE : boolean     ) inherit OB { do { n , p  : auto  ;  }  while ( _3   / SM     :: ! J    != Q   - XESDnP      ) ;   Aq  = T   % vCc    >= - Q     :: H     ;   t , U  : array [ 0 ] of float    = ! OL    <= 5      , v   - P    > y    :: FR   * ZH1       ;  }    ur7T_ , _ , rF , S  : auto  ;   YB3 : function void ( r : boolean     ) { }    """
		expect = """Program([
	FuncDecl(SQmS6, VoidType, [InheritOutParam(KE, BooleanType)], OB, BlockStmt([DoWhileStmt(BinExpr(::, BinExpr(/, Id(_3), Id(SM)), BinExpr(!=, UnExpr(!, Id(J)), BinExpr(-, Id(Q), Id(XESDnP)))), BlockStmt([VarDecl(n, AutoType), VarDecl(p, AutoType)])), AssignStmt(Id(Aq), BinExpr(::, BinExpr(>=, BinExpr(%, Id(T), Id(vCc)), UnExpr(-, Id(Q))), Id(H))), VarDecl(t, ArrayType([0], FloatType), BinExpr(<=, UnExpr(!, Id(OL)), IntegerLit(5))), VarDecl(U, ArrayType([0], FloatType), BinExpr(::, BinExpr(>, BinExpr(-, Id(v), Id(P)), Id(y)), BinExpr(*, Id(FR), Id(ZH1))))]))
	VarDecl(ur7T_, AutoType)
	VarDecl(_, AutoType)
	VarDecl(rF, AutoType)
	VarDecl(S, AutoType)
	FuncDecl(YB3, VoidType, [Param(r, BooleanType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 361))

	def test_362(self):
		input = """YQRT : function boolean   ( ) inherit WtTB { while ( BGG   && u     :: 0    == - t      ) J ( )  ;     eC  = R9   + apH      ;   while ( vLDg   * n40    >= X   % e     :: c   * RI    == O6Nh   / r      ) { pE , Hu , NC , R , T , q , b  : boolean   ;  B  : float   ;  }     }    Nu , l , j , c , G  : float   ;   """
		expect = """Program([
	FuncDecl(YQRT, BooleanType, [], WtTB, BlockStmt([WhileStmt(BinExpr(::, BinExpr(&&, Id(BGG), Id(u)), BinExpr(==, IntegerLit(0), UnExpr(-, Id(t)))), CallStmt(J, )), AssignStmt(Id(eC), BinExpr(+, Id(R9), Id(apH))), WhileStmt(BinExpr(::, BinExpr(>=, BinExpr(*, Id(vLDg), Id(n40)), BinExpr(%, Id(X), Id(e))), BinExpr(==, BinExpr(*, Id(c), Id(RI)), BinExpr(/, Id(O6Nh), Id(r)))), BlockStmt([VarDecl(pE, BooleanType), VarDecl(Hu, BooleanType), VarDecl(NC, BooleanType), VarDecl(R, BooleanType), VarDecl(T, BooleanType), VarDecl(q, BooleanType), VarDecl(b, BooleanType), VarDecl(B, FloatType)]))]))
	VarDecl(Nu, FloatType)
	VarDecl(l, FloatType)
	VarDecl(j, FloatType)
	VarDecl(c, FloatType)
	VarDecl(G, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 362))

	def test_363(self):
		input = """T  : string   ;   """
		expect = """Program([
	VarDecl(T, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 363))

	def test_364(self):
		input = """rn , E  : auto  ;   s : function integer   ( ) { ZJ , Da  : boolean   = LNe   || U    > - E      , H ( )     :: - iTPG2       ;  }    c : function auto  ( inherit out HH : auto    ) { G3G ( )  ;   }    """
		expect = """Program([
	VarDecl(rn, AutoType)
	VarDecl(E, AutoType)
	FuncDecl(s, IntegerType, [], None, BlockStmt([VarDecl(ZJ, BooleanType, BinExpr(>, BinExpr(||, Id(LNe), Id(U)), UnExpr(-, Id(E)))), VarDecl(Da, BooleanType, BinExpr(::, FuncCall(H, []), UnExpr(-, Id(iTPG2))))]))
	FuncDecl(c, AutoType, [InheritOutParam(HH, AutoType)], None, BlockStmt([CallStmt(G3G, )]))
])"""
		self.assertTrue(TestAST.test(input, expect, 364))

	def test_365(self):
		input = """H , x  : array [ 0 , 5_38_2115 ] of string    = uC   && GA4yAe    || f   - W     - ! z   / ez        , { }        ;   """
		expect = """Program([
	VarDecl(H, ArrayType([0, 5382115], StringType), BinExpr(||, BinExpr(&&, Id(uC), Id(GA4yAe)), BinExpr(-, BinExpr(-, Id(f), Id(W)), BinExpr(/, UnExpr(!, Id(z)), Id(ez)))))
	VarDecl(x, ArrayType([0, 5382115], StringType), ArrayLit([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 365))

	def test_366(self):
		input = """D : function string   ( out Stpc : boolean    , ZR : string    , YdG : auto   , inherit out _wP : auto    ) inherit M { }    hQ  : array [ 8 , 7_5_0 ] of string    = vGt ( )    == c   + TY    % Mt ( )     - ! V5a    - K   && mt         ;   BE : function array [ 0 , 1_2563_918_0 , 96 ] of boolean    ( ) { }    nmoZ : function auto  ( inherit Bg : string     ) inherit CZJ5M { return o1   && MT    != sCOYdD   + MHBY     :: Sqw9   - n    < l7   % x      ;   }    f : function auto  ( ) { while ( W   + H     :: - KV    != v   / T      ) break ;     C  : float   ;  }    """
		expect = """Program([
	FuncDecl(D, StringType, [OutParam(Stpc, BooleanType), Param(ZR, StringType), Param(YdG, AutoType), InheritOutParam(_wP, AutoType)], M, BlockStmt([]))
	VarDecl(hQ, ArrayType([8, 750], StringType), BinExpr(==, FuncCall(vGt, []), BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, Id(c), BinExpr(%, Id(TY), FuncCall(Mt, []))), UnExpr(!, Id(V5a))), Id(K)), Id(mt))))
	FuncDecl(BE, ArrayType([0, 125639180, 96], BooleanType), [], None, BlockStmt([]))
	FuncDecl(nmoZ, AutoType, [InheritParam(Bg, StringType)], CZJ5M, BlockStmt([ReturnStmt(BinExpr(::, BinExpr(!=, BinExpr(&&, Id(o1), Id(MT)), BinExpr(+, Id(sCOYdD), Id(MHBY))), BinExpr(<, BinExpr(-, Id(Sqw9), Id(n)), BinExpr(%, Id(l7), Id(x)))))]))
	FuncDecl(f, AutoType, [], None, BlockStmt([WhileStmt(BinExpr(::, BinExpr(+, Id(W), Id(H)), BinExpr(!=, UnExpr(-, Id(KV)), BinExpr(/, Id(v), Id(T)))), BreakStmt()), VarDecl(C, FloatType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 366))

	def test_367(self):
		input = """col : function void ( inherit out Teub_ : array [ 4 ] of string      ) inherit B7C { N , q  : array [ 0 , 895_53_4_044215_9345 , 6986 , 47_452_5 ] of string    = i   + DH     :: ! d    < B   / Fo      , lY   * iEOXlx     :: zq ( )       ;  xcO , qz , hA , t  : array [ 0 , 3_00_17 , 0 ] of integer    ;  K , G , v , k , B  : integer   = bO   * kDq      , - zV    <= ! i      , - u      , JI   * yA     :: - P6    > Gn3I   && GcDyUH      , - x    > er      ;  s  : integer   ;  sqZ3qCS  : integer   = ! brMa4     :: J ( )    < Km   - j       ;  }    A , h , w  : boolean   ;   """
		expect = """Program([
	FuncDecl(col, VoidType, [InheritOutParam(Teub_, ArrayType([4], StringType))], B7C, BlockStmt([VarDecl(N, ArrayType([0, 8955340442159345, 6986, 474525], StringType), BinExpr(::, BinExpr(+, Id(i), Id(DH)), BinExpr(<, UnExpr(!, Id(d)), BinExpr(/, Id(B), Id(Fo))))), VarDecl(q, ArrayType([0, 8955340442159345, 6986, 474525], StringType), BinExpr(::, BinExpr(*, Id(lY), Id(iEOXlx)), FuncCall(zq, []))), VarDecl(xcO, ArrayType([0, 30017, 0], IntegerType)), VarDecl(qz, ArrayType([0, 30017, 0], IntegerType)), VarDecl(hA, ArrayType([0, 30017, 0], IntegerType)), VarDecl(t, ArrayType([0, 30017, 0], IntegerType)), VarDecl(K, IntegerType, BinExpr(*, Id(bO), Id(kDq))), VarDecl(G, IntegerType, BinExpr(<=, UnExpr(-, Id(zV)), UnExpr(!, Id(i)))), VarDecl(v, IntegerType, UnExpr(-, Id(u))), VarDecl(k, IntegerType, BinExpr(::, BinExpr(*, Id(JI), Id(yA)), BinExpr(>, UnExpr(-, Id(P6)), BinExpr(&&, Id(Gn3I), Id(GcDyUH))))), VarDecl(B, IntegerType, BinExpr(>, UnExpr(-, Id(x)), Id(er))), VarDecl(s, IntegerType), VarDecl(sqZ3qCS, IntegerType, BinExpr(::, UnExpr(!, Id(brMa4)), BinExpr(<, FuncCall(J, []), BinExpr(-, Id(Km), Id(j)))))]))
	VarDecl(A, BooleanType)
	VarDecl(h, BooleanType)
	VarDecl(w, BooleanType)
])"""
		self.assertTrue(TestAST.test(input, expect, 367))

	def test_368(self):
		input = """i  : auto  = ! g   - N7G0SI1    - EJ      :: ! ! ! z         ;   w , iBGe  : array [ 0 ] of string    = CXdrpO   && hQ    * - VvCnK     || H7Z   && B    % tUre   || pj       :: uQmg   >= b   * uvA    + 2     / ! F    && R   / T8d        , 0    && G_   % z     % B   || dW    && Aw   + r       :: ! w   / G7    || K   / qD         ;   """
		expect = """Program([
	VarDecl(i, AutoType, BinExpr(::, BinExpr(-, BinExpr(-, UnExpr(!, Id(g)), Id(N7G0SI1)), Id(EJ)), UnExpr(!, UnExpr(!, UnExpr(!, Id(z))))))
	VarDecl(w, ArrayType([0], StringType), BinExpr(::, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(&&, Id(CXdrpO), BinExpr(*, Id(hQ), UnExpr(-, Id(VvCnK)))), Id(H7Z)), BinExpr(%, Id(B), Id(tUre))), Id(pj)), BinExpr(>=, Id(uQmg), BinExpr(&&, BinExpr(+, BinExpr(*, Id(b), Id(uvA)), BinExpr(/, IntegerLit(2), UnExpr(!, Id(F)))), BinExpr(/, Id(R), Id(T8d))))))
	VarDecl(iBGe, ArrayType([0], StringType), BinExpr(::, BinExpr(&&, BinExpr(||, BinExpr(&&, IntegerLit(0), BinExpr(%, BinExpr(%, Id(G_), Id(z)), Id(B))), Id(dW)), BinExpr(+, Id(Aw), Id(r))), BinExpr(||, BinExpr(/, UnExpr(!, Id(w)), Id(G7)), BinExpr(/, Id(K), Id(qD)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 368))

	def test_369(self):
		input = """TM : function void ( out rF : integer     ) { k  : float   = W   && VG     :: - L       ;  }    """
		expect = """Program([
	FuncDecl(TM, VoidType, [OutParam(rF, IntegerType)], None, BlockStmt([VarDecl(k, FloatType, BinExpr(::, BinExpr(&&, Id(W), Id(VG)), UnExpr(-, Id(L))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 369))

	def test_370(self):
		input = """a : function auto  ( io : auto    ) { p  = G ( )    < B   + kB     :: mi     ;   m  : array [ 0 ] of boolean    ;  QK , M  : array [ 0 ] of string    ;  while ( X   * m    <= - Z     :: fH   * V      ) break ;     s , D  : auto  = z53   && w      , jl5r ( )    == Z      ;  M , zaK73  : float   ;  if ( - O      ) break ;   else return ;     }    p : function void ( out z : array [ 32 ] of string     , inherit out aA : array [ 0 ] of float      ) inherit R { return ! D      ;   }    L : function void ( ) inherit cW { }    """
		expect = """Program([
	FuncDecl(a, AutoType, [Param(io, AutoType)], None, BlockStmt([AssignStmt(Id(p), BinExpr(::, BinExpr(<, FuncCall(G, []), BinExpr(+, Id(B), Id(kB))), Id(mi))), VarDecl(m, ArrayType([0], BooleanType)), VarDecl(QK, ArrayType([0], StringType)), VarDecl(M, ArrayType([0], StringType)), WhileStmt(BinExpr(::, BinExpr(<=, BinExpr(*, Id(X), Id(m)), UnExpr(-, Id(Z))), BinExpr(*, Id(fH), Id(V))), BreakStmt()), VarDecl(s, AutoType, BinExpr(&&, Id(z53), Id(w))), VarDecl(D, AutoType, BinExpr(==, FuncCall(jl5r, []), Id(Z))), VarDecl(M, FloatType), VarDecl(zaK73, FloatType), IfStmt(UnExpr(-, Id(O)), BreakStmt(), ReturnStmt())]))
	FuncDecl(p, VoidType, [OutParam(z, ArrayType([32], StringType)), InheritOutParam(aA, ArrayType([0], FloatType))], R, BlockStmt([ReturnStmt(UnExpr(!, Id(D)))]))
	FuncDecl(L, VoidType, [], cW, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 370))

	def test_371(self):
		input = """i , b2  : array [ 0 ] of float    = - uFqL   + pHtM     + ! vP   && O      == ! ! ""        , - B ( )     % b   / F    && P   * u         ;   R , vHT  : auto  = - z   && K    / bne   + G        , - N    + T    % ! Y   + JZ9s         ;   j : function void ( ) { }    O , Kl  : string   ;   """
		expect = """Program([
	VarDecl(i, ArrayType([0], FloatType), BinExpr(==, BinExpr(&&, BinExpr(+, BinExpr(+, UnExpr(-, Id(uFqL)), Id(pHtM)), UnExpr(!, Id(vP))), Id(O)), UnExpr(!, UnExpr(!, StringLit()))))
	VarDecl(b2, ArrayType([0], FloatType), BinExpr(&&, BinExpr(/, BinExpr(%, UnExpr(-, FuncCall(B, [])), Id(b)), Id(F)), BinExpr(*, Id(P), Id(u))))
	VarDecl(R, AutoType, BinExpr(&&, UnExpr(-, Id(z)), BinExpr(+, BinExpr(/, Id(K), Id(bne)), Id(G))))
	VarDecl(vHT, AutoType, BinExpr(+, BinExpr(+, UnExpr(-, Id(N)), BinExpr(%, Id(T), UnExpr(!, Id(Y)))), Id(JZ9s)))
	FuncDecl(j, VoidType, [], None, BlockStmt([]))
	VarDecl(O, StringType)
	VarDecl(Kl, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 371))

	def test_372(self):
		input = """r : function array [ 8_6_5816_491 , 0 ] of boolean    ( out m : integer     ) { }    m , u2  : string   = sm    :: ! ! ""        , d   - N    + vZs   / i     && Q ( )    / - yPA      == - - ! d       :: ! f   % s8B    && 0      <= z   + n    / - Qloh     - YM   * UL    + L   + d         ;   """
		expect = """Program([
	FuncDecl(r, ArrayType([865816491, 0], BooleanType), [OutParam(m, IntegerType)], None, BlockStmt([]))
	VarDecl(m, StringType, BinExpr(::, Id(sm), UnExpr(!, UnExpr(!, StringLit()))))
	VarDecl(u2, StringType, BinExpr(::, BinExpr(==, BinExpr(&&, BinExpr(+, BinExpr(-, Id(d), Id(N)), BinExpr(/, Id(vZs), Id(i))), BinExpr(/, FuncCall(Q, []), UnExpr(-, Id(yPA)))), UnExpr(-, UnExpr(-, UnExpr(!, Id(d))))), BinExpr(<=, BinExpr(&&, BinExpr(%, UnExpr(!, Id(f)), Id(s8B)), IntegerLit(0)), BinExpr(+, BinExpr(+, BinExpr(-, BinExpr(+, Id(z), BinExpr(/, Id(n), UnExpr(-, Id(Qloh)))), BinExpr(*, Id(YM), Id(UL))), Id(L)), Id(d)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 372))

	def test_373(self):
		input = """S : function void ( ) { do { }  while ( gKi   && Rt     :: GC2   + b      ) ;   }    vT : function array [ 0 , 80_7_8 , 0 ] of string    ( out ig : auto   , v : boolean    , t_T : auto    ) inherit o0e5qpJ { }    """
		expect = """Program([
	FuncDecl(S, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(::, BinExpr(&&, Id(gKi), Id(Rt)), BinExpr(+, Id(GC2), Id(b))), BlockStmt([]))]))
	FuncDecl(vT, ArrayType([0, 8078, 0], StringType), [OutParam(ig, AutoType), Param(v, BooleanType), Param(t_T, AutoType)], o0e5qpJ, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 373))

	def test_374(self):
		input = """mkw : function void ( inherit out i : auto    ) { return ;   }    """
		expect = """Program([
	FuncDecl(mkw, VoidType, [InheritOutParam(i, AutoType)], None, BlockStmt([ReturnStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 374))

	def test_375(self):
		input = """m8Ah : function void ( out S : auto    ) inherit Am { }    Mc : function array [ 0 ] of float    ( ) inherit A { }    """
		expect = """Program([
	FuncDecl(m8Ah, VoidType, [OutParam(S, AutoType)], Am, BlockStmt([]))
	FuncDecl(Mc, ArrayType([0], FloatType), [], A, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 375))

	def test_376(self):
		input = """V5l : function void ( out JF : boolean     ) { We9  : array [ 71 ] of float    ;  }    """
		expect = """Program([
	FuncDecl(V5l, VoidType, [OutParam(JF, BooleanType)], None, BlockStmt([VarDecl(We9, ArrayType([71], FloatType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 376))

	def test_377(self):
		input = """Y  : array [ 6_89_5 , 0 ] of string    = xc   % W    || - kOw     % H    >= h ( )    / - D    + P        ;   """
		expect = """Program([
	VarDecl(Y, ArrayType([6895, 0], StringType), BinExpr(>=, BinExpr(||, BinExpr(%, Id(xc), Id(W)), BinExpr(%, UnExpr(-, Id(kOw)), Id(H))), BinExpr(+, BinExpr(/, FuncCall(h, []), UnExpr(-, Id(D))), Id(P))))
])"""
		self.assertTrue(TestAST.test(input, expect, 377))

	def test_378(self):
		input = """SXZib : function void ( out zbt : string    , inherit out Qsy : array [ 0 , 7_0496_610070 ] of float      ) { }    """
		expect = """Program([
	FuncDecl(SXZib, VoidType, [OutParam(zbt, StringType), InheritOutParam(Qsy, ArrayType([0, 70496610070], FloatType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 378))

	def test_379(self):
		input = """IoS : function void ( ) inherit p { }    """
		expect = """Program([
	FuncDecl(IoS, VoidType, [], p, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 379))

	def test_380(self):
		input = """H : function boolean   ( ) inherit tg { P , G , b  : auto  ;  }    j , GB , SG1h  : integer   ;   gbgVWUQ : function array [ 0 , 65_28_22_88290_3_07 , 3_23_9 ] of boolean    ( ) inherit DxV2 { WKXVN  : array [ 6_4_000_0 , 56 , 8_9_9_33_8_1_3_0 , 4 ] of string    ;  }    """
		expect = """Program([
	FuncDecl(H, BooleanType, [], tg, BlockStmt([VarDecl(P, AutoType), VarDecl(G, AutoType), VarDecl(b, AutoType)]))
	VarDecl(j, IntegerType)
	VarDecl(GB, IntegerType)
	VarDecl(SG1h, IntegerType)
	FuncDecl(gbgVWUQ, ArrayType([0, 65282288290307, 3239], BooleanType), [], DxV2, BlockStmt([VarDecl(WKXVN, ArrayType([640000, 56, 899338130, 4], StringType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 380))

	def test_381(self):
		input = """iq : function void ( ) { }    w : function void ( ) inherit l { }    """
		expect = """Program([
	FuncDecl(iq, VoidType, [], None, BlockStmt([]))
	FuncDecl(w, VoidType, [], l, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 381))

	def test_382(self):
		input = """xt : function integer   ( Sfn : string     ) { }    """
		expect = """Program([
	FuncDecl(xt, IntegerType, [Param(Sfn, StringType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 382))

	def test_383(self):
		input = """yHEnX : function void ( ) inherit r { { rZ  : array [ 634 , 0 , 0 , 0 , 0 ] of boolean    ;  }   }    """
		expect = """Program([
	FuncDecl(yHEnX, VoidType, [], r, BlockStmt([BlockStmt([VarDecl(rZ, ArrayType([634, 0, 0, 0, 0], BooleanType))])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 383))

	def test_384(self):
		input = """q : function void ( inherit WS : integer    , inherit YZ : auto    ) { Z  : array [ 314 , 0 , 1_9787019 , 0 ] of integer    = H6t   || ib     :: - v68       ;  }    """
		expect = """Program([
	FuncDecl(q, VoidType, [InheritParam(WS, IntegerType), InheritParam(YZ, AutoType)], None, BlockStmt([VarDecl(Z, ArrayType([314, 0, 19787019, 0], IntegerType), BinExpr(::, BinExpr(||, Id(H6t), Id(ib)), UnExpr(-, Id(v68))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 384))

	def test_385(self):
		input = """p  : float   ;   """
		expect = """Program([
	VarDecl(p, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 385))

	def test_386(self):
		input = """h , O , v  : array [ 0 , 6 , 0 ] of boolean    ;   i , O  : array [ 3_74_85_81 , 742 ] of string    ;   """
		expect = """Program([
	VarDecl(h, ArrayType([0, 6, 0], BooleanType))
	VarDecl(O, ArrayType([0, 6, 0], BooleanType))
	VarDecl(v, ArrayType([0, 6, 0], BooleanType))
	VarDecl(i, ArrayType([3748581, 742], StringType))
	VarDecl(O, ArrayType([3748581, 742], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 386))

	def test_387(self):
		input = """W : function void ( ) { }    r  : auto  = Em   < ! rm     :: - - c     > - U   + f     - e   && YK    / 0         ;   """
		expect = """Program([
	FuncDecl(W, VoidType, [], None, BlockStmt([]))
	VarDecl(r, AutoType, BinExpr(::, BinExpr(<, Id(Em), UnExpr(!, Id(rm))), BinExpr(>, UnExpr(-, UnExpr(-, Id(c))), BinExpr(&&, BinExpr(-, BinExpr(+, UnExpr(-, Id(U)), Id(f)), Id(e)), BinExpr(/, Id(YK), IntegerLit(0))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 387))

	def test_388(self):
		input = """Wp  : auto  = ! B   + H     || - Ro    + y   && RupZeeD      < ""     :: ""    % ! 0      == I ( )    - ! ""         ;   """
		expect = """Program([
	VarDecl(Wp, AutoType, BinExpr(::, BinExpr(<, BinExpr(&&, BinExpr(||, BinExpr(+, UnExpr(!, Id(B)), Id(H)), BinExpr(+, UnExpr(-, Id(Ro)), Id(y))), Id(RupZeeD)), StringLit()), BinExpr(==, BinExpr(%, StringLit(), UnExpr(!, IntegerLit(0))), BinExpr(-, FuncCall(I, []), UnExpr(!, StringLit())))))
])"""
		self.assertTrue(TestAST.test(input, expect, 388))

	def test_389(self):
		input = """nEwd  : array [ 47 , 0 ] of boolean    ;   """
		expect = """Program([
	VarDecl(nEwd, ArrayType([47, 0], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 389))

	def test_390(self):
		input = """L3K , Qzv , m , KC  : array [ 0 ] of integer    = - rAF   && hi     / K2   && t    - ! ZeNl3        , ! a   / uR    / tg   - j      != - G   || e     && - O ( )        , VJY   % SeQUA   * nOm     + ! s1J   || E        , 0    % xRP   && H   && z         ;   t : function void ( ) { }    """
		expect = """Program([
	VarDecl(L3K, ArrayType([0], IntegerType), BinExpr(&&, BinExpr(&&, UnExpr(-, Id(rAF)), BinExpr(/, Id(hi), Id(K2))), BinExpr(-, Id(t), UnExpr(!, Id(ZeNl3)))))
	VarDecl(Qzv, ArrayType([0], IntegerType), BinExpr(!=, BinExpr(-, BinExpr(/, BinExpr(/, UnExpr(!, Id(a)), Id(uR)), Id(tg)), Id(j)), BinExpr(&&, BinExpr(||, UnExpr(-, Id(G)), Id(e)), UnExpr(-, FuncCall(O, [])))))
	VarDecl(m, ArrayType([0], IntegerType), BinExpr(||, BinExpr(+, BinExpr(*, BinExpr(%, Id(VJY), Id(SeQUA)), Id(nOm)), UnExpr(!, Id(s1J))), Id(E)))
	VarDecl(KC, ArrayType([0], IntegerType), BinExpr(&&, BinExpr(&&, BinExpr(%, IntegerLit(0), Id(xRP)), Id(H)), Id(z)))
	FuncDecl(t, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 390))

	def test_391(self):
		input = """j : function array [ 59_612_5_7_4 , 0 , 94_72 , 0 ] of float    ( ) { }    gcNRs , muZ  : string   ;   D : function void ( lWh : array [ 94 ] of boolean      ) inherit F { }    N : function void ( ) inherit e { }    """
		expect = """Program([
	FuncDecl(j, ArrayType([59612574, 0, 9472, 0], FloatType), [], None, BlockStmt([]))
	VarDecl(gcNRs, StringType)
	VarDecl(muZ, StringType)
	FuncDecl(D, VoidType, [Param(lWh, ArrayType([94], BooleanType))], F, BlockStmt([]))
	FuncDecl(N, VoidType, [], e, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 391))

	def test_392(self):
		input = """b  : boolean   = c   > ""    && - - Dh       :: - - - QTdpF         ;   eEzT  : auto  ;   """
		expect = """Program([
	VarDecl(b, BooleanType, BinExpr(::, BinExpr(>, Id(c), BinExpr(&&, StringLit(), UnExpr(-, UnExpr(-, Id(Dh))))), UnExpr(-, UnExpr(-, UnExpr(-, Id(QTdpF))))))
	VarDecl(eEzT, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 392))

	def test_393(self):
		input = """v , mY  : float   ;   """
		expect = """Program([
	VarDecl(v, FloatType)
	VarDecl(mY, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 393))

	def test_394(self):
		input = """D : function string   ( out ghCcS : array [ 0 ] of string     , h : array [ 0 ] of boolean      ) inherit WPuM { Q  = ! Cu     :: ! BP      ;   i , EGEu  : auto  = C   % b    != fD   + ktd      , Z   / oB    == s4qY   % GR     :: - T       ;  return ;   }    U , vRT , r_  : auto  ;   """
		expect = """Program([
	FuncDecl(D, StringType, [OutParam(ghCcS, ArrayType([0], StringType)), Param(h, ArrayType([0], BooleanType))], WPuM, BlockStmt([AssignStmt(Id(Q), BinExpr(::, UnExpr(!, Id(Cu)), UnExpr(!, Id(BP)))), VarDecl(i, AutoType, BinExpr(!=, BinExpr(%, Id(C), Id(b)), BinExpr(+, Id(fD), Id(ktd)))), VarDecl(EGEu, AutoType, BinExpr(::, BinExpr(==, BinExpr(/, Id(Z), Id(oB)), BinExpr(%, Id(s4qY), Id(GR))), UnExpr(-, Id(T)))), ReturnStmt()]))
	VarDecl(U, AutoType)
	VarDecl(vRT, AutoType)
	VarDecl(r_, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 394))

	def test_395(self):
		input = """rvKsvh : function void ( inherit sk : float     ) { Ip  : string   = D   && t     :: ""    == pKY   || U       ;  }    """
		expect = """Program([
	FuncDecl(rvKsvh, VoidType, [InheritParam(sk, FloatType)], None, BlockStmt([VarDecl(Ip, StringType, BinExpr(::, BinExpr(&&, Id(D), Id(t)), BinExpr(==, StringLit(), BinExpr(||, Id(pKY), Id(U)))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 395))

	def test_396(self):
		input = """O , WB , k , b , khTdd , t0  : float   ;   """
		expect = """Program([
	VarDecl(O, FloatType)
	VarDecl(WB, FloatType)
	VarDecl(k, FloatType)
	VarDecl(b, FloatType)
	VarDecl(khTdd, FloatType)
	VarDecl(t0, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 396))

	def test_397(self):
		input = """ti : function integer   ( out TtTYgr : boolean    , inherit out wyD : float    , out F : array [ 94 , 3 ] of integer     , G : string     ) { }    """
		expect = """Program([
	FuncDecl(ti, IntegerType, [OutParam(TtTYgr, BooleanType), InheritOutParam(wyD, FloatType), OutParam(F, ArrayType([94, 3], IntegerType)), Param(G, StringType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 397))

	def test_398(self):
		input = """M , _L , v  : auto  ;   eR , U , Z9I  : float   ;   """
		expect = """Program([
	VarDecl(M, AutoType)
	VarDecl(_L, AutoType)
	VarDecl(v, AutoType)
	VarDecl(eR, FloatType)
	VarDecl(U, FloatType)
	VarDecl(Z9I, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 398))

	def test_399(self):
		input = """A : function integer   ( inherit out A : auto    ) { }    HPyLP , wLLVxM , b  : auto  = - - RvAqj    - - j5      >= - ! GA8      :: ! Rf   * do1     && ! A    + Dl   - ba        , - UU    && p   && N     && C ( )    % ! Nss       :: - R    && - yuJ     / ! e   || c        , B9w ( )    + K   && o    % j   || y      == ! Yz   % Sn     / ! aK   % x         ;   IXR : function void ( ) { return R   + hwtD    < ! rKF     :: cC   && B      ;   }    """
		expect = """Program([
	FuncDecl(A, IntegerType, [InheritOutParam(A, AutoType)], None, BlockStmt([]))
	VarDecl(HPyLP, AutoType, BinExpr(::, BinExpr(>=, BinExpr(-, UnExpr(-, UnExpr(-, Id(RvAqj))), UnExpr(-, Id(j5))), UnExpr(-, UnExpr(!, Id(GA8)))), BinExpr(&&, BinExpr(*, UnExpr(!, Id(Rf)), Id(do1)), BinExpr(-, BinExpr(+, UnExpr(!, Id(A)), Id(Dl)), Id(ba)))))
	VarDecl(wLLVxM, AutoType, BinExpr(::, BinExpr(&&, BinExpr(&&, BinExpr(&&, UnExpr(-, Id(UU)), Id(p)), Id(N)), BinExpr(%, FuncCall(C, []), UnExpr(!, Id(Nss)))), BinExpr(||, BinExpr(&&, UnExpr(-, Id(R)), BinExpr(/, UnExpr(-, Id(yuJ)), UnExpr(!, Id(e)))), Id(c))))
	VarDecl(b, AutoType, BinExpr(==, BinExpr(||, BinExpr(&&, BinExpr(+, FuncCall(B9w, []), Id(K)), BinExpr(%, Id(o), Id(j))), Id(y)), BinExpr(%, BinExpr(/, BinExpr(%, UnExpr(!, Id(Yz)), Id(Sn)), UnExpr(!, Id(aK))), Id(x))))
	FuncDecl(IXR, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(::, BinExpr(<, BinExpr(+, Id(R), Id(hwtD)), UnExpr(!, Id(rKF))), BinExpr(&&, Id(cC), Id(B))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 399))

	def test_400(self):
		input = """P  : array [ 0 ] of float    = weO   <= ! ! kW     % - x   + wzgIsCJ         ;   m : function void ( inherit out f : auto    ) { xnfln  : array [ 0 ] of boolean    = - A     :: ! h    > a   / d       ;  G , M  : array [ 4_38_00_846 , 1 , 0 , 7 ] of float    ;  }    """
		expect = """Program([
	VarDecl(P, ArrayType([0], FloatType), BinExpr(<=, Id(weO), BinExpr(+, BinExpr(%, UnExpr(!, UnExpr(!, Id(kW))), UnExpr(-, Id(x))), Id(wzgIsCJ))))
	FuncDecl(m, VoidType, [InheritOutParam(f, AutoType)], None, BlockStmt([VarDecl(xnfln, ArrayType([0], BooleanType), BinExpr(::, UnExpr(-, Id(A)), BinExpr(>, UnExpr(!, Id(h)), BinExpr(/, Id(a), Id(d))))), VarDecl(G, ArrayType([43800846, 1, 0, 7], FloatType)), VarDecl(M, ArrayType([43800846, 1, 0, 7], FloatType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 400))

	def test_401(self):
		input = """XTp : function void ( ) inherit ba { }    """
		expect = """Program([
	FuncDecl(XTp, VoidType, [], ba, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 401))

	def test_402(self):
		input = """W4H : function auto  ( ) inherit Fe { O , kJ  : boolean   = G   + e     :: Tt_c2   % a      , _   - Ydw       ;  }    zX : function auto  ( ) inherit v { }    """
		expect = """Program([
	FuncDecl(W4H, AutoType, [], Fe, BlockStmt([VarDecl(O, BooleanType, BinExpr(::, BinExpr(+, Id(G), Id(e)), BinExpr(%, Id(Tt_c2), Id(a)))), VarDecl(kJ, BooleanType, BinExpr(-, Id(_), Id(Ydw)))]))
	FuncDecl(zX, AutoType, [], v, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 402))

	def test_403(self):
		input = """j , O  : string   ;   """
		expect = """Program([
	VarDecl(j, StringType)
	VarDecl(O, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 403))

	def test_404(self):
		input = """f : function integer   ( s : array [ 7 ] of boolean      ) inherit z { }    S , RJ  : array [ 0 ] of integer    ;   """
		expect = """Program([
	FuncDecl(f, IntegerType, [Param(s, ArrayType([7], BooleanType))], z, BlockStmt([]))
	VarDecl(S, ArrayType([0], IntegerType))
	VarDecl(RJ, ArrayType([0], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 404))

	def test_405(self):
		input = """xV , j , qB  : float   = - ""    - - SJg        , ! v   && A_q     - pvzi ( )    || ! c      < gt ( )    / ! o    + g   && px       :: 0    || ! o     * ! vay   * rD        , - sY   + L     / g4QB ( )     < { }        ;   """
		expect = """Program([
	VarDecl(xV, FloatType, BinExpr(-, UnExpr(-, StringLit()), UnExpr(-, Id(SJg))))
	VarDecl(j, FloatType, BinExpr(::, BinExpr(<, BinExpr(||, BinExpr(&&, UnExpr(!, Id(v)), BinExpr(-, Id(A_q), FuncCall(pvzi, []))), UnExpr(!, Id(c))), BinExpr(&&, BinExpr(+, BinExpr(/, FuncCall(gt, []), UnExpr(!, Id(o))), Id(g)), Id(px))), BinExpr(||, IntegerLit(0), BinExpr(*, BinExpr(*, UnExpr(!, Id(o)), UnExpr(!, Id(vay))), Id(rD)))))
	VarDecl(qB, FloatType, BinExpr(<, BinExpr(+, UnExpr(-, Id(sY)), BinExpr(/, Id(L), FuncCall(g4QB, []))), ArrayLit([])))
])"""
		self.assertTrue(TestAST.test(input, expect, 405))

	def test_406(self):
		input = """EK5P : function void ( ) { }    """
		expect = """Program([
	FuncDecl(EK5P, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 406))

	def test_407(self):
		input = """CA15 : function array [ 0 , 0 ] of integer    ( ) inherit y { Fh  : auto  ;  e , Z  : array [ 77 ] of integer    ;  }    """
		expect = """Program([
	FuncDecl(CA15, ArrayType([0, 0], IntegerType), [], y, BlockStmt([VarDecl(Fh, AutoType), VarDecl(e, ArrayType([77], IntegerType)), VarDecl(Z, ArrayType([77], IntegerType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 407))

	def test_408(self):
		input = """VSQj0 : function void ( ) inherit A { break ;   }    l : function integer   ( inherit out sqL : auto    ) { while ( l   % p     :: KS4   - B    <= fORjNe   && Sl      ) break ;     }    sC : function auto  ( out V : float    , out bLBhK : boolean     ) { }    ge : function void ( inherit out h : array [ 0 ] of float     , n : auto    ) { continue ;   continue ;   for ( w  = ! CF0     :: T   * K    == 0      , _k ( )    != ! d     :: O   - b      , c   % l      ) continue ;     S ( )  ;   }    oIf  : auto  ;   """
		expect = """Program([
	FuncDecl(VSQj0, VoidType, [], A, BlockStmt([BreakStmt()]))
	FuncDecl(l, IntegerType, [InheritOutParam(sqL, AutoType)], None, BlockStmt([WhileStmt(BinExpr(::, BinExpr(%, Id(l), Id(p)), BinExpr(<=, BinExpr(-, Id(KS4), Id(B)), BinExpr(&&, Id(fORjNe), Id(Sl)))), BreakStmt())]))
	FuncDecl(sC, AutoType, [OutParam(V, FloatType), OutParam(bLBhK, BooleanType)], None, BlockStmt([]))
	FuncDecl(ge, VoidType, [InheritOutParam(h, ArrayType([0], FloatType)), Param(n, AutoType)], None, BlockStmt([ContinueStmt(), ContinueStmt(), ForStmt(AssignStmt(Id(w), BinExpr(::, UnExpr(!, Id(CF0)), BinExpr(==, BinExpr(*, Id(T), Id(K)), IntegerLit(0)))), BinExpr(::, BinExpr(!=, FuncCall(_k, []), UnExpr(!, Id(d))), BinExpr(-, Id(O), Id(b))), BinExpr(%, Id(c), Id(l)), ContinueStmt()), CallStmt(S, )]))
	VarDecl(oIf, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 408))

	def test_409(self):
		input = """SK8 , JPN  : auto  ;   X : function integer   ( ) inherit j { }    """
		expect = """Program([
	VarDecl(SK8, AutoType)
	VarDecl(JPN, AutoType)
	FuncDecl(X, IntegerType, [], j, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 409))

	def test_410(self):
		input = """KgCgK : function float   ( ) inherit D { qeG , P4  : auto  ;  do { }  while ( ""     :: - X    >= N8j   - H      ) ;   }    """
		expect = """Program([
	FuncDecl(KgCgK, FloatType, [], D, BlockStmt([VarDecl(qeG, AutoType), VarDecl(P4, AutoType), DoWhileStmt(BinExpr(::, StringLit(), BinExpr(>=, UnExpr(-, Id(X)), BinExpr(-, Id(N8j), Id(H)))), BlockStmt([]))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 410))

	def test_411(self):
		input = """jnu : function void ( out nMA : boolean    , out U5R : auto   , inherit out Y : string     ) inherit oM0BUcz { m , _oz , A , kC  : boolean   = - oku    >= - a      , t   + KF0      , ! lW      , 0    > - Y       ;  }    """
		expect = """Program([
	FuncDecl(jnu, VoidType, [OutParam(nMA, BooleanType), OutParam(U5R, AutoType), InheritOutParam(Y, StringType)], oM0BUcz, BlockStmt([VarDecl(m, BooleanType, BinExpr(>=, UnExpr(-, Id(oku)), UnExpr(-, Id(a)))), VarDecl(_oz, BooleanType, BinExpr(+, Id(t), Id(KF0))), VarDecl(A, BooleanType, UnExpr(!, Id(lW))), VarDecl(kC, BooleanType, BinExpr(>, IntegerLit(0), UnExpr(-, Id(Y))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 411))

	def test_412(self):
		input = """PR : function void ( ) { }    i : function void ( inherit out d : array [ 46 , 0 , 2_8_72_504 , 0 ] of string     , out D : integer     ) { }    mu : function boolean   ( inherit yld : float     ) { W  : array [ 6 , 0 ] of integer    ;  S6P  : string   ;  _  = kbHzicXL3k   / v     :: - BfXf    != M   % noB2T      ;   }    dLC : function void ( ) { zh ( )  ;   }    p1 : function auto  ( inherit out l : auto    ) { G , Wo , e  : auto  ;  }    """
		expect = """Program([
	FuncDecl(PR, VoidType, [], None, BlockStmt([]))
	FuncDecl(i, VoidType, [InheritOutParam(d, ArrayType([46, 0, 2872504, 0], StringType)), OutParam(D, IntegerType)], None, BlockStmt([]))
	FuncDecl(mu, BooleanType, [InheritParam(yld, FloatType)], None, BlockStmt([VarDecl(W, ArrayType([6, 0], IntegerType)), VarDecl(S6P, StringType), AssignStmt(Id(_), BinExpr(::, BinExpr(/, Id(kbHzicXL3k), Id(v)), BinExpr(!=, UnExpr(-, Id(BfXf)), BinExpr(%, Id(M), Id(noB2T)))))]))
	FuncDecl(dLC, VoidType, [], None, BlockStmt([CallStmt(zh, )]))
	FuncDecl(p1, AutoType, [InheritOutParam(l, AutoType)], None, BlockStmt([VarDecl(G, AutoType), VarDecl(Wo, AutoType), VarDecl(e, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 412))

	def test_413(self):
		input = """k  : boolean   = ! nl    > ! N   || ttj    % Q   && t       :: Al4miY   && l    - X   || tUL     && ""    && k   - U7         ;   IL , q , NAV  : float   = QdS   + LKlRFR    * y    / ! PNH    || - y      != bbe   && umiH    - n   / tt     - true      :: ! - ! Gp      >= ! xwf      , - ! i9o    && ! ET        , m ( )       ;   a , m  : auto  ;   """
		expect = """Program([
	VarDecl(k, BooleanType, BinExpr(::, BinExpr(>, UnExpr(!, Id(nl)), BinExpr(&&, BinExpr(||, UnExpr(!, Id(N)), BinExpr(%, Id(ttj), Id(Q))), Id(t))), BinExpr(&&, BinExpr(&&, BinExpr(||, BinExpr(&&, Id(Al4miY), BinExpr(-, Id(l), Id(X))), Id(tUL)), StringLit()), BinExpr(-, Id(k), Id(U7)))))
	VarDecl(IL, FloatType, BinExpr(::, BinExpr(!=, BinExpr(||, BinExpr(+, Id(QdS), BinExpr(/, BinExpr(*, Id(LKlRFR), Id(y)), UnExpr(!, Id(PNH)))), UnExpr(-, Id(y))), BinExpr(&&, Id(bbe), BinExpr(-, BinExpr(-, Id(umiH), BinExpr(/, Id(n), Id(tt))), BooleanLit(True)))), BinExpr(>=, UnExpr(!, UnExpr(-, UnExpr(!, Id(Gp)))), UnExpr(!, Id(xwf)))))
	VarDecl(q, FloatType, BinExpr(&&, UnExpr(-, UnExpr(!, Id(i9o))), UnExpr(!, Id(ET))))
	VarDecl(NAV, FloatType, FuncCall(m, []))
	VarDecl(a, AutoType)
	VarDecl(m, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 413))

	def test_414(self):
		input = """TI3J  : float   ;   """
		expect = """Program([
	VarDecl(TI3J, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 414))

	def test_415(self):
		input = """b  : auto  ;   zt  : array [ 63 , 0 ] of string    ;   """
		expect = """Program([
	VarDecl(b, AutoType)
	VarDecl(zt, ArrayType([63, 0], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 415))

	def test_416(self):
		input = """A_3Wj : function void ( out w : auto   , inherit n6xPj : string     ) { }    """
		expect = """Program([
	FuncDecl(A_3Wj, VoidType, [OutParam(w, AutoType), InheritParam(n6xPj, StringType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 416))

	def test_417(self):
		input = """n  : auto  = - - l   / MX       :: fj   - W    * xFXN   || V     / ! HF   && eB         ;   S : function void ( E7Q : boolean     ) inherit X { }    T6 , UTZ  : string   ;   l_  : auto  = l0 ( )     :: Mu5R   && xr    * 0     * j       ;   CocmS : function auto  ( Pi : array [ 113 ] of integer      ) { }    k9  : array [ 0 ] of float    ;   H , K  : array [ 0 ] of float    = - Tb   - g    || ! Z      != d   - F    || n ( )     - Eu5g   + bc      :: ! n   / P    - Ym4   % b      <= eT     , P ( )    % ! u    || vnFP   * g      >= ! u   % k    % TF   % W         ;   u3 : function string   ( ) { Vgx  : auto  ;  }    """
		expect = """Program([
	VarDecl(n, AutoType, BinExpr(::, BinExpr(/, UnExpr(-, UnExpr(-, Id(l))), Id(MX)), BinExpr(&&, BinExpr(||, BinExpr(-, Id(fj), BinExpr(*, Id(W), Id(xFXN))), BinExpr(/, Id(V), UnExpr(!, Id(HF)))), Id(eB))))
	FuncDecl(S, VoidType, [Param(E7Q, BooleanType)], X, BlockStmt([]))
	VarDecl(T6, StringType)
	VarDecl(UTZ, StringType)
	VarDecl(l_, AutoType, BinExpr(::, FuncCall(l0, []), BinExpr(&&, Id(Mu5R), BinExpr(*, BinExpr(*, Id(xr), IntegerLit(0)), Id(j)))))
	FuncDecl(CocmS, AutoType, [Param(Pi, ArrayType([113], IntegerType))], None, BlockStmt([]))
	VarDecl(k9, ArrayType([0], FloatType))
	VarDecl(H, ArrayType([0], FloatType), BinExpr(::, BinExpr(!=, BinExpr(||, BinExpr(-, UnExpr(-, Id(Tb)), Id(g)), UnExpr(!, Id(Z))), BinExpr(||, BinExpr(-, Id(d), Id(F)), BinExpr(+, BinExpr(-, FuncCall(n, []), Id(Eu5g)), Id(bc)))), BinExpr(<=, BinExpr(-, BinExpr(/, UnExpr(!, Id(n)), Id(P)), BinExpr(%, Id(Ym4), Id(b))), Id(eT))))
	VarDecl(K, ArrayType([0], FloatType), BinExpr(>=, BinExpr(||, BinExpr(%, FuncCall(P, []), UnExpr(!, Id(u))), BinExpr(*, Id(vnFP), Id(g))), BinExpr(%, BinExpr(%, BinExpr(%, UnExpr(!, Id(u)), Id(k)), Id(TF)), Id(W))))
	FuncDecl(u3, StringType, [], None, BlockStmt([VarDecl(Vgx, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 417))

	def test_418(self):
		input = """D6 : function void ( ) inherit j { }    """
		expect = """Program([
	FuncDecl(D6, VoidType, [], j, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 418))

	def test_419(self):
		input = """M , u  : array [ 0 , 0 , 0 , 0 , 34_3 , 426_7 , 1 , 7015 ] of string    ;   """
		expect = """Program([
	VarDecl(M, ArrayType([0, 0, 0, 0, 343, 4267, 1, 7015], StringType))
	VarDecl(u, ArrayType([0, 0, 0, 0, 343, 4267, 1, 7015], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 419))

	def test_420(self):
		input = """E  : array [ 704 ] of boolean    = - - Vz2l ( )      >= ! B   && a    - Sp   % M         ;   xM , k , Z , QD , Su , G_  : float   ;   """
		expect = """Program([
	VarDecl(E, ArrayType([704], BooleanType), BinExpr(>=, UnExpr(-, UnExpr(-, FuncCall(Vz2l, []))), BinExpr(&&, UnExpr(!, Id(B)), BinExpr(-, Id(a), BinExpr(%, Id(Sp), Id(M))))))
	VarDecl(xM, FloatType)
	VarDecl(k, FloatType)
	VarDecl(Z, FloatType)
	VarDecl(QD, FloatType)
	VarDecl(Su, FloatType)
	VarDecl(G_, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 420))

	def test_421(self):
		input = """i , S  : auto  ;   """
		expect = """Program([
	VarDecl(i, AutoType)
	VarDecl(S, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 421))

	def test_422(self):
		input = """c , ts , IKD  : auto  = r ( )     :: H   != - - r     || - Q    - B2S   + P        , - Vu2   - t86    && vaZAy   * xHz      < YsDQ   - jPF    - UP   * t     + w ( )      :: - ReYt ( )    * ! MxV      >= ! TCpv    + ! e     % M ( )    - O   + n        , d   || Gf    % UY5a   - O     * ! WB   / w6         ;   """
		expect = """Program([
	VarDecl(c, AutoType, BinExpr(::, FuncCall(r, []), BinExpr(!=, Id(H), BinExpr(||, UnExpr(-, UnExpr(-, Id(r))), BinExpr(+, BinExpr(-, UnExpr(-, Id(Q)), Id(B2S)), Id(P))))))
	VarDecl(ts, AutoType, BinExpr(::, BinExpr(<, BinExpr(&&, BinExpr(-, UnExpr(-, Id(Vu2)), Id(t86)), BinExpr(*, Id(vaZAy), Id(xHz))), BinExpr(+, BinExpr(-, BinExpr(-, Id(YsDQ), Id(jPF)), BinExpr(*, Id(UP), Id(t))), FuncCall(w, []))), BinExpr(>=, BinExpr(*, UnExpr(-, FuncCall(ReYt, [])), UnExpr(!, Id(MxV))), BinExpr(+, BinExpr(-, BinExpr(+, UnExpr(!, Id(TCpv)), BinExpr(%, UnExpr(!, Id(e)), FuncCall(M, []))), Id(O)), Id(n)))))
	VarDecl(IKD, AutoType, BinExpr(||, Id(d), BinExpr(-, BinExpr(%, Id(Gf), Id(UY5a)), BinExpr(/, BinExpr(*, Id(O), UnExpr(!, Id(WB))), Id(w6)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 422))

	def test_423(self):
		input = """w : function void ( out K : auto    ) { for ( ms  = t   % o8wFp     :: uV   || H    > kZig   && J      , a13   || w    != pY   + t6     :: q2 ( )    >= TL   * E      , q   - j    >= - _     :: rOvK   % O      ) return ;     for ( b  = IwP   / hL    == w   && B11      , - w    != O   * wi     :: ! RW5z    < IS ( )      , ! D     :: - RgV    > yO   || QH      ) continue ;     continue ;   }    """
		expect = """Program([
	FuncDecl(w, VoidType, [OutParam(K, AutoType)], None, BlockStmt([ForStmt(AssignStmt(Id(ms), BinExpr(::, BinExpr(%, Id(t), Id(o8wFp)), BinExpr(>, BinExpr(||, Id(uV), Id(H)), BinExpr(&&, Id(kZig), Id(J))))), BinExpr(::, BinExpr(!=, BinExpr(||, Id(a13), Id(w)), BinExpr(+, Id(pY), Id(t6))), BinExpr(>=, FuncCall(q2, []), BinExpr(*, Id(TL), Id(E)))), BinExpr(::, BinExpr(>=, BinExpr(-, Id(q), Id(j)), UnExpr(-, Id(_))), BinExpr(%, Id(rOvK), Id(O))), ReturnStmt()), ForStmt(AssignStmt(Id(b), BinExpr(==, BinExpr(/, Id(IwP), Id(hL)), BinExpr(&&, Id(w), Id(B11)))), BinExpr(::, BinExpr(!=, UnExpr(-, Id(w)), BinExpr(*, Id(O), Id(wi))), BinExpr(<, UnExpr(!, Id(RW5z)), FuncCall(IS, []))), BinExpr(::, UnExpr(!, Id(D)), BinExpr(>, UnExpr(-, Id(RgV)), BinExpr(||, Id(yO), Id(QH)))), ContinueStmt()), ContinueStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 423))

	def test_424(self):
		input = """a : function void ( ) { }    """
		expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 424))

	def test_425(self):
		input = """I , Bx0m  : array [ 1 , 0 , 0 , 0 , 0 ] of string    ;   I  : auto  ;   """
		expect = """Program([
	VarDecl(I, ArrayType([1, 0, 0, 0, 0], StringType))
	VarDecl(Bx0m, ArrayType([1, 0, 0, 0, 0], StringType))
	VarDecl(I, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 425))

	def test_426(self):
		input = """j , De , GZ , muQu3XT  : boolean   ;   aSAF1 : function array [ 1 , 0 ] of string    ( inherit R : boolean    , t : boolean    , _t : array [ 0 , 2 ] of boolean     , inherit BFK6TK : string    , out HEh : auto    ) { }    """
		expect = """Program([
	VarDecl(j, BooleanType)
	VarDecl(De, BooleanType)
	VarDecl(GZ, BooleanType)
	VarDecl(muQu3XT, BooleanType)
	FuncDecl(aSAF1, ArrayType([1, 0], StringType), [InheritParam(R, BooleanType), Param(t, BooleanType), Param(_t, ArrayType([0, 2], BooleanType)), InheritParam(BFK6TK, StringType), OutParam(HEh, AutoType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 426))

	def test_427(self):
		input = """V : function void ( kX : array [ 33_6_5_637955 , 0 , 0 ] of float     , inherit dKU1c : array [ 0 , 0 ] of boolean     , out GK : auto    ) { j  : string   = yF   && d     :: r   / FC    < G   + DLKvDfR       ;  W , M8 , XY  : auto  = a   - Sb    != - z      , I   % F     :: c   % x      , ! TH     :: Y   - X    >= - S       ;  ggs , i  : array [ 0 , 0 ] of string    = ""      , c   + DzSm       ;  }    """
		expect = """Program([
	FuncDecl(V, VoidType, [Param(kX, ArrayType([3365637955, 0, 0], FloatType)), InheritParam(dKU1c, ArrayType([0, 0], BooleanType)), OutParam(GK, AutoType)], None, BlockStmt([VarDecl(j, StringType, BinExpr(::, BinExpr(&&, Id(yF), Id(d)), BinExpr(<, BinExpr(/, Id(r), Id(FC)), BinExpr(+, Id(G), Id(DLKvDfR))))), VarDecl(W, AutoType, BinExpr(!=, BinExpr(-, Id(a), Id(Sb)), UnExpr(-, Id(z)))), VarDecl(M8, AutoType, BinExpr(::, BinExpr(%, Id(I), Id(F)), BinExpr(%, Id(c), Id(x)))), VarDecl(XY, AutoType, BinExpr(::, UnExpr(!, Id(TH)), BinExpr(>=, BinExpr(-, Id(Y), Id(X)), UnExpr(-, Id(S))))), VarDecl(ggs, ArrayType([0, 0], StringType), StringLit()), VarDecl(i, ArrayType([0, 0], StringType), BinExpr(+, Id(c), Id(DzSm)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 427))

	def test_428(self):
		input = """or : function array [ 0 ] of float    ( inherit out Nh : auto    ) inherit SGvW { }    """
		expect = """Program([
	FuncDecl(or, ArrayType([0], FloatType), [InheritOutParam(Nh, AutoType)], SGvW, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 428))

	def test_429(self):
		input = """m : function void ( e : array [ 5 ] of float      ) { tA  = h   % B     :: U   * aTT4u      ;   B  = ! WD      ;   do { }  while ( o   || b     :: v   / U      ) ;   CC  : string   ;  }    """
		expect = """Program([
	FuncDecl(m, VoidType, [Param(e, ArrayType([5], FloatType))], None, BlockStmt([AssignStmt(Id(tA), BinExpr(::, BinExpr(%, Id(h), Id(B)), BinExpr(*, Id(U), Id(aTT4u)))), AssignStmt(Id(B), UnExpr(!, Id(WD))), DoWhileStmt(BinExpr(::, BinExpr(||, Id(o), Id(b)), BinExpr(/, Id(v), Id(U))), BlockStmt([])), VarDecl(CC, StringType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 429))

	def test_430(self):
		input = """dtxo , X  : auto  = wE   + cCc    + Zm   - pp     % X   + L    % E   / hk        , jFlyo0 ( )    * ! K7     || z     :: - x   || g   || t         ;   X : function void ( ) inherit H { }    J  : boolean   = r   % uy2l    || ! A2     + - bu    % ! J8C      <= - Uu ( )        ;   """
		expect = """Program([
	VarDecl(dtxo, AutoType, BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(+, Id(wE), Id(cCc)), Id(Zm)), BinExpr(%, Id(pp), Id(X))), BinExpr(/, BinExpr(%, Id(L), Id(E)), Id(hk))))
	VarDecl(X, AutoType, BinExpr(::, BinExpr(||, BinExpr(*, FuncCall(jFlyo0, []), UnExpr(!, Id(K7))), Id(z)), BinExpr(||, BinExpr(||, UnExpr(-, Id(x)), Id(g)), Id(t))))
	FuncDecl(X, VoidType, [], H, BlockStmt([]))
	VarDecl(J, BooleanType, BinExpr(<=, BinExpr(||, BinExpr(%, Id(r), Id(uy2l)), BinExpr(+, UnExpr(!, Id(A2)), BinExpr(%, UnExpr(-, Id(bu)), UnExpr(!, Id(J8C))))), UnExpr(-, FuncCall(Uu, []))))
])"""
		self.assertTrue(TestAST.test(input, expect, 430))

	def test_431(self):
		input = """DU , N , Z  : array [ 7 ] of string    ;   j : function integer   ( ) { while ( - LI     :: I   >= u6   - cb      ) continue ;     }    vvsM : function void ( inherit out eyE : auto    ) { ryaz  : auto  = Aw   && Sgj3t       ;  YarP  : array [ 0 ] of float    = gQv   - q       ;  if ( x   % MC    == RO   / xP     :: ! C      ) { Tq  : float   ;  }     }    qY : function auto  ( inherit S : array [ 0 , 0 ] of boolean      ) { }    """
		expect = """Program([
	VarDecl(DU, ArrayType([7], StringType))
	VarDecl(N, ArrayType([7], StringType))
	VarDecl(Z, ArrayType([7], StringType))
	FuncDecl(j, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(::, UnExpr(-, Id(LI)), BinExpr(>=, Id(I), BinExpr(-, Id(u6), Id(cb)))), ContinueStmt())]))
	FuncDecl(vvsM, VoidType, [InheritOutParam(eyE, AutoType)], None, BlockStmt([VarDecl(ryaz, AutoType, BinExpr(&&, Id(Aw), Id(Sgj3t))), VarDecl(YarP, ArrayType([0], FloatType), BinExpr(-, Id(gQv), Id(q))), IfStmt(BinExpr(::, BinExpr(==, BinExpr(%, Id(x), Id(MC)), BinExpr(/, Id(RO), Id(xP))), UnExpr(!, Id(C))), BlockStmt([VarDecl(Tq, FloatType)]))]))
	FuncDecl(qY, AutoType, [InheritParam(S, ArrayType([0, 0], BooleanType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 431))

	def test_432(self):
		input = """wb  : array [ 0 ] of integer    = - ! - S         ;   F0 : function void ( ) inherit Z { }    """
		expect = """Program([
	VarDecl(wb, ArrayType([0], IntegerType), UnExpr(-, UnExpr(!, UnExpr(-, Id(S)))))
	FuncDecl(F0, VoidType, [], Z, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 432))

	def test_433(self):
		input = """D , W  : integer   = ! n   - _Kz    + eLl   - nwS      == ! C9ce    || ! T     / ! ! f        , ! t   / szPC     || LT   % wj    + y   / G      <= ! ! t   / Sw         ;   ElB : function void ( inherit out S : float     ) inherit VTp { }    """
		expect = """Program([
	VarDecl(D, IntegerType, BinExpr(==, BinExpr(-, BinExpr(+, BinExpr(-, UnExpr(!, Id(n)), Id(_Kz)), Id(eLl)), Id(nwS)), BinExpr(||, UnExpr(!, Id(C9ce)), BinExpr(/, UnExpr(!, Id(T)), UnExpr(!, UnExpr(!, Id(f)))))))
	VarDecl(W, IntegerType, BinExpr(<=, BinExpr(||, BinExpr(/, UnExpr(!, Id(t)), Id(szPC)), BinExpr(+, BinExpr(%, Id(LT), Id(wj)), BinExpr(/, Id(y), Id(G)))), BinExpr(/, UnExpr(!, UnExpr(!, Id(t))), Id(Sw))))
	FuncDecl(ElB, VoidType, [InheritOutParam(S, FloatType)], VTp, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 433))

	def test_434(self):
		input = """Z : function array [ 5 ] of float    ( inherit i : string     ) inherit F { }    CYk7 : function void ( ) inherit t { }    """
		expect = """Program([
	FuncDecl(Z, ArrayType([5], FloatType), [InheritParam(i, StringType)], F, BlockStmt([]))
	FuncDecl(CYk7, VoidType, [], t, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 434))

	def test_435(self):
		input = """k , O  : auto  ;   X : function auto  ( teng : float    , J : auto   , inherit EP : boolean     ) inherit Dv { }    j  : auto  ;   c , z0Ey , _  : array [ 0 ] of boolean    ;   """
		expect = """Program([
	VarDecl(k, AutoType)
	VarDecl(O, AutoType)
	FuncDecl(X, AutoType, [Param(teng, FloatType), Param(J, AutoType), InheritParam(EP, BooleanType)], Dv, BlockStmt([]))
	VarDecl(j, AutoType)
	VarDecl(c, ArrayType([0], BooleanType))
	VarDecl(z0Ey, ArrayType([0], BooleanType))
	VarDecl(_, ArrayType([0], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 435))

	def test_436(self):
		input = """lb , zH , Y  : integer   ;   """
		expect = """Program([
	VarDecl(lb, IntegerType)
	VarDecl(zH, IntegerType)
	VarDecl(Y, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 436))

	def test_437(self):
		input = """H : function void ( ) { }    """
		expect = """Program([
	FuncDecl(H, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 437))

	def test_438(self):
		input = """bh : function auto  ( inherit out d30 : auto    ) inherit BV { P , v  : string   = h   + T    != ! RtQ     :: - Z    > gU1   && GirK      , ! G     :: Ya   && g       ;  }    """
		expect = """Program([
	FuncDecl(bh, AutoType, [InheritOutParam(d30, AutoType)], BV, BlockStmt([VarDecl(P, StringType, BinExpr(::, BinExpr(!=, BinExpr(+, Id(h), Id(T)), UnExpr(!, Id(RtQ))), BinExpr(>, UnExpr(-, Id(Z)), BinExpr(&&, Id(gU1), Id(GirK))))), VarDecl(v, StringType, BinExpr(::, UnExpr(!, Id(G)), BinExpr(&&, Id(Ya), Id(g))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 438))

	def test_439(self):
		input = """uCMoR3ytU : function void ( ) inherit a { continue ;   I , MzNb  : string   = - A    < ! x      , ""    == ! N1W     :: oZ   + i       ;  }    """
		expect = """Program([
	FuncDecl(uCMoR3ytU, VoidType, [], a, BlockStmt([ContinueStmt(), VarDecl(I, StringType, BinExpr(<, UnExpr(-, Id(A)), UnExpr(!, Id(x)))), VarDecl(MzNb, StringType, BinExpr(::, BinExpr(==, StringLit(), UnExpr(!, Id(N1W))), BinExpr(+, Id(oZ), Id(i))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 439))

	def test_440(self):
		input = """icWn  : auto  ;   M  : array [ 8928 ] of integer    = ! Rl   && F    / I   * p         ;   Kw : function boolean   ( ) { R  : array [ 0 ] of boolean    ;  }    l , z138f , T8  : auto  ;   Sd : function array [ 0 ] of boolean    ( out Es : boolean     ) { }    z , O , Y , et96cpp9 , UI  : string   = - ""     / K   && r7    * - NV      <= false     :: GJ ( )      , 1    % ! xf    % K   + yWl        , n   || b    - - ck     || { }      != a ( )    % - _   && F       :: qfR ( )    < C   && OcSj    * e8YH   - c     && - v   && M        , ! D ( )    || - e        , - - m   || m      == ! ANj   - Z    + K5v   + e       :: O   && Tfi    * ! eTB8     - - x    % NXIe   && XI         ;   f  : array [ 0 ] of boolean    = S_Wmd ( )    && m   || n     + - WI    + bhd   + Qgn         ;   l , W , Na  : auto  ;   END , b  : auto  = - C   + SCKzw    || - b       :: GS   / f ( )     <= x6w   + S    % BsGz5   / j     * - p    + - g        , ! ! aq   / j      > zp9   - H    && - s     * F       ;   n , dg  : auto  ;   """
		expect = """Program([
	VarDecl(icWn, AutoType)
	VarDecl(M, ArrayType([8928], IntegerType), BinExpr(&&, UnExpr(!, Id(Rl)), BinExpr(*, BinExpr(/, Id(F), Id(I)), Id(p))))
	FuncDecl(Kw, BooleanType, [], None, BlockStmt([VarDecl(R, ArrayType([0], BooleanType))]))
	VarDecl(l, AutoType)
	VarDecl(z138f, AutoType)
	VarDecl(T8, AutoType)
	FuncDecl(Sd, ArrayType([0], BooleanType), [OutParam(Es, BooleanType)], None, BlockStmt([]))
	VarDecl(z, StringType, BinExpr(::, BinExpr(<=, BinExpr(&&, BinExpr(/, UnExpr(-, StringLit()), Id(K)), BinExpr(*, Id(r7), UnExpr(-, Id(NV)))), BooleanLit(False)), FuncCall(GJ, [])))
	VarDecl(O, StringType, BinExpr(+, BinExpr(%, BinExpr(%, IntegerLit(1), UnExpr(!, Id(xf))), Id(K)), Id(yWl)))
	VarDecl(Y, StringType, BinExpr(::, BinExpr(!=, BinExpr(||, BinExpr(||, Id(n), BinExpr(-, Id(b), UnExpr(-, Id(ck)))), ArrayLit([])), BinExpr(&&, BinExpr(%, FuncCall(a, []), UnExpr(-, Id(_))), Id(F))), BinExpr(<, FuncCall(qfR, []), BinExpr(&&, BinExpr(&&, BinExpr(&&, Id(C), BinExpr(-, BinExpr(*, Id(OcSj), Id(e8YH)), Id(c))), UnExpr(-, Id(v))), Id(M)))))
	VarDecl(et96cpp9, StringType, BinExpr(||, UnExpr(!, FuncCall(D, [])), UnExpr(-, Id(e))))
	VarDecl(UI, StringType, BinExpr(::, BinExpr(==, BinExpr(||, UnExpr(-, UnExpr(-, Id(m))), Id(m)), BinExpr(+, BinExpr(+, BinExpr(-, UnExpr(!, Id(ANj)), Id(Z)), Id(K5v)), Id(e))), BinExpr(&&, BinExpr(&&, Id(O), BinExpr(-, BinExpr(*, Id(Tfi), UnExpr(!, Id(eTB8))), BinExpr(%, UnExpr(-, Id(x)), Id(NXIe)))), Id(XI))))
	VarDecl(f, ArrayType([0], BooleanType), BinExpr(||, BinExpr(&&, FuncCall(S_Wmd, []), Id(m)), BinExpr(+, BinExpr(+, BinExpr(+, Id(n), UnExpr(-, Id(WI))), Id(bhd)), Id(Qgn))))
	VarDecl(l, AutoType)
	VarDecl(W, AutoType)
	VarDecl(Na, AutoType)
	VarDecl(END, AutoType, BinExpr(::, BinExpr(||, BinExpr(+, UnExpr(-, Id(C)), Id(SCKzw)), UnExpr(-, Id(b))), BinExpr(<=, BinExpr(/, Id(GS), FuncCall(f, [])), BinExpr(+, BinExpr(+, Id(x6w), BinExpr(*, BinExpr(/, BinExpr(%, Id(S), Id(BsGz5)), Id(j)), UnExpr(-, Id(p)))), UnExpr(-, Id(g))))))
	VarDecl(b, AutoType, BinExpr(>, BinExpr(/, UnExpr(!, UnExpr(!, Id(aq))), Id(j)), BinExpr(&&, BinExpr(-, Id(zp9), Id(H)), BinExpr(*, UnExpr(-, Id(s)), Id(F)))))
	VarDecl(n, AutoType)
	VarDecl(dg, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 440))

	def test_441(self):
		input = """i  : array [ 170336822_8 ] of float    ;   K : function auto  ( ) inherit GrSZ4UK { }    """
		expect = """Program([
	VarDecl(i, ArrayType([1703368228], FloatType))
	FuncDecl(K, AutoType, [], GrSZ4UK, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 441))

	def test_442(self):
		input = """U , tPM  : array [ 0 , 622 ] of float    ;   """
		expect = """Program([
	VarDecl(U, ArrayType([0, 622], FloatType))
	VarDecl(tPM, ArrayType([0, 622], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 442))

	def test_443(self):
		input = """YSw  : auto  = Mi3   && - Iu     + ! ""       :: ! 0        ;   g  : array [ 0 ] of float    ;   xx : function void ( ) inherit zv { }    s : function void ( ) inherit Q { }    """
		expect = """Program([
	VarDecl(YSw, AutoType, BinExpr(::, BinExpr(&&, Id(Mi3), BinExpr(+, UnExpr(-, Id(Iu)), UnExpr(!, StringLit()))), UnExpr(!, IntegerLit(0))))
	VarDecl(g, ArrayType([0], FloatType))
	FuncDecl(xx, VoidType, [], zv, BlockStmt([]))
	FuncDecl(s, VoidType, [], Q, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 443))

	def test_444(self):
		input = """CW : function void ( ) { TH ( )  ;   }    """
		expect = """Program([
	FuncDecl(CW, VoidType, [], None, BlockStmt([CallStmt(TH, )]))
])"""
		self.assertTrue(TestAST.test(input, expect, 444))

	def test_445(self):
		input = """y : function void ( inherit e : auto   , inherit out _ : auto    ) { }    """
		expect = """Program([
	FuncDecl(y, VoidType, [InheritParam(e, AutoType), InheritOutParam(_, AutoType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 445))

	def test_446(self):
		input = """pf7gX4ti  : array [ 54_20601_14 , 0 ] of boolean    = ! SON   - H6     && - pxg ( )      < ! mQ   - xMTE    - t   % D       :: xTNqeC   % c   / s     * o    < ! ! B     - QYgv   - cK    && l   || O8S5E         ;   """
		expect = """Program([
	VarDecl(pf7gX4ti, ArrayType([542060114, 0], BooleanType), BinExpr(::, BinExpr(<, BinExpr(&&, BinExpr(-, UnExpr(!, Id(SON)), Id(H6)), UnExpr(-, FuncCall(pxg, []))), BinExpr(-, BinExpr(-, UnExpr(!, Id(mQ)), Id(xMTE)), BinExpr(%, Id(t), Id(D)))), BinExpr(<, BinExpr(*, BinExpr(/, BinExpr(%, Id(xTNqeC), Id(c)), Id(s)), Id(o)), BinExpr(||, BinExpr(&&, BinExpr(-, BinExpr(-, UnExpr(!, UnExpr(!, Id(B))), Id(QYgv)), Id(cK)), Id(l)), Id(O8S5E)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 446))

	def test_447(self):
		input = """W , WKFaGe_  : auto  ;   k : function void ( out U : auto    ) { }    o8g : function auto  ( ) { { continue ;   inz ( )  ;   }   }    """
		expect = """Program([
	VarDecl(W, AutoType)
	VarDecl(WKFaGe_, AutoType)
	FuncDecl(k, VoidType, [OutParam(U, AutoType)], None, BlockStmt([]))
	FuncDecl(o8g, AutoType, [], None, BlockStmt([BlockStmt([ContinueStmt(), CallStmt(inz, )])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 447))

	def test_448(self):
		input = """Q : function auto  ( inherit out hC : string    , ns5 : auto    ) { Q , TV , wTRj  : auto  = ! v7xu    > g   && m      , M   - r    == ! b     :: C ( )    >= ! ZA      , wI   || tN       ;  }    """
		expect = """Program([
	FuncDecl(Q, AutoType, [InheritOutParam(hC, StringType), Param(ns5, AutoType)], None, BlockStmt([VarDecl(Q, AutoType, BinExpr(>, UnExpr(!, Id(v7xu)), BinExpr(&&, Id(g), Id(m)))), VarDecl(TV, AutoType, BinExpr(::, BinExpr(==, BinExpr(-, Id(M), Id(r)), UnExpr(!, Id(b))), BinExpr(>=, FuncCall(C, []), UnExpr(!, Id(ZA))))), VarDecl(wTRj, AutoType, BinExpr(||, Id(wI), Id(tN)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 448))

	def test_449(self):
		input = """SNm  : boolean   = ! XdUo8n   && K    && ! X         ;   Me  : float   = M ( )    / - g     || A     :: E ( )    || ! _P     || VZ   && S    - w   * em         ;   STq : function array [ 802_0 ] of integer    ( inherit out h : array [ 2 ] of string      ) inherit k { }    Q , vg_  : float   = ! ! - u      > n ( )     :: Y_9KBE   <= - ! Wht    - ! F        , ! E   && b    && i   - cA      <= Qk ( )    && ! Xj00     - - G1U ( )       :: ""    + u   - P    || p        ;   Zk  : array [ 7 , 0 ] of string    = D   % VWM    || - w     + ! i5z        ;   q4 , P1  : integer   ;   """
		expect = """Program([
	VarDecl(SNm, BooleanType, BinExpr(&&, BinExpr(&&, UnExpr(!, Id(XdUo8n)), Id(K)), UnExpr(!, Id(X))))
	VarDecl(Me, FloatType, BinExpr(::, BinExpr(||, BinExpr(/, FuncCall(M, []), UnExpr(-, Id(g))), Id(A)), BinExpr(&&, BinExpr(||, BinExpr(||, FuncCall(E, []), UnExpr(!, Id(_P))), Id(VZ)), BinExpr(-, Id(S), BinExpr(*, Id(w), Id(em))))))
	FuncDecl(STq, ArrayType([8020], IntegerType), [InheritOutParam(h, ArrayType([2], StringType))], k, BlockStmt([]))
	VarDecl(Q, FloatType, BinExpr(::, BinExpr(>, UnExpr(!, UnExpr(!, UnExpr(-, Id(u)))), FuncCall(n, [])), BinExpr(<=, Id(Y_9KBE), BinExpr(-, UnExpr(-, UnExpr(!, Id(Wht))), UnExpr(!, Id(F))))))
	VarDecl(vg_, FloatType, BinExpr(::, BinExpr(<=, BinExpr(&&, BinExpr(&&, UnExpr(!, Id(E)), Id(b)), BinExpr(-, Id(i), Id(cA))), BinExpr(&&, FuncCall(Qk, []), BinExpr(-, UnExpr(!, Id(Xj00)), UnExpr(-, FuncCall(G1U, []))))), BinExpr(||, BinExpr(-, BinExpr(+, StringLit(), Id(u)), Id(P)), Id(p))))
	VarDecl(Zk, ArrayType([7, 0], StringType), BinExpr(||, BinExpr(%, Id(D), Id(VWM)), BinExpr(+, UnExpr(-, Id(w)), UnExpr(!, Id(i5z)))))
	VarDecl(q4, IntegerType)
	VarDecl(P1, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 449))

	def test_450(self):
		input = """Nl  : float   = ! Loj   + v    || z   || eFD      == - 5     * oz   - lVzm    || - H         ;   """
		expect = """Program([
	VarDecl(Nl, FloatType, BinExpr(==, BinExpr(||, BinExpr(||, BinExpr(+, UnExpr(!, Id(Loj)), Id(v)), Id(z)), Id(eFD)), BinExpr(||, BinExpr(-, BinExpr(*, UnExpr(-, IntegerLit(5)), Id(oz)), Id(lVzm)), UnExpr(-, Id(H)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 450))

	def test_451(self):
		input = """d : function void ( inherit L7 : string     ) { }    """
		expect = """Program([
	FuncDecl(d, VoidType, [InheritParam(L7, StringType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 451))

	def test_452(self):
		input = """f4P  : auto  = ! D   + U     && z    > ! - k    && - rfK       :: ! kKXXX    / ! OZ1   - C         ;   B : function void ( ) inherit g { u  : auto  ;  }    """
		expect = """Program([
	VarDecl(f4P, AutoType, BinExpr(::, BinExpr(>, BinExpr(&&, BinExpr(+, UnExpr(!, Id(D)), Id(U)), Id(z)), BinExpr(&&, UnExpr(!, UnExpr(-, Id(k))), UnExpr(-, Id(rfK)))), BinExpr(-, BinExpr(/, UnExpr(!, Id(kKXXX)), UnExpr(!, Id(OZ1))), Id(C))))
	FuncDecl(B, VoidType, [], g, BlockStmt([VarDecl(u, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 452))

	def test_453(self):
		input = """Fw : function array [ 9 ] of float    ( ) inherit f { yU  : array [ 9 ] of boolean    = l      ;  do { }  while ( N   || S      ) ;   }    x , H  : array [ 3 ] of float    = f ( )    == ! AJ   - ! N        , - ! - X       :: ! P   && V     || - mh        ;   B  : float   = - - Q   || uVj       :: 0.E99763       ;   C : function auto  ( ) { break ;   while ( ! m2H     :: nU   + e    <= zs   % ZP      ) break ;     }    e : function void ( inherit _V_ : integer     ) { for ( P  = M   - n7     :: - IN    <= T2o     , - G    != Z   + X     :: A   || GtQd      , i   || BUP    != b   / KwE4SU     :: J   || I    >= ! m      ) return ;     }    """
		expect = """Program([
	FuncDecl(Fw, ArrayType([9], FloatType), [], f, BlockStmt([VarDecl(yU, ArrayType([9], BooleanType), Id(l)), DoWhileStmt(BinExpr(||, Id(N), Id(S)), BlockStmt([]))]))
	VarDecl(x, ArrayType([3], FloatType), BinExpr(==, FuncCall(f, []), BinExpr(-, UnExpr(!, Id(AJ)), UnExpr(!, Id(N)))))
	VarDecl(H, ArrayType([3], FloatType), BinExpr(::, UnExpr(-, UnExpr(!, UnExpr(-, Id(X)))), BinExpr(||, BinExpr(&&, UnExpr(!, Id(P)), Id(V)), UnExpr(-, Id(mh)))))
	VarDecl(B, FloatType, BinExpr(::, BinExpr(||, UnExpr(-, UnExpr(-, Id(Q))), Id(uVj)), FloatLit(0.0)))
	FuncDecl(C, AutoType, [], None, BlockStmt([BreakStmt(), WhileStmt(BinExpr(::, UnExpr(!, Id(m2H)), BinExpr(<=, BinExpr(+, Id(nU), Id(e)), BinExpr(%, Id(zs), Id(ZP)))), BreakStmt())]))
	FuncDecl(e, VoidType, [InheritParam(_V_, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(P), BinExpr(::, BinExpr(-, Id(M), Id(n7)), BinExpr(<=, UnExpr(-, Id(IN)), Id(T2o)))), BinExpr(::, BinExpr(!=, UnExpr(-, Id(G)), BinExpr(+, Id(Z), Id(X))), BinExpr(||, Id(A), Id(GtQd))), BinExpr(::, BinExpr(!=, BinExpr(||, Id(i), Id(BUP)), BinExpr(/, Id(b), Id(KwE4SU))), BinExpr(>=, BinExpr(||, Id(J), Id(I)), UnExpr(!, Id(m)))), ReturnStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 453))

	def test_454(self):
		input = """jB , K  : integer   = ! - FyyY     / { }      <= - ml    % M   - R7xpN6     || lR   + H    - RR ( )        , - 5     || Hr   - k    % fk ( )      < ! EdwjYP   - W    && uN   || wlNP       :: - ! Pf    * - T         ;   e : function void ( ) inherit u { for ( I  = ""     :: Gqq   + Ye      , c6   * k      , D1   + __    == v   && HT     :: - u    < dK   - kTb      ) return ;     }    """
		expect = """Program([
	VarDecl(jB, IntegerType, BinExpr(<=, BinExpr(/, UnExpr(!, UnExpr(-, Id(FyyY))), ArrayLit([])), BinExpr(||, BinExpr(-, BinExpr(%, UnExpr(-, Id(ml)), Id(M)), Id(R7xpN6)), BinExpr(-, BinExpr(+, Id(lR), Id(H)), FuncCall(RR, [])))))
	VarDecl(K, IntegerType, BinExpr(::, BinExpr(<, BinExpr(||, UnExpr(-, IntegerLit(5)), BinExpr(-, Id(Hr), BinExpr(%, Id(k), FuncCall(fk, [])))), BinExpr(||, BinExpr(&&, BinExpr(-, UnExpr(!, Id(EdwjYP)), Id(W)), Id(uN)), Id(wlNP))), BinExpr(*, UnExpr(-, UnExpr(!, Id(Pf))), UnExpr(-, Id(T)))))
	FuncDecl(e, VoidType, [], u, BlockStmt([ForStmt(AssignStmt(Id(I), BinExpr(::, StringLit(), BinExpr(+, Id(Gqq), Id(Ye)))), BinExpr(*, Id(c6), Id(k)), BinExpr(::, BinExpr(==, BinExpr(+, Id(D1), Id(__)), BinExpr(&&, Id(v), Id(HT))), BinExpr(<, UnExpr(-, Id(u)), BinExpr(-, Id(dK), Id(kTb)))), ReturnStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 454))

	def test_455(self):
		input = """r : function void ( ) { }    """
		expect = """Program([
	FuncDecl(r, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 455))

	def test_456(self):
		input = """K : function void ( mP : float    , inherit out daZ : integer     ) { do { H ( )  ;   continue ;   }  while ( - KERq     :: aE   - je    < z   / K      ) ;   }    Zu  : array [ 16_630 , 1730 , 0 ] of float    ;   lPn : function void ( ) { do { }  while ( 0    < ! l      ) ;   DXN , oZ  : integer   = zSR   && JrQJ      , - y       ;  }    O : function auto  ( w : auto    ) { L , hFP  : array [ 99 , 680_6_9 , 6 , 1_0_6835_4 ] of integer    ;  }    """
		expect = """Program([
	FuncDecl(K, VoidType, [Param(mP, FloatType), InheritOutParam(daZ, IntegerType)], None, BlockStmt([DoWhileStmt(BinExpr(::, UnExpr(-, Id(KERq)), BinExpr(<, BinExpr(-, Id(aE), Id(je)), BinExpr(/, Id(z), Id(K)))), BlockStmt([CallStmt(H, ), ContinueStmt()]))]))
	VarDecl(Zu, ArrayType([16630, 1730, 0], FloatType))
	FuncDecl(lPn, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, IntegerLit(0), UnExpr(!, Id(l))), BlockStmt([])), VarDecl(DXN, IntegerType, BinExpr(&&, Id(zSR), Id(JrQJ))), VarDecl(oZ, IntegerType, UnExpr(-, Id(y)))]))
	FuncDecl(O, AutoType, [Param(w, AutoType)], None, BlockStmt([VarDecl(L, ArrayType([99, 68069, 6, 1068354], IntegerType)), VarDecl(hFP, ArrayType([99, 68069, 6, 1068354], IntegerType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 456))

	def test_457(self):
		input = """B , M , kd0n7 , l  : string   ;   """
		expect = """Program([
	VarDecl(B, StringType)
	VarDecl(M, StringType)
	VarDecl(kd0n7, StringType)
	VarDecl(l, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 457))

	def test_458(self):
		input = """x : function void ( ) inherit T { WOj , Ha  : boolean   ;  }    roaLC , m  : auto  = ! ! hUR     || NIs   * ! VJ      >= - ! C4_     && - dW    + z1A ( )        , - ! z_lF    || S ( )       :: - H   * I12    % u   * C      == - ""     - A   % MWtu   || r         ;   """
		expect = """Program([
	FuncDecl(x, VoidType, [], T, BlockStmt([VarDecl(WOj, BooleanType), VarDecl(Ha, BooleanType)]))
	VarDecl(roaLC, AutoType, BinExpr(>=, BinExpr(||, UnExpr(!, UnExpr(!, Id(hUR))), BinExpr(*, Id(NIs), UnExpr(!, Id(VJ)))), BinExpr(&&, UnExpr(-, UnExpr(!, Id(C4_))), BinExpr(+, UnExpr(-, Id(dW)), FuncCall(z1A, [])))))
	VarDecl(m, AutoType, BinExpr(::, BinExpr(||, UnExpr(-, UnExpr(!, Id(z_lF))), FuncCall(S, [])), BinExpr(==, BinExpr(*, BinExpr(%, BinExpr(*, UnExpr(-, Id(H)), Id(I12)), Id(u)), Id(C)), BinExpr(||, BinExpr(-, UnExpr(-, StringLit()), BinExpr(%, Id(A), Id(MWtu))), Id(r)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 458))

	def test_459(self):
		input = """QhU : function float   ( ) { M ( )  ;   fs , EXeMA , jK  : integer   ;  return ;   }    g3 : function integer   ( inherit out nX9j : string     ) { }    """
		expect = """Program([
	FuncDecl(QhU, FloatType, [], None, BlockStmt([CallStmt(M, ), VarDecl(fs, IntegerType), VarDecl(EXeMA, IntegerType), VarDecl(jK, IntegerType), ReturnStmt()]))
	FuncDecl(g3, IntegerType, [InheritOutParam(nX9j, StringType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 459))

	def test_460(self):
		input = """vvk  : array [ 0 , 0 , 0 , 4 , 0 ] of boolean    = - jb   + J     - - ZL    + - f       :: ! zSzDX46J    % ! Jlb     && Qcr   * g    && ! c      >= ! ! ""         ;   """
		expect = """Program([
	VarDecl(vvk, ArrayType([0, 0, 0, 4, 0], BooleanType), BinExpr(::, BinExpr(+, BinExpr(-, BinExpr(+, UnExpr(-, Id(jb)), Id(J)), UnExpr(-, Id(ZL))), UnExpr(-, Id(f))), BinExpr(>=, BinExpr(&&, BinExpr(&&, BinExpr(%, UnExpr(!, Id(zSzDX46J)), UnExpr(!, Id(Jlb))), BinExpr(*, Id(Qcr), Id(g))), UnExpr(!, Id(c))), UnExpr(!, UnExpr(!, StringLit())))))
])"""
		self.assertTrue(TestAST.test(input, expect, 460))

	def test_461(self):
		input = """y , g3  : auto  = - 3     * w   && f3    || ! AH      >= { }       , ! 0    + rQ   % v      >= ! - ! klB         ;   Bb : function void ( ) inherit x { }    """
		expect = """Program([
	VarDecl(y, AutoType, BinExpr(>=, BinExpr(||, BinExpr(&&, BinExpr(*, UnExpr(-, IntegerLit(3)), Id(w)), Id(f3)), UnExpr(!, Id(AH))), ArrayLit([])))
	VarDecl(g3, AutoType, BinExpr(>=, BinExpr(+, UnExpr(!, IntegerLit(0)), BinExpr(%, Id(rQ), Id(v))), UnExpr(!, UnExpr(-, UnExpr(!, Id(klB))))))
	FuncDecl(Bb, VoidType, [], x, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 461))

	def test_462(self):
		input = """GA  : string   ;   """
		expect = """Program([
	VarDecl(GA, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 462))

	def test_463(self):
		input = """O : function float   ( out Sa : string    , out HU : string     ) inherit F { ht  : array [ 553321 , 0 , 0 , 2 , 1034_83 ] of integer    ;  continue ;   }    rvW , v  : auto  ;   w  : float   ;   c  : array [ 52 , 0 ] of boolean    ;   """
		expect = """Program([
	FuncDecl(O, FloatType, [OutParam(Sa, StringType), OutParam(HU, StringType)], F, BlockStmt([VarDecl(ht, ArrayType([553321, 0, 0, 2, 103483], IntegerType)), ContinueStmt()]))
	VarDecl(rvW, AutoType)
	VarDecl(v, AutoType)
	VarDecl(w, FloatType)
	VarDecl(c, ArrayType([52, 0], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 463))

	def test_464(self):
		input = """t : function integer   ( ) { }    Y : function void ( ) { }    """
		expect = """Program([
	FuncDecl(t, IntegerType, [], None, BlockStmt([]))
	FuncDecl(Y, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 464))

	def test_465(self):
		input = """ME , O  : auto  = P   || KGu    / ! _     % b ( )       , ! DR0   * o    - DyEFb   / N      > ! { }         ;   """
		expect = """Program([
	VarDecl(ME, AutoType, BinExpr(||, Id(P), BinExpr(%, BinExpr(/, Id(KGu), UnExpr(!, Id(_))), FuncCall(b, []))))
	VarDecl(O, AutoType, BinExpr(>, BinExpr(-, BinExpr(*, UnExpr(!, Id(DR0)), Id(o)), BinExpr(/, Id(DyEFb), Id(N))), UnExpr(!, ArrayLit([]))))
])"""
		self.assertTrue(TestAST.test(input, expect, 465))

	def test_466(self):
		input = """VN , X  : auto  ;   B , Lj7 , l  : array [ 0 , 0 , 86_7 , 0 ] of string    = - - iw     && - o   * M      > K ( )    && ! AM96     / - z    && ! aLd       :: ! a   || m8    && r   - A      < - 7     - J ( )       , ! - i   && k      > q   + Xs    % Z   && KJ     + ! k   % lRcyN        , cog   % anh    - J   + z     * ! TFeUS ( )         ;   """
		expect = """Program([
	VarDecl(VN, AutoType)
	VarDecl(X, AutoType)
	VarDecl(B, ArrayType([0, 0, 867, 0], StringType), BinExpr(::, BinExpr(>, BinExpr(&&, UnExpr(-, UnExpr(-, Id(iw))), BinExpr(*, UnExpr(-, Id(o)), Id(M))), BinExpr(&&, BinExpr(&&, FuncCall(K, []), BinExpr(/, UnExpr(!, Id(AM96)), UnExpr(-, Id(z)))), UnExpr(!, Id(aLd)))), BinExpr(<, BinExpr(&&, BinExpr(||, UnExpr(!, Id(a)), Id(m8)), BinExpr(-, Id(r), Id(A))), BinExpr(-, UnExpr(-, IntegerLit(7)), FuncCall(J, [])))))
	VarDecl(Lj7, ArrayType([0, 0, 867, 0], StringType), BinExpr(>, BinExpr(&&, UnExpr(!, UnExpr(-, Id(i))), Id(k)), BinExpr(&&, BinExpr(+, Id(q), BinExpr(%, Id(Xs), Id(Z))), BinExpr(+, Id(KJ), BinExpr(%, UnExpr(!, Id(k)), Id(lRcyN))))))
	VarDecl(l, ArrayType([0, 0, 867, 0], StringType), BinExpr(+, BinExpr(-, BinExpr(%, Id(cog), Id(anh)), Id(J)), BinExpr(*, Id(z), UnExpr(!, FuncCall(TFeUS, [])))))
])"""
		self.assertTrue(TestAST.test(input, expect, 466))

	def test_467(self):
		input = """I : function array [ 13 ] of boolean    ( ) { bXtjyVv , P , tbA  : array [ 0 ] of boolean    = r   && N    > - Vu     :: - XB      , kroL   / j      , ! r       ;  p , h  : array [ 7912884 , 8 ] of float    ;  for ( j  = ""    >= xoGQ   / J     :: X   + MY      , nJedBFdyS   / Z      , E   || ct     :: k   % PFVdq      ) { }     for ( evy  = ! aD    <= r3   % er      , t ( )    >= ! c     :: lkC   + s    >= - K38P      , M   / rs     :: - Y    != - TV      ) { continue ;   }     h ( )  ;   }    """
		expect = """Program([
	FuncDecl(I, ArrayType([13], BooleanType), [], None, BlockStmt([VarDecl(bXtjyVv, ArrayType([0], BooleanType), BinExpr(::, BinExpr(>, BinExpr(&&, Id(r), Id(N)), UnExpr(-, Id(Vu))), UnExpr(-, Id(XB)))), VarDecl(P, ArrayType([0], BooleanType), BinExpr(/, Id(kroL), Id(j))), VarDecl(tbA, ArrayType([0], BooleanType), UnExpr(!, Id(r))), VarDecl(p, ArrayType([7912884, 8], FloatType)), VarDecl(h, ArrayType([7912884, 8], FloatType)), ForStmt(AssignStmt(Id(j), BinExpr(::, BinExpr(>=, StringLit(), BinExpr(/, Id(xoGQ), Id(J))), BinExpr(+, Id(X), Id(MY)))), BinExpr(/, Id(nJedBFdyS), Id(Z)), BinExpr(::, BinExpr(||, Id(E), Id(ct)), BinExpr(%, Id(k), Id(PFVdq))), BlockStmt([])), ForStmt(AssignStmt(Id(evy), BinExpr(<=, UnExpr(!, Id(aD)), BinExpr(%, Id(r3), Id(er)))), BinExpr(::, BinExpr(>=, FuncCall(t, []), UnExpr(!, Id(c))), BinExpr(>=, BinExpr(+, Id(lkC), Id(s)), UnExpr(-, Id(K38P)))), BinExpr(::, BinExpr(/, Id(M), Id(rs)), BinExpr(!=, UnExpr(-, Id(Y)), UnExpr(-, Id(TV)))), BlockStmt([ContinueStmt()])), CallStmt(h, )]))
])"""
		self.assertTrue(TestAST.test(input, expect, 467))

	def test_468(self):
		input = """zm : function void ( i : array [ 0 , 0 , 0 ] of string      ) inherit l { }    X , u , GEn  : auto  ;   """
		expect = """Program([
	FuncDecl(zm, VoidType, [Param(i, ArrayType([0, 0, 0], StringType))], l, BlockStmt([]))
	VarDecl(X, AutoType)
	VarDecl(u, AutoType)
	VarDecl(GEn, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 468))

	def test_469(self):
		input = """x , i  : boolean   ;   """
		expect = """Program([
	VarDecl(x, BooleanType)
	VarDecl(i, BooleanType)
])"""
		self.assertTrue(TestAST.test(input, expect, 469))

	def test_470(self):
		input = """t : function array [ 0 , 0 , 9_2_32_45107 , 0 ] of integer    ( inherit out N : auto    ) { { }   }    """
		expect = """Program([
	FuncDecl(t, ArrayType([0, 0, 923245107, 0], IntegerType), [InheritOutParam(N, AutoType)], None, BlockStmt([BlockStmt([])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 470))

	def test_471(self):
		input = """y , UT  : auto  ;   H : function void ( ) { }    """
		expect = """Program([
	VarDecl(y, AutoType)
	VarDecl(UT, AutoType)
	FuncDecl(H, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 471))

	def test_472(self):
		input = """baX : function void ( out N : auto   , c4S : float     ) inherit K { c ( )  ;   }    """
		expect = """Program([
	FuncDecl(baX, VoidType, [OutParam(N, AutoType), Param(c4S, FloatType)], K, BlockStmt([CallStmt(c, )]))
])"""
		self.assertTrue(TestAST.test(input, expect, 472))

	def test_473(self):
		input = """W : function boolean   ( ) { while ( eE   + p     :: ! qLE    > E   - gM      ) return ;     }    """
		expect = """Program([
	FuncDecl(W, BooleanType, [], None, BlockStmt([WhileStmt(BinExpr(::, BinExpr(+, Id(eE), Id(p)), BinExpr(>, UnExpr(!, Id(qLE)), BinExpr(-, Id(E), Id(gM)))), ReturnStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 473))

	def test_474(self):
		input = """rGY : function void ( ) inherit oG { }    """
		expect = """Program([
	FuncDecl(rGY, VoidType, [], oG, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 474))

	def test_475(self):
		input = """YC  : array [ 9 , 4 , 0 ] of float    ;   """
		expect = """Program([
	VarDecl(YC, ArrayType([9, 4, 0], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 475))

	def test_476(self):
		input = """N0 : function integer   ( ) { continue ;   }    """
		expect = """Program([
	FuncDecl(N0, IntegerType, [], None, BlockStmt([ContinueStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 476))

	def test_477(self):
		input = """Q9S : function array [ 72_8_7 , 5 ] of boolean    ( ) { }    Q : function array [ 6 , 91_9 , 0 , 1 ] of string    ( ) { }    j : function array [ 4 ] of float    ( ) { if ( te   && p7AL6    > yZ_XAyL   * V      ) continue ;     }    n , g , d  : array [ 0 ] of string    ;   """
		expect = """Program([
	FuncDecl(Q9S, ArrayType([7287, 5], BooleanType), [], None, BlockStmt([]))
	FuncDecl(Q, ArrayType([6, 919, 0, 1], StringType), [], None, BlockStmt([]))
	FuncDecl(j, ArrayType([4], FloatType), [], None, BlockStmt([IfStmt(BinExpr(>, BinExpr(&&, Id(te), Id(p7AL6)), BinExpr(*, Id(yZ_XAyL), Id(V))), ContinueStmt())]))
	VarDecl(n, ArrayType([0], StringType))
	VarDecl(g, ArrayType([0], StringType))
	VarDecl(d, ArrayType([0], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 477))

	def test_478(self):
		input = """IZU : function array [ 6364 , 5 , 0 , 380_4 , 0 ] of integer    ( p : auto   , rz1 : array [ 0 , 0 , 6495_6 , 12 ] of string     , out B : array [ 0 , 0 ] of integer      ) { }    Y , u4qh , oHvX , H  : auto  = { }     >= ! l      , Qn8   + TDf    - JX   % O     || ! BnHF   && H        , - pQ ( )       , RZ ( )    > - d ( )    && b   % Y         ;   H , N  : array [ 6_7 , 0 , 6 ] of string    = ikAKsI ( )    % K   + w     || ! - f      <= - ! m   || rC        , - - W    || - I       :: ! - ! IXjlAe         ;   """
		expect = """Program([
	FuncDecl(IZU, ArrayType([6364, 5, 0, 3804, 0], IntegerType), [Param(p, AutoType), Param(rz1, ArrayType([0, 0, 64956, 12], StringType)), OutParam(B, ArrayType([0, 0], IntegerType))], None, BlockStmt([]))
	VarDecl(Y, AutoType, BinExpr(>=, ArrayLit([]), UnExpr(!, Id(l))))
	VarDecl(u4qh, AutoType, BinExpr(&&, BinExpr(||, BinExpr(-, BinExpr(+, Id(Qn8), Id(TDf)), BinExpr(%, Id(JX), Id(O))), UnExpr(!, Id(BnHF))), Id(H)))
	VarDecl(oHvX, AutoType, UnExpr(-, FuncCall(pQ, [])))
	VarDecl(H, AutoType, BinExpr(>, FuncCall(RZ, []), BinExpr(&&, UnExpr(-, FuncCall(d, [])), BinExpr(%, Id(b), Id(Y)))))
	VarDecl(H, ArrayType([67, 0, 6], StringType), BinExpr(<=, BinExpr(||, BinExpr(+, BinExpr(%, FuncCall(ikAKsI, []), Id(K)), Id(w)), UnExpr(!, UnExpr(-, Id(f)))), BinExpr(||, UnExpr(-, UnExpr(!, Id(m))), Id(rC))))
	VarDecl(N, ArrayType([67, 0, 6], StringType), BinExpr(::, BinExpr(||, UnExpr(-, UnExpr(-, Id(W))), UnExpr(-, Id(I))), UnExpr(!, UnExpr(-, UnExpr(!, Id(IXjlAe))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 478))

	def test_479(self):
		input = """e : function void ( ) inherit i { }    TG  : auto  = Z   + ""     - ! i    || e   - R83      < - a6 ( )     - ! C   + i         ;   y : function auto  ( ) inherit j { }    EB : function auto  ( ) { }    Cb : function auto  ( ) inherit lc9G { dv , s  : array [ 1 , 0 ] of integer    = x ( )     :: - T    > - Y      , e   * e5     :: Q   / I       ;  continue ;   }    o  : auto  = vd   - LR    + ! Dq     / ! z    % 0      < U ( )       ;   """
		expect = """Program([
	FuncDecl(e, VoidType, [], i, BlockStmt([]))
	VarDecl(TG, AutoType, BinExpr(<, BinExpr(||, BinExpr(-, BinExpr(+, Id(Z), StringLit()), UnExpr(!, Id(i))), BinExpr(-, Id(e), Id(R83))), BinExpr(+, BinExpr(-, UnExpr(-, FuncCall(a6, [])), UnExpr(!, Id(C))), Id(i))))
	FuncDecl(y, AutoType, [], j, BlockStmt([]))
	FuncDecl(EB, AutoType, [], None, BlockStmt([]))
	FuncDecl(Cb, AutoType, [], lc9G, BlockStmt([VarDecl(dv, ArrayType([1, 0], IntegerType), BinExpr(::, FuncCall(x, []), BinExpr(>, UnExpr(-, Id(T)), UnExpr(-, Id(Y))))), VarDecl(s, ArrayType([1, 0], IntegerType), BinExpr(::, BinExpr(*, Id(e), Id(e5)), BinExpr(/, Id(Q), Id(I)))), ContinueStmt()]))
	VarDecl(o, AutoType, BinExpr(<, BinExpr(+, BinExpr(-, Id(vd), Id(LR)), BinExpr(%, BinExpr(/, UnExpr(!, Id(Dq)), UnExpr(!, Id(z))), IntegerLit(0))), FuncCall(U, [])))
])"""
		self.assertTrue(TestAST.test(input, expect, 479))

	def test_480(self):
		input = """e : function array [ 5_0 , 8_67_77 , 0 , 0 , 9 ] of string    ( ) { z0  : integer   = Z ( )    < ! j       ;  { }   }    """
		expect = """Program([
	FuncDecl(e, ArrayType([50, 86777, 0, 0, 9], StringType), [], None, BlockStmt([VarDecl(z0, IntegerType, BinExpr(<, FuncCall(Z, []), UnExpr(!, Id(j)))), BlockStmt([])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 480))

	def test_481(self):
		input = """g : function void ( ) { }    EDg , u8 , g , j , s , wW , oA  : auto  = ! n    / b   && y     - - v     <= vw6   * q    / ""     || Wm      , ! RaQ   + i    % c   || w        , ! Y9c   - u    && - f       :: n9I ( )      , ! X0   / E    || L   + N      >= 0    % m      , ! - ""      < ! - dny4    + ! kFXAS       :: HDXk   + rz_xbVuM    && - T     && - yh   / t        , ""    < - ""    / j   || E       :: ! - GHEG     || ""     < a8Q     , ! ! ! o      == false    * ! ! u         ;   """
		expect = """Program([
	FuncDecl(g, VoidType, [], None, BlockStmt([]))
	VarDecl(EDg, AutoType, BinExpr(<=, BinExpr(&&, BinExpr(/, UnExpr(!, Id(n)), Id(b)), BinExpr(-, Id(y), UnExpr(-, Id(v)))), BinExpr(||, BinExpr(/, BinExpr(*, Id(vw6), Id(q)), StringLit()), Id(Wm))))
	VarDecl(u8, AutoType, BinExpr(||, BinExpr(+, UnExpr(!, Id(RaQ)), BinExpr(%, Id(i), Id(c))), Id(w)))
	VarDecl(g, AutoType, BinExpr(::, BinExpr(&&, BinExpr(-, UnExpr(!, Id(Y9c)), Id(u)), UnExpr(-, Id(f))), FuncCall(n9I, [])))
	VarDecl(j, AutoType, BinExpr(>=, BinExpr(||, BinExpr(/, UnExpr(!, Id(X0)), Id(E)), BinExpr(+, Id(L), Id(N))), BinExpr(%, IntegerLit(0), Id(m))))
	VarDecl(s, AutoType, BinExpr(::, BinExpr(<, UnExpr(!, UnExpr(-, StringLit())), BinExpr(+, UnExpr(!, UnExpr(-, Id(dny4))), UnExpr(!, Id(kFXAS)))), BinExpr(&&, BinExpr(&&, BinExpr(+, Id(HDXk), Id(rz_xbVuM)), UnExpr(-, Id(T))), BinExpr(/, UnExpr(-, Id(yh)), Id(t)))))
	VarDecl(wW, AutoType, BinExpr(::, BinExpr(<, StringLit(), BinExpr(||, BinExpr(/, UnExpr(-, StringLit()), Id(j)), Id(E))), BinExpr(<, BinExpr(||, UnExpr(!, UnExpr(-, Id(GHEG))), StringLit()), Id(a8Q))))
	VarDecl(oA, AutoType, BinExpr(==, UnExpr(!, UnExpr(!, UnExpr(!, Id(o)))), BinExpr(*, BooleanLit(False), UnExpr(!, UnExpr(!, Id(u))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 481))

	def test_482(self):
		input = """z : function auto  ( ) inherit N6Ven { }    a  : auto  = - ! - Y      != - t   - st     + ikNz_n     :: ! tG    && t   / XM     - B ( )        ;   """
		expect = """Program([
	FuncDecl(z, AutoType, [], N6Ven, BlockStmt([]))
	VarDecl(a, AutoType, BinExpr(::, BinExpr(!=, UnExpr(-, UnExpr(!, UnExpr(-, Id(Y)))), BinExpr(+, BinExpr(-, UnExpr(-, Id(t)), Id(st)), Id(ikNz_n))), BinExpr(&&, UnExpr(!, Id(tG)), BinExpr(-, BinExpr(/, Id(t), Id(XM)), FuncCall(B, [])))))
])"""
		self.assertTrue(TestAST.test(input, expect, 482))

	def test_483(self):
		input = """r  : auto  ;   """
		expect = """Program([
	VarDecl(r, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 483))

	def test_484(self):
		input = """TIz , RfFKGo  : array [ 0 ] of integer    ;   """
		expect = """Program([
	VarDecl(TIz, ArrayType([0], IntegerType))
	VarDecl(RfFKGo, ArrayType([0], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 484))

	def test_485(self):
		input = """v , C , wyT  : array [ 666447_1 ] of float    ;   """
		expect = """Program([
	VarDecl(v, ArrayType([6664471], FloatType))
	VarDecl(C, ArrayType([6664471], FloatType))
	VarDecl(wyT, ArrayType([6664471], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 485))

	def test_486(self):
		input = """XRa : function void ( ) inherit D { }    """
		expect = """Program([
	FuncDecl(XRa, VoidType, [], D, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 486))

	def test_487(self):
		input = """_ : function auto  ( inherit out e : auto   , out ND : array [ 8725 ] of string      ) inherit PidS { }    """
		expect = """Program([
	FuncDecl(_, AutoType, [InheritOutParam(e, AutoType), OutParam(ND, ArrayType([8725], StringType))], PidS, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 487))

	def test_488(self):
		input = """z7Y : function auto  ( ) { while ( s   || jJq      ) { }     { }   }    Q : function void ( out Y23 : array [ 84 ] of boolean      ) { }    """
		expect = """Program([
	FuncDecl(z7Y, AutoType, [], None, BlockStmt([WhileStmt(BinExpr(||, Id(s), Id(jJq)), BlockStmt([])), BlockStmt([])]))
	FuncDecl(Q, VoidType, [OutParam(Y23, ArrayType([84], BooleanType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 488))

	def test_489(self):
		input = """nZI , I , H  : string   = - - ! zFo6      < r6N    :: - ! am    && ! g      != - Z    && - fLp     + y   - TIF    && - k        , ! Qmm    || - FN     - ! - U      > z ( )      , - - i5g4Ct     || - y     != ! ! V6     || ! I    + oKDT   + g         ;   """
		expect = """Program([
	VarDecl(nZI, StringType, BinExpr(::, BinExpr(<, UnExpr(-, UnExpr(-, UnExpr(!, Id(zFo6)))), Id(r6N)), BinExpr(!=, BinExpr(&&, UnExpr(-, UnExpr(!, Id(am))), UnExpr(!, Id(g))), BinExpr(&&, BinExpr(&&, UnExpr(-, Id(Z)), BinExpr(-, BinExpr(+, UnExpr(-, Id(fLp)), Id(y)), Id(TIF))), UnExpr(-, Id(k))))))
	VarDecl(I, StringType, BinExpr(>, BinExpr(||, UnExpr(!, Id(Qmm)), BinExpr(-, UnExpr(-, Id(FN)), UnExpr(!, UnExpr(-, Id(U))))), FuncCall(z, [])))
	VarDecl(H, StringType, BinExpr(!=, BinExpr(||, UnExpr(-, UnExpr(-, Id(i5g4Ct))), UnExpr(-, Id(y))), BinExpr(||, UnExpr(!, UnExpr(!, Id(V6))), BinExpr(+, BinExpr(+, UnExpr(!, Id(I)), Id(oKDT)), Id(g)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 489))

	def test_490(self):
		input = """m : function integer   ( ) inherit Go { z  : float   ;  B ( )  ;   }    In  : array [ 9 ] of float    ;   WRSUzGG : function void ( B : auto   , j_i : string     ) { }    y : function auto  ( ) { C  : array [ 34610 , 0 , 8_14_39248 , 0 , 0 , 0 , 0 , 0 , 0 ] of integer    ;  }    m : function void ( out v3 : auto    ) inherit RLHTr4Fe { }    G : function boolean   ( ) inherit J { }    """
		expect = """Program([
	FuncDecl(m, IntegerType, [], Go, BlockStmt([VarDecl(z, FloatType), CallStmt(B, )]))
	VarDecl(In, ArrayType([9], FloatType))
	FuncDecl(WRSUzGG, VoidType, [Param(B, AutoType), Param(j_i, StringType)], None, BlockStmt([]))
	FuncDecl(y, AutoType, [], None, BlockStmt([VarDecl(C, ArrayType([34610, 0, 81439248, 0, 0, 0, 0, 0, 0], IntegerType))]))
	FuncDecl(m, VoidType, [OutParam(v3, AutoType)], RLHTr4Fe, BlockStmt([]))
	FuncDecl(G, BooleanType, [], J, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 490))

	def test_491(self):
		input = """MLkR2 , R  : integer   = ! R   * YU     || ! - e       :: - ! T   && P      >= ! ! l    / - ev        , ! - gl     + { }      > - m   + In     % - o   || dbM         ;   """
		expect = """Program([
	VarDecl(MLkR2, IntegerType, BinExpr(::, BinExpr(||, BinExpr(*, UnExpr(!, Id(R)), Id(YU)), UnExpr(!, UnExpr(-, Id(e)))), BinExpr(>=, BinExpr(&&, UnExpr(-, UnExpr(!, Id(T))), Id(P)), BinExpr(/, UnExpr(!, UnExpr(!, Id(l))), UnExpr(-, Id(ev))))))
	VarDecl(R, IntegerType, BinExpr(>, BinExpr(+, UnExpr(!, UnExpr(-, Id(gl))), ArrayLit([])), BinExpr(||, BinExpr(+, UnExpr(-, Id(m)), BinExpr(%, Id(In), UnExpr(-, Id(o)))), Id(dbM))))
])"""
		self.assertTrue(TestAST.test(input, expect, 491))

	def test_492(self):
		input = """z , _T , b  : auto  ;   M  : float   = dI ( )       ;   """
		expect = """Program([
	VarDecl(z, AutoType)
	VarDecl(_T, AutoType)
	VarDecl(b, AutoType)
	VarDecl(M, FloatType, FuncCall(dI, []))
])"""
		self.assertTrue(TestAST.test(input, expect, 492))

	def test_493(self):
		input = """B  : array [ 838 , 0 ] of string    ;   q , I , T8iomH , Ylr , w  : array [ 66 , 0 , 0 ] of integer    = N1D   / G    * - U     + - S8    - C   / f        , ! BS    && i   / u     / - K   + s0        , ! s   / Y3eU     * - F    + nd2gG   / s5u      <= - ! rW   || A62S        , - ZyNB ( )     * Q   % J    + ! z      <= - - oc   / Ekp       :: 0    || 5       , ! l    - uWMCG   && K     / ! r    - vr   % q7         ;   Kv , e , _x0M  : boolean   ;   """
		expect = """Program([
	VarDecl(B, ArrayType([838, 0], StringType))
	VarDecl(q, ArrayType([66, 0, 0], IntegerType), BinExpr(-, BinExpr(+, BinExpr(*, BinExpr(/, Id(N1D), Id(G)), UnExpr(-, Id(U))), UnExpr(-, Id(S8))), BinExpr(/, Id(C), Id(f))))
	VarDecl(I, ArrayType([66, 0, 0], IntegerType), BinExpr(&&, UnExpr(!, Id(BS)), BinExpr(+, BinExpr(/, BinExpr(/, Id(i), Id(u)), UnExpr(-, Id(K))), Id(s0))))
	VarDecl(T8iomH, ArrayType([66, 0, 0], IntegerType), BinExpr(<=, BinExpr(+, BinExpr(*, BinExpr(/, UnExpr(!, Id(s)), Id(Y3eU)), UnExpr(-, Id(F))), BinExpr(/, Id(nd2gG), Id(s5u))), BinExpr(||, UnExpr(-, UnExpr(!, Id(rW))), Id(A62S))))
	VarDecl(Ylr, ArrayType([66, 0, 0], IntegerType), BinExpr(::, BinExpr(<=, BinExpr(+, BinExpr(%, BinExpr(*, UnExpr(-, FuncCall(ZyNB, [])), Id(Q)), Id(J)), UnExpr(!, Id(z))), BinExpr(/, UnExpr(-, UnExpr(-, Id(oc))), Id(Ekp))), BinExpr(||, IntegerLit(0), IntegerLit(5))))
	VarDecl(w, ArrayType([66, 0, 0], IntegerType), BinExpr(&&, BinExpr(-, UnExpr(!, Id(l)), Id(uWMCG)), BinExpr(-, BinExpr(/, Id(K), UnExpr(!, Id(r))), BinExpr(%, Id(vr), Id(q7)))))
	VarDecl(Kv, BooleanType)
	VarDecl(e, BooleanType)
	VarDecl(_x0M, BooleanType)
])"""
		self.assertTrue(TestAST.test(input, expect, 493))

	def test_494(self):
		input = """d : function string   ( ) inherit _ { }    h0u : function boolean   ( ) inherit zd { }    w4 : function void ( U : float    , inherit i4A : auto    ) inherit Gm { }    iU , s  : auto  = - ! - P      < Iy    :: ! y   || K    - Q9   / Mj2dNo        , ! h ( )      :: "\\f\\t\\n"    + - Q ( )         ;   """
		expect = """Program([
	FuncDecl(d, StringType, [], _, BlockStmt([]))
	FuncDecl(h0u, BooleanType, [], zd, BlockStmt([]))
	FuncDecl(w4, VoidType, [Param(U, FloatType), InheritParam(i4A, AutoType)], Gm, BlockStmt([]))
	VarDecl(iU, AutoType, BinExpr(::, BinExpr(<, UnExpr(-, UnExpr(!, UnExpr(-, Id(P)))), Id(Iy)), BinExpr(||, UnExpr(!, Id(y)), BinExpr(-, Id(K), BinExpr(/, Id(Q9), Id(Mj2dNo))))))
	VarDecl(s, AutoType, BinExpr(::, UnExpr(!, FuncCall(h, [])), BinExpr(+, StringLit(\\f\\t\\n), UnExpr(-, FuncCall(Q, [])))))
])"""
		self.assertTrue(TestAST.test(input, expect, 494))

	def test_495(self):
		input = """JU , L , dBZo  : auto  = ! bDjT_   - bjmK    && n   && K      != ! c   % ! bQFkwt        , je ( )    || v   - B     + - ow   * AAV      >= r ( )    || ldvOM ( )      :: vDi   % SaRhOz    || xBIp   % zlR     || p   / a8_    - O4Y6X1   - g_q      >= ! ! - ZW        , H   + L    && ! C     || X   * q    + - YO3dy      > ! R     :: _HO9 ( )    + _s   + WerWp     || MD ( )     == J ( )       ;   """
		expect = """Program([
	VarDecl(JU, AutoType, BinExpr(!=, BinExpr(&&, BinExpr(&&, BinExpr(-, UnExpr(!, Id(bDjT_)), Id(bjmK)), Id(n)), Id(K)), BinExpr(%, UnExpr(!, Id(c)), UnExpr(!, Id(bQFkwt)))))
	VarDecl(L, AutoType, BinExpr(::, BinExpr(>=, BinExpr(||, FuncCall(je, []), BinExpr(+, BinExpr(-, Id(v), Id(B)), BinExpr(*, UnExpr(-, Id(ow)), Id(AAV)))), BinExpr(||, FuncCall(r, []), FuncCall(ldvOM, []))), BinExpr(>=, BinExpr(||, BinExpr(||, BinExpr(%, Id(vDi), Id(SaRhOz)), BinExpr(%, Id(xBIp), Id(zlR))), BinExpr(-, BinExpr(-, BinExpr(/, Id(p), Id(a8_)), Id(O4Y6X1)), Id(g_q))), UnExpr(!, UnExpr(!, UnExpr(-, Id(ZW)))))))
	VarDecl(dBZo, AutoType, BinExpr(::, BinExpr(>, BinExpr(||, BinExpr(&&, BinExpr(+, Id(H), Id(L)), UnExpr(!, Id(C))), BinExpr(+, BinExpr(*, Id(X), Id(q)), UnExpr(-, Id(YO3dy)))), UnExpr(!, Id(R))), BinExpr(==, BinExpr(||, BinExpr(+, BinExpr(+, FuncCall(_HO9, []), Id(_s)), Id(WerWp)), FuncCall(MD, [])), FuncCall(J, []))))
])"""
		self.assertTrue(TestAST.test(input, expect, 495))

	def test_496(self):
		input = """n : function auto  ( ) { }    f3  : float   ;   """
		expect = """Program([
	FuncDecl(n, AutoType, [], None, BlockStmt([]))
	VarDecl(f3, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 496))

	def test_497(self):
		input = """v  : string   = Fu9K ( )    || b   && t     && - w    % ! Zkaa      <= ! u_ZF   - o    || - Z         ;   Wy  : integer   ;   """
		expect = """Program([
	VarDecl(v, StringType, BinExpr(<=, BinExpr(&&, BinExpr(&&, BinExpr(||, FuncCall(Fu9K, []), Id(b)), Id(t)), BinExpr(%, UnExpr(-, Id(w)), UnExpr(!, Id(Zkaa)))), BinExpr(||, BinExpr(-, UnExpr(!, Id(u_ZF)), Id(o)), UnExpr(-, Id(Z)))))
	VarDecl(Wy, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 497))

	def test_498(self):
		input = """K3  : array [ 50883_7_39685 , 6 , 0 , 1 , 8 ] of string    = ! io   / fo     || ! J5   - q       :: c   - - Yt   * D      > - Fh    - z   * k     * ! - FDd         ;   D : function void ( out m : array [ 0 , 6505 ] of boolean      ) { }    """
		expect = """Program([
	VarDecl(K3, ArrayType([50883739685, 6, 0, 1, 8], StringType), BinExpr(::, BinExpr(||, BinExpr(/, UnExpr(!, Id(io)), Id(fo)), BinExpr(-, UnExpr(!, Id(J5)), Id(q))), BinExpr(>, BinExpr(-, Id(c), BinExpr(*, UnExpr(-, Id(Yt)), Id(D))), BinExpr(-, UnExpr(-, Id(Fh)), BinExpr(*, BinExpr(*, Id(z), Id(k)), UnExpr(!, UnExpr(-, Id(FDd))))))))
	FuncDecl(D, VoidType, [OutParam(m, ArrayType([0, 6505], BooleanType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 498))

	def test_499(self):
		input = """b  : auto  = LV      ;   """
		expect = """Program([
	VarDecl(b, AutoType, Id(LV))
])"""
		self.assertTrue(TestAST.test(input, expect, 499))

	def test_500(self):
		input = """m : function array [ 0 ] of boolean    ( ) inherit VBI { }    Z , I  : boolean   = - true      :: ! t ( )    && AGX   - I        , ! V    || S   * Z     + ! - t         ;   q : function void ( E : float    , tB : auto    ) inherit T { }    """
		expect = """Program([
	FuncDecl(m, ArrayType([0], BooleanType), [], VBI, BlockStmt([]))
	VarDecl(Z, BooleanType, BinExpr(::, UnExpr(-, BooleanLit(True)), BinExpr(&&, UnExpr(!, FuncCall(t, [])), BinExpr(-, Id(AGX), Id(I)))))
	VarDecl(I, BooleanType, BinExpr(||, UnExpr(!, Id(V)), BinExpr(+, BinExpr(*, Id(S), Id(Z)), UnExpr(!, UnExpr(-, Id(t))))))
	FuncDecl(q, VoidType, [Param(E, FloatType), Param(tB, AutoType)], T, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 500))

	def test_501(self):
		input = """yi : function array [ 0 , 0 ] of boolean    ( ) inherit Jb { while ( - iBP    != Wv   && Gj     :: e ( )    > 8      ) C ( )  ;     }    """
		expect = """Program([
	FuncDecl(yi, ArrayType([0, 0], BooleanType), [], Jb, BlockStmt([WhileStmt(BinExpr(::, BinExpr(!=, UnExpr(-, Id(iBP)), BinExpr(&&, Id(Wv), Id(Gj))), BinExpr(>, FuncCall(e, []), IntegerLit(8))), CallStmt(C, ))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 501))

	def test_502(self):
		input = """MSI  : auto  = b   || oy    % mYK   * t     % t   && PM    - a   - JG       :: ! - t     && - - o      > lrgeO   % mE    || J ( )     && - k   || Mt4x6A         ;   H : function integer   ( inherit A : boolean    , inherit out Y : array [ 0 ] of float      ) inherit K { F , v  : auto  = B   - v1oBx     :: B   + o    >= ! fPWb0      , c   + X    == M ( )     :: h   / u       ;  for ( b  = ! _b     :: - o      , k   && X12Nb9    == lQ6   || e1gO     :: ! L      , ! H      ) return ;     }    """
		expect = """Program([
	VarDecl(MSI, AutoType, BinExpr(::, BinExpr(&&, BinExpr(||, Id(b), BinExpr(%, BinExpr(*, BinExpr(%, Id(oy), Id(mYK)), Id(t)), Id(t))), BinExpr(-, BinExpr(-, Id(PM), Id(a)), Id(JG))), BinExpr(>, BinExpr(&&, UnExpr(!, UnExpr(-, Id(t))), UnExpr(-, UnExpr(-, Id(o)))), BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(%, Id(lrgeO), Id(mE)), FuncCall(J, [])), UnExpr(-, Id(k))), Id(Mt4x6A)))))
	FuncDecl(H, IntegerType, [InheritParam(A, BooleanType), InheritOutParam(Y, ArrayType([0], FloatType))], K, BlockStmt([VarDecl(F, AutoType, BinExpr(::, BinExpr(-, Id(B), Id(v1oBx)), BinExpr(>=, BinExpr(+, Id(B), Id(o)), UnExpr(!, Id(fPWb0))))), VarDecl(v, AutoType, BinExpr(::, BinExpr(==, BinExpr(+, Id(c), Id(X)), FuncCall(M, [])), BinExpr(/, Id(h), Id(u)))), ForStmt(AssignStmt(Id(b), BinExpr(::, UnExpr(!, Id(_b)), UnExpr(-, Id(o)))), BinExpr(::, BinExpr(==, BinExpr(&&, Id(k), Id(X12Nb9)), BinExpr(||, Id(lQ6), Id(e1gO))), UnExpr(!, Id(L))), UnExpr(!, Id(H)), ReturnStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 502))

	def test_503(self):
		input = """tVDwG : function void ( ) inherit PU { }    """
		expect = """Program([
	FuncDecl(tVDwG, VoidType, [], PU, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 503))

	def test_504(self):
		input = """X : function void ( inherit Jb : auto    ) { }    _nW : function void ( out a : array [ 0 , 0 ] of float      ) inherit bd { mO  : auto  = ! Z2_8     :: t   || F       ;  }    v : function auto  ( ) inherit gFBL { }    zoy : function array [ 90_5_64 , 0 , 0 ] of integer    ( ) inherit v { if ( ! z    <= 5     :: - YW      ) M ( )  ;   else { }     do { break ;   TP , I  : integer   ;  bg9jMp , me  : auto  ;  wKq , cj  : auto  ;  P6i  : boolean   ;  { }   K , Z  : float   ;  Pda , R , TG  : array [ 0 , 0 ] of boolean    ;  }  while ( AuPfl   >= - yW     :: XO   || k      ) ;   s  : auto  = SZ ( )    > B ( )       ;  }    Js3 : function void ( out O : boolean     ) inherit r { }    """
		expect = """Program([
	FuncDecl(X, VoidType, [InheritParam(Jb, AutoType)], None, BlockStmt([]))
	FuncDecl(_nW, VoidType, [OutParam(a, ArrayType([0, 0], FloatType))], bd, BlockStmt([VarDecl(mO, AutoType, BinExpr(::, UnExpr(!, Id(Z2_8)), BinExpr(||, Id(t), Id(F))))]))
	FuncDecl(v, AutoType, [], gFBL, BlockStmt([]))
	FuncDecl(zoy, ArrayType([90564, 0, 0], IntegerType), [], v, BlockStmt([IfStmt(BinExpr(::, BinExpr(<=, UnExpr(!, Id(z)), IntegerLit(5)), UnExpr(-, Id(YW))), CallStmt(M, ), BlockStmt([])), DoWhileStmt(BinExpr(::, BinExpr(>=, Id(AuPfl), UnExpr(-, Id(yW))), BinExpr(||, Id(XO), Id(k))), BlockStmt([BreakStmt(), VarDecl(TP, IntegerType), VarDecl(I, IntegerType), VarDecl(bg9jMp, AutoType), VarDecl(me, AutoType), VarDecl(wKq, AutoType), VarDecl(cj, AutoType), VarDecl(P6i, BooleanType), BlockStmt([]), VarDecl(K, FloatType), VarDecl(Z, FloatType), VarDecl(Pda, ArrayType([0, 0], BooleanType)), VarDecl(R, ArrayType([0, 0], BooleanType)), VarDecl(TG, ArrayType([0, 0], BooleanType))])), VarDecl(s, AutoType, BinExpr(>, FuncCall(SZ, []), FuncCall(B, [])))]))
	FuncDecl(Js3, VoidType, [OutParam(O, BooleanType)], r, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 504))

	def test_505(self):
		input = """KG : function auto  ( inherit out u : float     ) { if ( k   && c    == o   + nQzb     :: ! b      ) return ;     m  : auto  = A   / R    > om   % x       ;  }    """
		expect = """Program([
	FuncDecl(KG, AutoType, [InheritOutParam(u, FloatType)], None, BlockStmt([IfStmt(BinExpr(::, BinExpr(==, BinExpr(&&, Id(k), Id(c)), BinExpr(+, Id(o), Id(nQzb))), UnExpr(!, Id(b))), ReturnStmt()), VarDecl(m, AutoType, BinExpr(>, BinExpr(/, Id(A), Id(R)), BinExpr(%, Id(om), Id(x))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 505))

	def test_506(self):
		input = """A , _ , t6  : array [ 0 ] of integer    = - JmG ( )       , - ! Gz   * d      == ! mGB   - oH     - J   % L    || y_h   || l       :: ""    / S7   - Tqv     / Bc   + f    || H   - x        , N ( )    < - sNl   % hNp    && N ( )       :: 0    / - w     - s ( )        ;   T : function void ( out fCA : boolean     ) inherit D { }    dR  : float   = ev ( )    - - ag    + t     > ! D    && - Y     + "\\\'\\r"      :: - t    && Bwi5p    - W ( )    || A3   * r      > YHT   - A    && k    || - _9_fy    + s   / g         ;   """
		expect = """Program([
	VarDecl(A, ArrayType([0], IntegerType), UnExpr(-, FuncCall(JmG, [])))
	VarDecl(_, ArrayType([0], IntegerType), BinExpr(::, BinExpr(==, BinExpr(*, UnExpr(-, UnExpr(!, Id(Gz))), Id(d)), BinExpr(||, BinExpr(||, BinExpr(-, BinExpr(-, UnExpr(!, Id(mGB)), Id(oH)), BinExpr(%, Id(J), Id(L))), Id(y_h)), Id(l))), BinExpr(||, BinExpr(+, BinExpr(-, BinExpr(/, StringLit(), Id(S7)), BinExpr(/, Id(Tqv), Id(Bc))), Id(f)), BinExpr(-, Id(H), Id(x)))))
	VarDecl(t6, ArrayType([0], IntegerType), BinExpr(::, BinExpr(<, FuncCall(N, []), BinExpr(&&, BinExpr(%, UnExpr(-, Id(sNl)), Id(hNp)), FuncCall(N, []))), BinExpr(-, BinExpr(/, IntegerLit(0), UnExpr(-, Id(w))), FuncCall(s, []))))
	FuncDecl(T, VoidType, [OutParam(fCA, BooleanType)], D, BlockStmt([]))
	VarDecl(dR, FloatType, BinExpr(::, BinExpr(>, BinExpr(+, BinExpr(-, FuncCall(ev, []), UnExpr(-, Id(ag))), Id(t)), BinExpr(&&, UnExpr(!, Id(D)), BinExpr(+, UnExpr(-, Id(Y)), StringLit(\\'\\r)))), BinExpr(>, BinExpr(||, BinExpr(&&, UnExpr(-, Id(t)), BinExpr(-, Id(Bwi5p), FuncCall(W, []))), BinExpr(*, Id(A3), Id(r))), BinExpr(||, BinExpr(&&, BinExpr(-, Id(YHT), Id(A)), Id(k)), BinExpr(+, UnExpr(-, Id(_9_fy)), BinExpr(/, Id(s), Id(g)))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 506))

	def test_507(self):
		input = """RpORO : function array [ 123 ] of float    ( inherit out o45 : auto   , out K : float     ) inherit gF { }    D , T , Y  : auto  = ! g    * CN ( )     || ! v   || Svs      <= - f     :: ! Ltc   || RoSGRwO     - - R   || Ux        , ! XM_ ( )    * - HGg        , ! FT   % A     && - uf    && - T      >= 4_221077    - gK   || ! w         ;   """
		expect = """Program([
	FuncDecl(RpORO, ArrayType([123], FloatType), [InheritOutParam(o45, AutoType), OutParam(K, FloatType)], gF, BlockStmt([]))
	VarDecl(D, AutoType, BinExpr(::, BinExpr(<=, BinExpr(||, BinExpr(||, BinExpr(*, UnExpr(!, Id(g)), FuncCall(CN, [])), UnExpr(!, Id(v))), Id(Svs)), UnExpr(-, Id(f))), BinExpr(||, BinExpr(||, UnExpr(!, Id(Ltc)), BinExpr(-, Id(RoSGRwO), UnExpr(-, Id(R)))), Id(Ux))))
	VarDecl(T, AutoType, BinExpr(*, UnExpr(!, FuncCall(XM_, [])), UnExpr(-, Id(HGg))))
	VarDecl(Y, AutoType, BinExpr(>=, BinExpr(&&, BinExpr(&&, BinExpr(%, UnExpr(!, Id(FT)), Id(A)), UnExpr(-, Id(uf))), UnExpr(-, Id(T))), BinExpr(||, BinExpr(-, IntegerLit(4221077), Id(gK)), UnExpr(!, Id(w)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 507))

	def test_508(self):
		input = """T , H , d , i  : array [ 0 ] of boolean    ;   """
		expect = """Program([
	VarDecl(T, ArrayType([0], BooleanType))
	VarDecl(H, ArrayType([0], BooleanType))
	VarDecl(d, ArrayType([0], BooleanType))
	VarDecl(i, ArrayType([0], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 508))

	def test_509(self):
		input = """uB  : array [ 0 ] of string    = s_   == ! - T0NQ   * qN       :: yNl   * Kx9LC    / - h     % U ( )     != K3o      ;   G : function string   ( inherit cg : float     ) inherit W { }    """
		expect = """Program([
	VarDecl(uB, ArrayType([0], StringType), BinExpr(::, BinExpr(==, Id(s_), BinExpr(*, UnExpr(!, UnExpr(-, Id(T0NQ))), Id(qN))), BinExpr(!=, BinExpr(%, BinExpr(/, BinExpr(*, Id(yNl), Id(Kx9LC)), UnExpr(-, Id(h))), FuncCall(U, [])), Id(K3o))))
	FuncDecl(G, StringType, [InheritParam(cg, FloatType)], W, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 509))

	def test_510(self):
		input = """n  : array [ 0 , 550 ] of string    = ES3iOq   % u    * - L     - Z   || e    * - ZC0V_8      <= b ( )    + N ( )      :: ! fHGf   * IEh     * hq5 ( )        ;   """
		expect = """Program([
	VarDecl(n, ArrayType([0, 550], StringType), BinExpr(::, BinExpr(<=, BinExpr(||, BinExpr(-, BinExpr(*, BinExpr(%, Id(ES3iOq), Id(u)), UnExpr(-, Id(L))), Id(Z)), BinExpr(*, Id(e), UnExpr(-, Id(ZC0V_8)))), BinExpr(+, FuncCall(b, []), FuncCall(N, []))), BinExpr(*, BinExpr(*, UnExpr(!, Id(fHGf)), Id(IEh)), FuncCall(hq5, []))))
])"""
		self.assertTrue(TestAST.test(input, expect, 510))

	def test_511(self):
		input = """i_ : function auto  ( inherit A : float     ) inherit a { if ( Ral_x   == H     ) R8 ( )  ;     P  : string   ;  }    """
		expect = """Program([
	FuncDecl(i_, AutoType, [InheritParam(A, FloatType)], a, BlockStmt([IfStmt(BinExpr(==, Id(Ral_x), Id(H)), CallStmt(R8, )), VarDecl(P, StringType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 511))

	def test_512(self):
		input = """es , oa , h , jO  : float   ;   Macb : function void ( inherit K : boolean    , X4K : array [ 0 ] of boolean      ) { }    """
		expect = """Program([
	VarDecl(es, FloatType)
	VarDecl(oa, FloatType)
	VarDecl(h, FloatType)
	VarDecl(jO, FloatType)
	FuncDecl(Macb, VoidType, [InheritParam(K, BooleanType), Param(X4K, ArrayType([0], BooleanType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 512))

	def test_513(self):
		input = """aU : function void ( ) { }    """
		expect = """Program([
	FuncDecl(aU, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 513))

	def test_514(self):
		input = """Yzb13 , Zvc , X8Z  : array [ 365843_0_1 , 0 , 0 ] of string    = u   && S    % ""     && ! Rm    || ! b        , 7    || t   && v     - pjk   || Bd3    && zaEtEk   || UoE       :: E     , "\\b\\b"    <= - ! e   + uBl       :: ! ! u    && p   * L         ;   IT : function auto  ( inherit out qsy94 : boolean    , inherit out KSJp : auto    ) inherit U { if ( S   <= a   - E     :: l   / S    != U   + XCLDaV      ) break ;   else return ;     }    F5kwBx : function array [ 0 ] of float    ( ) { R  = I ( )    == g   || v0     :: RAbu   * mQJ      ;   }    """
		expect = """Program([
	VarDecl(Yzb13, ArrayType([36584301, 0, 0], StringType), BinExpr(||, BinExpr(&&, BinExpr(&&, Id(u), BinExpr(%, Id(S), StringLit())), UnExpr(!, Id(Rm))), UnExpr(!, Id(b))))
	VarDecl(Zvc, ArrayType([36584301, 0, 0], StringType), BinExpr(::, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(&&, BinExpr(||, IntegerLit(7), Id(t)), BinExpr(-, Id(v), Id(pjk))), Id(Bd3)), Id(zaEtEk)), Id(UoE)), Id(E)))
	VarDecl(X8Z, ArrayType([36584301, 0, 0], StringType), BinExpr(::, BinExpr(<=, StringLit(\\b\\b), BinExpr(+, UnExpr(-, UnExpr(!, Id(e))), Id(uBl))), BinExpr(&&, UnExpr(!, UnExpr(!, Id(u))), BinExpr(*, Id(p), Id(L)))))
	FuncDecl(IT, AutoType, [InheritOutParam(qsy94, BooleanType), InheritOutParam(KSJp, AutoType)], U, BlockStmt([IfStmt(BinExpr(::, BinExpr(<=, Id(S), BinExpr(-, Id(a), Id(E))), BinExpr(!=, BinExpr(/, Id(l), Id(S)), BinExpr(+, Id(U), Id(XCLDaV)))), BreakStmt(), ReturnStmt())]))
	FuncDecl(F5kwBx, ArrayType([0], FloatType), [], None, BlockStmt([AssignStmt(Id(R), BinExpr(::, BinExpr(==, FuncCall(I, []), BinExpr(||, Id(g), Id(v0))), BinExpr(*, Id(RAbu), Id(mQJ))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 514))

	def test_515(self):
		input = """LHU , y , t  : boolean   ;   A , y  : string   ;   """
		expect = """Program([
	VarDecl(LHU, BooleanType)
	VarDecl(y, BooleanType)
	VarDecl(t, BooleanType)
	VarDecl(A, StringType)
	VarDecl(y, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 515))

	def test_516(self):
		input = """u : function array [ 5 ] of float    ( ) { }    """
		expect = """Program([
	FuncDecl(u, ArrayType([5], FloatType), [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 516))

	def test_517(self):
		input = """J  : auto  ;   """
		expect = """Program([
	VarDecl(J, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 517))

	def test_518(self):
		input = """xB , WJ , Nd  : array [ 0 , 60 , 3_7 , 98 , 0 , 3 , 3786_582 ] of boolean    ;   u : function array [ 8_4 ] of float    ( ) inherit Bp { TUi , g , pZ  : float   ;  }    """
		expect = """Program([
	VarDecl(xB, ArrayType([0, 60, 37, 98, 0, 3, 3786582], BooleanType))
	VarDecl(WJ, ArrayType([0, 60, 37, 98, 0, 3, 3786582], BooleanType))
	VarDecl(Nd, ArrayType([0, 60, 37, 98, 0, 3, 3786582], BooleanType))
	FuncDecl(u, ArrayType([84], FloatType), [], Bp, BlockStmt([VarDecl(TUi, FloatType), VarDecl(g, FloatType), VarDecl(pZ, FloatType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 518))

	def test_519(self):
		input = """fCv : function boolean   ( ) { }    jdj : function void ( ) { Im , Fv , p  : auto  = g   >= T   + bp      , ! ts_    > Q7g3lo   * B     :: w   * W51      , - t     :: e4CV   && cgJ7vL       ;  }    w : function void ( ) inherit Itd { }    """
		expect = """Program([
	FuncDecl(fCv, BooleanType, [], None, BlockStmt([]))
	FuncDecl(jdj, VoidType, [], None, BlockStmt([VarDecl(Im, AutoType, BinExpr(>=, Id(g), BinExpr(+, Id(T), Id(bp)))), VarDecl(Fv, AutoType, BinExpr(::, BinExpr(>, UnExpr(!, Id(ts_)), BinExpr(*, Id(Q7g3lo), Id(B))), BinExpr(*, Id(w), Id(W51)))), VarDecl(p, AutoType, BinExpr(::, UnExpr(-, Id(t)), BinExpr(&&, Id(e4CV), Id(cgJ7vL))))]))
	FuncDecl(w, VoidType, [], Itd, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 519))

	def test_520(self):
		input = """Yr7I  : auto  ;   """
		expect = """Program([
	VarDecl(Yr7I, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 520))

	def test_521(self):
		input = """H : function integer   ( ) { }    """
		expect = """Program([
	FuncDecl(H, IntegerType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 521))

	def test_522(self):
		input = """Kf , Qw , RnW1  : auto  = DW   - D   * O    / i   - K       :: d0   && u   * m   % W      == ! HAPZ   % P     || Z   && ttc9FCE    || qUV   || vz        , - ip   && X     && - xn5    % tN   * s        , ! 5    + d     <= - tG   / SymvDV2     || ! E   - g1jfK         ;   """
		expect = """Program([
	VarDecl(Kf, AutoType, BinExpr(::, BinExpr(-, BinExpr(-, Id(DW), BinExpr(/, BinExpr(*, Id(D), Id(O)), Id(i))), Id(K)), BinExpr(==, BinExpr(&&, Id(d0), BinExpr(%, BinExpr(*, Id(u), Id(m)), Id(W))), BinExpr(||, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(%, UnExpr(!, Id(HAPZ)), Id(P)), Id(Z)), Id(ttc9FCE)), Id(qUV)), Id(vz)))))
	VarDecl(Qw, AutoType, BinExpr(&&, BinExpr(&&, UnExpr(-, Id(ip)), Id(X)), BinExpr(*, BinExpr(%, UnExpr(-, Id(xn5)), Id(tN)), Id(s))))
	VarDecl(RnW1, AutoType, BinExpr(<=, BinExpr(+, UnExpr(!, IntegerLit(5)), Id(d)), BinExpr(||, BinExpr(/, UnExpr(-, Id(tG)), Id(SymvDV2)), BinExpr(-, UnExpr(!, Id(E)), Id(g1jfK)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 522))

	def test_523(self):
		input = """Wwm : function void ( out W2K : array [ 0 ] of boolean     , qk : auto    ) inherit bw { }    q0IH , C  : boolean   ;   m : function void ( inherit out z : array [ 0 ] of float      ) inherit Z { }    """
		expect = """Program([
	FuncDecl(Wwm, VoidType, [OutParam(W2K, ArrayType([0], BooleanType)), Param(qk, AutoType)], bw, BlockStmt([]))
	VarDecl(q0IH, BooleanType)
	VarDecl(C, BooleanType)
	FuncDecl(m, VoidType, [InheritOutParam(z, ArrayType([0], FloatType))], Z, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 523))

	def test_524(self):
		input = """K3 : function auto  ( V : array [ 5_3_8 ] of boolean     , Z : array [ 30636_96405_7 ] of boolean     , out yS : integer     ) { L  : array [ 931_63342_225 ] of boolean    ;  }    p : function void ( inherit Z : float    , inherit out hC : array [ 0 , 6724 ] of float     , out v : auto   , out w : auto    ) { OP  : array [ 0 ] of string    ;  x , z , Ty  : auto  = ! vX    < - RO     :: - w1    == - X      , ! j    >= t   && R     :: P   && Ht      , j   || l       ;  }    """
		expect = """Program([
	FuncDecl(K3, AutoType, [Param(V, ArrayType([538], BooleanType)), Param(Z, ArrayType([30636964057], BooleanType)), OutParam(yS, IntegerType)], None, BlockStmt([VarDecl(L, ArrayType([93163342225], BooleanType))]))
	FuncDecl(p, VoidType, [InheritParam(Z, FloatType), InheritOutParam(hC, ArrayType([0, 6724], FloatType)), OutParam(v, AutoType), OutParam(w, AutoType)], None, BlockStmt([VarDecl(OP, ArrayType([0], StringType)), VarDecl(x, AutoType, BinExpr(::, BinExpr(<, UnExpr(!, Id(vX)), UnExpr(-, Id(RO))), BinExpr(==, UnExpr(-, Id(w1)), UnExpr(-, Id(X))))), VarDecl(z, AutoType, BinExpr(::, BinExpr(>=, UnExpr(!, Id(j)), BinExpr(&&, Id(t), Id(R))), BinExpr(&&, Id(P), Id(Ht)))), VarDecl(Ty, AutoType, BinExpr(||, Id(j), Id(l)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 524))

	def test_525(self):
		input = """WG : function void ( out lP : float     ) { G ( )  ;   }    C : function void ( inherit O : integer     ) inherit bM { while ( ! I    == - BM      ) T ( )  ;     e  : integer   = Wt   / L    > ! w     :: - E       ;  }    """
		expect = """Program([
	FuncDecl(WG, VoidType, [OutParam(lP, FloatType)], None, BlockStmt([CallStmt(G, )]))
	FuncDecl(C, VoidType, [InheritParam(O, IntegerType)], bM, BlockStmt([WhileStmt(BinExpr(==, UnExpr(!, Id(I)), UnExpr(-, Id(BM))), CallStmt(T, )), VarDecl(e, IntegerType, BinExpr(::, BinExpr(>, BinExpr(/, Id(Wt), Id(L)), UnExpr(!, Id(w))), UnExpr(-, Id(E))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 525))

	def test_526(self):
		input = """e , v  : array [ 0 , 4 , 0 ] of boolean    ;   """
		expect = """Program([
	VarDecl(e, ArrayType([0, 4, 0], BooleanType))
	VarDecl(v, ArrayType([0, 4, 0], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 526))

	def test_527(self):
		input = """JMW : function string   ( out Qo : auto   , out lSyBww : auto    ) inherit O { Ow8  : auto  ;  }    """
		expect = """Program([
	FuncDecl(JMW, StringType, [OutParam(Qo, AutoType), OutParam(lSyBww, AutoType)], O, BlockStmt([VarDecl(Ow8, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 527))

	def test_528(self):
		input = """e , qU  : float   ;   O : function float   ( out X : integer     ) inherit GW { return ;   }    """
		expect = """Program([
	VarDecl(e, FloatType)
	VarDecl(qU, FloatType)
	FuncDecl(O, FloatType, [OutParam(X, IntegerType)], GW, BlockStmt([ReturnStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 528))

	def test_529(self):
		input = """MqX : function void ( ) inherit v { F  : float   = H   / UZ     :: - R6       ;  }    X : function void ( inherit K9xOY1rsm : boolean     ) inherit l { }    """
		expect = """Program([
	FuncDecl(MqX, VoidType, [], v, BlockStmt([VarDecl(F, FloatType, BinExpr(::, BinExpr(/, Id(H), Id(UZ)), UnExpr(-, Id(R6))))]))
	FuncDecl(X, VoidType, [InheritParam(K9xOY1rsm, BooleanType)], l, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 529))

	def test_530(self):
		input = """evC , ktIS  : auto  ;   p  : integer   = - - R     || rdL   * R    || HtiOE   - eet      < y ( )    && EFOdTT   || e     || ! ! bP       :: ! ! - c         ;   r  : boolean   ;   """
		expect = """Program([
	VarDecl(evC, AutoType)
	VarDecl(ktIS, AutoType)
	VarDecl(p, IntegerType, BinExpr(::, BinExpr(<, BinExpr(||, BinExpr(||, UnExpr(-, UnExpr(-, Id(R))), BinExpr(*, Id(rdL), Id(R))), BinExpr(-, Id(HtiOE), Id(eet))), BinExpr(||, BinExpr(||, BinExpr(&&, FuncCall(y, []), Id(EFOdTT)), Id(e)), UnExpr(!, UnExpr(!, Id(bP))))), UnExpr(!, UnExpr(!, UnExpr(-, Id(c))))))
	VarDecl(r, BooleanType)
])"""
		self.assertTrue(TestAST.test(input, expect, 530))

	def test_531(self):
		input = """rMLFK : function auto  ( inherit out y : boolean    , inherit out M : array [ 0 , 582_6_81 ] of string      ) { continue ;   return ;   break ;   }    """
		expect = """Program([
	FuncDecl(rMLFK, AutoType, [InheritOutParam(y, BooleanType), InheritOutParam(M, ArrayType([0, 582681], StringType))], None, BlockStmt([ContinueStmt(), ReturnStmt(), BreakStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 531))

	def test_532(self):
		input = """Z  : array [ 939 , 8 , 0 ] of float    = ! - mSW   + O      >= - WIIj   && e    && d   || kt       :: - ! ! SAT1      < { }     / Rc   + eFnv    - ""         ;   j  : integer   ;   f  : auto  = Lj ( )    > P   % - ! v0j         ;   h : function void ( ) { }    """
		expect = """Program([
	VarDecl(Z, ArrayType([939, 8, 0], FloatType), BinExpr(::, BinExpr(>=, BinExpr(+, UnExpr(!, UnExpr(-, Id(mSW))), Id(O)), BinExpr(||, BinExpr(&&, BinExpr(&&, UnExpr(-, Id(WIIj)), Id(e)), Id(d)), Id(kt))), BinExpr(<, UnExpr(-, UnExpr(!, UnExpr(!, Id(SAT1)))), BinExpr(-, BinExpr(+, BinExpr(/, ArrayLit([]), Id(Rc)), Id(eFnv)), StringLit()))))
	VarDecl(j, IntegerType)
	VarDecl(f, AutoType, BinExpr(>, FuncCall(Lj, []), BinExpr(%, Id(P), UnExpr(-, UnExpr(!, Id(v0j))))))
	FuncDecl(h, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 532))

	def test_533(self):
		input = """Z  : array [ 7572333_0 ] of string    ;   M , IAYk  : array [ 7 , 0 , 363 ] of string    ;   j  : array [ 9 , 0 , 5 , 394953 , 0 , 0 ] of integer    = Q ( )    == .e+51050     :: - X2k1    && ! J     % V ( )     <= Gf   / vv    + 0     || y   && wxB   / RH         ;   u : function void ( inherit wg : array [ 2_3_9747737_3_708_1 , 0 , 0 , 43_55 , 32_6_107_0_6 ] of boolean      ) { }    k , k  : integer   = - o    || _   - n    + c ( )      >= - ! x    || HT   - EV        , UjXwl   / - P    - - V      == - ! H     || x   + n    * ""       :: FHQR9 ( )       ;   x  : array [ 1_784 , 0 ] of integer    = ! - i    + X   && ZBX      <= - X3   || WF    || ! YVHu         ;   ibO , E  : string   ;   """
		expect = """Program([
	VarDecl(Z, ArrayType([75723330], StringType))
	VarDecl(M, ArrayType([7, 0, 363], StringType))
	VarDecl(IAYk, ArrayType([7, 0, 363], StringType))
	VarDecl(j, ArrayType([9, 0, 5, 394953, 0, 0], IntegerType), BinExpr(::, BinExpr(==, FuncCall(Q, []), FloatLit(0.0)), BinExpr(<=, BinExpr(&&, UnExpr(-, Id(X2k1)), BinExpr(%, UnExpr(!, Id(J)), FuncCall(V, []))), BinExpr(&&, BinExpr(||, BinExpr(+, BinExpr(/, Id(Gf), Id(vv)), IntegerLit(0)), Id(y)), BinExpr(/, Id(wxB), Id(RH))))))
	FuncDecl(u, VoidType, [InheritParam(wg, ArrayType([23974773737081, 0, 0, 4355, 32610706], BooleanType))], None, BlockStmt([]))
	VarDecl(k, IntegerType, BinExpr(>=, BinExpr(||, UnExpr(-, Id(o)), BinExpr(+, BinExpr(-, Id(_), Id(n)), FuncCall(c, []))), BinExpr(||, UnExpr(-, UnExpr(!, Id(x))), BinExpr(-, Id(HT), Id(EV)))))
	VarDecl(k, IntegerType, BinExpr(::, BinExpr(==, BinExpr(-, BinExpr(/, Id(UjXwl), UnExpr(-, Id(P))), UnExpr(-, Id(V))), BinExpr(||, UnExpr(-, UnExpr(!, Id(H))), BinExpr(+, Id(x), BinExpr(*, Id(n), StringLit())))), FuncCall(FHQR9, [])))
	VarDecl(x, ArrayType([1784, 0], IntegerType), BinExpr(<=, BinExpr(&&, BinExpr(+, UnExpr(!, UnExpr(-, Id(i))), Id(X)), Id(ZBX)), BinExpr(||, BinExpr(||, UnExpr(-, Id(X3)), Id(WF)), UnExpr(!, Id(YVHu)))))
	VarDecl(ibO, StringType)
	VarDecl(E, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 533))

	def test_534(self):
		input = """D5  : integer   = - - w     && M   * L    * f   % m      >= - - yj    % Uh   / YJP         ;   zdp , AC_m , Pz  : integer   ;   """
		expect = """Program([
	VarDecl(D5, IntegerType, BinExpr(>=, BinExpr(&&, UnExpr(-, UnExpr(-, Id(w))), BinExpr(%, BinExpr(*, BinExpr(*, Id(M), Id(L)), Id(f)), Id(m))), BinExpr(/, BinExpr(%, UnExpr(-, UnExpr(-, Id(yj))), Id(Uh)), Id(YJP))))
	VarDecl(zdp, IntegerType)
	VarDecl(AC_m, IntegerType)
	VarDecl(Pz, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 534))

	def test_535(self):
		input = """sK  : array [ 32 , 0 ] of string    = lh   - ! - n_YKlY      >= - fPTEP83   * Y    - m   + aqmcb         ;   """
		expect = """Program([
	VarDecl(sK, ArrayType([32, 0], StringType), BinExpr(>=, BinExpr(-, Id(lh), UnExpr(!, UnExpr(-, Id(n_YKlY)))), BinExpr(+, BinExpr(-, BinExpr(*, UnExpr(-, Id(fPTEP83)), Id(Y)), Id(m)), Id(aqmcb))))
])"""
		self.assertTrue(TestAST.test(input, expect, 535))

	def test_536(self):
		input = """T  : auto  ;   x : function auto  ( ) { if ( f   + p_    > z ( )      ) break ;   else break ;     }    B : function auto  ( inherit PfrUT : array [ 1 ] of float     , inherit Ydw : auto    ) { }    """
		expect = """Program([
	VarDecl(T, AutoType)
	FuncDecl(x, AutoType, [], None, BlockStmt([IfStmt(BinExpr(>, BinExpr(+, Id(f), Id(p_)), FuncCall(z, [])), BreakStmt(), BreakStmt())]))
	FuncDecl(B, AutoType, [InheritParam(PfrUT, ArrayType([1], FloatType)), InheritParam(Ydw, AutoType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 536))

	def test_537(self):
		input = """Js9 : function void ( ) inherit m { }    """
		expect = """Program([
	FuncDecl(Js9, VoidType, [], m, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 537))

	def test_538(self):
		input = """e : function auto  ( inherit baKLO : array [ 5 ] of string      ) inherit C { while ( ""    == ! w      ) { continue ;   }     break ;   }    yxHa , X , o  : auto  ;   """
		expect = """Program([
	FuncDecl(e, AutoType, [InheritParam(baKLO, ArrayType([5], StringType))], C, BlockStmt([WhileStmt(BinExpr(==, StringLit(), UnExpr(!, Id(w))), BlockStmt([ContinueStmt()])), BreakStmt()]))
	VarDecl(yxHa, AutoType)
	VarDecl(X, AutoType)
	VarDecl(o, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 538))

	def test_539(self):
		input = """ZjGF : function array [ 0 ] of string    ( out R : array [ 0 ] of boolean      ) inherit ai { break ;   do { }  while ( 0     :: XC   == k     ) ;   }    T : function void ( ) inherit bwk { }    RA  : integer   = - SVj   - K     || ! aJ    / - X4wEjXYCwX      == ! m   - t    - ""         ;   O : function auto  ( ) { }    """
		expect = """Program([
	FuncDecl(ZjGF, ArrayType([0], StringType), [OutParam(R, ArrayType([0], BooleanType))], ai, BlockStmt([BreakStmt(), DoWhileStmt(BinExpr(::, IntegerLit(0), BinExpr(==, Id(XC), Id(k))), BlockStmt([]))]))
	FuncDecl(T, VoidType, [], bwk, BlockStmt([]))
	VarDecl(RA, IntegerType, BinExpr(==, BinExpr(||, BinExpr(-, UnExpr(-, Id(SVj)), Id(K)), BinExpr(/, UnExpr(!, Id(aJ)), UnExpr(-, Id(X4wEjXYCwX)))), BinExpr(-, BinExpr(-, UnExpr(!, Id(m)), Id(t)), StringLit())))
	FuncDecl(O, AutoType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 539))

	def test_540(self):
		input = """gET : function void ( ) { }    TMMfysn , y , GZj , iN  : string   = { }     - { }        , bfCWnL   || Y    - wMb   / _F     - m   && yZ    && - tg      >= ! - l     - nI1   / f    || - v       :: a ( )    && { }      < ! F6m    || xMKVH ( )     + R   * nqI6    / ! Q        , - ! i    + Hj   + fE       :: - xo   - HQy3     / kvT      , - gt   % H    || ""      >= - t ( )      :: ! ! xI    / - C      > ! ! S ( )         ;   """
		expect = """Program([
	FuncDecl(gET, VoidType, [], None, BlockStmt([]))
	VarDecl(TMMfysn, StringType, BinExpr(-, ArrayLit([]), ArrayLit([])))
	VarDecl(y, StringType, BinExpr(::, BinExpr(>=, BinExpr(&&, BinExpr(&&, BinExpr(||, Id(bfCWnL), BinExpr(-, BinExpr(-, Id(Y), BinExpr(/, Id(wMb), Id(_F))), Id(m))), Id(yZ)), UnExpr(-, Id(tg))), BinExpr(||, BinExpr(-, UnExpr(!, UnExpr(-, Id(l))), BinExpr(/, Id(nI1), Id(f))), UnExpr(-, Id(v)))), BinExpr(<, BinExpr(&&, FuncCall(a, []), ArrayLit([])), BinExpr(||, UnExpr(!, Id(F6m)), BinExpr(+, FuncCall(xMKVH, []), BinExpr(/, BinExpr(*, Id(R), Id(nqI6)), UnExpr(!, Id(Q))))))))
	VarDecl(GZj, StringType, BinExpr(::, BinExpr(+, BinExpr(+, UnExpr(-, UnExpr(!, Id(i))), Id(Hj)), Id(fE)), BinExpr(-, UnExpr(-, Id(xo)), BinExpr(/, Id(HQy3), Id(kvT)))))
	VarDecl(iN, StringType, BinExpr(::, BinExpr(>=, BinExpr(||, BinExpr(%, UnExpr(-, Id(gt)), Id(H)), StringLit()), UnExpr(-, FuncCall(t, []))), BinExpr(>, BinExpr(/, UnExpr(!, UnExpr(!, Id(xI))), UnExpr(-, Id(C))), UnExpr(!, UnExpr(!, FuncCall(S, []))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 540))

	def test_541(self):
		input = """i : function void ( inherit out Ar : string     ) inherit m7 { }    PF  : boolean   ;   Jo : function integer   ( ) inherit L { for ( xN  = Y2   + tcV    < sd   && T     :: C   - _aR    != ! MqnRB      , Z7   && N    >= - Y     :: a   - NCK    == C6   + aU      , ! S    >= ""      ) continue ;     }    """
		expect = """Program([
	FuncDecl(i, VoidType, [InheritOutParam(Ar, StringType)], m7, BlockStmt([]))
	VarDecl(PF, BooleanType)
	FuncDecl(Jo, IntegerType, [], L, BlockStmt([ForStmt(AssignStmt(Id(xN), BinExpr(::, BinExpr(<, BinExpr(+, Id(Y2), Id(tcV)), BinExpr(&&, Id(sd), Id(T))), BinExpr(!=, BinExpr(-, Id(C), Id(_aR)), UnExpr(!, Id(MqnRB))))), BinExpr(::, BinExpr(>=, BinExpr(&&, Id(Z7), Id(N)), UnExpr(-, Id(Y))), BinExpr(==, BinExpr(-, Id(a), Id(NCK)), BinExpr(+, Id(C6), Id(aU)))), BinExpr(>=, UnExpr(!, Id(S)), StringLit()), ContinueStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 541))

	def test_542(self):
		input = """S  : auto  ;   """
		expect = """Program([
	VarDecl(S, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 542))

	def test_543(self):
		input = """qWqa  : auto  ;   S : function float   ( ) { ug  : auto  ;  break ;   PF  : auto  = P ( )       ;  }    """
		expect = """Program([
	VarDecl(qWqa, AutoType)
	FuncDecl(S, FloatType, [], None, BlockStmt([VarDecl(ug, AutoType), BreakStmt(), VarDecl(PF, AutoType, FuncCall(P, []))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 543))

	def test_544(self):
		input = """O4 , h , bP , Eu  : float   = 8    - ! z     && ! a   / j      >= c     , I   || Om    > x38   && _C   - Jrc7c     && - - R        , ! - CN     || ! - D      > ! ! UE ( )       :: ! Zx    / RaF   && iB     - ! p9    || ! Hr        , 89_0E5       ;   """
		expect = """Program([
	VarDecl(O4, FloatType, BinExpr(>=, BinExpr(&&, BinExpr(-, IntegerLit(8), UnExpr(!, Id(z))), BinExpr(/, UnExpr(!, Id(a)), Id(j))), Id(c)))
	VarDecl(h, FloatType, BinExpr(>, BinExpr(||, Id(I), Id(Om)), BinExpr(&&, BinExpr(&&, Id(x38), BinExpr(-, Id(_C), Id(Jrc7c))), UnExpr(-, UnExpr(-, Id(R))))))
	VarDecl(bP, FloatType, BinExpr(::, BinExpr(>, BinExpr(||, UnExpr(!, UnExpr(-, Id(CN))), UnExpr(!, UnExpr(-, Id(D)))), UnExpr(!, UnExpr(!, FuncCall(UE, [])))), BinExpr(||, BinExpr(&&, BinExpr(/, UnExpr(!, Id(Zx)), Id(RaF)), BinExpr(-, Id(iB), UnExpr(!, Id(p9)))), UnExpr(!, Id(Hr)))))
	VarDecl(Eu, FloatType, FloatLit(89000000.0))
])"""
		self.assertTrue(TestAST.test(input, expect, 544))

	def test_545(self):
		input = """BS  : auto  ;   """
		expect = """Program([
	VarDecl(BS, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 545))

	def test_546(self):
		input = """d7V , Tz , Pg , h , Q  : array [ 29_93_5541_1 ] of float    ;   """
		expect = """Program([
	VarDecl(d7V, ArrayType([299355411], FloatType))
	VarDecl(Tz, ArrayType([299355411], FloatType))
	VarDecl(Pg, ArrayType([299355411], FloatType))
	VarDecl(h, ArrayType([299355411], FloatType))
	VarDecl(Q, ArrayType([299355411], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 546))

	def test_547(self):
		input = """G  : array [ 0 , 78_8004 ] of float    = I   && V    * v   % JX     % X   / zo    % L2AR   || D       :: 60       ;   """
		expect = """Program([
	VarDecl(G, ArrayType([0, 788004], FloatType), BinExpr(::, BinExpr(||, BinExpr(&&, Id(I), BinExpr(%, BinExpr(/, BinExpr(%, BinExpr(%, BinExpr(*, Id(V), Id(v)), Id(JX)), Id(X)), Id(zo)), Id(L2AR))), Id(D)), IntegerLit(60)))
])"""
		self.assertTrue(TestAST.test(input, expect, 547))

	def test_548(self):
		input = """c , YqGD  : array [ 5_3_32 , 264 ] of integer    ;   """
		expect = """Program([
	VarDecl(c, ArrayType([5332, 264], IntegerType))
	VarDecl(YqGD, ArrayType([5332, 264], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 548))

	def test_549(self):
		input = """c , D , RMVHAG , GAE7 , Zt , Lk_ , M  : auto  ;   eSvk0 , B_ , n , RW  : auto  ;   P : function void ( ) { if ( m   || g9Gg    == ! I4G     :: oE   % jT    != - x      ) { }   else break ;     continue ;   }    cJ , d  : array [ 61 , 0 , 0 , 0 , 0 , 5_6_8212_07 , 0 ] of integer    ;   """
		expect = """Program([
	VarDecl(c, AutoType)
	VarDecl(D, AutoType)
	VarDecl(RMVHAG, AutoType)
	VarDecl(GAE7, AutoType)
	VarDecl(Zt, AutoType)
	VarDecl(Lk_, AutoType)
	VarDecl(M, AutoType)
	VarDecl(eSvk0, AutoType)
	VarDecl(B_, AutoType)
	VarDecl(n, AutoType)
	VarDecl(RW, AutoType)
	FuncDecl(P, VoidType, [], None, BlockStmt([IfStmt(BinExpr(::, BinExpr(==, BinExpr(||, Id(m), Id(g9Gg)), UnExpr(!, Id(I4G))), BinExpr(!=, BinExpr(%, Id(oE), Id(jT)), UnExpr(-, Id(x)))), BlockStmt([]), BreakStmt()), ContinueStmt()]))
	VarDecl(cJ, ArrayType([61, 0, 0, 0, 0, 56821207, 0], IntegerType))
	VarDecl(d, ArrayType([61, 0, 0, 0, 0, 56821207, 0], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 549))

	def test_550(self):
		input = """PB5 , nZp , rw , YYW  : auto  = W   / l    / - DW     || ! Y    && _W1   + bN        , ! U   - ! Cqlv       :: - - h     * p ( )     < ! WKG   && Cto8     - ZU4   % ! I        , - - h     || PVf ( )     <= ! - sSCp     + - ! V        , ! true      :: ""    / ""     * ! xO    % ! q0cQ         ;   A : function void ( inherit out se : integer    , inherit out q : float    , inherit Zhd : array [ 0 , 72 , 0 , 0 ] of float     , inherit out R : auto    ) inherit RFN { L , Wa , X , dR , RPQ2x , fY , m15o , c , C  : array [ 2 ] of float    ;  }    """
		expect = """Program([
	VarDecl(PB5, AutoType, BinExpr(&&, BinExpr(||, BinExpr(/, BinExpr(/, Id(W), Id(l)), UnExpr(-, Id(DW))), UnExpr(!, Id(Y))), BinExpr(+, Id(_W1), Id(bN))))
	VarDecl(nZp, AutoType, BinExpr(::, BinExpr(-, UnExpr(!, Id(U)), UnExpr(!, Id(Cqlv))), BinExpr(<, BinExpr(*, UnExpr(-, UnExpr(-, Id(h))), FuncCall(p, [])), BinExpr(&&, UnExpr(!, Id(WKG)), BinExpr(-, Id(Cto8), BinExpr(%, Id(ZU4), UnExpr(!, Id(I))))))))
	VarDecl(rw, AutoType, BinExpr(<=, BinExpr(||, UnExpr(-, UnExpr(-, Id(h))), FuncCall(PVf, [])), BinExpr(+, UnExpr(!, UnExpr(-, Id(sSCp))), UnExpr(-, UnExpr(!, Id(V))))))
	VarDecl(YYW, AutoType, BinExpr(::, UnExpr(!, BooleanLit(True)), BinExpr(%, BinExpr(*, BinExpr(/, StringLit(), StringLit()), UnExpr(!, Id(xO))), UnExpr(!, Id(q0cQ)))))
	FuncDecl(A, VoidType, [InheritOutParam(se, IntegerType), InheritOutParam(q, FloatType), InheritParam(Zhd, ArrayType([0, 72, 0, 0], FloatType)), InheritOutParam(R, AutoType)], RFN, BlockStmt([VarDecl(L, ArrayType([2], FloatType)), VarDecl(Wa, ArrayType([2], FloatType)), VarDecl(X, ArrayType([2], FloatType)), VarDecl(dR, ArrayType([2], FloatType)), VarDecl(RPQ2x, ArrayType([2], FloatType)), VarDecl(fY, ArrayType([2], FloatType)), VarDecl(m15o, ArrayType([2], FloatType)), VarDecl(c, ArrayType([2], FloatType)), VarDecl(C, ArrayType([2], FloatType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 550))

	def test_551(self):
		input = """z : function void ( ) { }    Y7 , dZ , kd  : array [ 0 , 86977 , 4 ] of integer    = - - ! v      != U   || nM3    - F   || m     && ""    || W      :: pX ( )      , - - dJ9WDqPx    + ze   % Srs      >= - afa   + z    % _   - K        , ! - t   || g      != ! J       ;   xM , wQd , d , T , t , UDm  : string   = C ( )    || - mB     % H ( )     != q ( )    / dV   || y     / - x   - L        , - ! - A       :: - K9   / G    - S       , BwLb     , z ( )    / W   * Z    % 9       :: - sIr    || N   + eqg     || - eW    && - Vk        , - 0    + ! lW       :: - Y   + G     * q ( )    + k   || gm      == ngYsYJA3c   || IO6g    && - j     - EtJ2 ( )       , - mco     :: h   || e ( )     != ! G    / x   % f2if     / - nO   || V         ;   x : function array [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ] of boolean    ( ) { }    """
		expect = """Program([
	FuncDecl(z, VoidType, [], None, BlockStmt([]))
	VarDecl(Y7, ArrayType([0, 86977, 4], IntegerType), BinExpr(::, BinExpr(!=, UnExpr(-, UnExpr(-, UnExpr(!, Id(v)))), BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(||, Id(U), BinExpr(-, Id(nM3), Id(F))), Id(m)), StringLit()), Id(W))), FuncCall(pX, [])))
	VarDecl(dZ, ArrayType([0, 86977, 4], IntegerType), BinExpr(>=, BinExpr(+, UnExpr(-, UnExpr(-, Id(dJ9WDqPx))), BinExpr(%, Id(ze), Id(Srs))), BinExpr(-, BinExpr(+, UnExpr(-, Id(afa)), BinExpr(%, Id(z), Id(_))), Id(K))))
	VarDecl(kd, ArrayType([0, 86977, 4], IntegerType), BinExpr(!=, BinExpr(||, UnExpr(!, UnExpr(-, Id(t))), Id(g)), UnExpr(!, Id(J))))
	VarDecl(xM, StringType, BinExpr(!=, BinExpr(||, FuncCall(C, []), BinExpr(%, UnExpr(-, Id(mB)), FuncCall(H, []))), BinExpr(||, BinExpr(/, FuncCall(q, []), Id(dV)), BinExpr(-, BinExpr(/, Id(y), UnExpr(-, Id(x))), Id(L)))))
	VarDecl(wQd, StringType, BinExpr(::, UnExpr(-, UnExpr(!, UnExpr(-, Id(A)))), BinExpr(-, BinExpr(/, UnExpr(-, Id(K9)), Id(G)), Id(S))))
	VarDecl(d, StringType, Id(BwLb))
	VarDecl(T, StringType, BinExpr(::, BinExpr(%, BinExpr(*, BinExpr(/, FuncCall(z, []), Id(W)), Id(Z)), IntegerLit(9)), BinExpr(&&, BinExpr(||, BinExpr(||, UnExpr(-, Id(sIr)), BinExpr(+, Id(N), Id(eqg))), UnExpr(-, Id(eW))), UnExpr(-, Id(Vk)))))
	VarDecl(t, StringType, BinExpr(::, BinExpr(+, UnExpr(-, IntegerLit(0)), UnExpr(!, Id(lW))), BinExpr(==, BinExpr(||, BinExpr(+, BinExpr(+, UnExpr(-, Id(Y)), BinExpr(*, Id(G), FuncCall(q, []))), Id(k)), Id(gm)), BinExpr(&&, BinExpr(||, Id(ngYsYJA3c), Id(IO6g)), BinExpr(-, UnExpr(-, Id(j)), FuncCall(EtJ2, []))))))
	VarDecl(UDm, StringType, BinExpr(::, UnExpr(-, Id(mco)), BinExpr(!=, BinExpr(||, Id(h), FuncCall(e, [])), BinExpr(||, BinExpr(/, BinExpr(%, BinExpr(/, UnExpr(!, Id(G)), Id(x)), Id(f2if)), UnExpr(-, Id(nO))), Id(V)))))
	FuncDecl(x, ArrayType([0, 0, 0, 0, 0, 0, 0], BooleanType), [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 551))

	def test_552(self):
		input = """Re : function void ( ) inherit o6A { a8VG  : boolean   = ! Nj3       ;  for ( B  = ISX   / V    == ! Yp      , - X     :: p   || c      , JTo   || UXbm    != D   / g7L     :: u   % M      ) return ;     V ( )  ;   XJwC , zPr , a , Z , q , i , r , SH , KvXX  : auto  = zCN     , S   && C      , JMyW   < ! ni      , Q   <= g   || s     :: sYq   + b6t      , ""    == pIm     , ! x    != MsoSMd    :: - Zd      , - Sq      , - uRF    <= y   / I     :: TX   + MR    == ! B      , - x    == - O     :: K   || b       ;  break ;   continue ;   cW  = n2Gs   % k    > _   && l      ;   T , r  : auto  ;  }    O  : float   = - ! XC   / mTf      != ! L3    + - c     - Mdjk   - e    && P   - n         ;   J : function boolean   ( inherit J : array [ 0 ] of boolean     , out Kt : auto   , inherit POfcv : array [ 6 ] of float      ) { j6 , B3 , sBv , WdH  : array [ 0 , 0 ] of string    = KdS   - P4p     :: - B      , Y   && hXI      , n   / U     :: Z   / oQ    <= ! C      , IFNB   && J     :: p   / p    >= ""       ;  if ( - R     :: ""    == F   && eno      ) return ;   else continue ;     }    """
		expect = """Program([
	FuncDecl(Re, VoidType, [], o6A, BlockStmt([VarDecl(a8VG, BooleanType, UnExpr(!, Id(Nj3))), ForStmt(AssignStmt(Id(B), BinExpr(==, BinExpr(/, Id(ISX), Id(V)), UnExpr(!, Id(Yp)))), BinExpr(::, UnExpr(-, Id(X)), BinExpr(||, Id(p), Id(c))), BinExpr(::, BinExpr(!=, BinExpr(||, Id(JTo), Id(UXbm)), BinExpr(/, Id(D), Id(g7L))), BinExpr(%, Id(u), Id(M))), ReturnStmt()), CallStmt(V, ), VarDecl(XJwC, AutoType, Id(zCN)), VarDecl(zPr, AutoType, BinExpr(&&, Id(S), Id(C))), VarDecl(a, AutoType, BinExpr(<, Id(JMyW), UnExpr(!, Id(ni)))), VarDecl(Z, AutoType, BinExpr(::, BinExpr(<=, Id(Q), BinExpr(||, Id(g), Id(s))), BinExpr(+, Id(sYq), Id(b6t)))), VarDecl(q, AutoType, BinExpr(==, StringLit(), Id(pIm))), VarDecl(i, AutoType, BinExpr(::, BinExpr(!=, UnExpr(!, Id(x)), Id(MsoSMd)), UnExpr(-, Id(Zd)))), VarDecl(r, AutoType, UnExpr(-, Id(Sq))), VarDecl(SH, AutoType, BinExpr(::, BinExpr(<=, UnExpr(-, Id(uRF)), BinExpr(/, Id(y), Id(I))), BinExpr(==, BinExpr(+, Id(TX), Id(MR)), UnExpr(!, Id(B))))), VarDecl(KvXX, AutoType, BinExpr(::, BinExpr(==, UnExpr(-, Id(x)), UnExpr(-, Id(O))), BinExpr(||, Id(K), Id(b)))), BreakStmt(), ContinueStmt(), AssignStmt(Id(cW), BinExpr(>, BinExpr(%, Id(n2Gs), Id(k)), BinExpr(&&, Id(_), Id(l)))), VarDecl(T, AutoType), VarDecl(r, AutoType)]))
	VarDecl(O, FloatType, BinExpr(!=, BinExpr(/, UnExpr(-, UnExpr(!, Id(XC))), Id(mTf)), BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(+, UnExpr(!, Id(L3)), UnExpr(-, Id(c))), Id(Mdjk)), Id(e)), BinExpr(-, Id(P), Id(n)))))
	FuncDecl(J, BooleanType, [InheritParam(J, ArrayType([0], BooleanType)), OutParam(Kt, AutoType), InheritParam(POfcv, ArrayType([6], FloatType))], None, BlockStmt([VarDecl(j6, ArrayType([0, 0], StringType), BinExpr(::, BinExpr(-, Id(KdS), Id(P4p)), UnExpr(-, Id(B)))), VarDecl(B3, ArrayType([0, 0], StringType), BinExpr(&&, Id(Y), Id(hXI))), VarDecl(sBv, ArrayType([0, 0], StringType), BinExpr(::, BinExpr(/, Id(n), Id(U)), BinExpr(<=, BinExpr(/, Id(Z), Id(oQ)), UnExpr(!, Id(C))))), VarDecl(WdH, ArrayType([0, 0], StringType), BinExpr(::, BinExpr(&&, Id(IFNB), Id(J)), BinExpr(>=, BinExpr(/, Id(p), Id(p)), StringLit()))), IfStmt(BinExpr(::, UnExpr(-, Id(R)), BinExpr(==, StringLit(), BinExpr(&&, Id(F), Id(eno)))), ReturnStmt(), ContinueStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 552))

	def test_553(self):
		input = """h , I , rL  : auto  = - - vcQ ( )        , yZ ( )     :: kEw ( )    + - lRwu     + ! O   * erv        , - p    / YV   || Wf     * t   || dH    * B   / R         ;   Y : function boolean   ( inherit O : float     ) inherit G { wf  = w   || ngi    < ! sSYN     :: NZ   || w2O    != ! H      ;   }    """
		expect = """Program([
	VarDecl(h, AutoType, UnExpr(-, UnExpr(-, FuncCall(vcQ, []))))
	VarDecl(I, AutoType, BinExpr(::, FuncCall(yZ, []), BinExpr(+, BinExpr(+, FuncCall(kEw, []), UnExpr(-, Id(lRwu))), BinExpr(*, UnExpr(!, Id(O)), Id(erv)))))
	VarDecl(rL, AutoType, BinExpr(||, BinExpr(||, BinExpr(/, UnExpr(-, Id(p)), Id(YV)), BinExpr(*, Id(Wf), Id(t))), BinExpr(/, BinExpr(*, Id(dH), Id(B)), Id(R))))
	FuncDecl(Y, BooleanType, [InheritParam(O, FloatType)], G, BlockStmt([AssignStmt(Id(wf), BinExpr(::, BinExpr(<, BinExpr(||, Id(w), Id(ngi)), UnExpr(!, Id(sSYN))), BinExpr(!=, BinExpr(||, Id(NZ), Id(w2O)), UnExpr(!, Id(H)))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 553))

	def test_554(self):
		input = """Z1Z : function string   ( ) { }    z : function void ( inherit l_ : array [ 0 ] of float     , out AW : string    , out D : auto   , M : integer    , u : auto   , inherit LDP : auto   , inherit fC : auto    ) inherit xzbxR { }    """
		expect = """Program([
	FuncDecl(Z1Z, StringType, [], None, BlockStmt([]))
	FuncDecl(z, VoidType, [InheritParam(l_, ArrayType([0], FloatType)), OutParam(AW, StringType), OutParam(D, AutoType), Param(M, IntegerType), Param(u, AutoType), InheritParam(LDP, AutoType), InheritParam(fC, AutoType)], xzbxR, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 554))

	def test_555(self):
		input = """Y1 , h , B  : array [ 0 , 0 ] of string    = f0Eu ( )    + ! Jm     < - ""    || l   / WbcO3rI        , .e-349    == CG    :: ! ! ol   + ETfK      < - ! - H        , G   + s   * n    || QF   || ab       :: - ef   + i    && U6 ( )      >= Ui ( )       ;   """
		expect = """Program([
	VarDecl(Y1, ArrayType([0, 0], StringType), BinExpr(<, BinExpr(+, FuncCall(f0Eu, []), UnExpr(!, Id(Jm))), BinExpr(||, UnExpr(-, StringLit()), BinExpr(/, Id(l), Id(WbcO3rI)))))
	VarDecl(h, ArrayType([0, 0], StringType), BinExpr(::, BinExpr(==, FloatLit(0.0), Id(CG)), BinExpr(<, BinExpr(+, UnExpr(!, UnExpr(!, Id(ol))), Id(ETfK)), UnExpr(-, UnExpr(!, UnExpr(-, Id(H)))))))
	VarDecl(B, ArrayType([0, 0], StringType), BinExpr(::, BinExpr(||, BinExpr(||, BinExpr(+, Id(G), BinExpr(*, Id(s), Id(n))), Id(QF)), Id(ab)), BinExpr(>=, BinExpr(&&, BinExpr(+, UnExpr(-, Id(ef)), Id(i)), FuncCall(U6, [])), FuncCall(Ui, []))))
])"""
		self.assertTrue(TestAST.test(input, expect, 555))

	def test_556(self):
		input = """D : function auto  ( W : array [ 0 ] of integer      ) { _UBLC , w  : string   = - e    > GA   - V      , - C    != - t     :: iNt ( )    <= - lPxi       ;  }    P : function void ( out kluz : auto   , QurCUL : string    , g : boolean     ) { f39q , F  : auto  ;  return z ( )      ;   { return ;   }   break ;   }    """
		expect = """Program([
	FuncDecl(D, AutoType, [Param(W, ArrayType([0], IntegerType))], None, BlockStmt([VarDecl(_UBLC, StringType, BinExpr(>, UnExpr(-, Id(e)), BinExpr(-, Id(GA), Id(V)))), VarDecl(w, StringType, BinExpr(::, BinExpr(!=, UnExpr(-, Id(C)), UnExpr(-, Id(t))), BinExpr(<=, FuncCall(iNt, []), UnExpr(-, Id(lPxi)))))]))
	FuncDecl(P, VoidType, [OutParam(kluz, AutoType), Param(QurCUL, StringType), Param(g, BooleanType)], None, BlockStmt([VarDecl(f39q, AutoType), VarDecl(F, AutoType), ReturnStmt(FuncCall(z, [])), BlockStmt([ReturnStmt()]), BreakStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 556))

	def test_557(self):
		input = """S7JY : function void ( out f5 : array [ 0 ] of integer     , inherit out E6w : boolean    , X : auto    ) inherit C { }    B , h , B  : float   = RF   / X    - q    / SB ( )    || iCOP   && e        , ! ! J     && HIX   / QIH       , ! ! p     / - 0      != ! a    % N   + P     && vK ( )    && O   && T       :: - x   - j     / - np    && ! T6G      != ! ! L   - ku         ;   t : function float   ( inherit ip : float     ) inherit Sg { JF ( )  ;   }    u  : auto  = nn ( )       ;   """
		expect = """Program([
	FuncDecl(S7JY, VoidType, [OutParam(f5, ArrayType([0], IntegerType)), InheritOutParam(E6w, BooleanType), Param(X, AutoType)], C, BlockStmt([]))
	VarDecl(B, FloatType, BinExpr(&&, BinExpr(||, BinExpr(-, BinExpr(/, Id(RF), Id(X)), BinExpr(/, Id(q), FuncCall(SB, []))), Id(iCOP)), Id(e)))
	VarDecl(h, FloatType, BinExpr(&&, UnExpr(!, UnExpr(!, Id(J))), BinExpr(/, Id(HIX), Id(QIH))))
	VarDecl(B, FloatType, BinExpr(::, BinExpr(!=, BinExpr(/, UnExpr(!, UnExpr(!, Id(p))), UnExpr(-, IntegerLit(0))), BinExpr(&&, BinExpr(&&, BinExpr(&&, BinExpr(+, BinExpr(%, UnExpr(!, Id(a)), Id(N)), Id(P)), FuncCall(vK, [])), Id(O)), Id(T))), BinExpr(!=, BinExpr(&&, BinExpr(-, UnExpr(-, Id(x)), BinExpr(/, Id(j), UnExpr(-, Id(np)))), UnExpr(!, Id(T6G))), BinExpr(-, UnExpr(!, UnExpr(!, Id(L))), Id(ku)))))
	FuncDecl(t, FloatType, [InheritParam(ip, FloatType)], Sg, BlockStmt([CallStmt(JF, )]))
	VarDecl(u, AutoType, FuncCall(nn, []))
])"""
		self.assertTrue(TestAST.test(input, expect, 557))

	def test_558(self):
		input = """Yv6 : function void ( inherit f : auto    ) inherit cU { }    m  : array [ 0 ] of string    ;   """
		expect = """Program([
	FuncDecl(Yv6, VoidType, [InheritParam(f, AutoType)], cU, BlockStmt([]))
	VarDecl(m, ArrayType([0], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 558))

	def test_559(self):
		input = """pkqI  : integer   = jU ( )    > ohz   || 8_63        ;   """
		expect = """Program([
	VarDecl(pkqI, IntegerType, BinExpr(>, FuncCall(jU, []), BinExpr(||, Id(ohz), IntegerLit(863))))
])"""
		self.assertTrue(TestAST.test(input, expect, 559))

	def test_560(self):
		input = """g  : boolean   ;   """
		expect = """Program([
	VarDecl(g, BooleanType)
])"""
		self.assertTrue(TestAST.test(input, expect, 560))

	def test_561(self):
		input = """k  : integer   ;   oo : function void ( ) { if ( UNIP7fe    :: m   && N6EPEuI    >= Ws   + mu      ) break ;     if ( m   && EiXfD    > ! P      ) continue ;   else return ;     k_8Pa  : auto  ;  A , k  : integer   = k   || n9V      , UMfE   / s    >= _r   || B     :: p   + EJa    != hbWk      ;  DJ  = zs   + i2AK    == R3   - yg     :: ! K    >= v   * KC      ;   }    mM : function auto  ( ) { }    I , W5p , X , p  : auto  ;   o  : auto  = - w   - x    || ! Kjnr5         ;   """
		expect = """Program([
	VarDecl(k, IntegerType)
	FuncDecl(oo, VoidType, [], None, BlockStmt([IfStmt(BinExpr(::, Id(UNIP7fe), BinExpr(>=, BinExpr(&&, Id(m), Id(N6EPEuI)), BinExpr(+, Id(Ws), Id(mu)))), BreakStmt()), IfStmt(BinExpr(>, BinExpr(&&, Id(m), Id(EiXfD)), UnExpr(!, Id(P))), ContinueStmt(), ReturnStmt()), VarDecl(k_8Pa, AutoType), VarDecl(A, IntegerType, BinExpr(||, Id(k), Id(n9V))), VarDecl(k, IntegerType, BinExpr(::, BinExpr(>=, BinExpr(/, Id(UMfE), Id(s)), BinExpr(||, Id(_r), Id(B))), BinExpr(!=, BinExpr(+, Id(p), Id(EJa)), Id(hbWk)))), AssignStmt(Id(DJ), BinExpr(::, BinExpr(==, BinExpr(+, Id(zs), Id(i2AK)), BinExpr(-, Id(R3), Id(yg))), BinExpr(>=, UnExpr(!, Id(K)), BinExpr(*, Id(v), Id(KC)))))]))
	FuncDecl(mM, AutoType, [], None, BlockStmt([]))
	VarDecl(I, AutoType)
	VarDecl(W5p, AutoType)
	VarDecl(X, AutoType)
	VarDecl(p, AutoType)
	VarDecl(o, AutoType, BinExpr(||, BinExpr(-, UnExpr(-, Id(w)), Id(x)), UnExpr(!, Id(Kjnr5))))
])"""
		self.assertTrue(TestAST.test(input, expect, 561))

	def test_562(self):
		input = """g  : array [ 2188279_094_51_5_45_7_801589 , 0 ] of integer    = ! P    - 3     % m7 ( )        ;   """
		expect = """Program([
	VarDecl(g, ArrayType([2188279094515457801589, 0], IntegerType), BinExpr(-, UnExpr(!, Id(P)), BinExpr(%, IntegerLit(3), FuncCall(m7, []))))
])"""
		self.assertTrue(TestAST.test(input, expect, 562))

	def test_563(self):
		input = """o  : string   ;   oD : function void ( ) inherit R { }    zY : function auto  ( inherit out Gk : float    , inherit s0 : auto    ) { Ue , b , Cm  : auto  ;  do { }  while ( JW   - fKovf    > - YMB     :: C ( )    <= S   * ZKH      ) ;   tAB , sB  : float   ;  a , Rb  : array [ 0 ] of float    = - n     :: - w    > ! h21C      , ""       ;  _  : string   ;  { }   while ( v   + nwD     :: u   || r      ) return ;     z , b8 , c  : auto  ;  }    """
		expect = """Program([
	VarDecl(o, StringType)
	FuncDecl(oD, VoidType, [], R, BlockStmt([]))
	FuncDecl(zY, AutoType, [InheritOutParam(Gk, FloatType), InheritParam(s0, AutoType)], None, BlockStmt([VarDecl(Ue, AutoType), VarDecl(b, AutoType), VarDecl(Cm, AutoType), DoWhileStmt(BinExpr(::, BinExpr(>, BinExpr(-, Id(JW), Id(fKovf)), UnExpr(-, Id(YMB))), BinExpr(<=, FuncCall(C, []), BinExpr(*, Id(S), Id(ZKH)))), BlockStmt([])), VarDecl(tAB, FloatType), VarDecl(sB, FloatType), VarDecl(a, ArrayType([0], FloatType), BinExpr(::, UnExpr(-, Id(n)), BinExpr(>, UnExpr(-, Id(w)), UnExpr(!, Id(h21C))))), VarDecl(Rb, ArrayType([0], FloatType), StringLit()), VarDecl(_, StringType), BlockStmt([]), WhileStmt(BinExpr(::, BinExpr(+, Id(v), Id(nwD)), BinExpr(||, Id(u), Id(r))), ReturnStmt()), VarDecl(z, AutoType), VarDecl(b8, AutoType), VarDecl(c, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 563))

	def test_564(self):
		input = """Q : function void ( out q : string     ) { break ;   XV6 , m , SNbA  : array [ 0 ] of float    = C    :: U ( )    >= U   + e531      , D   * dekmq    == - MK      , CA   * zQ6       ;  B  : float   ;  }    KU : function void ( ) { hnxj  : string   ;  }    """
		expect = """Program([
	FuncDecl(Q, VoidType, [OutParam(q, StringType)], None, BlockStmt([BreakStmt(), VarDecl(XV6, ArrayType([0], FloatType), BinExpr(::, Id(C), BinExpr(>=, FuncCall(U, []), BinExpr(+, Id(U), Id(e531))))), VarDecl(m, ArrayType([0], FloatType), BinExpr(==, BinExpr(*, Id(D), Id(dekmq)), UnExpr(-, Id(MK)))), VarDecl(SNbA, ArrayType([0], FloatType), BinExpr(*, Id(CA), Id(zQ6))), VarDecl(B, FloatType)]))
	FuncDecl(KU, VoidType, [], None, BlockStmt([VarDecl(hnxj, StringType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 564))

	def test_565(self):
		input = """N : function string   ( B : auto    ) inherit w { lNq  : string   = yZ   % e       ;  }    RhXON : function void ( P : auto   , out Oi : float    , inherit lnDj7E : integer    , inherit La : array [ 2 , 0 ] of boolean      ) { }    JZEqJ  : auto  = ! ! I79     * ! AVS ( )      < - ne    + - l     || S     :: ! bA   * ! m         ;   """
		expect = """Program([
	FuncDecl(N, StringType, [Param(B, AutoType)], w, BlockStmt([VarDecl(lNq, StringType, BinExpr(%, Id(yZ), Id(e)))]))
	FuncDecl(RhXON, VoidType, [Param(P, AutoType), OutParam(Oi, FloatType), InheritParam(lnDj7E, IntegerType), InheritParam(La, ArrayType([2, 0], BooleanType))], None, BlockStmt([]))
	VarDecl(JZEqJ, AutoType, BinExpr(::, BinExpr(<, BinExpr(*, UnExpr(!, UnExpr(!, Id(I79))), UnExpr(!, FuncCall(AVS, []))), BinExpr(||, BinExpr(+, UnExpr(-, Id(ne)), UnExpr(-, Id(l))), Id(S))), BinExpr(*, UnExpr(!, Id(bA)), UnExpr(!, Id(m)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 565))

	def test_566(self):
		input = """vH : function auto  ( out Bc : auto   , inherit WL : auto    ) inherit ccOF { }    p9Z7  : auto  ;   A : function void ( inherit dp : auto    ) inherit wA { n ( )  ;   u , si5I , C , X , u , B , ke , c , V , tQ  : boolean   = COd   / w    >= zN   - Q5Gw      , X   || G     :: cU   / P      , ""    >= L   % q      , FW7   && I    >= - a7m     :: pci   != A   && lW      , - V    <= S    :: yt   && O    == ! z8DX      , u   - E     :: ! a3mjLaoQap      , Kb   + j    < x6   + J     :: - Q0t0      , ""    > c3   + S6wKk      , uSXl   - k    < - M1      , ! Fu    == - k       ;  break ;   }    MhwJx : function void ( ) inherit ee { uX , O  : auto  ;  for ( M  = d   || n    < ! f      , v_90   / fK      , ! Z    == JSR   + r     :: ! v    < K     ) { GVm4oG ( )  ;   Ft , sv  : auto  ;  P2SZd  : integer   ;  o1 , E , SNw , L  : boolean   ;  LQCtB  : float   ;  }     Bu , V11 , fDA7  : auto  = mKpju   / rqb      , - LT     :: Vm     , - vVyB    < - sR     :: h3   * VW       ;  do { _i  : array [ 0 , 0 ] of boolean    ;  return ;   { mH , Ozy , n , K , RETa_Zm  : auto  ;  }   }  while ( WM   + ad    != N6LEt   / u     :: - wm      ) ;   JX  = - ig      ;   }    fH5L : function void ( out y : array [ 0 ] of integer      ) { }    xHjb : function void ( inherit out R : array [ 0 , 0 , 52028 , 0 ] of float      ) { }    B  : auto  ;   s , D , T , bQt5  : array [ 0 ] of string    ;   """
		expect = """Program([
	FuncDecl(vH, AutoType, [OutParam(Bc, AutoType), InheritParam(WL, AutoType)], ccOF, BlockStmt([]))
	VarDecl(p9Z7, AutoType)
	FuncDecl(A, VoidType, [InheritParam(dp, AutoType)], wA, BlockStmt([CallStmt(n, ), VarDecl(u, BooleanType, BinExpr(>=, BinExpr(/, Id(COd), Id(w)), BinExpr(-, Id(zN), Id(Q5Gw)))), VarDecl(si5I, BooleanType, BinExpr(::, BinExpr(||, Id(X), Id(G)), BinExpr(/, Id(cU), Id(P)))), VarDecl(C, BooleanType, BinExpr(>=, StringLit(), BinExpr(%, Id(L), Id(q)))), VarDecl(X, BooleanType, BinExpr(::, BinExpr(>=, BinExpr(&&, Id(FW7), Id(I)), UnExpr(-, Id(a7m))), BinExpr(!=, Id(pci), BinExpr(&&, Id(A), Id(lW))))), VarDecl(u, BooleanType, BinExpr(::, BinExpr(<=, UnExpr(-, Id(V)), Id(S)), BinExpr(==, BinExpr(&&, Id(yt), Id(O)), UnExpr(!, Id(z8DX))))), VarDecl(B, BooleanType, BinExpr(::, BinExpr(-, Id(u), Id(E)), UnExpr(!, Id(a3mjLaoQap)))), VarDecl(ke, BooleanType, BinExpr(::, BinExpr(<, BinExpr(+, Id(Kb), Id(j)), BinExpr(+, Id(x6), Id(J))), UnExpr(-, Id(Q0t0)))), VarDecl(c, BooleanType, BinExpr(>, StringLit(), BinExpr(+, Id(c3), Id(S6wKk)))), VarDecl(V, BooleanType, BinExpr(<, BinExpr(-, Id(uSXl), Id(k)), UnExpr(-, Id(M1)))), VarDecl(tQ, BooleanType, BinExpr(==, UnExpr(!, Id(Fu)), UnExpr(-, Id(k)))), BreakStmt()]))
	FuncDecl(MhwJx, VoidType, [], ee, BlockStmt([VarDecl(uX, AutoType), VarDecl(O, AutoType), ForStmt(AssignStmt(Id(M), BinExpr(<, BinExpr(||, Id(d), Id(n)), UnExpr(!, Id(f)))), BinExpr(/, Id(v_90), Id(fK)), BinExpr(::, BinExpr(==, UnExpr(!, Id(Z)), BinExpr(+, Id(JSR), Id(r))), BinExpr(<, UnExpr(!, Id(v)), Id(K))), BlockStmt([CallStmt(GVm4oG, ), VarDecl(Ft, AutoType), VarDecl(sv, AutoType), VarDecl(P2SZd, IntegerType), VarDecl(o1, BooleanType), VarDecl(E, BooleanType), VarDecl(SNw, BooleanType), VarDecl(L, BooleanType), VarDecl(LQCtB, FloatType)])), VarDecl(Bu, AutoType, BinExpr(/, Id(mKpju), Id(rqb))), VarDecl(V11, AutoType, BinExpr(::, UnExpr(-, Id(LT)), Id(Vm))), VarDecl(fDA7, AutoType, BinExpr(::, BinExpr(<, UnExpr(-, Id(vVyB)), UnExpr(-, Id(sR))), BinExpr(*, Id(h3), Id(VW)))), DoWhileStmt(BinExpr(::, BinExpr(!=, BinExpr(+, Id(WM), Id(ad)), BinExpr(/, Id(N6LEt), Id(u))), UnExpr(-, Id(wm))), BlockStmt([VarDecl(_i, ArrayType([0, 0], BooleanType)), ReturnStmt(), BlockStmt([VarDecl(mH, AutoType), VarDecl(Ozy, AutoType), VarDecl(n, AutoType), VarDecl(K, AutoType), VarDecl(RETa_Zm, AutoType)])])), AssignStmt(Id(JX), UnExpr(-, Id(ig)))]))
	FuncDecl(fH5L, VoidType, [OutParam(y, ArrayType([0], IntegerType))], None, BlockStmt([]))
	FuncDecl(xHjb, VoidType, [InheritOutParam(R, ArrayType([0, 0, 52028, 0], FloatType))], None, BlockStmt([]))
	VarDecl(B, AutoType)
	VarDecl(s, ArrayType([0], StringType))
	VarDecl(D, ArrayType([0], StringType))
	VarDecl(T, ArrayType([0], StringType))
	VarDecl(bQt5, ArrayType([0], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 566))

	def test_567(self):
		input = """tIi  : float   = ! dGf ( )     / - h   && U      == Jo ( )     :: ! g   % m    % U0F   + u      == ! - ! g         ;   UZ : function array [ 8319260 ] of float    ( ) { while ( 5    >= f   / bHa8     :: q   * vG      ) break ;     }    """
		expect = """Program([
	VarDecl(tIi, FloatType, BinExpr(::, BinExpr(==, BinExpr(&&, BinExpr(/, UnExpr(!, FuncCall(dGf, [])), UnExpr(-, Id(h))), Id(U)), FuncCall(Jo, [])), BinExpr(==, BinExpr(+, BinExpr(%, BinExpr(%, UnExpr(!, Id(g)), Id(m)), Id(U0F)), Id(u)), UnExpr(!, UnExpr(-, UnExpr(!, Id(g)))))))
	FuncDecl(UZ, ArrayType([8319260], FloatType), [], None, BlockStmt([WhileStmt(BinExpr(::, BinExpr(>=, IntegerLit(5), BinExpr(/, Id(f), Id(bHa8))), BinExpr(*, Id(q), Id(vG))), BreakStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 567))

	def test_568(self):
		input = """UJ  : integer   ;   F : function void ( out jokq : string     ) inherit s3lh { }    """
		expect = """Program([
	VarDecl(UJ, IntegerType)
	FuncDecl(F, VoidType, [OutParam(jokq, StringType)], s3lh, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 568))

	def test_569(self):
		input = """k : function void ( F : array [ 0 ] of string      ) inherit tx { }    """
		expect = """Program([
	FuncDecl(k, VoidType, [Param(F, ArrayType([0], StringType))], tx, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 569))

	def test_570(self):
		input = """dq  : array [ 591 ] of float    ;   _j : function void ( ) { Af4k7 , D  : array [ 2497 ] of integer    ;  }    z , E6 , dD , t  : boolean   = - r0R   && m    / Hy   * nZ      >= - P ( )      :: ! - W     > lAn ( )      , ! _   / _     + ! bS    - H   - m      > w   / K     :: - f0    / - d     - nF   % O    * N   * e      >= Zva   - - PG   * mZv        , ! _A   / lM    / ""      >= e ( )    % ! ! zG        , ! bsC ( )        ;   E4 : function integer   ( inherit R : array [ 801 , 0 , 4_1 ] of float      ) { }    """
		expect = """Program([
	VarDecl(dq, ArrayType([591], FloatType))
	FuncDecl(_j, VoidType, [], None, BlockStmt([VarDecl(Af4k7, ArrayType([2497], IntegerType)), VarDecl(D, ArrayType([2497], IntegerType))]))
	VarDecl(z, BooleanType, BinExpr(::, BinExpr(>=, BinExpr(&&, UnExpr(-, Id(r0R)), BinExpr(*, BinExpr(/, Id(m), Id(Hy)), Id(nZ))), UnExpr(-, FuncCall(P, []))), BinExpr(>, UnExpr(!, UnExpr(-, Id(W))), FuncCall(lAn, []))))
	VarDecl(E6, BooleanType, BinExpr(::, BinExpr(>, BinExpr(-, BinExpr(-, BinExpr(+, BinExpr(/, UnExpr(!, Id(_)), Id(_)), UnExpr(!, Id(bS))), Id(H)), Id(m)), BinExpr(/, Id(w), Id(K))), BinExpr(>=, BinExpr(-, BinExpr(/, UnExpr(-, Id(f0)), UnExpr(-, Id(d))), BinExpr(*, BinExpr(*, BinExpr(%, Id(nF), Id(O)), Id(N)), Id(e))), BinExpr(-, Id(Zva), BinExpr(*, UnExpr(-, Id(PG)), Id(mZv))))))
	VarDecl(dD, BooleanType, BinExpr(>=, BinExpr(/, BinExpr(/, UnExpr(!, Id(_A)), Id(lM)), StringLit()), BinExpr(%, FuncCall(e, []), UnExpr(!, UnExpr(!, Id(zG))))))
	VarDecl(t, BooleanType, UnExpr(!, FuncCall(bsC, [])))
	FuncDecl(E4, IntegerType, [InheritParam(R, ArrayType([801, 0, 41], FloatType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 570))

	def test_571(self):
		input = """kZ : function void ( inherit out vb : array [ 5_49_6_40_0 ] of boolean     , e_ : auto    ) { d  : integer   = k   % F    < s   / R6     :: YLyC_I   - H9       ;  while ( T   - j     :: ! i6N      ) break ;     l ( )  ;   }    """
		expect = """Program([
	FuncDecl(kZ, VoidType, [InheritOutParam(vb, ArrayType([5496400], BooleanType)), Param(e_, AutoType)], None, BlockStmt([VarDecl(d, IntegerType, BinExpr(::, BinExpr(<, BinExpr(%, Id(k), Id(F)), BinExpr(/, Id(s), Id(R6))), BinExpr(-, Id(YLyC_I), Id(H9)))), WhileStmt(BinExpr(::, BinExpr(-, Id(T), Id(j)), UnExpr(!, Id(i6N))), BreakStmt()), CallStmt(l, )]))
])"""
		self.assertTrue(TestAST.test(input, expect, 571))

	def test_572(self):
		input = """sE : function auto  ( out p_1 : integer     ) inherit f { ZKTr , xjM , d , GS , N9  : array [ 0 , 0 , 0 , 0 ] of integer    = ! X      , ! Fpr    == 2     :: - zZN      , y   % KEvp     :: - V      , o   || p     :: K   || e      , V   * F     :: ! m       ;  h  : integer   ;  }    """
		expect = """Program([
	FuncDecl(sE, AutoType, [OutParam(p_1, IntegerType)], f, BlockStmt([VarDecl(ZKTr, ArrayType([0, 0, 0, 0], IntegerType), UnExpr(!, Id(X))), VarDecl(xjM, ArrayType([0, 0, 0, 0], IntegerType), BinExpr(::, BinExpr(==, UnExpr(!, Id(Fpr)), IntegerLit(2)), UnExpr(-, Id(zZN)))), VarDecl(d, ArrayType([0, 0, 0, 0], IntegerType), BinExpr(::, BinExpr(%, Id(y), Id(KEvp)), UnExpr(-, Id(V)))), VarDecl(GS, ArrayType([0, 0, 0, 0], IntegerType), BinExpr(::, BinExpr(||, Id(o), Id(p)), BinExpr(||, Id(K), Id(e)))), VarDecl(N9, ArrayType([0, 0, 0, 0], IntegerType), BinExpr(::, BinExpr(*, Id(V), Id(F)), UnExpr(!, Id(m)))), VarDecl(h, IntegerType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 572))

	def test_573(self):
		input = """bE , m  : float   = ! - H     >= oW3   || r    + B   + Q     % ! WHgJK   && A       :: - - W     - - d    - 9      == ! - ""        , - nhsz0   % MDsl4    && g6Rc   * X       :: - A   / F     - - att     <= - B    - dg   - l     + T   && Y    && ! s         ;   n , XUt , h  : array [ 5 , 98 , 0 ] of boolean    ;   """
		expect = """Program([
	VarDecl(bE, FloatType, BinExpr(::, BinExpr(>=, UnExpr(!, UnExpr(-, Id(H))), BinExpr(&&, BinExpr(||, Id(oW3), BinExpr(+, BinExpr(+, Id(r), Id(B)), BinExpr(%, Id(Q), UnExpr(!, Id(WHgJK))))), Id(A))), BinExpr(==, BinExpr(-, BinExpr(-, UnExpr(-, UnExpr(-, Id(W))), UnExpr(-, Id(d))), IntegerLit(9)), UnExpr(!, UnExpr(-, StringLit())))))
	VarDecl(m, FloatType, BinExpr(::, BinExpr(&&, BinExpr(%, UnExpr(-, Id(nhsz0)), Id(MDsl4)), BinExpr(*, Id(g6Rc), Id(X))), BinExpr(<=, BinExpr(-, BinExpr(/, UnExpr(-, Id(A)), Id(F)), UnExpr(-, Id(att))), BinExpr(&&, BinExpr(&&, BinExpr(+, BinExpr(-, BinExpr(-, UnExpr(-, Id(B)), Id(dg)), Id(l)), Id(T)), Id(Y)), UnExpr(!, Id(s))))))
	VarDecl(n, ArrayType([5, 98, 0], BooleanType))
	VarDecl(XUt, ArrayType([5, 98, 0], BooleanType))
	VarDecl(h, ArrayType([5, 98, 0], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 573))

	def test_574(self):
		input = """J : function array [ 0 , 4 , 0 ] of float    ( ) inherit ZXj { N , JzC , Oy  : auto  = E   - dYSMC     :: e   - Bf      , g     , ! lN    <= ""     :: V   / J       ;  }    G , R , Y , NO  : array [ 0 , 734728 , 57380760_31 ] of boolean    = ! s     :: ! ""     / n   || G    + Dq3uK   % klr      < ! - io    || y       , ! 0     % _   % H    + b   || hl      < - fb   || bi     + e      , LN   || ! RC   || Z       :: ! f   % rgz     + ow ( )     != - ! Xfw    && ! S        , Tswsy ( )    / ! cm   - U      < V      ;   """
		expect = """Program([
	FuncDecl(J, ArrayType([0, 4, 0], FloatType), [], ZXj, BlockStmt([VarDecl(N, AutoType, BinExpr(::, BinExpr(-, Id(E), Id(dYSMC)), BinExpr(-, Id(e), Id(Bf)))), VarDecl(JzC, AutoType, Id(g)), VarDecl(Oy, AutoType, BinExpr(::, BinExpr(<=, UnExpr(!, Id(lN)), StringLit()), BinExpr(/, Id(V), Id(J))))]))
	VarDecl(G, ArrayType([0, 734728, 5738076031], BooleanType), BinExpr(::, UnExpr(!, Id(s)), BinExpr(<, BinExpr(||, BinExpr(/, UnExpr(!, StringLit()), Id(n)), BinExpr(+, Id(G), BinExpr(%, Id(Dq3uK), Id(klr)))), BinExpr(||, UnExpr(!, UnExpr(-, Id(io))), Id(y)))))
	VarDecl(R, ArrayType([0, 734728, 5738076031], BooleanType), BinExpr(<, BinExpr(||, BinExpr(+, BinExpr(%, BinExpr(%, UnExpr(!, IntegerLit(0)), Id(_)), Id(H)), Id(b)), Id(hl)), BinExpr(||, UnExpr(-, Id(fb)), BinExpr(+, Id(bi), Id(e)))))
	VarDecl(Y, ArrayType([0, 734728, 5738076031], BooleanType), BinExpr(::, BinExpr(||, BinExpr(||, Id(LN), UnExpr(!, Id(RC))), Id(Z)), BinExpr(!=, BinExpr(+, BinExpr(%, UnExpr(!, Id(f)), Id(rgz)), FuncCall(ow, [])), BinExpr(&&, UnExpr(-, UnExpr(!, Id(Xfw))), UnExpr(!, Id(S))))))
	VarDecl(NO, ArrayType([0, 734728, 5738076031], BooleanType), BinExpr(<, BinExpr(-, BinExpr(/, FuncCall(Tswsy, []), UnExpr(!, Id(cm))), Id(U)), Id(V)))
])"""
		self.assertTrue(TestAST.test(input, expect, 574))

	def test_575(self):
		input = """s : function void ( out bU : array [ 0 ] of integer      ) { }    U : function array [ 0 ] of string    ( inherit qVA : array [ 0 , 0 ] of float     , inherit out G : float     ) inherit q { }    """
		expect = """Program([
	FuncDecl(s, VoidType, [OutParam(bU, ArrayType([0], IntegerType))], None, BlockStmt([]))
	FuncDecl(U, ArrayType([0], StringType), [InheritParam(qVA, ArrayType([0, 0], FloatType)), InheritOutParam(G, FloatType)], q, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 575))

	def test_576(self):
		input = """I : function void ( ) { continue ;   }    vXH : function array [ 0 ] of boolean    ( ) { }    """
		expect = """Program([
	FuncDecl(I, VoidType, [], None, BlockStmt([ContinueStmt()]))
	FuncDecl(vXH, ArrayType([0], BooleanType), [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 576))

	def test_577(self):
		input = """h , K4e  : string   = ! ! z   || XKnj       :: ! ! XX2     + ! I    || c   || Bc      == z   / IP    * sAB   / l3     && - Qj   - m        , H    :: MD   && x1Q    - N    && - i    && - u      >= ! a    % Jh   * Kck     / TA   - uAZYrOQ    && l6   + OOt         ;   FA : function array [ 0 , 5 ] of string    ( ) inherit Yc8Ylf { }    tmg87 : function auto  ( out mOg : auto    ) inherit kld2 { R , O4r  : array [ 0 ] of string    ;  continue ;   }    mN : function boolean   ( inherit out a : array [ 2_0 ] of boolean     , L : auto    ) inherit ug { break ;   while ( UTQi   * O     :: 9      ) continue ;     }    _K  : auto  ;   K : function boolean   ( out X : integer     ) { continue ;   continue ;   }    """
		expect = """Program([
	VarDecl(h, StringType, BinExpr(::, BinExpr(||, UnExpr(!, UnExpr(!, Id(z))), Id(XKnj)), BinExpr(==, BinExpr(||, BinExpr(||, BinExpr(+, UnExpr(!, UnExpr(!, Id(XX2))), UnExpr(!, Id(I))), Id(c)), Id(Bc)), BinExpr(&&, BinExpr(/, BinExpr(*, BinExpr(/, Id(z), Id(IP)), Id(sAB)), Id(l3)), BinExpr(-, UnExpr(-, Id(Qj)), Id(m))))))
	VarDecl(K4e, StringType, BinExpr(::, Id(H), BinExpr(>=, BinExpr(&&, BinExpr(&&, BinExpr(&&, Id(MD), BinExpr(-, Id(x1Q), Id(N))), UnExpr(-, Id(i))), UnExpr(-, Id(u))), BinExpr(&&, BinExpr(-, BinExpr(/, BinExpr(*, BinExpr(%, UnExpr(!, Id(a)), Id(Jh)), Id(Kck)), Id(TA)), Id(uAZYrOQ)), BinExpr(+, Id(l6), Id(OOt))))))
	FuncDecl(FA, ArrayType([0, 5], StringType), [], Yc8Ylf, BlockStmt([]))
	FuncDecl(tmg87, AutoType, [OutParam(mOg, AutoType)], kld2, BlockStmt([VarDecl(R, ArrayType([0], StringType)), VarDecl(O4r, ArrayType([0], StringType)), ContinueStmt()]))
	FuncDecl(mN, BooleanType, [InheritOutParam(a, ArrayType([20], BooleanType)), Param(L, AutoType)], ug, BlockStmt([BreakStmt(), WhileStmt(BinExpr(::, BinExpr(*, Id(UTQi), Id(O)), IntegerLit(9)), ContinueStmt())]))
	VarDecl(_K, AutoType)
	FuncDecl(K, BooleanType, [OutParam(X, IntegerType)], None, BlockStmt([ContinueStmt(), ContinueStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 577))

	def test_578(self):
		input = """f0 : function array [ 0 ] of float    ( r : auto    ) inherit I5d { }    """
		expect = """Program([
	FuncDecl(f0, ArrayType([0], FloatType), [Param(r, AutoType)], I5d, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 578))

	def test_579(self):
		input = """F  : auto  = ""       ;   """
		expect = """Program([
	VarDecl(F, AutoType, StringLit())
])"""
		self.assertTrue(TestAST.test(input, expect, 579))

	def test_580(self):
		input = """rhDN : function void ( ) { v  : boolean   ;  if ( v    :: - zkcYVU      ) k ( )  ;     Vs  : auto  = u   && O       ;  return ;   }    jdy , MAw5J , K , CkS , b  : auto  ;   Wk  : auto  ;   """
		expect = """Program([
	FuncDecl(rhDN, VoidType, [], None, BlockStmt([VarDecl(v, BooleanType), IfStmt(BinExpr(::, Id(v), UnExpr(-, Id(zkcYVU))), CallStmt(k, )), VarDecl(Vs, AutoType, BinExpr(&&, Id(u), Id(O))), ReturnStmt()]))
	VarDecl(jdy, AutoType)
	VarDecl(MAw5J, AutoType)
	VarDecl(K, AutoType)
	VarDecl(CkS, AutoType)
	VarDecl(b, AutoType)
	VarDecl(Wk, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 580))

	def test_581(self):
		input = """x : function void ( ) inherit DNd { }    L : function auto  ( out g8 : boolean     ) { }    """
		expect = """Program([
	FuncDecl(x, VoidType, [], DNd, BlockStmt([]))
	FuncDecl(L, AutoType, [OutParam(g8, BooleanType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 581))

	def test_582(self):
		input = """x : function void ( ) { AV  : auto  = Q   / x    <= S      ;  X , k , P  : auto  = fe   - t    < - L     :: U   || B    == ! j      , I   * gQ     :: - mH      , ! N     :: h   || Y    <= - p       ;  while ( ! _      ) continue ;     hY  : auto  ;  N , Z  : auto  ;  rqu , T , Az  : boolean   ;  r , m  : auto  = O   - VH     :: - A    < - t      , ! XNj       ;  }    """
		expect = """Program([
	FuncDecl(x, VoidType, [], None, BlockStmt([VarDecl(AV, AutoType, BinExpr(<=, BinExpr(/, Id(Q), Id(x)), Id(S))), VarDecl(X, AutoType, BinExpr(::, BinExpr(<, BinExpr(-, Id(fe), Id(t)), UnExpr(-, Id(L))), BinExpr(==, BinExpr(||, Id(U), Id(B)), UnExpr(!, Id(j))))), VarDecl(k, AutoType, BinExpr(::, BinExpr(*, Id(I), Id(gQ)), UnExpr(-, Id(mH)))), VarDecl(P, AutoType, BinExpr(::, UnExpr(!, Id(N)), BinExpr(<=, BinExpr(||, Id(h), Id(Y)), UnExpr(-, Id(p))))), WhileStmt(UnExpr(!, Id(_)), ContinueStmt()), VarDecl(hY, AutoType), VarDecl(N, AutoType), VarDecl(Z, AutoType), VarDecl(rqu, BooleanType), VarDecl(T, BooleanType), VarDecl(Az, BooleanType), VarDecl(r, AutoType, BinExpr(::, BinExpr(-, Id(O), Id(VH)), BinExpr(<, UnExpr(-, Id(A)), UnExpr(-, Id(t))))), VarDecl(m, AutoType, UnExpr(!, Id(XNj)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 582))

	def test_583(self):
		input = """E : function array [ 0 , 990 ] of float    ( ) { }    y : function auto  ( inherit k : auto    ) inherit BeU { }    Bgo  : array [ 0 ] of float    ;   """
		expect = """Program([
	FuncDecl(E, ArrayType([0, 990], FloatType), [], None, BlockStmt([]))
	FuncDecl(y, AutoType, [InheritParam(k, AutoType)], BeU, BlockStmt([]))
	VarDecl(Bgo, ArrayType([0], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 583))

	def test_584(self):
		input = """U  : array [ 0 , 791 ] of boolean    ;   """
		expect = """Program([
	VarDecl(U, ArrayType([0, 791], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 584))

	def test_585(self):
		input = """QG : function void ( inherit i : boolean     ) inherit kR { }    """
		expect = """Program([
	FuncDecl(QG, VoidType, [InheritParam(i, BooleanType)], kR, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 585))

	def test_586(self):
		input = """s  : auto  ;   """
		expect = """Program([
	VarDecl(s, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 586))

	def test_587(self):
		input = """_4 : function array [ 0 ] of string    ( ) { }    H : function auto  ( inherit out G : float     ) inherit V { }    """
		expect = """Program([
	FuncDecl(_4, ArrayType([0], StringType), [], None, BlockStmt([]))
	FuncDecl(H, AutoType, [InheritOutParam(G, FloatType)], V, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 587))

	def test_588(self):
		input = """R : function auto  ( inherit A : auto   , inherit out d : auto    ) { }    N  : boolean   = 52_1       ;   Ky8  : array [ 0 ] of integer    = 14_19    == o ( )    * - tFA     + Jo   && Y    - ixQ   || Z         ;   KxyaS : function array [ 0 ] of boolean    ( ) inherit T { continue ;   }    gb  : integer   ;   """
		expect = """Program([
	FuncDecl(R, AutoType, [InheritParam(A, AutoType), InheritOutParam(d, AutoType)], None, BlockStmt([]))
	VarDecl(N, BooleanType, IntegerLit(521))
	VarDecl(Ky8, ArrayType([0], IntegerType), BinExpr(==, IntegerLit(1419), BinExpr(||, BinExpr(&&, BinExpr(+, BinExpr(*, FuncCall(o, []), UnExpr(-, Id(tFA))), Id(Jo)), BinExpr(-, Id(Y), Id(ixQ))), Id(Z))))
	FuncDecl(KxyaS, ArrayType([0], BooleanType), [], T, BlockStmt([ContinueStmt()]))
	VarDecl(gb, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 588))

	def test_589(self):
		input = """g : function array [ 6_3_4 , 4 ] of string    ( ) inherit wt { Rs , OhJi , P  : array [ 0 , 0 ] of string    ;  }    VA  : float   ;   p2x : function void ( inherit EFV : auto    ) inherit v { }    """
		expect = """Program([
	FuncDecl(g, ArrayType([634, 4], StringType), [], wt, BlockStmt([VarDecl(Rs, ArrayType([0, 0], StringType)), VarDecl(OhJi, ArrayType([0, 0], StringType)), VarDecl(P, ArrayType([0, 0], StringType))]))
	VarDecl(VA, FloatType)
	FuncDecl(p2x, VoidType, [InheritParam(EFV, AutoType)], v, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 589))

	def test_590(self):
		input = """xFK : function void ( ) inherit Z { jtjD  : string   = ! Z    < n   % G       ;  { }   S  = ! V     :: Wh   - nK7    <= WW   || WMIs      ;   m  : float   ;  { }   }    """
		expect = """Program([
	FuncDecl(xFK, VoidType, [], Z, BlockStmt([VarDecl(jtjD, StringType, BinExpr(<, UnExpr(!, Id(Z)), BinExpr(%, Id(n), Id(G)))), BlockStmt([]), AssignStmt(Id(S), BinExpr(::, UnExpr(!, Id(V)), BinExpr(<=, BinExpr(-, Id(Wh), Id(nK7)), BinExpr(||, Id(WW), Id(WMIs))))), VarDecl(m, FloatType), BlockStmt([])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 590))

	def test_591(self):
		input = """G , X  : array [ 0 , 0 , 0 , 0 , 8_328_6789 , 0 , 0 , 0 , 0 , 0 , 4_3 , 9_66 ] of integer    ;   wWJM : function float   ( out dx7d : float    , pZK : array [ 0 ] of string     , inherit M_4QzVkQV : auto    ) inherit h { XoV , C  : float   = XEu   * C     :: ! _      , ! lz       ;  mT5b7L5 , pdoCvm  : auto  ;  }    nF : function integer   ( out o : float    , out T4 : array [ 0 , 4_3_4820 ] of boolean     , out D : auto    ) inherit aqx { }    h : function array [ 7 ] of integer    ( ) inherit ETM { }    """
		expect = """Program([
	VarDecl(G, ArrayType([0, 0, 0, 0, 83286789, 0, 0, 0, 0, 0, 43, 966], IntegerType))
	VarDecl(X, ArrayType([0, 0, 0, 0, 83286789, 0, 0, 0, 0, 0, 43, 966], IntegerType))
	FuncDecl(wWJM, FloatType, [OutParam(dx7d, FloatType), Param(pZK, ArrayType([0], StringType)), InheritParam(M_4QzVkQV, AutoType)], h, BlockStmt([VarDecl(XoV, FloatType, BinExpr(::, BinExpr(*, Id(XEu), Id(C)), UnExpr(!, Id(_)))), VarDecl(C, FloatType, UnExpr(!, Id(lz))), VarDecl(mT5b7L5, AutoType), VarDecl(pdoCvm, AutoType)]))
	FuncDecl(nF, IntegerType, [OutParam(o, FloatType), OutParam(T4, ArrayType([0, 434820], BooleanType)), OutParam(D, AutoType)], aqx, BlockStmt([]))
	FuncDecl(h, ArrayType([7], IntegerType), [], ETM, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 591))

	def test_592(self):
		input = """X  : auto  = - X   || FLrUf27T7     - E ( )     != ! T   && XgF     - e   || hy    + - t8       :: ! fAb    || zQ   + R     - - - PW         ;   """
		expect = """Program([
	VarDecl(X, AutoType, BinExpr(::, BinExpr(!=, BinExpr(||, UnExpr(-, Id(X)), BinExpr(-, Id(FLrUf27T7), FuncCall(E, []))), BinExpr(||, BinExpr(&&, UnExpr(!, Id(T)), BinExpr(-, Id(XgF), Id(e))), BinExpr(+, Id(hy), UnExpr(-, Id(t8))))), BinExpr(||, UnExpr(!, Id(fAb)), BinExpr(-, BinExpr(+, Id(zQ), Id(R)), UnExpr(-, UnExpr(-, Id(PW)))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 592))

	def test_593(self):
		input = """kc , b02 , D , AfYnt , mH4 , r0  : integer   ;   """
		expect = """Program([
	VarDecl(kc, IntegerType)
	VarDecl(b02, IntegerType)
	VarDecl(D, IntegerType)
	VarDecl(AfYnt, IntegerType)
	VarDecl(mH4, IntegerType)
	VarDecl(r0, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 593))

	def test_594(self):
		input = """YB : function void ( fac5 : auto    ) { }    """
		expect = """Program([
	FuncDecl(YB, VoidType, [Param(fac5, AutoType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 594))

	def test_595(self):
		input = """q  : boolean   ;   YMEE0Sx , cB  : integer   = J   || O    % - FQrmSqV     || E1gZ   % X4eZO    || ! Z        , kM6f    :: - j ( )    && ! G         ;   """
		expect = """Program([
	VarDecl(q, BooleanType)
	VarDecl(YMEE0Sx, IntegerType, BinExpr(||, BinExpr(||, BinExpr(||, Id(J), BinExpr(%, Id(O), UnExpr(-, Id(FQrmSqV)))), BinExpr(%, Id(E1gZ), Id(X4eZO))), UnExpr(!, Id(Z))))
	VarDecl(cB, IntegerType, BinExpr(::, Id(kM6f), BinExpr(&&, UnExpr(-, FuncCall(j, [])), UnExpr(!, Id(G)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 595))

	def test_596(self):
		input = """z : function void ( inherit X : string    , inherit out xI : integer    , lN : string    , inherit nk : array [ 67200 ] of boolean      ) { }    """
		expect = """Program([
	FuncDecl(z, VoidType, [InheritParam(X, StringType), InheritOutParam(xI, IntegerType), Param(lN, StringType), InheritParam(nk, ArrayType([67200], BooleanType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 596))

	def test_597(self):
		input = """h : function void ( ) { }    Lp  : auto  = - ! Y   && G         ;   """
		expect = """Program([
	FuncDecl(h, VoidType, [], None, BlockStmt([]))
	VarDecl(Lp, AutoType, BinExpr(&&, UnExpr(-, UnExpr(!, Id(Y))), Id(G)))
])"""
		self.assertTrue(TestAST.test(input, expect, 597))

	def test_598(self):
		input = """l  : auto  ;   """
		expect = """Program([
	VarDecl(l, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 598))

	def test_599(self):
		input = """ZF : function void ( out _0II : string     ) { }    """
		expect = """Program([
	FuncDecl(ZF, VoidType, [OutParam(_0II, StringType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 599))

	def test_600(self):
		input = """AAr : function array [ 90_87 , 0 , 0 , 0 , 0 ] of integer    ( p : auto   , j : auto    ) inherit L { break ;   return ! g    < c   && U     :: f ( )      ;   }    K : function void ( ) inherit pjc { }    """
		expect = """Program([
	FuncDecl(AAr, ArrayType([9087, 0, 0, 0, 0], IntegerType), [Param(p, AutoType), Param(j, AutoType)], L, BlockStmt([BreakStmt(), ReturnStmt(BinExpr(::, BinExpr(<, UnExpr(!, Id(g)), BinExpr(&&, Id(c), Id(U))), FuncCall(f, [])))]))
	FuncDecl(K, VoidType, [], pjc, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 600))

	def test_601(self):
		input = """f : function void ( inherit out i : float    , inherit S9 : float     ) inherit HJ { L  : string   = E   && ErI    != r   - l     :: ! M8       ;  }    """
		expect = """Program([
	FuncDecl(f, VoidType, [InheritOutParam(i, FloatType), InheritParam(S9, FloatType)], HJ, BlockStmt([VarDecl(L, StringType, BinExpr(::, BinExpr(!=, BinExpr(&&, Id(E), Id(ErI)), BinExpr(-, Id(r), Id(l))), UnExpr(!, Id(M8))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 601))

	def test_602(self):
		input = """Om , T  : auto  ;   g , A  : array [ 0 , 0 , 0 ] of boolean    = ! ! ow    / Cg   - H        , ! { }         ;   """
		expect = """Program([
	VarDecl(Om, AutoType)
	VarDecl(T, AutoType)
	VarDecl(g, ArrayType([0, 0, 0], BooleanType), BinExpr(-, BinExpr(/, UnExpr(!, UnExpr(!, Id(ow))), Id(Cg)), Id(H)))
	VarDecl(A, ArrayType([0, 0, 0], BooleanType), UnExpr(!, ArrayLit([])))
])"""
		self.assertTrue(TestAST.test(input, expect, 602))

	def test_603(self):
		input = """Xshe , nRpv , h , goNHIHf  : integer   ;   """
		expect = """Program([
	VarDecl(Xshe, IntegerType)
	VarDecl(nRpv, IntegerType)
	VarDecl(h, IntegerType)
	VarDecl(goNHIHf, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 603))

	def test_604(self):
		input = """n , g , C_TC , l  : auto  ;   N : function void ( ) { AcX , L , k , pGA , F1 , e , I_8xL  : boolean   = iti5   - Q      , e   % j    == NK   + Q      , Pe   || le    <= e   + tw      , s   / Ecp6     :: d   % S    < vY   || H7      , p   || d      , A   / OH      , S   / w       ;  VJ , N  : string   = RK   && r    < ! b     :: BE   - S    >= q     , rP9   - jDBx    == ! He     :: ""       ;  lk  = ! P      ;   }    """
		expect = """Program([
	VarDecl(n, AutoType)
	VarDecl(g, AutoType)
	VarDecl(C_TC, AutoType)
	VarDecl(l, AutoType)
	FuncDecl(N, VoidType, [], None, BlockStmt([VarDecl(AcX, BooleanType, BinExpr(-, Id(iti5), Id(Q))), VarDecl(L, BooleanType, BinExpr(==, BinExpr(%, Id(e), Id(j)), BinExpr(+, Id(NK), Id(Q)))), VarDecl(k, BooleanType, BinExpr(<=, BinExpr(||, Id(Pe), Id(le)), BinExpr(+, Id(e), Id(tw)))), VarDecl(pGA, BooleanType, BinExpr(::, BinExpr(/, Id(s), Id(Ecp6)), BinExpr(<, BinExpr(%, Id(d), Id(S)), BinExpr(||, Id(vY), Id(H7))))), VarDecl(F1, BooleanType, BinExpr(||, Id(p), Id(d))), VarDecl(e, BooleanType, BinExpr(/, Id(A), Id(OH))), VarDecl(I_8xL, BooleanType, BinExpr(/, Id(S), Id(w))), VarDecl(VJ, StringType, BinExpr(::, BinExpr(<, BinExpr(&&, Id(RK), Id(r)), UnExpr(!, Id(b))), BinExpr(>=, BinExpr(-, Id(BE), Id(S)), Id(q)))), VarDecl(N, StringType, BinExpr(::, BinExpr(==, BinExpr(-, Id(rP9), Id(jDBx)), UnExpr(!, Id(He))), StringLit())), AssignStmt(Id(lk), UnExpr(!, Id(P)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 604))

	def test_605(self):
		input = """K : function auto  ( ) inherit Hx { }    el7 : function void ( inherit sX8 : array [ 0 ] of integer     , inherit iXei52nH : array [ 0 ] of integer     , uT95 : float    , out rSN : string     ) { DyH ( )  ;   M , FM8Z , I , SjS , wz , hXaC , d , S7f6  : auto  ;  crx  = w   > b   - T     :: uDWk   + Y    > ! NPB      ;   }    h : function auto  ( ) { }    """
		expect = """Program([
	FuncDecl(K, AutoType, [], Hx, BlockStmt([]))
	FuncDecl(el7, VoidType, [InheritParam(sX8, ArrayType([0], IntegerType)), InheritParam(iXei52nH, ArrayType([0], IntegerType)), Param(uT95, FloatType), OutParam(rSN, StringType)], None, BlockStmt([CallStmt(DyH, ), VarDecl(M, AutoType), VarDecl(FM8Z, AutoType), VarDecl(I, AutoType), VarDecl(SjS, AutoType), VarDecl(wz, AutoType), VarDecl(hXaC, AutoType), VarDecl(d, AutoType), VarDecl(S7f6, AutoType), AssignStmt(Id(crx), BinExpr(::, BinExpr(>, Id(w), BinExpr(-, Id(b), Id(T))), BinExpr(>, BinExpr(+, Id(uDWk), Id(Y)), UnExpr(!, Id(NPB)))))]))
	FuncDecl(h, AutoType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 605))

	def test_606(self):
		input = """fv  : array [ 432 ] of string    ;   x0h : function void ( u : auto   , coDh42 : auto    ) inherit Nt { }    J : function array [ 11155 , 3_9 ] of integer    ( ) { }    x , h , Y , eN , ccS , z  : auto  = - ! T     + zws   % m   + r        , ! TG   * I     % a   || m    / B   / s7z      != ! - gm_    * E   * a       :: - X ( )       , y   - J    % ! X     % MY ( )    - 0      >= - BtF      , ! { }       :: 39_958    && - Nw9   || lD        , - ! bRVh   - qUqq      > - ! hZ     / - - F42       :: 0    && ! d     * - ! Dr        , - ! ! A         ;   A , Hg  : boolean   = uk   + z    || ! e     % D   || - k      > ! - ! m       :: a ( )      , G ( )    || ! T     * - - Z         ;   f , F  : array [ 0 ] of float    ;   """
		expect = """Program([
	VarDecl(fv, ArrayType([432], StringType))
	FuncDecl(x0h, VoidType, [Param(u, AutoType), Param(coDh42, AutoType)], Nt, BlockStmt([]))
	FuncDecl(J, ArrayType([11155, 39], IntegerType), [], None, BlockStmt([]))
	VarDecl(x, AutoType, BinExpr(+, BinExpr(+, UnExpr(-, UnExpr(!, Id(T))), BinExpr(%, Id(zws), Id(m))), Id(r)))
	VarDecl(h, AutoType, BinExpr(::, BinExpr(!=, BinExpr(||, BinExpr(%, BinExpr(*, UnExpr(!, Id(TG)), Id(I)), Id(a)), BinExpr(/, BinExpr(/, Id(m), Id(B)), Id(s7z))), BinExpr(*, BinExpr(*, UnExpr(!, UnExpr(-, Id(gm_))), Id(E)), Id(a))), UnExpr(-, FuncCall(X, []))))
	VarDecl(Y, AutoType, BinExpr(>=, BinExpr(-, BinExpr(-, Id(y), BinExpr(%, BinExpr(%, Id(J), UnExpr(!, Id(X))), FuncCall(MY, []))), IntegerLit(0)), UnExpr(-, Id(BtF))))
	VarDecl(eN, AutoType, BinExpr(::, UnExpr(!, ArrayLit([])), BinExpr(||, BinExpr(&&, IntegerLit(39958), UnExpr(-, Id(Nw9))), Id(lD))))
	VarDecl(ccS, AutoType, BinExpr(::, BinExpr(>, BinExpr(-, UnExpr(-, UnExpr(!, Id(bRVh))), Id(qUqq)), BinExpr(/, UnExpr(-, UnExpr(!, Id(hZ))), UnExpr(-, UnExpr(-, Id(F42))))), BinExpr(&&, IntegerLit(0), BinExpr(*, UnExpr(!, Id(d)), UnExpr(-, UnExpr(!, Id(Dr)))))))
	VarDecl(z, AutoType, UnExpr(-, UnExpr(!, UnExpr(!, Id(A)))))
	VarDecl(A, BooleanType, BinExpr(::, BinExpr(>, BinExpr(||, BinExpr(||, BinExpr(+, Id(uk), Id(z)), BinExpr(%, UnExpr(!, Id(e)), Id(D))), UnExpr(-, Id(k))), UnExpr(!, UnExpr(-, UnExpr(!, Id(m))))), FuncCall(a, [])))
	VarDecl(Hg, BooleanType, BinExpr(||, FuncCall(G, []), BinExpr(*, UnExpr(!, Id(T)), UnExpr(-, UnExpr(-, Id(Z))))))
	VarDecl(f, ArrayType([0], FloatType))
	VarDecl(F, ArrayType([0], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 606))

	def test_607(self):
		input = """x  : auto  = - ! F     - ! Q   % wA       :: Q ( )       ;   """
		expect = """Program([
	VarDecl(x, AutoType, BinExpr(::, BinExpr(-, UnExpr(-, UnExpr(!, Id(F))), BinExpr(%, UnExpr(!, Id(Q)), Id(wA))), FuncCall(Q, [])))
])"""
		self.assertTrue(TestAST.test(input, expect, 607))

	def test_608(self):
		input = """pJ3u1m , x  : boolean   = - - I    || Qo   - zRZpwQv      <= wy ( )      , - - XH     >= ! Ubd   - B    && P   / O       :: Y   && o0    % ""     || Dq   / CSC0    + XY   && C      < - ! q   + w304         ;   """
		expect = """Program([
	VarDecl(pJ3u1m, BooleanType, BinExpr(<=, BinExpr(||, UnExpr(-, UnExpr(-, Id(I))), BinExpr(-, Id(Qo), Id(zRZpwQv))), FuncCall(wy, [])))
	VarDecl(x, BooleanType, BinExpr(::, BinExpr(>=, UnExpr(-, UnExpr(-, Id(XH))), BinExpr(&&, BinExpr(-, UnExpr(!, Id(Ubd)), Id(B)), BinExpr(/, Id(P), Id(O)))), BinExpr(<, BinExpr(&&, BinExpr(||, BinExpr(&&, Id(Y), BinExpr(%, Id(o0), StringLit())), BinExpr(+, BinExpr(/, Id(Dq), Id(CSC0)), Id(XY))), Id(C)), BinExpr(+, UnExpr(-, UnExpr(!, Id(q))), Id(w304)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 608))

	def test_609(self):
		input = """uY4X : function void ( ) { }    """
		expect = """Program([
	FuncDecl(uY4X, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 609))

	def test_610(self):
		input = """e  : auto  ;   """
		expect = """Program([
	VarDecl(e, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 610))

	def test_611(self):
		input = """X : function string   ( ) { }    """
		expect = """Program([
	FuncDecl(X, StringType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 611))

	def test_612(self):
		input = """x : function array [ 0 ] of float    ( ) { break ;   }    """
		expect = """Program([
	FuncDecl(x, ArrayType([0], FloatType), [], None, BlockStmt([BreakStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 612))

	def test_613(self):
		input = """Q , w , bw  : auto  ;   """
		expect = """Program([
	VarDecl(Q, AutoType)
	VarDecl(w, AutoType)
	VarDecl(bw, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 613))

	def test_614(self):
		input = """rX , x , EuzZ , F  : array [ 0 ] of float    = - I   || p    + g   * a      == ! ! xy ( )       :: ! - - c      >= .e-7      , S   * LP    * ""     || false      :: - zBZ    % w6D0   && h     - pd   % IoE    + gG   || vGY5g9      > - - x ( )        , ! PI7kK   + lk    || hd   || e1       :: a   % _E    + - nP     / s   + J    / f2   && Y      < { }       , - E2 ( )      :: - - ! C      == q      ;   """
		expect = """Program([
	VarDecl(rX, ArrayType([0], FloatType), BinExpr(::, BinExpr(==, BinExpr(||, UnExpr(-, Id(I)), BinExpr(+, Id(p), BinExpr(*, Id(g), Id(a)))), UnExpr(!, UnExpr(!, FuncCall(xy, [])))), BinExpr(>=, UnExpr(!, UnExpr(-, UnExpr(-, Id(c)))), FloatLit(0.0))))
	VarDecl(x, ArrayType([0], FloatType), BinExpr(::, BinExpr(||, BinExpr(*, BinExpr(*, Id(S), Id(LP)), StringLit()), BooleanLit(False)), BinExpr(>, BinExpr(||, BinExpr(&&, BinExpr(%, UnExpr(-, Id(zBZ)), Id(w6D0)), BinExpr(+, BinExpr(-, Id(h), BinExpr(%, Id(pd), Id(IoE))), Id(gG))), Id(vGY5g9)), UnExpr(-, UnExpr(-, FuncCall(x, []))))))
	VarDecl(EuzZ, ArrayType([0], FloatType), BinExpr(::, BinExpr(||, BinExpr(||, BinExpr(+, UnExpr(!, Id(PI7kK)), Id(lk)), Id(hd)), Id(e1)), BinExpr(<, BinExpr(&&, BinExpr(+, BinExpr(+, BinExpr(%, Id(a), Id(_E)), BinExpr(/, UnExpr(-, Id(nP)), Id(s))), BinExpr(/, Id(J), Id(f2))), Id(Y)), ArrayLit([]))))
	VarDecl(F, ArrayType([0], FloatType), BinExpr(::, UnExpr(-, FuncCall(E2, [])), BinExpr(==, UnExpr(-, UnExpr(-, UnExpr(!, Id(C)))), Id(q))))
])"""
		self.assertTrue(TestAST.test(input, expect, 614))

	def test_615(self):
		input = """q , M , T  : array [ 84 ] of integer    ;   """
		expect = """Program([
	VarDecl(q, ArrayType([84], IntegerType))
	VarDecl(M, ArrayType([84], IntegerType))
	VarDecl(T, ArrayType([84], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 615))

	def test_616(self):
		input = """hRL : function string   ( inherit out wd : auto   , inherit out GhA : array [ 856 ] of integer      ) inherit qA { }    kRfW  : auto  ;   C  : integer   ;   T1k , UCf , Yf  : array [ 0 , 6 , 2_6_3079_4767870524 ] of integer    ;   Z : function void ( out E : integer    , inherit V : boolean     ) inherit StIY { }    """
		expect = """Program([
	FuncDecl(hRL, StringType, [InheritOutParam(wd, AutoType), InheritOutParam(GhA, ArrayType([856], IntegerType))], qA, BlockStmt([]))
	VarDecl(kRfW, AutoType)
	VarDecl(C, IntegerType)
	VarDecl(T1k, ArrayType([0, 6, 2630794767870524], IntegerType))
	VarDecl(UCf, ArrayType([0, 6, 2630794767870524], IntegerType))
	VarDecl(Yf, ArrayType([0, 6, 2630794767870524], IntegerType))
	FuncDecl(Z, VoidType, [OutParam(E, IntegerType), InheritParam(V, BooleanType)], StIY, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 616))

	def test_617(self):
		input = """v : function void ( ) { continue ;   LWj , C  : boolean   ;  do { iI ( )  ;   return ;   }  while ( ""    == ! D     :: - ifW    < - lz      ) ;   }    o4 , PN3  : float   ;   """
		expect = """Program([
	FuncDecl(v, VoidType, [], None, BlockStmt([ContinueStmt(), VarDecl(LWj, BooleanType), VarDecl(C, BooleanType), DoWhileStmt(BinExpr(::, BinExpr(==, StringLit(), UnExpr(!, Id(D))), BinExpr(<, UnExpr(-, Id(ifW)), UnExpr(-, Id(lz)))), BlockStmt([CallStmt(iI, ), ReturnStmt()]))]))
	VarDecl(o4, FloatType)
	VarDecl(PN3, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 617))

	def test_618(self):
		input = """W : function void ( ) { GL , k , q , R , ZB14 , Uq , l  : float   = ! B      , F   * l      , ZC_F   + kg     :: 0    < ! V0c      , e ( )    >= g   - XM     :: Moq   || X    > ""      , s   && Fx    >= ! Rg     :: Ls ( )    != g   + ZM7      , - G     :: ! M      , ! m       ;  }    h , g02  : auto  ;   U , M , w , b  : integer   ;   """
		expect = """Program([
	FuncDecl(W, VoidType, [], None, BlockStmt([VarDecl(GL, FloatType, UnExpr(!, Id(B))), VarDecl(k, FloatType, BinExpr(*, Id(F), Id(l))), VarDecl(q, FloatType, BinExpr(::, BinExpr(+, Id(ZC_F), Id(kg)), BinExpr(<, IntegerLit(0), UnExpr(!, Id(V0c))))), VarDecl(R, FloatType, BinExpr(::, BinExpr(>=, FuncCall(e, []), BinExpr(-, Id(g), Id(XM))), BinExpr(>, BinExpr(||, Id(Moq), Id(X)), StringLit()))), VarDecl(ZB14, FloatType, BinExpr(::, BinExpr(>=, BinExpr(&&, Id(s), Id(Fx)), UnExpr(!, Id(Rg))), BinExpr(!=, FuncCall(Ls, []), BinExpr(+, Id(g), Id(ZM7))))), VarDecl(Uq, FloatType, BinExpr(::, UnExpr(-, Id(G)), UnExpr(!, Id(M)))), VarDecl(l, FloatType, UnExpr(!, Id(m)))]))
	VarDecl(h, AutoType)
	VarDecl(g02, AutoType)
	VarDecl(U, IntegerType)
	VarDecl(M, IntegerType)
	VarDecl(w, IntegerType)
	VarDecl(b, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 618))

	def test_619(self):
		input = """U  : integer   ;   CzC6 : function void ( out fU : string    , h : array [ 0 ] of integer      ) inherit dy { }    """
		expect = """Program([
	VarDecl(U, IntegerType)
	FuncDecl(CzC6, VoidType, [OutParam(fU, StringType), Param(h, ArrayType([0], IntegerType))], dy, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 619))

	def test_620(self):
		input = """W : function array [ 6_3 ] of float    ( ) inherit q { P , co  : string   = MhQ   || H     :: kAwp   - x9    == erwsfQ   || SP      , ZW   + R       ;  }    e  : array [ 0 ] of boolean    = ! ! UF    + d93   && siH       :: I   && P    || ym    - ! g9   || Q         ;   """
		expect = """Program([
	FuncDecl(W, ArrayType([63], FloatType), [], q, BlockStmt([VarDecl(P, StringType, BinExpr(::, BinExpr(||, Id(MhQ), Id(H)), BinExpr(==, BinExpr(-, Id(kAwp), Id(x9)), BinExpr(||, Id(erwsfQ), Id(SP))))), VarDecl(co, StringType, BinExpr(+, Id(ZW), Id(R)))]))
	VarDecl(e, ArrayType([0], BooleanType), BinExpr(::, BinExpr(&&, BinExpr(+, UnExpr(!, UnExpr(!, Id(UF))), Id(d93)), Id(siH)), BinExpr(||, BinExpr(||, BinExpr(&&, Id(I), Id(P)), BinExpr(-, Id(ym), UnExpr(!, Id(g9)))), Id(Q))))
])"""
		self.assertTrue(TestAST.test(input, expect, 620))

	def test_621(self):
		input = """Am : function void ( p : boolean     ) inherit x { IK  = LJ ( )      ;   }    pW : function boolean   ( ) inherit g { }    fM2 : function array [ 61 , 366_72409_953_67_71_67 ] of float    ( ) { }    CpkmMsnRv : function void ( ) { A2 ( )  ;   mRT  : array [ 0 ] of float    ;  continue ;   for ( w  = Bb   % f2l    == i7   || P      , icE   || rn9D    != e   - rr      , SV6aN   + b2K2    != Q   + N4wlM     :: - V      ) { }     z , VFEPub , pQ  : array [ 0 ] of integer    ;  }    ot  : float   ;   R : function void ( inherit out D : auto   , out Z : float    , inherit out TQec : float     ) { for ( g  = u   / j     :: ! R    == eA   || q      , ! Ffu      , ! dX    < - z      ) g ( )  ;     }    oIg  : array [ 0 , 0 ] of string    = ! ! - dtL      < ! D_E    || - n    * ! XVQar       :: - ! i   - R      >= .2e+81       ;   E1Tj  : auto  = - ! rJ   * e3       :: M   > ! kA   || o0l     - true        ;   s : function void ( Q : array [ 13 ] of string     , inherit f7U : boolean     ) inherit r5sf { }    """
		expect = """Program([
	FuncDecl(Am, VoidType, [Param(p, BooleanType)], x, BlockStmt([AssignStmt(Id(IK), FuncCall(LJ, []))]))
	FuncDecl(pW, BooleanType, [], g, BlockStmt([]))
	FuncDecl(fM2, ArrayType([61, 36672409953677167], FloatType), [], None, BlockStmt([]))
	FuncDecl(CpkmMsnRv, VoidType, [], None, BlockStmt([CallStmt(A2, ), VarDecl(mRT, ArrayType([0], FloatType)), ContinueStmt(), ForStmt(AssignStmt(Id(w), BinExpr(==, BinExpr(%, Id(Bb), Id(f2l)), BinExpr(||, Id(i7), Id(P)))), BinExpr(!=, BinExpr(||, Id(icE), Id(rn9D)), BinExpr(-, Id(e), Id(rr))), BinExpr(::, BinExpr(!=, BinExpr(+, Id(SV6aN), Id(b2K2)), BinExpr(+, Id(Q), Id(N4wlM))), UnExpr(-, Id(V))), BlockStmt([])), VarDecl(z, ArrayType([0], IntegerType)), VarDecl(VFEPub, ArrayType([0], IntegerType)), VarDecl(pQ, ArrayType([0], IntegerType))]))
	VarDecl(ot, FloatType)
	FuncDecl(R, VoidType, [InheritOutParam(D, AutoType), OutParam(Z, FloatType), InheritOutParam(TQec, FloatType)], None, BlockStmt([ForStmt(AssignStmt(Id(g), BinExpr(::, BinExpr(/, Id(u), Id(j)), BinExpr(==, UnExpr(!, Id(R)), BinExpr(||, Id(eA), Id(q))))), UnExpr(!, Id(Ffu)), BinExpr(<, UnExpr(!, Id(dX)), UnExpr(-, Id(z))), CallStmt(g, ))]))
	VarDecl(oIg, ArrayType([0, 0], StringType), BinExpr(::, BinExpr(<, UnExpr(!, UnExpr(!, UnExpr(-, Id(dtL)))), BinExpr(||, UnExpr(!, Id(D_E)), BinExpr(*, UnExpr(-, Id(n)), UnExpr(!, Id(XVQar))))), BinExpr(>=, BinExpr(-, UnExpr(-, UnExpr(!, Id(i))), Id(R)), FloatLit(2e+80))))
	VarDecl(E1Tj, AutoType, BinExpr(::, BinExpr(*, UnExpr(-, UnExpr(!, Id(rJ))), Id(e3)), BinExpr(>, Id(M), BinExpr(||, UnExpr(!, Id(kA)), BinExpr(-, Id(o0l), BooleanLit(True))))))
	FuncDecl(s, VoidType, [Param(Q, ArrayType([13], StringType)), InheritParam(f7U, BooleanType)], r5sf, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 621))

	def test_622(self):
		input = """_ , I  : array [ 0 , 6_625_400_16 , 22 ] of string    = - - V9   / gN        , ! ! x    - - kT       :: W   * cK    - h   / sJ     - - c        ;   """
		expect = """Program([
	VarDecl(_, ArrayType([0, 662540016, 22], StringType), BinExpr(/, UnExpr(-, UnExpr(-, Id(V9))), Id(gN)))
	VarDecl(I, ArrayType([0, 662540016, 22], StringType), BinExpr(::, BinExpr(-, UnExpr(!, UnExpr(!, Id(x))), UnExpr(-, Id(kT))), BinExpr(-, BinExpr(-, BinExpr(*, Id(W), Id(cK)), BinExpr(/, Id(h), Id(sJ))), UnExpr(-, Id(c)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 622))

	def test_623(self):
		input = """PFX , nj  : auto  ;   jnq , v  : integer   ;   """
		expect = """Program([
	VarDecl(PFX, AutoType)
	VarDecl(nj, AutoType)
	VarDecl(jnq, IntegerType)
	VarDecl(v, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 623))

	def test_624(self):
		input = """W : function void ( inherit out jK : float     ) inherit z { }    """
		expect = """Program([
	FuncDecl(W, VoidType, [InheritOutParam(jK, FloatType)], z, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 624))

	def test_625(self):
		input = """q , e , S  : auto  = DI   - z_X    % - H     % ! SP   / b      < r ( )     :: ! ! Awn     % ! _    || - W        , - pA   / iJ    - q6   + Vg      >= ! CL ( )       , ! ! ZEyH    - VQ   && x       :: ! ! r     && h ( )     == ! t   && O    % P7C5eV ( )         ;   """
		expect = """Program([
	VarDecl(q, AutoType, BinExpr(::, BinExpr(<, BinExpr(-, Id(DI), BinExpr(/, BinExpr(%, BinExpr(%, Id(z_X), UnExpr(-, Id(H))), UnExpr(!, Id(SP))), Id(b))), FuncCall(r, [])), BinExpr(||, BinExpr(%, UnExpr(!, UnExpr(!, Id(Awn))), UnExpr(!, Id(_))), UnExpr(-, Id(W)))))
	VarDecl(e, AutoType, BinExpr(>=, BinExpr(+, BinExpr(-, BinExpr(/, UnExpr(-, Id(pA)), Id(iJ)), Id(q6)), Id(Vg)), UnExpr(!, FuncCall(CL, []))))
	VarDecl(S, AutoType, BinExpr(::, BinExpr(&&, BinExpr(-, UnExpr(!, UnExpr(!, Id(ZEyH))), Id(VQ)), Id(x)), BinExpr(==, BinExpr(&&, UnExpr(!, UnExpr(!, Id(r))), FuncCall(h, [])), BinExpr(&&, UnExpr(!, Id(t)), BinExpr(%, Id(O), FuncCall(P7C5eV, []))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 625))

	def test_626(self):
		input = """S : function array [ 1_01 , 8_1_2_2137 , 0 , 58 , 0 , 4 , 2_9_7_22 , 3807822_33_056_457 ] of string    ( ) { }    """
		expect = """Program([
	FuncDecl(S, ArrayType([101, 8122137, 0, 58, 0, 4, 29722, 380782233056457], StringType), [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 626))

	def test_627(self):
		input = """P , dZ  : auto  ;   jJC : function integer   ( Y : array [ 375314 ] of boolean     , out X : array [ 95 ] of boolean      ) { W  : array [ 6 , 24094 , 43_7_830 ] of boolean    ;  }    ZxH  : auto  ;   NGhY : function void ( ) { BM3O , T , cw  : integer   = - L    >= L_   + _Mz      , ! h    > OB   || MjK      , i   - oQR     :: ! L31       ;  }    """
		expect = """Program([
	VarDecl(P, AutoType)
	VarDecl(dZ, AutoType)
	FuncDecl(jJC, IntegerType, [Param(Y, ArrayType([375314], BooleanType)), OutParam(X, ArrayType([95], BooleanType))], None, BlockStmt([VarDecl(W, ArrayType([6, 24094, 437830], BooleanType))]))
	VarDecl(ZxH, AutoType)
	FuncDecl(NGhY, VoidType, [], None, BlockStmt([VarDecl(BM3O, IntegerType, BinExpr(>=, UnExpr(-, Id(L)), BinExpr(+, Id(L_), Id(_Mz)))), VarDecl(T, IntegerType, BinExpr(>, UnExpr(!, Id(h)), BinExpr(||, Id(OB), Id(MjK)))), VarDecl(cw, IntegerType, BinExpr(::, BinExpr(-, Id(i), Id(oQR)), UnExpr(!, Id(L31))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 627))

	def test_628(self):
		input = """mBh  : auto  = - - Vh    + - VwIhE       :: CR7   && A    || T_   - rbT     * - ""         ;   ph , N  : string   = - O    / - mx     + - S   - a        , ! V4   - S    + _a     >= i    :: J   / m    && - aO     || ! gqeOL    || QfaQ   - w         ;   """
		expect = """Program([
	VarDecl(mBh, AutoType, BinExpr(::, BinExpr(+, UnExpr(-, UnExpr(-, Id(Vh))), UnExpr(-, Id(VwIhE))), BinExpr(||, BinExpr(&&, Id(CR7), Id(A)), BinExpr(-, Id(T_), BinExpr(*, Id(rbT), UnExpr(-, StringLit()))))))
	VarDecl(ph, StringType, BinExpr(-, BinExpr(+, BinExpr(/, UnExpr(-, Id(O)), UnExpr(-, Id(mx))), UnExpr(-, Id(S))), Id(a)))
	VarDecl(N, StringType, BinExpr(::, BinExpr(>=, BinExpr(+, BinExpr(-, UnExpr(!, Id(V4)), Id(S)), Id(_a)), Id(i)), BinExpr(||, BinExpr(||, BinExpr(&&, BinExpr(/, Id(J), Id(m)), UnExpr(-, Id(aO))), UnExpr(!, Id(gqeOL))), BinExpr(-, Id(QfaQ), Id(w)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 628))

	def test_629(self):
		input = """Z : function array [ 0 ] of float    ( ) inherit M { }    h : function array [ 0 , 0 ] of float    ( inherit out HaM : float    , D : boolean     ) inherit Xyo { D  : boolean   ;  }    """
		expect = """Program([
	FuncDecl(Z, ArrayType([0], FloatType), [], M, BlockStmt([]))
	FuncDecl(h, ArrayType([0, 0], FloatType), [InheritOutParam(HaM, FloatType), Param(D, BooleanType)], Xyo, BlockStmt([VarDecl(D, BooleanType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 629))

	def test_630(self):
		input = """hfq : function array [ 90_63 , 0 ] of string    ( ) { f , ZH5 , in , CiR4S  : string   = U   / Rq    >= s5   && c      , Q   - P6      , - gsiIdM      , Z   % RF    < pkj5   % Q     :: a   && in4       ;  }    """
		expect = """Program([
	FuncDecl(hfq, ArrayType([9063, 0], StringType), [], None, BlockStmt([VarDecl(f, StringType, BinExpr(>=, BinExpr(/, Id(U), Id(Rq)), BinExpr(&&, Id(s5), Id(c)))), VarDecl(ZH5, StringType, BinExpr(-, Id(Q), Id(P6))), VarDecl(in, StringType, UnExpr(-, Id(gsiIdM))), VarDecl(CiR4S, StringType, BinExpr(::, BinExpr(<, BinExpr(%, Id(Z), Id(RF)), BinExpr(%, Id(pkj5), Id(Q))), BinExpr(&&, Id(a), Id(in4))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 630))

	def test_631(self):
		input = """Z , QT , o  : array [ 0 , 0 , 0 ] of string    = false    != - - N1   && s2        , ! SBj   * NPfY    + tG1      :: ! { }      == ""      , ! ! s    % F   - m      >= g   - Ehdc    * - A     / 1    + - FPs         ;   kOK : function auto  ( inherit out KWOH : array [ 0 ] of boolean     , X : integer    , B : array [ 867 , 80_7_540 ] of integer      ) { while ( - T      ) a4 ( )  ;     }    """
		expect = """Program([
	VarDecl(Z, ArrayType([0, 0, 0], StringType), BinExpr(!=, BooleanLit(False), BinExpr(&&, UnExpr(-, UnExpr(-, Id(N1))), Id(s2))))
	VarDecl(QT, ArrayType([0, 0, 0], StringType), BinExpr(::, BinExpr(+, BinExpr(*, UnExpr(!, Id(SBj)), Id(NPfY)), Id(tG1)), BinExpr(==, UnExpr(!, ArrayLit([])), StringLit())))
	VarDecl(o, ArrayType([0, 0, 0], StringType), BinExpr(>=, BinExpr(-, BinExpr(%, UnExpr(!, UnExpr(!, Id(s))), Id(F)), Id(m)), BinExpr(+, BinExpr(-, Id(g), BinExpr(/, BinExpr(*, Id(Ehdc), UnExpr(-, Id(A))), IntegerLit(1))), UnExpr(-, Id(FPs)))))
	FuncDecl(kOK, AutoType, [InheritOutParam(KWOH, ArrayType([0], BooleanType)), Param(X, IntegerType), Param(B, ArrayType([867, 807540], IntegerType))], None, BlockStmt([WhileStmt(UnExpr(-, Id(T)), CallStmt(a4, ))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 631))

	def test_632(self):
		input = """VH : function array [ 0 ] of integer    ( ) { break ;   }    """
		expect = """Program([
	FuncDecl(VH, ArrayType([0], IntegerType), [], None, BlockStmt([BreakStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 632))

	def test_633(self):
		input = """ZAz : function void ( ) { h , X , D  : auto  = ! r     :: MT   - q      , Ub   == MD   - V      , vc   && IoaCyik       ;  }    """
		expect = """Program([
	FuncDecl(ZAz, VoidType, [], None, BlockStmt([VarDecl(h, AutoType, BinExpr(::, UnExpr(!, Id(r)), BinExpr(-, Id(MT), Id(q)))), VarDecl(X, AutoType, BinExpr(==, Id(Ub), BinExpr(-, Id(MD), Id(V)))), VarDecl(D, AutoType, BinExpr(&&, Id(vc), Id(IoaCyik)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 633))

	def test_634(self):
		input = """VT3 : function auto  ( out l : auto   , NAO : integer     ) inherit mjYtz { for ( x9  = aQ   % L    <= ! dJH     :: Y   || jE      , - x    < ""     :: - l    < ! KA      , F   + gY    != - PlhFKk      ) O ( )  ;     N  : boolean   ;  if ( Xf   - BC    == w   % aiW      ) k ( )  ;     QLy  : array [ 0 , 24 , 2_0 , 9 , 0 ] of string    = Lmn   - N     :: s   + T    != ! Mg       ;  Yu  = ""     :: ! yJH    < ""      ;   }    """
		expect = """Program([
	FuncDecl(VT3, AutoType, [OutParam(l, AutoType), Param(NAO, IntegerType)], mjYtz, BlockStmt([ForStmt(AssignStmt(Id(x9), BinExpr(::, BinExpr(<=, BinExpr(%, Id(aQ), Id(L)), UnExpr(!, Id(dJH))), BinExpr(||, Id(Y), Id(jE)))), BinExpr(::, BinExpr(<, UnExpr(-, Id(x)), StringLit()), BinExpr(<, UnExpr(-, Id(l)), UnExpr(!, Id(KA)))), BinExpr(!=, BinExpr(+, Id(F), Id(gY)), UnExpr(-, Id(PlhFKk))), CallStmt(O, )), VarDecl(N, BooleanType), IfStmt(BinExpr(==, BinExpr(-, Id(Xf), Id(BC)), BinExpr(%, Id(w), Id(aiW))), CallStmt(k, )), VarDecl(QLy, ArrayType([0, 24, 20, 9, 0], StringType), BinExpr(::, BinExpr(-, Id(Lmn), Id(N)), BinExpr(!=, BinExpr(+, Id(s), Id(T)), UnExpr(!, Id(Mg))))), AssignStmt(Id(Yu), BinExpr(::, StringLit(), BinExpr(<, UnExpr(!, Id(yJH)), StringLit())))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 634))

	def test_635(self):
		input = """_ , FlD  : auto  ;   u2  : boolean   = - YR    * W   / l     || E   && H    * f   || xD         ;   b : function boolean   ( out QN : integer     ) inherit GHc { do { }  while ( TE ( )      ) ;   }    nO9e : function void ( ) inherit Vi { }    qFP_yv8 : function array [ 6_676808 , 0 , 0 ] of integer    ( inherit t : boolean     ) inherit jU { break ;   R ( )  ;   return ;   if ( mETv   * Ela    < UB   || yFF      ) break ;   else break ;     break ;   }    """
		expect = """Program([
	VarDecl(_, AutoType)
	VarDecl(FlD, AutoType)
	VarDecl(u2, BooleanType, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(/, BinExpr(*, UnExpr(-, Id(YR)), Id(W)), Id(l)), Id(E)), BinExpr(*, Id(H), Id(f))), Id(xD)))
	FuncDecl(b, BooleanType, [OutParam(QN, IntegerType)], GHc, BlockStmt([DoWhileStmt(FuncCall(TE, []), BlockStmt([]))]))
	FuncDecl(nO9e, VoidType, [], Vi, BlockStmt([]))
	FuncDecl(qFP_yv8, ArrayType([6676808, 0, 0], IntegerType), [InheritParam(t, BooleanType)], jU, BlockStmt([BreakStmt(), CallStmt(R, ), ReturnStmt(), IfStmt(BinExpr(<, BinExpr(*, Id(mETv), Id(Ela)), BinExpr(||, Id(UB), Id(yFF))), BreakStmt(), BreakStmt()), BreakStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 635))

	def test_636(self):
		input = """Q8L  : auto  = 5_49_06     :: j      ;   ab : function void ( out a : boolean     ) inherit zpTW { while ( k   && Fcw    <= - TgW4Z      ) break ;     }    """
		expect = """Program([
	VarDecl(Q8L, AutoType, BinExpr(::, IntegerLit(54906), Id(j)))
	FuncDecl(ab, VoidType, [OutParam(a, BooleanType)], zpTW, BlockStmt([WhileStmt(BinExpr(<=, BinExpr(&&, Id(k), Id(Fcw)), UnExpr(-, Id(TgW4Z))), BreakStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 636))

	def test_637(self):
		input = """F , Wdgi , xs  : array [ 0 ] of string    ;   T  : auto  = - m   + onl    || Cm   + y       :: ! W4T   * qU     && - ! M      <= ! eK   + R     % - - a         ;   """
		expect = """Program([
	VarDecl(F, ArrayType([0], StringType))
	VarDecl(Wdgi, ArrayType([0], StringType))
	VarDecl(xs, ArrayType([0], StringType))
	VarDecl(T, AutoType, BinExpr(::, BinExpr(||, BinExpr(+, UnExpr(-, Id(m)), Id(onl)), BinExpr(+, Id(Cm), Id(y))), BinExpr(<=, BinExpr(&&, BinExpr(*, UnExpr(!, Id(W4T)), Id(qU)), UnExpr(-, UnExpr(!, Id(M)))), BinExpr(+, UnExpr(!, Id(eK)), BinExpr(%, Id(R), UnExpr(-, UnExpr(-, Id(a))))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 637))

	def test_638(self):
		input = """m : function void ( ) { { }   lj  = ""    >= ! W      ;   s  : auto  ;  }    """
		expect = """Program([
	FuncDecl(m, VoidType, [], None, BlockStmt([BlockStmt([]), AssignStmt(Id(lj), BinExpr(>=, StringLit(), UnExpr(!, Id(W)))), VarDecl(s, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 638))

	def test_639(self):
		input = """f : function void ( TEv : auto   , inherit out K : auto    ) { T  : string   = n   % S05     :: c   % rz    <= Y   - rjXX       ;  }    """
		expect = """Program([
	FuncDecl(f, VoidType, [Param(TEv, AutoType), InheritOutParam(K, AutoType)], None, BlockStmt([VarDecl(T, StringType, BinExpr(::, BinExpr(%, Id(n), Id(S05)), BinExpr(<=, BinExpr(%, Id(c), Id(rz)), BinExpr(-, Id(Y), Id(rjXX)))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 639))

	def test_640(self):
		input = """y : function void ( ) inherit wy { }    """
		expect = """Program([
	FuncDecl(y, VoidType, [], wy, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 640))

	def test_641(self):
		input = """_ , B  : boolean   ;   x , h  : auto  ;   """
		expect = """Program([
	VarDecl(_, BooleanType)
	VarDecl(B, BooleanType)
	VarDecl(x, AutoType)
	VarDecl(h, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 641))

	def test_642(self):
		input = """Ks , GXX  : float   = - Q   && f     + ! EKK   - CjRS       :: X8 ( )    > ! - zsRXN    % - FW        , ! ! gANp ( )      >= - z    / ! nyKb     + - 4       :: ZD   * C    / - hib     * ! - kf         ;   q , om1Mc  : array [ 0 , 0 , 0 , 0 ] of string    = - b   - kypU     || V      , ! true      :: - - u   + t0      < i ( )    || - k    || - s2m         ;   E , bU  : auto  = - - ! nj      <= ZJ ( )    || v      , ! k ( )    - Ga   % P      < ! L    && ! - kC       :: ! eAJKKz    + ZjRf   + gq     % - EQge    % aVx   - lnh         ;   """
		expect = """Program([
	VarDecl(Ks, FloatType, BinExpr(::, BinExpr(&&, UnExpr(-, Id(Q)), BinExpr(-, BinExpr(+, Id(f), UnExpr(!, Id(EKK))), Id(CjRS))), BinExpr(>, FuncCall(X8, []), BinExpr(%, UnExpr(!, UnExpr(-, Id(zsRXN))), UnExpr(-, Id(FW))))))
	VarDecl(GXX, FloatType, BinExpr(::, BinExpr(>=, UnExpr(!, UnExpr(!, FuncCall(gANp, []))), BinExpr(+, BinExpr(/, UnExpr(-, Id(z)), UnExpr(!, Id(nyKb))), UnExpr(-, IntegerLit(4)))), BinExpr(*, BinExpr(/, BinExpr(*, Id(ZD), Id(C)), UnExpr(-, Id(hib))), UnExpr(!, UnExpr(-, Id(kf))))))
	VarDecl(q, ArrayType([0, 0, 0, 0], StringType), BinExpr(||, BinExpr(-, UnExpr(-, Id(b)), Id(kypU)), Id(V)))
	VarDecl(om1Mc, ArrayType([0, 0, 0, 0], StringType), BinExpr(::, UnExpr(!, BooleanLit(True)), BinExpr(<, BinExpr(+, UnExpr(-, UnExpr(-, Id(u))), Id(t0)), BinExpr(||, BinExpr(||, FuncCall(i, []), UnExpr(-, Id(k))), UnExpr(-, Id(s2m))))))
	VarDecl(E, AutoType, BinExpr(<=, UnExpr(-, UnExpr(-, UnExpr(!, Id(nj)))), BinExpr(||, FuncCall(ZJ, []), Id(v))))
	VarDecl(bU, AutoType, BinExpr(::, BinExpr(<, BinExpr(-, UnExpr(!, FuncCall(k, [])), BinExpr(%, Id(Ga), Id(P))), BinExpr(&&, UnExpr(!, Id(L)), UnExpr(!, UnExpr(-, Id(kC))))), BinExpr(-, BinExpr(+, BinExpr(+, UnExpr(!, Id(eAJKKz)), Id(ZjRf)), BinExpr(%, BinExpr(%, Id(gq), UnExpr(-, Id(EQge))), Id(aVx))), Id(lnh))))
])"""
		self.assertTrue(TestAST.test(input, expect, 642))

	def test_643(self):
		input = """h : function auto  ( M : auto    ) { break ;   y , GcH3  : auto  = E   / T    >= W   && JWy     :: ""      , N1    :: ! Z5       ;  JBuIv , q , e , _ , K , E  : array [ 0 , 0 , 2 , 9 , 13_098_9_6 ] of integer    = S   % IrvO    >= - C     :: ! x    <= x   + on      , ! P    > mx   % bTS      , D   / U      , ! sxo     :: f ( )      , ! D    < ""      , t   && Ph    > 0     :: X ( )       ;  NW4 , Z , b , S9gG , F  : auto  ;  L , x , h  : array [ 0 , 0 ] of string    ;  }    """
		expect = """Program([
	FuncDecl(h, AutoType, [Param(M, AutoType)], None, BlockStmt([BreakStmt(), VarDecl(y, AutoType, BinExpr(::, BinExpr(>=, BinExpr(/, Id(E), Id(T)), BinExpr(&&, Id(W), Id(JWy))), StringLit())), VarDecl(GcH3, AutoType, BinExpr(::, Id(N1), UnExpr(!, Id(Z5)))), VarDecl(JBuIv, ArrayType([0, 0, 2, 9, 1309896], IntegerType), BinExpr(::, BinExpr(>=, BinExpr(%, Id(S), Id(IrvO)), UnExpr(-, Id(C))), BinExpr(<=, UnExpr(!, Id(x)), BinExpr(+, Id(x), Id(on))))), VarDecl(q, ArrayType([0, 0, 2, 9, 1309896], IntegerType), BinExpr(>, UnExpr(!, Id(P)), BinExpr(%, Id(mx), Id(bTS)))), VarDecl(e, ArrayType([0, 0, 2, 9, 1309896], IntegerType), BinExpr(/, Id(D), Id(U))), VarDecl(_, ArrayType([0, 0, 2, 9, 1309896], IntegerType), BinExpr(::, UnExpr(!, Id(sxo)), FuncCall(f, []))), VarDecl(K, ArrayType([0, 0, 2, 9, 1309896], IntegerType), BinExpr(<, UnExpr(!, Id(D)), StringLit())), VarDecl(E, ArrayType([0, 0, 2, 9, 1309896], IntegerType), BinExpr(::, BinExpr(>, BinExpr(&&, Id(t), Id(Ph)), IntegerLit(0)), FuncCall(X, []))), VarDecl(NW4, AutoType), VarDecl(Z, AutoType), VarDecl(b, AutoType), VarDecl(S9gG, AutoType), VarDecl(F, AutoType), VarDecl(L, ArrayType([0, 0], StringType)), VarDecl(x, ArrayType([0, 0], StringType)), VarDecl(h, ArrayType([0, 0], StringType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 643))

	def test_644(self):
		input = """oqH : function boolean   ( ) inherit k { L0y  : float   ;  }    g : function void ( ) { }    """
		expect = """Program([
	FuncDecl(oqH, BooleanType, [], k, BlockStmt([VarDecl(L0y, FloatType)]))
	FuncDecl(g, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 644))

	def test_645(self):
		input = """zk : function void ( out j : integer     ) { }    """
		expect = """Program([
	FuncDecl(zk, VoidType, [OutParam(j, IntegerType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 645))

	def test_646(self):
		input = """e , u , j  : array [ 0 ] of float    ;   """
		expect = """Program([
	VarDecl(e, ArrayType([0], FloatType))
	VarDecl(u, ArrayType([0], FloatType))
	VarDecl(j, ArrayType([0], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 646))

	def test_647(self):
		input = """u : function void ( f : auto   , inherit out MzNnWS3Z : auto   , out b7 : array [ 0 ] of string     , inherit out CH : auto    ) { I , oZ , d8 , kN  : auto  = ! M     :: tve   && Ls      , XTJ   / k      , D   - x    <= B   || X     :: ! H      , GTk   - B       ;  break ;   }    v : function array [ 0 , 0 , 80 ] of string    ( ) inherit GZv7y { }    """
		expect = """Program([
	FuncDecl(u, VoidType, [Param(f, AutoType), InheritOutParam(MzNnWS3Z, AutoType), OutParam(b7, ArrayType([0], StringType)), InheritOutParam(CH, AutoType)], None, BlockStmt([VarDecl(I, AutoType, BinExpr(::, UnExpr(!, Id(M)), BinExpr(&&, Id(tve), Id(Ls)))), VarDecl(oZ, AutoType, BinExpr(/, Id(XTJ), Id(k))), VarDecl(d8, AutoType, BinExpr(::, BinExpr(<=, BinExpr(-, Id(D), Id(x)), BinExpr(||, Id(B), Id(X))), UnExpr(!, Id(H)))), VarDecl(kN, AutoType, BinExpr(-, Id(GTk), Id(B))), BreakStmt()]))
	FuncDecl(v, ArrayType([0, 0, 80], StringType), [], GZv7y, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 647))

	def test_648(self):
		input = """c_  : boolean   = - ! t     / Xv3   / P    % ! g      <= nJZC ( )    - vFDX   % ws     || - N    - - Vx       :: F   % np   || lEE     + W   - G    * Go   / z      > - nyD    - K   - k     / X       ;   """
		expect = """Program([
	VarDecl(c_, BooleanType, BinExpr(::, BinExpr(<=, BinExpr(%, BinExpr(/, BinExpr(/, UnExpr(-, UnExpr(!, Id(t))), Id(Xv3)), Id(P)), UnExpr(!, Id(g))), BinExpr(||, BinExpr(-, FuncCall(nJZC, []), BinExpr(%, Id(vFDX), Id(ws))), BinExpr(-, UnExpr(-, Id(N)), UnExpr(-, Id(Vx))))), BinExpr(>, BinExpr(||, BinExpr(%, Id(F), Id(np)), BinExpr(-, BinExpr(+, Id(lEE), Id(W)), BinExpr(/, BinExpr(*, Id(G), Id(Go)), Id(z)))), BinExpr(-, BinExpr(-, UnExpr(-, Id(nyD)), Id(K)), BinExpr(/, Id(k), Id(X))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 648))

	def test_649(self):
		input = """rp : function array [ 8 ] of string    ( m : auto    ) inherit sp { p , y , n  : boolean   ;  wW , XV7C , f  : integer   ;  }    MR : function array [ 0 , 0 ] of integer    ( ) { }    z : function void ( out Om : auto    ) { }    """
		expect = """Program([
	FuncDecl(rp, ArrayType([8], StringType), [Param(m, AutoType)], sp, BlockStmt([VarDecl(p, BooleanType), VarDecl(y, BooleanType), VarDecl(n, BooleanType), VarDecl(wW, IntegerType), VarDecl(XV7C, IntegerType), VarDecl(f, IntegerType)]))
	FuncDecl(MR, ArrayType([0, 0], IntegerType), [], None, BlockStmt([]))
	FuncDecl(z, VoidType, [OutParam(Om, AutoType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 649))

	def test_650(self):
		input = """zPr4eY : function auto  ( inherit V : float    , inherit _x : float     ) inherit E { }    """
		expect = """Program([
	FuncDecl(zPr4eY, AutoType, [InheritParam(V, FloatType), InheritParam(_x, FloatType)], E, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 650))

	def test_651(self):
		input = """F9 : function array [ 0 , 0 ] of string    ( inherit out kAYNa : auto    ) inherit yW02 { }    """
		expect = """Program([
	FuncDecl(F9, ArrayType([0, 0], StringType), [InheritOutParam(kAYNa, AutoType)], yW02, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 651))

	def test_652(self):
		input = """h  : float   = ""    / sc   + g4     - 9_91_1     < ! ! r   && Pk       :: ! ! eZ    && - k      != 246    % - v   && u         ;   """
		expect = """Program([
	VarDecl(h, FloatType, BinExpr(::, BinExpr(<, BinExpr(-, BinExpr(+, BinExpr(/, StringLit(), Id(sc)), Id(g4)), IntegerLit(9911)), BinExpr(&&, UnExpr(!, UnExpr(!, Id(r))), Id(Pk))), BinExpr(!=, BinExpr(&&, UnExpr(!, UnExpr(!, Id(eZ))), UnExpr(-, Id(k))), BinExpr(&&, BinExpr(%, IntegerLit(246), UnExpr(-, Id(v))), Id(u)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 652))

	def test_653(self):
		input = """c : function boolean   ( out QK : auto    ) { tO  : float   = - H    >= - tm     :: ! DFrW2h    > k2   || a       ;  H , Xo  : auto  = ! _    <= D   || E      , s   && z    > 3     :: L   - Wy    > gzF ( )       ;  R  : array [ 0 , 29 ] of float    ;  E , jF5 , OicD , H , q  : array [ 1 , 0 , 0 , 0 , 0 , 0 ] of integer    ;  }    """
		expect = """Program([
	FuncDecl(c, BooleanType, [OutParam(QK, AutoType)], None, BlockStmt([VarDecl(tO, FloatType, BinExpr(::, BinExpr(>=, UnExpr(-, Id(H)), UnExpr(-, Id(tm))), BinExpr(>, UnExpr(!, Id(DFrW2h)), BinExpr(||, Id(k2), Id(a))))), VarDecl(H, AutoType, BinExpr(<=, UnExpr(!, Id(_)), BinExpr(||, Id(D), Id(E)))), VarDecl(Xo, AutoType, BinExpr(::, BinExpr(>, BinExpr(&&, Id(s), Id(z)), IntegerLit(3)), BinExpr(>, BinExpr(-, Id(L), Id(Wy)), FuncCall(gzF, [])))), VarDecl(R, ArrayType([0, 29], FloatType)), VarDecl(E, ArrayType([1, 0, 0, 0, 0, 0], IntegerType)), VarDecl(jF5, ArrayType([1, 0, 0, 0, 0, 0], IntegerType)), VarDecl(OicD, ArrayType([1, 0, 0, 0, 0, 0], IntegerType)), VarDecl(H, ArrayType([1, 0, 0, 0, 0, 0], IntegerType)), VarDecl(q, ArrayType([1, 0, 0, 0, 0, 0], IntegerType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 653))

	def test_654(self):
		input = """i  : array [ 0 , 8 , 0 , 8 , 20 ] of float    ;   nzGmJ : function boolean   ( ) { }    """
		expect = """Program([
	VarDecl(i, ArrayType([0, 8, 0, 8, 20], FloatType))
	FuncDecl(nzGmJ, BooleanType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 654))

	def test_655(self):
		input = """O , x  : array [ 569 ] of integer    ;   """
		expect = """Program([
	VarDecl(O, ArrayType([569], IntegerType))
	VarDecl(x, ArrayType([569], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 655))

	def test_656(self):
		input = """HL : function void ( ) inherit Fp { O  : array [ 6936052 ] of boolean    ;  do { }  while ( m6Fa   % S    <= - Vt0     :: w   * BS    >= ObB   && E      ) ;   break ;   }    """
		expect = """Program([
	FuncDecl(HL, VoidType, [], Fp, BlockStmt([VarDecl(O, ArrayType([6936052], BooleanType)), DoWhileStmt(BinExpr(::, BinExpr(<=, BinExpr(%, Id(m6Fa), Id(S)), UnExpr(-, Id(Vt0))), BinExpr(>=, BinExpr(*, Id(w), Id(BS)), BinExpr(&&, Id(ObB), Id(E)))), BlockStmt([])), BreakStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 656))

	def test_657(self):
		input = """jijQt : function void ( ) { }    """
		expect = """Program([
	FuncDecl(jijQt, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 657))

	def test_658(self):
		input = """J : function void ( ) { }    Q : function array [ 0 ] of integer    ( inherit out M : array [ 9_8_9 , 2_5 , 0 ] of string      ) { }    c , o , F  : auto  ;   """
		expect = """Program([
	FuncDecl(J, VoidType, [], None, BlockStmt([]))
	FuncDecl(Q, ArrayType([0], IntegerType), [InheritOutParam(M, ArrayType([989, 25, 0], StringType))], None, BlockStmt([]))
	VarDecl(c, AutoType)
	VarDecl(o, AutoType)
	VarDecl(F, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 658))

	def test_659(self):
		input = """j , z  : float   = - YA ( )    / WX   || JQ        , vtUf ( )     :: { }     != - as    || ! j     / ! ""         ;   """
		expect = """Program([
	VarDecl(j, FloatType, BinExpr(||, BinExpr(/, UnExpr(-, FuncCall(YA, [])), Id(WX)), Id(JQ)))
	VarDecl(z, FloatType, BinExpr(::, FuncCall(vtUf, []), BinExpr(!=, ArrayLit([]), BinExpr(||, UnExpr(-, Id(as)), BinExpr(/, UnExpr(!, Id(j)), UnExpr(!, StringLit()))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 659))

	def test_660(self):
		input = """F : function void ( inherit GwE : auto   , out z6 : array [ 0 ] of float      ) inherit D { }    t6J : function auto  ( ) inherit a { }    """
		expect = """Program([
	FuncDecl(F, VoidType, [InheritParam(GwE, AutoType), OutParam(z6, ArrayType([0], FloatType))], D, BlockStmt([]))
	FuncDecl(t6J, AutoType, [], a, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 660))

	def test_661(self):
		input = """LB , JmjiH , a5t3 , u  : auto  = ! L_xlNWeU9    || - FJkK     - - n    % ! xDL      < ! - ""        , ! dq   - T     % ""    * ! H       :: - - J     >= - { }        , ! f   - s     / - f1   || UY       :: ! M   && t     + ! a    + - L__        , H   >= - g    && - U     + jfv6   * D_    / i   && l         ;   """
		expect = """Program([
	VarDecl(LB, AutoType, BinExpr(<, BinExpr(||, UnExpr(!, Id(L_xlNWeU9)), BinExpr(-, UnExpr(-, Id(FJkK)), BinExpr(%, UnExpr(-, Id(n)), UnExpr(!, Id(xDL))))), UnExpr(!, UnExpr(-, StringLit()))))
	VarDecl(JmjiH, AutoType, BinExpr(::, BinExpr(-, UnExpr(!, Id(dq)), BinExpr(*, BinExpr(%, Id(T), StringLit()), UnExpr(!, Id(H)))), BinExpr(>=, UnExpr(-, UnExpr(-, Id(J))), UnExpr(-, ArrayLit([])))))
	VarDecl(a5t3, AutoType, BinExpr(::, BinExpr(||, BinExpr(-, UnExpr(!, Id(f)), BinExpr(/, Id(s), UnExpr(-, Id(f1)))), Id(UY)), BinExpr(&&, UnExpr(!, Id(M)), BinExpr(+, BinExpr(+, Id(t), UnExpr(!, Id(a))), UnExpr(-, Id(L__))))))
	VarDecl(u, AutoType, BinExpr(>=, Id(H), BinExpr(&&, BinExpr(&&, UnExpr(-, Id(g)), BinExpr(+, UnExpr(-, Id(U)), BinExpr(/, BinExpr(*, Id(jfv6), Id(D_)), Id(i)))), Id(l))))
])"""
		self.assertTrue(TestAST.test(input, expect, 661))

	def test_662(self):
		input = """e  : auto  ;   Rpx5 : function array [ 0 , 0 , 2_7136_2_007_1 ] of integer    ( ) { }    """
		expect = """Program([
	VarDecl(e, AutoType)
	FuncDecl(Rpx5, ArrayType([0, 0, 2713620071], IntegerType), [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 662))

	def test_663(self):
		input = """zWB : function void ( ) inherit Oo_ { }    Uh : function void ( ) { }    """
		expect = """Program([
	FuncDecl(zWB, VoidType, [], Oo_, BlockStmt([]))
	FuncDecl(Uh, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 663))

	def test_664(self):
		input = """VADU : function array [ 76_1 , 8_27_1 , 0 , 0 , 0 , 35206_672818 , 0 ] of string    ( ) { }    D3l , _tqT  : array [ 0 , 4 ] of float    ;   """
		expect = """Program([
	FuncDecl(VADU, ArrayType([761, 8271, 0, 0, 0, 35206672818, 0], StringType), [], None, BlockStmt([]))
	VarDecl(D3l, ArrayType([0, 4], FloatType))
	VarDecl(_tqT, ArrayType([0, 4], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 664))

	def test_665(self):
		input = """oS : function void ( inherit out ps : auto    ) { return - a     :: - Gq      ;   i8fuRZ3 , xyyO  : array [ 0 ] of string    ;  continue ;   do { A , NXy  : boolean   ;  ci , X  : array [ 0 , 0 ] of string    ;  }  while ( D4m1   || H     :: ! Eq    <= Wn   * M      ) ;   }    """
		expect = """Program([
	FuncDecl(oS, VoidType, [InheritOutParam(ps, AutoType)], None, BlockStmt([ReturnStmt(BinExpr(::, UnExpr(-, Id(a)), UnExpr(-, Id(Gq)))), VarDecl(i8fuRZ3, ArrayType([0], StringType)), VarDecl(xyyO, ArrayType([0], StringType)), ContinueStmt(), DoWhileStmt(BinExpr(::, BinExpr(||, Id(D4m1), Id(H)), BinExpr(<=, UnExpr(!, Id(Eq)), BinExpr(*, Id(Wn), Id(M)))), BlockStmt([VarDecl(A, BooleanType), VarDecl(NXy, BooleanType), VarDecl(ci, ArrayType([0, 0], StringType)), VarDecl(X, ArrayType([0, 0], StringType))]))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 665))

	def test_666(self):
		input = """klzHVv  : array [ 13_7_38 ] of boolean    = - eJUj    && - B     && p   || ANdH8    || w   - O         ;   """
		expect = """Program([
	VarDecl(klzHVv, ArrayType([13738], BooleanType), BinExpr(||, BinExpr(||, BinExpr(&&, BinExpr(&&, UnExpr(-, Id(eJUj)), UnExpr(-, Id(B))), Id(p)), Id(ANdH8)), BinExpr(-, Id(w), Id(O))))
])"""
		self.assertTrue(TestAST.test(input, expect, 666))

	def test_667(self):
		input = """_2sR : function float   ( out N : float    , f4 : integer     ) inherit o { G , D , V  : auto  ;  wQ3Ii , g  : float   ;  }    """
		expect = """Program([
	FuncDecl(_2sR, FloatType, [OutParam(N, FloatType), Param(f4, IntegerType)], o, BlockStmt([VarDecl(G, AutoType), VarDecl(D, AutoType), VarDecl(V, AutoType), VarDecl(wQ3Ii, FloatType), VarDecl(g, FloatType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 667))

	def test_668(self):
		input = """XDL , f  : boolean   ;   X , Ez  : array [ 0 , 0 , 7248_615 , 8_5_0 , 0 ] of integer    ;   W : function void ( inherit L3 : array [ 4 , 0 , 4_00_4 , 7_295_6_74 ] of string     , Q : float     ) { Qq  : string   = ! t     :: h   == tzMP   * qKXA       ;  }    """
		expect = """Program([
	VarDecl(XDL, BooleanType)
	VarDecl(f, BooleanType)
	VarDecl(X, ArrayType([0, 0, 7248615, 850, 0], IntegerType))
	VarDecl(Ez, ArrayType([0, 0, 7248615, 850, 0], IntegerType))
	FuncDecl(W, VoidType, [InheritParam(L3, ArrayType([4, 0, 4004, 7295674], StringType)), Param(Q, FloatType)], None, BlockStmt([VarDecl(Qq, StringType, BinExpr(::, UnExpr(!, Id(t)), BinExpr(==, Id(h), BinExpr(*, Id(tzMP), Id(qKXA)))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 668))

	def test_669(self):
		input = """M , Q  : array [ 0 ] of boolean    ;   O , o  : array [ 7883_1_38 ] of integer    = S   + - ! VZ      >= - f    || f   || oU     * - q   - L95qi        , - - QI     && ! C4AR    / Gb   && w8y      >= ! ! H     || - ! I       :: - ! yk   || z      <= ! q   && E2    - Dg5   + b0iC         ;   """
		expect = """Program([
	VarDecl(M, ArrayType([0], BooleanType))
	VarDecl(Q, ArrayType([0], BooleanType))
	VarDecl(O, ArrayType([7883138], IntegerType), BinExpr(>=, BinExpr(+, Id(S), UnExpr(-, UnExpr(!, Id(VZ)))), BinExpr(||, BinExpr(||, UnExpr(-, Id(f)), Id(f)), BinExpr(-, BinExpr(*, Id(oU), UnExpr(-, Id(q))), Id(L95qi)))))
	VarDecl(o, ArrayType([7883138], IntegerType), BinExpr(::, BinExpr(>=, BinExpr(&&, BinExpr(&&, UnExpr(-, UnExpr(-, Id(QI))), BinExpr(/, UnExpr(!, Id(C4AR)), Id(Gb))), Id(w8y)), BinExpr(||, UnExpr(!, UnExpr(!, Id(H))), UnExpr(-, UnExpr(!, Id(I))))), BinExpr(<=, BinExpr(||, UnExpr(-, UnExpr(!, Id(yk))), Id(z)), BinExpr(&&, UnExpr(!, Id(q)), BinExpr(+, BinExpr(-, Id(E2), Id(Dg5)), Id(b0iC))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 669))

	def test_670(self):
		input = """W  : array [ 3000_324 , 0 ] of string    = ! P   && V     / - - W      >= - hl    * - z    * A   * k         ;   """
		expect = """Program([
	VarDecl(W, ArrayType([3000324, 0], StringType), BinExpr(>=, BinExpr(&&, UnExpr(!, Id(P)), BinExpr(/, Id(V), UnExpr(-, UnExpr(-, Id(W))))), BinExpr(*, BinExpr(*, BinExpr(*, UnExpr(-, Id(hl)), UnExpr(-, Id(z))), Id(A)), Id(k))))
])"""
		self.assertTrue(TestAST.test(input, expect, 670))

	def test_671(self):
		input = """xd : function auto  ( ) inherit Bbu { return O   && l    == e   && B      ;   }    D  : array [ 0 ] of integer    ;   """
		expect = """Program([
	FuncDecl(xd, AutoType, [], Bbu, BlockStmt([ReturnStmt(BinExpr(==, BinExpr(&&, Id(O), Id(l)), BinExpr(&&, Id(e), Id(B))))]))
	VarDecl(D, ArrayType([0], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 671))

	def test_672(self):
		input = """g  : array [ 0 ] of boolean    = Qhh   != - - ! S       :: - Pe    + h   % WnB     - Gt   || W    % ""         ;   """
		expect = """Program([
	VarDecl(g, ArrayType([0], BooleanType), BinExpr(::, BinExpr(!=, Id(Qhh), UnExpr(-, UnExpr(-, UnExpr(!, Id(S))))), BinExpr(||, BinExpr(-, BinExpr(+, UnExpr(-, Id(Pe)), BinExpr(%, Id(h), Id(WnB))), Id(Gt)), BinExpr(%, Id(W), StringLit()))))
])"""
		self.assertTrue(TestAST.test(input, expect, 672))

	def test_673(self):
		input = """wPP , v  : auto  = ! N   + dURIW    - s     < t   % - ! r        , - v   / O     - - zST    - ! y1M      < - ! WN ( )       :: VQ   - SB   || dsko     / - T    && ""      <= - l   / R     - ! DX   && n         ;   J : function void ( out H : array [ 0 ] of float      ) { }    """
		expect = """Program([
	VarDecl(wPP, AutoType, BinExpr(<, BinExpr(-, BinExpr(+, UnExpr(!, Id(N)), Id(dURIW)), Id(s)), BinExpr(%, Id(t), UnExpr(-, UnExpr(!, Id(r))))))
	VarDecl(v, AutoType, BinExpr(::, BinExpr(<, BinExpr(-, BinExpr(-, BinExpr(/, UnExpr(-, Id(v)), Id(O)), UnExpr(-, Id(zST))), UnExpr(!, Id(y1M))), UnExpr(-, UnExpr(!, FuncCall(WN, [])))), BinExpr(<=, BinExpr(&&, BinExpr(||, BinExpr(-, Id(VQ), Id(SB)), BinExpr(/, Id(dsko), UnExpr(-, Id(T)))), StringLit()), BinExpr(&&, BinExpr(-, BinExpr(/, UnExpr(-, Id(l)), Id(R)), UnExpr(!, Id(DX))), Id(n)))))
	FuncDecl(J, VoidType, [OutParam(H, ArrayType([0], FloatType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 673))

	def test_674(self):
		input = """u , i  : array [ 26_409 , 0 ] of float    ;   h , H , r  : integer   ;   """
		expect = """Program([
	VarDecl(u, ArrayType([26409, 0], FloatType))
	VarDecl(i, ArrayType([26409, 0], FloatType))
	VarDecl(h, IntegerType)
	VarDecl(H, IntegerType)
	VarDecl(r, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 674))

	def test_675(self):
		input = """CH : function void ( inherit MB : auto   , out f5 : string    , inherit out Fs : auto   , uha : array [ 66 , 0 ] of float     , Fn : auto    ) { }    """
		expect = """Program([
	FuncDecl(CH, VoidType, [InheritParam(MB, AutoType), OutParam(f5, StringType), InheritOutParam(Fs, AutoType), Param(uha, ArrayType([66, 0], FloatType)), Param(Fn, AutoType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 675))

	def test_676(self):
		input = """O : function string   ( ) { v  : auto  ;  }    """
		expect = """Program([
	FuncDecl(O, StringType, [], None, BlockStmt([VarDecl(v, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 676))

	def test_677(self):
		input = """V6O : function void ( out q : integer    , out w : string    , inherit V : auto   , V : string    , out _3 : float    , out L : auto    ) inherit S_ { R  : auto  ;  }    """
		expect = """Program([
	FuncDecl(V6O, VoidType, [OutParam(q, IntegerType), OutParam(w, StringType), InheritParam(V, AutoType), Param(V, StringType), OutParam(_3, FloatType), OutParam(L, AutoType)], S_, BlockStmt([VarDecl(R, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 677))

	def test_678(self):
		input = """c , o , Hoo  : array [ 0 ] of float    ;   """
		expect = """Program([
	VarDecl(c, ArrayType([0], FloatType))
	VarDecl(o, ArrayType([0], FloatType))
	VarDecl(Hoo, ArrayType([0], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 678))

	def test_679(self):
		input = """Mw : function void ( inherit out XCdlSr5 : boolean    , out Sy : array [ 4_5_400 ] of string     , inherit Q : float     ) { }    ID : function void ( ) inherit AnW { M  : auto  ;  }    O , E4P  : auto  = Xt   * Q    && ! E     / ! qR   + K        , t   + e    || G   + N     - - jG2K    && m ( )      != d      ;   Ik : function void ( ) inherit j { }    y : function void ( ) inherit z { }    i : function void ( out q : array [ 0 , 0 , 0 ] of integer     , fSK : string    , inherit bWV : array [ 16 ] of boolean      ) { }    Y : function array [ 0 , 0 ] of boolean    ( ) inherit IWyI { }    """
		expect = """Program([
	FuncDecl(Mw, VoidType, [InheritOutParam(XCdlSr5, BooleanType), OutParam(Sy, ArrayType([45400], StringType)), InheritParam(Q, FloatType)], None, BlockStmt([]))
	FuncDecl(ID, VoidType, [], AnW, BlockStmt([VarDecl(M, AutoType)]))
	VarDecl(O, AutoType, BinExpr(&&, BinExpr(*, Id(Xt), Id(Q)), BinExpr(+, BinExpr(/, UnExpr(!, Id(E)), UnExpr(!, Id(qR))), Id(K))))
	VarDecl(E4P, AutoType, BinExpr(!=, BinExpr(&&, BinExpr(||, BinExpr(+, Id(t), Id(e)), BinExpr(-, BinExpr(+, Id(G), Id(N)), UnExpr(-, Id(jG2K)))), FuncCall(m, [])), Id(d)))
	FuncDecl(Ik, VoidType, [], j, BlockStmt([]))
	FuncDecl(y, VoidType, [], z, BlockStmt([]))
	FuncDecl(i, VoidType, [OutParam(q, ArrayType([0, 0, 0], IntegerType)), Param(fSK, StringType), InheritParam(bWV, ArrayType([16], BooleanType))], None, BlockStmt([]))
	FuncDecl(Y, ArrayType([0, 0], BooleanType), [], IWyI, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 679))

	def test_680(self):
		input = """D : function auto  ( inherit out Kf : auto   , out D : array [ 12214_00 , 0 ] of boolean      ) { }    v : function auto  ( ) inherit f { }    OweF , W , Fo , c  : array [ 0 , 0 ] of boolean    = ! x   || MG     || o   + ! s0RaEM5E      <= ! ! W   + R       :: ! - C       , ! N    * ! - foq79A       :: o9 ( )    && ! x     && yY   - ehBy0    + Z   * c      > ! pqs      , ! M ( )       , oFgx ( )       ;   """
		expect = """Program([
	FuncDecl(D, AutoType, [InheritOutParam(Kf, AutoType), OutParam(D, ArrayType([1221400, 0], BooleanType))], None, BlockStmt([]))
	FuncDecl(v, AutoType, [], f, BlockStmt([]))
	VarDecl(OweF, ArrayType([0, 0], BooleanType), BinExpr(::, BinExpr(<=, BinExpr(||, BinExpr(||, UnExpr(!, Id(x)), Id(MG)), BinExpr(+, Id(o), UnExpr(!, Id(s0RaEM5E)))), BinExpr(+, UnExpr(!, UnExpr(!, Id(W))), Id(R))), UnExpr(!, UnExpr(-, Id(C)))))
	VarDecl(W, ArrayType([0, 0], BooleanType), BinExpr(::, BinExpr(*, UnExpr(!, Id(N)), UnExpr(!, UnExpr(-, Id(foq79A)))), BinExpr(>, BinExpr(&&, BinExpr(&&, FuncCall(o9, []), UnExpr(!, Id(x))), BinExpr(+, BinExpr(-, Id(yY), Id(ehBy0)), BinExpr(*, Id(Z), Id(c)))), UnExpr(!, Id(pqs)))))
	VarDecl(Fo, ArrayType([0, 0], BooleanType), UnExpr(!, FuncCall(M, [])))
	VarDecl(c, ArrayType([0, 0], BooleanType), FuncCall(oFgx, []))
])"""
		self.assertTrue(TestAST.test(input, expect, 680))

	def test_681(self):
		input = """xN5hSs  : string   ;   """
		expect = """Program([
	VarDecl(xN5hSs, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 681))

	def test_682(self):
		input = """i , G  : integer   = ! ka ( )     - ! ! v      != - VP   % J    + _       , ! ! h    && iD ( )      <= W ( )     :: ! - J     + ! T9    && d   * b         ;   """
		expect = """Program([
	VarDecl(i, IntegerType, BinExpr(!=, BinExpr(-, UnExpr(!, FuncCall(ka, [])), UnExpr(!, UnExpr(!, Id(v)))), BinExpr(+, BinExpr(%, UnExpr(-, Id(VP)), Id(J)), Id(_))))
	VarDecl(G, IntegerType, BinExpr(::, BinExpr(<=, BinExpr(&&, UnExpr(!, UnExpr(!, Id(h))), FuncCall(iD, [])), FuncCall(W, [])), BinExpr(&&, BinExpr(+, UnExpr(!, UnExpr(-, Id(J))), UnExpr(!, Id(T9))), BinExpr(*, Id(d), Id(b)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 682))

	def test_683(self):
		input = """Np : function array [ 190 ] of boolean    ( e6 : array [ 0 , 0 , 0 ] of string     , out G : float    , inherit si : array [ 4 ] of string      ) { z  : integer   ;  }    x  : integer   ;   pac4ih : function array [ 0 , 0 ] of boolean    ( ) { }    HZ : function array [ 0 , 0 , 0 ] of float    ( ) { for ( v  = - wPj5d    >= O   && rO     :: ! x3      , ""      , Fo   / P9nT     :: eH   || M    > y ( )      ) break ;     for ( Y  = It   + s8CoDN    != U   / N0      , ! Cg4jD9     :: b   || Okdj      , bax     ) IBsw ( )  ;     continue ;   }    """
		expect = """Program([
	FuncDecl(Np, ArrayType([190], BooleanType), [Param(e6, ArrayType([0, 0, 0], StringType)), OutParam(G, FloatType), InheritParam(si, ArrayType([4], StringType))], None, BlockStmt([VarDecl(z, IntegerType)]))
	VarDecl(x, IntegerType)
	FuncDecl(pac4ih, ArrayType([0, 0], BooleanType), [], None, BlockStmt([]))
	FuncDecl(HZ, ArrayType([0, 0, 0], FloatType), [], None, BlockStmt([ForStmt(AssignStmt(Id(v), BinExpr(::, BinExpr(>=, UnExpr(-, Id(wPj5d)), BinExpr(&&, Id(O), Id(rO))), UnExpr(!, Id(x3)))), StringLit(), BinExpr(::, BinExpr(/, Id(Fo), Id(P9nT)), BinExpr(>, BinExpr(||, Id(eH), Id(M)), FuncCall(y, []))), BreakStmt()), ForStmt(AssignStmt(Id(Y), BinExpr(!=, BinExpr(+, Id(It), Id(s8CoDN)), BinExpr(/, Id(U), Id(N0)))), BinExpr(::, UnExpr(!, Id(Cg4jD9)), BinExpr(||, Id(b), Id(Okdj))), Id(bax), CallStmt(IBsw, )), ContinueStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 683))

	def test_684(self):
		input = """VNK : function array [ 0 , 4 ] of string    ( ) { m  : string   ;  }    j , iAD6 , yv , Qx , NX , r , K , mtQjN9xke  : integer   ;   R , B  : auto  = ! ! Umm     || ! - KzH      < ! a0     :: k     , ! UVDzBFBH   && gv     || S   * RPeatF    || xx1   && daK4pE       :: ! g    || h   % I     + uJb       ;   """
		expect = """Program([
	FuncDecl(VNK, ArrayType([0, 4], StringType), [], None, BlockStmt([VarDecl(m, StringType)]))
	VarDecl(j, IntegerType)
	VarDecl(iAD6, IntegerType)
	VarDecl(yv, IntegerType)
	VarDecl(Qx, IntegerType)
	VarDecl(NX, IntegerType)
	VarDecl(r, IntegerType)
	VarDecl(K, IntegerType)
	VarDecl(mtQjN9xke, IntegerType)
	VarDecl(R, AutoType, BinExpr(::, BinExpr(<, BinExpr(||, UnExpr(!, UnExpr(!, Id(Umm))), UnExpr(!, UnExpr(-, Id(KzH)))), UnExpr(!, Id(a0))), Id(k)))
	VarDecl(B, AutoType, BinExpr(::, BinExpr(&&, BinExpr(||, BinExpr(||, BinExpr(&&, UnExpr(!, Id(UVDzBFBH)), Id(gv)), BinExpr(*, Id(S), Id(RPeatF))), Id(xx1)), Id(daK4pE)), BinExpr(||, UnExpr(!, Id(g)), BinExpr(+, BinExpr(%, Id(h), Id(I)), Id(uJb)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 684))

	def test_685(self):
		input = """JXTM , tQGz , E2N  : string   ;   """
		expect = """Program([
	VarDecl(JXTM, StringType)
	VarDecl(tQGz, StringType)
	VarDecl(E2N, StringType)
])"""
		self.assertTrue(TestAST.test(input, expect, 685))

	def test_686(self):
		input = """WZ  : auto  = - ! b2e    && J   / h         ;   """
		expect = """Program([
	VarDecl(WZ, AutoType, BinExpr(&&, UnExpr(-, UnExpr(!, Id(b2e))), BinExpr(/, Id(J), Id(h))))
])"""
		self.assertTrue(TestAST.test(input, expect, 686))

	def test_687(self):
		input = """N , H , uA , By  : float   = - - o   || X      <= - 0      :: p ( )    * - N    - - L        , u8   && K    && dX   % W8     || O   % OW    - 0       :: ! ! R     || K   + XU_    + eUD   % Q      < ! - ! c        , QU   * CD    + q   && wUkH     % 0     > - ! M    + a   * eCov       :: { }       , - 0     == 8    * F   && LKCj     && ! B    * - YzxJ         ;   wG : function void ( out W : array [ 0 ] of integer     , out a : float    , inherit J : integer     ) { }    """
		expect = """Program([
	VarDecl(N, FloatType, BinExpr(::, BinExpr(<=, BinExpr(||, UnExpr(-, UnExpr(-, Id(o))), Id(X)), UnExpr(-, IntegerLit(0))), BinExpr(-, BinExpr(*, FuncCall(p, []), UnExpr(-, Id(N))), UnExpr(-, Id(L)))))
	VarDecl(H, FloatType, BinExpr(::, BinExpr(||, BinExpr(&&, BinExpr(&&, Id(u8), Id(K)), BinExpr(%, Id(dX), Id(W8))), BinExpr(-, BinExpr(%, Id(O), Id(OW)), IntegerLit(0))), BinExpr(<, BinExpr(||, UnExpr(!, UnExpr(!, Id(R))), BinExpr(+, BinExpr(+, Id(K), Id(XU_)), BinExpr(%, Id(eUD), Id(Q)))), UnExpr(!, UnExpr(-, UnExpr(!, Id(c)))))))
	VarDecl(uA, FloatType, BinExpr(::, BinExpr(>, BinExpr(&&, BinExpr(+, BinExpr(*, Id(QU), Id(CD)), Id(q)), BinExpr(%, Id(wUkH), IntegerLit(0))), BinExpr(+, UnExpr(-, UnExpr(!, Id(M))), BinExpr(*, Id(a), Id(eCov)))), ArrayLit([])))
	VarDecl(By, FloatType, BinExpr(==, UnExpr(-, IntegerLit(0)), BinExpr(&&, BinExpr(&&, BinExpr(*, IntegerLit(8), Id(F)), Id(LKCj)), BinExpr(*, UnExpr(!, Id(B)), UnExpr(-, Id(YzxJ))))))
	FuncDecl(wG, VoidType, [OutParam(W, ArrayType([0], IntegerType)), OutParam(a, FloatType), InheritParam(J, IntegerType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 687))

	def test_688(self):
		input = """Q : function void ( ) { l , Qq5  : integer   ;  continue ;   if ( wt23   - x    > fjY   && X     :: RHV   && LYN    > - PA      ) continue ;     while ( ! _gZ     :: ! aZ    == - g      ) { }     }    Kut : function array [ 7 ] of integer    ( ) inherit s { }    m  : boolean   ;   """
		expect = """Program([
	FuncDecl(Q, VoidType, [], None, BlockStmt([VarDecl(l, IntegerType), VarDecl(Qq5, IntegerType), ContinueStmt(), IfStmt(BinExpr(::, BinExpr(>, BinExpr(-, Id(wt23), Id(x)), BinExpr(&&, Id(fjY), Id(X))), BinExpr(>, BinExpr(&&, Id(RHV), Id(LYN)), UnExpr(-, Id(PA)))), ContinueStmt()), WhileStmt(BinExpr(::, UnExpr(!, Id(_gZ)), BinExpr(==, UnExpr(!, Id(aZ)), UnExpr(-, Id(g)))), BlockStmt([]))]))
	FuncDecl(Kut, ArrayType([7], IntegerType), [], s, BlockStmt([]))
	VarDecl(m, BooleanType)
])"""
		self.assertTrue(TestAST.test(input, expect, 688))

	def test_689(self):
		input = """lHAP2J , m , BNi , sl  : auto  = ll   - K   && k     - { }        , r0q82UA6 ( )    || { }       :: ""    >= { }     && D7f      , d ( )      , ! s   + c     - ! c    % Q   && BycJZ         ;   R : function void ( inherit out L_W : string     ) { VP , mX  : array [ 2_42 , 3 , 3 , 0 , 0 ] of integer    ;  { return ;   }   }    """
		expect = """Program([
	VarDecl(lHAP2J, AutoType, BinExpr(&&, BinExpr(-, Id(ll), Id(K)), BinExpr(-, Id(k), ArrayLit([]))))
	VarDecl(m, AutoType, BinExpr(::, BinExpr(||, FuncCall(r0q82UA6, []), ArrayLit([])), BinExpr(>=, StringLit(), BinExpr(&&, ArrayLit([]), Id(D7f)))))
	VarDecl(BNi, AutoType, FuncCall(d, []))
	VarDecl(sl, AutoType, BinExpr(&&, BinExpr(-, BinExpr(+, UnExpr(!, Id(s)), Id(c)), BinExpr(%, UnExpr(!, Id(c)), Id(Q))), Id(BycJZ)))
	FuncDecl(R, VoidType, [InheritOutParam(L_W, StringType)], None, BlockStmt([VarDecl(VP, ArrayType([242, 3, 3, 0, 0], IntegerType)), VarDecl(mX, ArrayType([242, 3, 3, 0, 0], IntegerType)), BlockStmt([ReturnStmt()])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 689))

	def test_690(self):
		input = """R , ccBb , A  : float   ;   """
		expect = """Program([
	VarDecl(R, FloatType)
	VarDecl(ccBb, FloatType)
	VarDecl(A, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 690))

	def test_691(self):
		input = """I , UQ  : array [ 3453700_4498_4 , 0 ] of string    ;   Y  : array [ 79 , 0 ] of string    = ! Z   || WN    % - VkL       :: wa      ;   """
		expect = """Program([
	VarDecl(I, ArrayType([345370044984, 0], StringType))
	VarDecl(UQ, ArrayType([345370044984, 0], StringType))
	VarDecl(Y, ArrayType([79, 0], StringType), BinExpr(::, BinExpr(||, UnExpr(!, Id(Z)), BinExpr(%, Id(WN), UnExpr(-, Id(VkL)))), Id(wa)))
])"""
		self.assertTrue(TestAST.test(input, expect, 691))

	def test_692(self):
		input = """Q , m  : array [ 0 ] of integer    ;   """
		expect = """Program([
	VarDecl(Q, ArrayType([0], IntegerType))
	VarDecl(m, ArrayType([0], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 692))

	def test_693(self):
		input = """ny , L  : auto  = - - okQN   + vW       :: cP ( )      , ! iz   - LI9    + S   - f      > - - ! mXW       :: - v   || nhFtu     || X ( )    || J   && Pr         ;   """
		expect = """Program([
	VarDecl(ny, AutoType, BinExpr(::, BinExpr(+, UnExpr(-, UnExpr(-, Id(okQN))), Id(vW)), FuncCall(cP, [])))
	VarDecl(L, AutoType, BinExpr(::, BinExpr(>, BinExpr(-, BinExpr(+, BinExpr(-, UnExpr(!, Id(iz)), Id(LI9)), Id(S)), Id(f)), UnExpr(-, UnExpr(-, UnExpr(!, Id(mXW))))), BinExpr(&&, BinExpr(||, BinExpr(||, BinExpr(||, UnExpr(-, Id(v)), Id(nhFtu)), FuncCall(X, [])), Id(J)), Id(Pr))))
])"""
		self.assertTrue(TestAST.test(input, expect, 693))

	def test_694(self):
		input = """e : function void ( ) inherit d { uhI , G4 , fa , D  : boolean   ;  ti  = e   + Tsl    > a   / DAvzQq      ;   d , J  : array [ 1 ] of boolean    ;  Zh  : float   = ! D    <= G   - i     :: - yk    == BI3   - b       ;  for ( rn  = - SsrZ8    == ! t     :: HX   - mx    <= qhP2   / C6      , ""     :: - n      , nfg   + lu     :: ezc   / c    < PO ( )      ) { }     }    LKHa : function array [ 4_5 ] of float    ( ) inherit U { D  = HR   + B     :: 0      ;   { }   }    fW : function integer   ( h : boolean    , S : float    , Y : array [ 0 ] of boolean     , x : auto   , inherit nvZ : integer     ) inherit HG { Y , NY , _ , a  : auto  ;  if ( - m      ) break ;     do { }  while ( wJsyE   % uh    >= jsN   / eH     :: ! H      ) ;   O , Q , eL , Ti  : array [ 0 ] of boolean    = eKn   + xUwD     :: ! aT    > aO1cN   - XW      , i   + aL     :: - di      , VkS   % D      , D   || iRI    != 0       ;  }    m : function void ( inherit t : array [ 7_131_9_2611291 ] of string      ) inherit K { }    """
		expect = """Program([
	FuncDecl(e, VoidType, [], d, BlockStmt([VarDecl(uhI, BooleanType), VarDecl(G4, BooleanType), VarDecl(fa, BooleanType), VarDecl(D, BooleanType), AssignStmt(Id(ti), BinExpr(>, BinExpr(+, Id(e), Id(Tsl)), BinExpr(/, Id(a), Id(DAvzQq)))), VarDecl(d, ArrayType([1], BooleanType)), VarDecl(J, ArrayType([1], BooleanType)), VarDecl(Zh, FloatType, BinExpr(::, BinExpr(<=, UnExpr(!, Id(D)), BinExpr(-, Id(G), Id(i))), BinExpr(==, UnExpr(-, Id(yk)), BinExpr(-, Id(BI3), Id(b))))), ForStmt(AssignStmt(Id(rn), BinExpr(::, BinExpr(==, UnExpr(-, Id(SsrZ8)), UnExpr(!, Id(t))), BinExpr(<=, BinExpr(-, Id(HX), Id(mx)), BinExpr(/, Id(qhP2), Id(C6))))), BinExpr(::, StringLit(), UnExpr(-, Id(n))), BinExpr(::, BinExpr(+, Id(nfg), Id(lu)), BinExpr(<, BinExpr(/, Id(ezc), Id(c)), FuncCall(PO, []))), BlockStmt([]))]))
	FuncDecl(LKHa, ArrayType([45], FloatType), [], U, BlockStmt([AssignStmt(Id(D), BinExpr(::, BinExpr(+, Id(HR), Id(B)), IntegerLit(0))), BlockStmt([])]))
	FuncDecl(fW, IntegerType, [Param(h, BooleanType), Param(S, FloatType), Param(Y, ArrayType([0], BooleanType)), Param(x, AutoType), InheritParam(nvZ, IntegerType)], HG, BlockStmt([VarDecl(Y, AutoType), VarDecl(NY, AutoType), VarDecl(_, AutoType), VarDecl(a, AutoType), IfStmt(UnExpr(-, Id(m)), BreakStmt()), DoWhileStmt(BinExpr(::, BinExpr(>=, BinExpr(%, Id(wJsyE), Id(uh)), BinExpr(/, Id(jsN), Id(eH))), UnExpr(!, Id(H))), BlockStmt([])), VarDecl(O, ArrayType([0], BooleanType), BinExpr(::, BinExpr(+, Id(eKn), Id(xUwD)), BinExpr(>, UnExpr(!, Id(aT)), BinExpr(-, Id(aO1cN), Id(XW))))), VarDecl(Q, ArrayType([0], BooleanType), BinExpr(::, BinExpr(+, Id(i), Id(aL)), UnExpr(-, Id(di)))), VarDecl(eL, ArrayType([0], BooleanType), BinExpr(%, Id(VkS), Id(D))), VarDecl(Ti, ArrayType([0], BooleanType), BinExpr(!=, BinExpr(||, Id(D), Id(iRI)), IntegerLit(0)))]))
	FuncDecl(m, VoidType, [InheritParam(t, ArrayType([713192611291], StringType))], K, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 694))

	def test_695(self):
		input = """OFrh , k , ad  : auto  ;   """
		expect = """Program([
	VarDecl(OFrh, AutoType)
	VarDecl(k, AutoType)
	VarDecl(ad, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 695))

	def test_696(self):
		input = """BT , X , E  : string   = ! r    + RSPVPx   && A     - ! EV   && Ns       :: Sx ( )    + BG      , - k5     :: - ! ct     <= b ( )    || - r     / - v    + Dr_p   % p        , W   <= - y    && - LBH     - ! VDA    && - B       :: - ! ! L4         ;   JW : function boolean   ( X : integer    , inherit n9 : array [ 0 ] of string     , inherit out T0mR : auto   , inherit GI : array [ 8_5 ] of string     , jRk : float     ) inherit Gp { Vx  : array [ 40144 ] of boolean    ;  Bq , Z  : auto  = l     , r   || j     :: - dgCjr       ;  }    """
		expect = """Program([
	VarDecl(BT, StringType, BinExpr(::, BinExpr(&&, BinExpr(&&, BinExpr(+, UnExpr(!, Id(r)), Id(RSPVPx)), BinExpr(-, Id(A), UnExpr(!, Id(EV)))), Id(Ns)), BinExpr(+, FuncCall(Sx, []), Id(BG))))
	VarDecl(X, StringType, BinExpr(::, UnExpr(-, Id(k5)), BinExpr(<=, UnExpr(-, UnExpr(!, Id(ct))), BinExpr(||, FuncCall(b, []), BinExpr(+, BinExpr(/, UnExpr(-, Id(r)), UnExpr(-, Id(v))), BinExpr(%, Id(Dr_p), Id(p)))))))
	VarDecl(E, StringType, BinExpr(::, BinExpr(<=, Id(W), BinExpr(&&, BinExpr(&&, UnExpr(-, Id(y)), BinExpr(-, UnExpr(-, Id(LBH)), UnExpr(!, Id(VDA)))), UnExpr(-, Id(B)))), UnExpr(-, UnExpr(!, UnExpr(!, Id(L4))))))
	FuncDecl(JW, BooleanType, [Param(X, IntegerType), InheritParam(n9, ArrayType([0], StringType)), InheritOutParam(T0mR, AutoType), InheritParam(GI, ArrayType([85], StringType)), Param(jRk, FloatType)], Gp, BlockStmt([VarDecl(Vx, ArrayType([40144], BooleanType)), VarDecl(Bq, AutoType, Id(l)), VarDecl(Z, AutoType, BinExpr(::, BinExpr(||, Id(r), Id(j)), UnExpr(-, Id(dgCjr))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 696))

	def test_697(self):
		input = """Rs7e : function void ( ) inherit WPR { DBEw  : array [ 0 ] of boolean    = - h    > ! KZ     :: - v       ;  d8 , F , b , z  : boolean   = i ( )     :: k0   < q   || Cg      , ssR    :: dqr   / ry6    <= tKp   / S      , n   * C      , hV   % E     :: G   && w       ;  fMx , O  : array [ 0 , 0 ] of integer    ;  yOU , O3Z  : auto  = ! j     :: Mup   / Y    != bM   + Tttn      , BIM9 ( )    > l   * nK     :: WFH   * j    > ZJG_   + n       ;  Ja  : array [ 0 ] of integer    ;  }    TkTm  : array [ 0 , 0 , 1_97223_112 ] of float    = ! o7   % k     + ! 4      < - xm     :: ! B   / uA    || E9ls ( )      == ""    && M   * bO     / false        ;   """
		expect = """Program([
	FuncDecl(Rs7e, VoidType, [], WPR, BlockStmt([VarDecl(DBEw, ArrayType([0], BooleanType), BinExpr(::, BinExpr(>, UnExpr(-, Id(h)), UnExpr(!, Id(KZ))), UnExpr(-, Id(v)))), VarDecl(d8, BooleanType, BinExpr(::, FuncCall(i, []), BinExpr(<, Id(k0), BinExpr(||, Id(q), Id(Cg))))), VarDecl(F, BooleanType, BinExpr(::, Id(ssR), BinExpr(<=, BinExpr(/, Id(dqr), Id(ry6)), BinExpr(/, Id(tKp), Id(S))))), VarDecl(b, BooleanType, BinExpr(*, Id(n), Id(C))), VarDecl(z, BooleanType, BinExpr(::, BinExpr(%, Id(hV), Id(E)), BinExpr(&&, Id(G), Id(w)))), VarDecl(fMx, ArrayType([0, 0], IntegerType)), VarDecl(O, ArrayType([0, 0], IntegerType)), VarDecl(yOU, AutoType, BinExpr(::, UnExpr(!, Id(j)), BinExpr(!=, BinExpr(/, Id(Mup), Id(Y)), BinExpr(+, Id(bM), Id(Tttn))))), VarDecl(O3Z, AutoType, BinExpr(::, BinExpr(>, FuncCall(BIM9, []), BinExpr(*, Id(l), Id(nK))), BinExpr(>, BinExpr(*, Id(WFH), Id(j)), BinExpr(+, Id(ZJG_), Id(n))))), VarDecl(Ja, ArrayType([0], IntegerType))]))
	VarDecl(TkTm, ArrayType([0, 0, 197223112], FloatType), BinExpr(::, BinExpr(<, BinExpr(+, BinExpr(%, UnExpr(!, Id(o7)), Id(k)), UnExpr(!, IntegerLit(4))), UnExpr(-, Id(xm))), BinExpr(==, BinExpr(||, BinExpr(/, UnExpr(!, Id(B)), Id(uA)), FuncCall(E9ls, [])), BinExpr(&&, StringLit(), BinExpr(/, BinExpr(*, Id(M), Id(bO)), BooleanLit(False))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 697))

	def test_698(self):
		input = """U , q69  : integer   ;   lF  : auto  ;   """
		expect = """Program([
	VarDecl(U, IntegerType)
	VarDecl(q69, IntegerType)
	VarDecl(lF, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 698))

	def test_699(self):
		input = """J , S  : boolean   ;   """
		expect = """Program([
	VarDecl(J, BooleanType)
	VarDecl(S, BooleanType)
])"""
		self.assertTrue(TestAST.test(input, expect, 699))

	def test_700(self):
		input = """sh : function void ( ) { }    mVGH : function void ( out lbx : integer     ) { y  : integer   = z   - VI     :: G   / S    != - Fa       ;  }    """
		expect = """Program([
	FuncDecl(sh, VoidType, [], None, BlockStmt([]))
	FuncDecl(mVGH, VoidType, [OutParam(lbx, IntegerType)], None, BlockStmt([VarDecl(y, IntegerType, BinExpr(::, BinExpr(-, Id(z), Id(VI)), BinExpr(!=, BinExpr(/, Id(G), Id(S)), UnExpr(-, Id(Fa)))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 700))

	def test_701(self):
		input = """A  : integer   ;   LC , Cz  : string   ;   h : function array [ 734_22 ] of integer    ( ) inherit m { continue ;   }    """
		expect = """Program([
	VarDecl(A, IntegerType)
	VarDecl(LC, StringType)
	VarDecl(Cz, StringType)
	FuncDecl(h, ArrayType([73422], IntegerType), [], m, BlockStmt([ContinueStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 701))

	def test_702(self):
		input = """K  : array [ 0 , 0 , 28 ] of boolean    = - Zd   && z6   || kDrE       :: 507_3_309_1_33_0    > e4Hp   % - Id7    + F   - gzzL         ;   """
		expect = """Program([
	VarDecl(K, ArrayType([0, 0, 28], BooleanType), BinExpr(::, BinExpr(||, BinExpr(&&, UnExpr(-, Id(Zd)), Id(z6)), Id(kDrE)), BinExpr(>, IntegerLit(50733091330), BinExpr(-, BinExpr(+, BinExpr(%, Id(e4Hp), UnExpr(-, Id(Id7))), Id(F)), Id(gzzL)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 702))

	def test_703(self):
		input = """cRz : function void ( ) inherit V { }    """
		expect = """Program([
	FuncDecl(cRz, VoidType, [], V, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 703))

	def test_704(self):
		input = """r  : auto  = 0       ;   """
		expect = """Program([
	VarDecl(r, AutoType, IntegerLit(0))
])"""
		self.assertTrue(TestAST.test(input, expect, 704))

	def test_705(self):
		input = """T : function void ( inherit VzzR : auto   , out XmAK : float     ) inherit X { do { return ;   }  while ( - F0      ) ;   }    g0 , PO  : auto  = - zt   * OROp    || - mWzq      <= - - n    * cH   && IrN5       :: o   - ! pFO   / O      != ftqI7 ( )      , - - _Vk    - t4_        ;   """
		expect = """Program([
	FuncDecl(T, VoidType, [InheritParam(VzzR, AutoType), OutParam(XmAK, FloatType)], X, BlockStmt([DoWhileStmt(UnExpr(-, Id(F0)), BlockStmt([ReturnStmt()]))]))
	VarDecl(g0, AutoType, BinExpr(::, BinExpr(<=, BinExpr(||, BinExpr(*, UnExpr(-, Id(zt)), Id(OROp)), UnExpr(-, Id(mWzq))), BinExpr(&&, BinExpr(*, UnExpr(-, UnExpr(-, Id(n))), Id(cH)), Id(IrN5))), BinExpr(!=, BinExpr(-, Id(o), BinExpr(/, UnExpr(!, Id(pFO)), Id(O))), FuncCall(ftqI7, []))))
	VarDecl(PO, AutoType, BinExpr(-, UnExpr(-, UnExpr(-, Id(_Vk))), Id(t4_)))
])"""
		self.assertTrue(TestAST.test(input, expect, 705))

	def test_706(self):
		input = """Be , j , gu  : float   ;   x : function void ( inherit E : integer     ) { }    """
		expect = """Program([
	VarDecl(Be, FloatType)
	VarDecl(j, FloatType)
	VarDecl(gu, FloatType)
	FuncDecl(x, VoidType, [InheritParam(E, IntegerType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 706))

	def test_707(self):
		input = """A , L , j , bv  : float   = ! Q4    && hQ   && S0N     / ! ! o      < p2   && - zb     % rX      , ! ! Q ( )      <= Z5k   * M    || IKj   || iu     * - rGzaydLNy      :: - - cX   * DGm        , - h   * uk    && FF   + oZj        , ! r_    && ! m     + ! jZ    % j   || EJEg         ;   """
		expect = """Program([
	VarDecl(A, FloatType, BinExpr(<, BinExpr(&&, BinExpr(&&, UnExpr(!, Id(Q4)), Id(hQ)), BinExpr(/, Id(S0N), UnExpr(!, UnExpr(!, Id(o))))), BinExpr(&&, Id(p2), BinExpr(%, UnExpr(-, Id(zb)), Id(rX)))))
	VarDecl(L, FloatType, BinExpr(::, BinExpr(<=, UnExpr(!, UnExpr(!, FuncCall(Q, []))), BinExpr(||, BinExpr(||, BinExpr(*, Id(Z5k), Id(M)), Id(IKj)), BinExpr(*, Id(iu), UnExpr(-, Id(rGzaydLNy))))), BinExpr(*, UnExpr(-, UnExpr(-, Id(cX))), Id(DGm))))
	VarDecl(j, FloatType, BinExpr(&&, BinExpr(*, UnExpr(-, Id(h)), Id(uk)), BinExpr(+, Id(FF), Id(oZj))))
	VarDecl(bv, FloatType, BinExpr(||, BinExpr(&&, UnExpr(!, Id(r_)), BinExpr(+, UnExpr(!, Id(m)), BinExpr(%, UnExpr(!, Id(jZ)), Id(j)))), Id(EJEg)))
])"""
		self.assertTrue(TestAST.test(input, expect, 707))

	def test_708(self):
		input = """Xn : function auto  ( ) inherit u { }    XL , Oa , J  : auto  = ! - SV   && R       :: G   + A7    / _   - eo16     && o   && h    * ""      <= - _   - I3     - ! - SX        , ! ! W     % kBf2 ( )    * T   - QRP        , ""    <= - D       ;   """
		expect = """Program([
	FuncDecl(Xn, AutoType, [], u, BlockStmt([]))
	VarDecl(XL, AutoType, BinExpr(::, BinExpr(&&, UnExpr(!, UnExpr(-, Id(SV))), Id(R)), BinExpr(<=, BinExpr(&&, BinExpr(&&, BinExpr(-, BinExpr(+, Id(G), BinExpr(/, Id(A7), Id(_))), Id(eo16)), Id(o)), BinExpr(*, Id(h), StringLit())), BinExpr(-, BinExpr(-, UnExpr(-, Id(_)), Id(I3)), UnExpr(!, UnExpr(-, Id(SX)))))))
	VarDecl(Oa, AutoType, BinExpr(-, BinExpr(*, BinExpr(%, UnExpr(!, UnExpr(!, Id(W))), FuncCall(kBf2, [])), Id(T)), Id(QRP)))
	VarDecl(J, AutoType, BinExpr(<=, StringLit(), UnExpr(-, Id(D))))
])"""
		self.assertTrue(TestAST.test(input, expect, 708))

	def test_709(self):
		input = """h : function array [ 7356941 , 0 ] of integer    ( inherit out d : auto    ) { do { Ql , o  : array [ 0 ] of boolean    ;  }  while ( R0   || yD    > s   + Z     :: C   || L    <= - co      ) ;   }    _G : function auto  ( inherit KKn : auto   , out SS : array [ 31 , 0 , 0 , 561 , 1 ] of integer      ) inherit pK { og , F , x , W  : integer   = f   - _    > ! j5     :: e   || ag      , l   * t    < s   * K      , LgH   / _BwCR      , o   && Hc       ;  }    u : function array [ 0 ] of boolean    ( inherit Y : array [ 0 , 0 ] of boolean     , inherit out H : integer     ) { }    Rr , W , ScRw  : auto  = ! x   % F    - a   - NW      == z ( )    * lH9      , ! - ebx     - - g0   - zv_      <= ! z4 ( )     % ! Q    * ! z        , ""    || - Y   * S      != ! g   && p    + I   && j         ;   """
		expect = """Program([
	FuncDecl(h, ArrayType([7356941, 0], IntegerType), [InheritOutParam(d, AutoType)], None, BlockStmt([DoWhileStmt(BinExpr(::, BinExpr(>, BinExpr(||, Id(R0), Id(yD)), BinExpr(+, Id(s), Id(Z))), BinExpr(<=, BinExpr(||, Id(C), Id(L)), UnExpr(-, Id(co)))), BlockStmt([VarDecl(Ql, ArrayType([0], BooleanType)), VarDecl(o, ArrayType([0], BooleanType))]))]))
	FuncDecl(_G, AutoType, [InheritParam(KKn, AutoType), OutParam(SS, ArrayType([31, 0, 0, 561, 1], IntegerType))], pK, BlockStmt([VarDecl(og, IntegerType, BinExpr(::, BinExpr(>, BinExpr(-, Id(f), Id(_)), UnExpr(!, Id(j5))), BinExpr(||, Id(e), Id(ag)))), VarDecl(F, IntegerType, BinExpr(<, BinExpr(*, Id(l), Id(t)), BinExpr(*, Id(s), Id(K)))), VarDecl(x, IntegerType, BinExpr(/, Id(LgH), Id(_BwCR))), VarDecl(W, IntegerType, BinExpr(&&, Id(o), Id(Hc)))]))
	FuncDecl(u, ArrayType([0], BooleanType), [InheritParam(Y, ArrayType([0, 0], BooleanType)), InheritOutParam(H, IntegerType)], None, BlockStmt([]))
	VarDecl(Rr, AutoType, BinExpr(==, BinExpr(-, BinExpr(-, BinExpr(%, UnExpr(!, Id(x)), Id(F)), Id(a)), Id(NW)), BinExpr(*, FuncCall(z, []), Id(lH9))))
	VarDecl(W, AutoType, BinExpr(<=, BinExpr(-, BinExpr(-, UnExpr(!, UnExpr(-, Id(ebx))), UnExpr(-, Id(g0))), Id(zv_)), BinExpr(*, BinExpr(%, UnExpr(!, FuncCall(z4, [])), UnExpr(!, Id(Q))), UnExpr(!, Id(z)))))
	VarDecl(ScRw, AutoType, BinExpr(!=, BinExpr(||, StringLit(), BinExpr(*, UnExpr(-, Id(Y)), Id(S))), BinExpr(&&, BinExpr(&&, UnExpr(!, Id(g)), BinExpr(+, Id(p), Id(I))), Id(j))))
])"""
		self.assertTrue(TestAST.test(input, expect, 709))

	def test_710(self):
		input = """x , nLqT  : auto  = - { }        , - O2   && V8k    && z1 ( )      != ! X   - al_Rq6    % UaP   || OH       :: ! T       ;   """
		expect = """Program([
	VarDecl(x, AutoType, UnExpr(-, ArrayLit([])))
	VarDecl(nLqT, AutoType, BinExpr(::, BinExpr(!=, BinExpr(&&, BinExpr(&&, UnExpr(-, Id(O2)), Id(V8k)), FuncCall(z1, [])), BinExpr(||, BinExpr(-, UnExpr(!, Id(X)), BinExpr(%, Id(al_Rq6), Id(UaP))), Id(OH))), UnExpr(!, Id(T))))
])"""
		self.assertTrue(TestAST.test(input, expect, 710))

	def test_711(self):
		input = """q : function void ( ) inherit B { }    ws  : array [ 0 , 45_54_0 ] of boolean    ;   F  : auto  ;   """
		expect = """Program([
	FuncDecl(q, VoidType, [], B, BlockStmt([]))
	VarDecl(ws, ArrayType([0, 45540], BooleanType))
	VarDecl(F, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 711))

	def test_712(self):
		input = """Q : function integer   ( out c : array [ 0 ] of string     , inherit out r : boolean     ) { j , XS  : array [ 0 ] of integer    = ! mK    != ! Np7      , jF   && A       ;  }    pB3  : boolean   = ! - - bcf      > d ( )     :: - F    && q   % n     || xaptOWd   - Y    * X   * h      != ! uG   && KxI     / d   / eTBI    * 4         ;   b0C , D  : auto  ;   QFU : function void ( inherit M : auto   , inherit tseA : auto    ) { }    """
		expect = """Program([
	FuncDecl(Q, IntegerType, [OutParam(c, ArrayType([0], StringType)), InheritOutParam(r, BooleanType)], None, BlockStmt([VarDecl(j, ArrayType([0], IntegerType), BinExpr(!=, UnExpr(!, Id(mK)), UnExpr(!, Id(Np7)))), VarDecl(XS, ArrayType([0], IntegerType), BinExpr(&&, Id(jF), Id(A)))]))
	VarDecl(pB3, BooleanType, BinExpr(::, BinExpr(>, UnExpr(!, UnExpr(-, UnExpr(-, Id(bcf)))), FuncCall(d, [])), BinExpr(!=, BinExpr(||, BinExpr(&&, UnExpr(-, Id(F)), BinExpr(%, Id(q), Id(n))), BinExpr(-, Id(xaptOWd), BinExpr(*, BinExpr(*, Id(Y), Id(X)), Id(h)))), BinExpr(&&, UnExpr(!, Id(uG)), BinExpr(*, BinExpr(/, BinExpr(/, Id(KxI), Id(d)), Id(eTBI)), IntegerLit(4))))))
	VarDecl(b0C, AutoType)
	VarDecl(D, AutoType)
	FuncDecl(QFU, VoidType, [InheritParam(M, AutoType), InheritParam(tseA, AutoType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 712))

	def test_713(self):
		input = """XSZp , v  : array [ 0 , 848 ] of float    ;   """
		expect = """Program([
	VarDecl(XSZp, ArrayType([0, 848], FloatType))
	VarDecl(v, ArrayType([0, 848], FloatType))
])"""
		self.assertTrue(TestAST.test(input, expect, 713))

	def test_714(self):
		input = """kj , WIL  : array [ 1 ] of integer    = qb     , ! b       ;   """
		expect = """Program([
	VarDecl(kj, ArrayType([1], IntegerType), Id(qb))
	VarDecl(WIL, ArrayType([1], IntegerType), UnExpr(!, Id(b)))
])"""
		self.assertTrue(TestAST.test(input, expect, 714))

	def test_715(self):
		input = """me , r  : float   ;   """
		expect = """Program([
	VarDecl(me, FloatType)
	VarDecl(r, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 715))

	def test_716(self):
		input = """L : function array [ 6 ] of integer    ( ) { }    tcm  : auto  = ! ! rG    || _9   / DS       :: K1JC   - To    - ZgX    - ! PAxfi   && bu      <= ! rK   || GSH    || Z   % k         ;   """
		expect = """Program([
	FuncDecl(L, ArrayType([6], IntegerType), [], None, BlockStmt([]))
	VarDecl(tcm, AutoType, BinExpr(::, BinExpr(||, UnExpr(!, UnExpr(!, Id(rG))), BinExpr(/, Id(_9), Id(DS))), BinExpr(<=, BinExpr(&&, BinExpr(-, BinExpr(-, BinExpr(-, Id(K1JC), Id(To)), Id(ZgX)), UnExpr(!, Id(PAxfi))), Id(bu)), BinExpr(||, BinExpr(||, UnExpr(!, Id(rK)), Id(GSH)), BinExpr(%, Id(Z), Id(k))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 716))

	def test_717(self):
		input = """JS1ZK  : array [ 0 ] of string    = - gug   + OB1o     - Rr ( )     < ! Mq   - y    + c2      :: ! - ! R      != - h   % h     - - HcMYm   && FG3         ;   _  : array [ 0 ] of integer    ;   """
		expect = """Program([
	VarDecl(JS1ZK, ArrayType([0], StringType), BinExpr(::, BinExpr(<, BinExpr(-, BinExpr(+, UnExpr(-, Id(gug)), Id(OB1o)), FuncCall(Rr, [])), BinExpr(+, BinExpr(-, UnExpr(!, Id(Mq)), Id(y)), Id(c2))), BinExpr(!=, UnExpr(!, UnExpr(-, UnExpr(!, Id(R)))), BinExpr(&&, BinExpr(-, BinExpr(%, UnExpr(-, Id(h)), Id(h)), UnExpr(-, Id(HcMYm))), Id(FG3)))))
	VarDecl(_, ArrayType([0], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 717))

	def test_718(self):
		input = """Pj : function array [ 610 ] of string    ( inherit out Pe : array [ 8_8 ] of integer     , out PnR : boolean     ) { }    Y1m : function void ( ) { }    """
		expect = """Program([
	FuncDecl(Pj, ArrayType([610], StringType), [InheritOutParam(Pe, ArrayType([88], IntegerType)), OutParam(PnR, BooleanType)], None, BlockStmt([]))
	FuncDecl(Y1m, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 718))

	def test_719(self):
		input = """Tp  : auto  ;   FC , z , O1 , Co_ , F , HeB , I , x  : auto  ;   f  : auto  = On   > ! ! k    && - VK         ;   """
		expect = """Program([
	VarDecl(Tp, AutoType)
	VarDecl(FC, AutoType)
	VarDecl(z, AutoType)
	VarDecl(O1, AutoType)
	VarDecl(Co_, AutoType)
	VarDecl(F, AutoType)
	VarDecl(HeB, AutoType)
	VarDecl(I, AutoType)
	VarDecl(x, AutoType)
	VarDecl(f, AutoType, BinExpr(>, Id(On), BinExpr(&&, UnExpr(!, UnExpr(!, Id(k))), UnExpr(-, Id(VK)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 719))

	def test_720(self):
		input = """K : function array [ 0 ] of float    ( inherit out lC : integer    , out M : array [ 8 ] of string      ) inherit s { }    U : function void ( ) inherit t { { continue ;   return ;   }   }    _JSZ3w , Ft  : auto  ;   """
		expect = """Program([
	FuncDecl(K, ArrayType([0], FloatType), [InheritOutParam(lC, IntegerType), OutParam(M, ArrayType([8], StringType))], s, BlockStmt([]))
	FuncDecl(U, VoidType, [], t, BlockStmt([BlockStmt([ContinueStmt(), ReturnStmt()])]))
	VarDecl(_JSZ3w, AutoType)
	VarDecl(Ft, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 720))

	def test_721(self):
		input = """Y  : array [ 3_5555 , 0 , 0 , 0 , 43_07_211855 , 0 , 0 , 0 ] of string    = 0       ;   """
		expect = """Program([
	VarDecl(Y, ArrayType([35555, 0, 0, 0, 4307211855, 0, 0, 0], StringType), IntegerLit(0))
])"""
		self.assertTrue(TestAST.test(input, expect, 721))

	def test_722(self):
		input = """Wf  : auto  = ce ( )    || { }         ;   C : function array [ 197 , 0 ] of integer    ( inherit GO30 : boolean     ) inherit R4 { fwO , T  : auto  = f   * _    == ! CS      , - Y     :: - D       ;  }    G_Ruh : function void ( ) inherit L { while ( vHcz   / P    > - _K      ) break ;     break ;   }    """
		expect = """Program([
	VarDecl(Wf, AutoType, BinExpr(||, FuncCall(ce, []), ArrayLit([])))
	FuncDecl(C, ArrayType([197, 0], IntegerType), [InheritParam(GO30, BooleanType)], R4, BlockStmt([VarDecl(fwO, AutoType, BinExpr(==, BinExpr(*, Id(f), Id(_)), UnExpr(!, Id(CS)))), VarDecl(T, AutoType, BinExpr(::, UnExpr(-, Id(Y)), UnExpr(-, Id(D))))]))
	FuncDecl(G_Ruh, VoidType, [], L, BlockStmt([WhileStmt(BinExpr(>, BinExpr(/, Id(vHcz), Id(P)), UnExpr(-, Id(_K))), BreakStmt()), BreakStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 722))

	def test_723(self):
		input = """y , ak  : array [ 395 ] of float    ;   v4  : array [ 0 ] of string    ;   """
		expect = """Program([
	VarDecl(y, ArrayType([395], FloatType))
	VarDecl(ak, ArrayType([395], FloatType))
	VarDecl(v4, ArrayType([0], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 723))

	def test_724(self):
		input = """me , Da  : auto  ;   """
		expect = """Program([
	VarDecl(me, AutoType)
	VarDecl(Da, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 724))

	def test_725(self):
		input = """p : function void ( inherit q : float    , Qm : array [ 10_8 ] of float      ) inherit Y { }    T  : boolean   = ! - E    && - j       :: ! - k     + ! k    - 2         ;   gg : function void ( inherit K : array [ 1677 ] of float     , out x : float     ) inherit GU { { continue ;   x ( )  ;   break ;   return ;   }   }    """
		expect = """Program([
	FuncDecl(p, VoidType, [InheritParam(q, FloatType), Param(Qm, ArrayType([108], FloatType))], Y, BlockStmt([]))
	VarDecl(T, BooleanType, BinExpr(::, BinExpr(&&, UnExpr(!, UnExpr(-, Id(E))), UnExpr(-, Id(j))), BinExpr(-, BinExpr(+, UnExpr(!, UnExpr(-, Id(k))), UnExpr(!, Id(k))), IntegerLit(2))))
	FuncDecl(gg, VoidType, [InheritParam(K, ArrayType([1677], FloatType)), OutParam(x, FloatType)], GU, BlockStmt([BlockStmt([ContinueStmt(), CallStmt(x, ), BreakStmt(), ReturnStmt()])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 725))

	def test_726(self):
		input = """LH  : boolean   = - c    && e   + O     - wd   && m    % ! S      != ! G   - _    + VFp   && S       :: ! FgcR2w    && aY   + o     - Hr9q   - A_    && lb   + pK         ;   bhnS4H  : float   = - - yn     / P9Xe63   / M    * J   && u       :: - ! wVzFW   * nnw      > ! o   * x     % c   * T    + 3         ;   """
		expect = """Program([
	VarDecl(LH, BooleanType, BinExpr(::, BinExpr(!=, BinExpr(&&, BinExpr(&&, UnExpr(-, Id(c)), BinExpr(-, BinExpr(+, Id(e), Id(O)), Id(wd))), BinExpr(%, Id(m), UnExpr(!, Id(S)))), BinExpr(&&, BinExpr(+, BinExpr(-, UnExpr(!, Id(G)), Id(_)), Id(VFp)), Id(S))), BinExpr(&&, BinExpr(&&, UnExpr(!, Id(FgcR2w)), BinExpr(-, BinExpr(-, BinExpr(+, Id(aY), Id(o)), Id(Hr9q)), Id(A_))), BinExpr(+, Id(lb), Id(pK)))))
	VarDecl(bhnS4H, FloatType, BinExpr(::, BinExpr(&&, BinExpr(*, BinExpr(/, BinExpr(/, UnExpr(-, UnExpr(-, Id(yn))), Id(P9Xe63)), Id(M)), Id(J)), Id(u)), BinExpr(>, BinExpr(*, UnExpr(-, UnExpr(!, Id(wVzFW))), Id(nnw)), BinExpr(+, BinExpr(*, BinExpr(%, BinExpr(*, UnExpr(!, Id(o)), Id(x)), Id(c)), Id(T)), IntegerLit(3)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 726))

	def test_727(self):
		input = """BA : function array [ 3_00_53 ] of boolean    ( ) { if ( P   % M    >= r   - X      ) return ;     }    bilCI : function auto  ( ) inherit xC { return - o    == j0JjX6   - k      ;   C , QH75  : array [ 6 , 0 , 5_28_413 , 9 ] of boolean    = VRj   / B6     :: - K4      , RU   - g    > t   || u     :: RE   % VRHnKwKs       ;  }    """
		expect = """Program([
	FuncDecl(BA, ArrayType([30053], BooleanType), [], None, BlockStmt([IfStmt(BinExpr(>=, BinExpr(%, Id(P), Id(M)), BinExpr(-, Id(r), Id(X))), ReturnStmt())]))
	FuncDecl(bilCI, AutoType, [], xC, BlockStmt([ReturnStmt(BinExpr(==, UnExpr(-, Id(o)), BinExpr(-, Id(j0JjX6), Id(k)))), VarDecl(C, ArrayType([6, 0, 528413, 9], BooleanType), BinExpr(::, BinExpr(/, Id(VRj), Id(B6)), UnExpr(-, Id(K4)))), VarDecl(QH75, ArrayType([6, 0, 528413, 9], BooleanType), BinExpr(::, BinExpr(>, BinExpr(-, Id(RU), Id(g)), BinExpr(||, Id(t), Id(u))), BinExpr(%, Id(RE), Id(VRHnKwKs))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 727))

	def test_728(self):
		input = """h , G , SZ7 , zZ , _ , X  : array [ 91126 ] of boolean    ;   """
		expect = """Program([
	VarDecl(h, ArrayType([91126], BooleanType))
	VarDecl(G, ArrayType([91126], BooleanType))
	VarDecl(SZ7, ArrayType([91126], BooleanType))
	VarDecl(zZ, ArrayType([91126], BooleanType))
	VarDecl(_, ArrayType([91126], BooleanType))
	VarDecl(X, ArrayType([91126], BooleanType))
])"""
		self.assertTrue(TestAST.test(input, expect, 728))

	def test_729(self):
		input = """k , N  : array [ 2_04_6_9_7_6_3_59 ] of boolean    ;   P_  : array [ 24 , 0 , 0 ] of float    = ! D   + J    + Qri   - nj      == ! - h     + ! E   + k         ;   C : function void ( inherit out W8g : auto    ) inherit S { }    cs , i , R , W , hd , T , d , vQ , BI , O  : boolean   = ! ! xc     - eCub     :: ! c   % R     + false       , - xVF   * hM2A    || - W       :: H1R   * c    * - Q     && ! F    || E4   && i        , G ( )      , ! Or    + Jj    / bG0 ( )    * b   || _        , o   || FZR    - w   && e     / ! ! C        , V ( )    % ! wP    / - nF       :: L ( )    > ! V8H      , - B_    * t      , C   % ! I    - ! _       :: ! X   + vAOmY6Q    % Nq   - dP      > ! Ge   && X     - y   - Dwcjr4    + w   && Nb        , - ""    / - Sc        , ! bL   && F     + ! ! bI         ;   """
		expect = """Program([
	VarDecl(k, ArrayType([2046976359], BooleanType))
	VarDecl(N, ArrayType([2046976359], BooleanType))
	VarDecl(P_, ArrayType([24, 0, 0], FloatType), BinExpr(==, BinExpr(-, BinExpr(+, BinExpr(+, UnExpr(!, Id(D)), Id(J)), Id(Qri)), Id(nj)), BinExpr(+, BinExpr(+, UnExpr(!, UnExpr(-, Id(h))), UnExpr(!, Id(E))), Id(k))))
	FuncDecl(C, VoidType, [InheritOutParam(W8g, AutoType)], S, BlockStmt([]))
	VarDecl(cs, BooleanType, BinExpr(::, BinExpr(-, UnExpr(!, UnExpr(!, Id(xc))), Id(eCub)), BinExpr(+, BinExpr(%, UnExpr(!, Id(c)), Id(R)), BooleanLit(False))))
	VarDecl(i, BooleanType, BinExpr(::, BinExpr(||, BinExpr(*, UnExpr(-, Id(xVF)), Id(hM2A)), UnExpr(-, Id(W))), BinExpr(&&, BinExpr(||, BinExpr(&&, BinExpr(*, BinExpr(*, Id(H1R), Id(c)), UnExpr(-, Id(Q))), UnExpr(!, Id(F))), Id(E4)), Id(i))))
	VarDecl(R, BooleanType, FuncCall(G, []))
	VarDecl(W, BooleanType, BinExpr(||, BinExpr(+, UnExpr(!, Id(Or)), BinExpr(*, BinExpr(/, Id(Jj), FuncCall(bG0, [])), Id(b))), Id(_)))
	VarDecl(hd, BooleanType, BinExpr(&&, BinExpr(||, Id(o), BinExpr(-, Id(FZR), Id(w))), BinExpr(/, Id(e), UnExpr(!, UnExpr(!, Id(C))))))
	VarDecl(T, BooleanType, BinExpr(::, BinExpr(/, BinExpr(%, FuncCall(V, []), UnExpr(!, Id(wP))), UnExpr(-, Id(nF))), BinExpr(>, FuncCall(L, []), UnExpr(!, Id(V8H)))))
	VarDecl(d, BooleanType, BinExpr(*, UnExpr(-, Id(B_)), Id(t)))
	VarDecl(vQ, BooleanType, BinExpr(::, BinExpr(-, BinExpr(%, Id(C), UnExpr(!, Id(I))), UnExpr(!, Id(_))), BinExpr(>, BinExpr(-, BinExpr(+, UnExpr(!, Id(X)), BinExpr(%, Id(vAOmY6Q), Id(Nq))), Id(dP)), BinExpr(&&, BinExpr(&&, UnExpr(!, Id(Ge)), BinExpr(+, BinExpr(-, BinExpr(-, Id(X), Id(y)), Id(Dwcjr4)), Id(w))), Id(Nb)))))
	VarDecl(BI, BooleanType, BinExpr(/, UnExpr(-, StringLit()), UnExpr(-, Id(Sc))))
	VarDecl(O, BooleanType, BinExpr(&&, UnExpr(!, Id(bL)), BinExpr(+, Id(F), UnExpr(!, UnExpr(!, Id(bI))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 729))

	def test_730(self):
		input = """T0 , x  : float   ;   """
		expect = """Program([
	VarDecl(T0, FloatType)
	VarDecl(x, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 730))

	def test_731(self):
		input = """e , fW , nuwLQ  : array [ 0 ] of string    ;   eNa7 : function array [ 88 , 9 , 59 ] of float    ( out xn : string    , HO : auto   , _ : auto    ) inherit x { }    """
		expect = """Program([
	VarDecl(e, ArrayType([0], StringType))
	VarDecl(fW, ArrayType([0], StringType))
	VarDecl(nuwLQ, ArrayType([0], StringType))
	FuncDecl(eNa7, ArrayType([88, 9, 59], FloatType), [OutParam(xn, StringType), Param(HO, AutoType), Param(_, AutoType)], x, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 731))

	def test_732(self):
		input = """r : function integer   ( ) { }    """
		expect = """Program([
	FuncDecl(r, IntegerType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 732))

	def test_733(self):
		input = """F5 : function void ( Dl : string    , out Mg8 : auto   , inherit S : auto    ) inherit c { { continue ;   break ;   T , Bn , iKc  : array [ 609570_78_9 ] of string    ;  }   return ;   Se0  : auto  ;  jWlzHF , f0OlezpRbe , OZ , Eb , M , il  : auto  = B   || oaLP      , - l    != Qn    :: ol ( )    <= - hD      , B   && Wy    < w     , z   - K     :: B   - G      , b   || HR     :: loFgh ( )      , Hp3tf8w   % F    == sD   || n       ;  }    qo9ox  : auto  = p    :: ! B   / uWrv    + ! sV7x         ;   """
		expect = """Program([
	FuncDecl(F5, VoidType, [Param(Dl, StringType), OutParam(Mg8, AutoType), InheritParam(S, AutoType)], c, BlockStmt([BlockStmt([ContinueStmt(), BreakStmt(), VarDecl(T, ArrayType([609570789], StringType)), VarDecl(Bn, ArrayType([609570789], StringType)), VarDecl(iKc, ArrayType([609570789], StringType))]), ReturnStmt(), VarDecl(Se0, AutoType), VarDecl(jWlzHF, AutoType, BinExpr(||, Id(B), Id(oaLP))), VarDecl(f0OlezpRbe, AutoType, BinExpr(::, BinExpr(!=, UnExpr(-, Id(l)), Id(Qn)), BinExpr(<=, FuncCall(ol, []), UnExpr(-, Id(hD))))), VarDecl(OZ, AutoType, BinExpr(<, BinExpr(&&, Id(B), Id(Wy)), Id(w))), VarDecl(Eb, AutoType, BinExpr(::, BinExpr(-, Id(z), Id(K)), BinExpr(-, Id(B), Id(G)))), VarDecl(M, AutoType, BinExpr(::, BinExpr(||, Id(b), Id(HR)), FuncCall(loFgh, []))), VarDecl(il, AutoType, BinExpr(==, BinExpr(%, Id(Hp3tf8w), Id(F)), BinExpr(||, Id(sD), Id(n))))]))
	VarDecl(qo9ox, AutoType, BinExpr(::, Id(p), BinExpr(+, BinExpr(/, UnExpr(!, Id(B)), Id(uWrv)), UnExpr(!, Id(sV7x)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 733))

	def test_734(self):
		input = """E  : auto  = j9In8Th ( )       ;   """
		expect = """Program([
	VarDecl(E, AutoType, FuncCall(j9In8Th, []))
])"""
		self.assertTrue(TestAST.test(input, expect, 734))

	def test_735(self):
		input = """xc , c  : auto  ;   """
		expect = """Program([
	VarDecl(xc, AutoType)
	VarDecl(c, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 735))

	def test_736(self):
		input = """S : function auto  ( out Z : string    , inherit u2F : boolean     ) { }    b  : array [ 0 , 0 ] of boolean    = Z ( )     :: ! Son   && Kl     + - C   && d      >= - i    - X   || d    * - aC         ;   Y , Y , SrC  : auto  ;   MNr  : auto  ;   FS , Nm  : auto  = ! - BgH    && X   && Jr      != - false       , - ocR    + ""     || ! Mm   - A       :: c   * Bec    - H   % c     % ! erX    - ""         ;   """
		expect = """Program([
	FuncDecl(S, AutoType, [OutParam(Z, StringType), InheritParam(u2F, BooleanType)], None, BlockStmt([]))
	VarDecl(b, ArrayType([0, 0], BooleanType), BinExpr(::, FuncCall(Z, []), BinExpr(>=, BinExpr(&&, BinExpr(&&, UnExpr(!, Id(Son)), BinExpr(+, Id(Kl), UnExpr(-, Id(C)))), Id(d)), BinExpr(||, BinExpr(-, UnExpr(-, Id(i)), Id(X)), BinExpr(*, Id(d), UnExpr(-, Id(aC)))))))
	VarDecl(Y, AutoType)
	VarDecl(Y, AutoType)
	VarDecl(SrC, AutoType)
	VarDecl(MNr, AutoType)
	VarDecl(FS, AutoType, BinExpr(!=, BinExpr(&&, BinExpr(&&, UnExpr(!, UnExpr(-, Id(BgH))), Id(X)), Id(Jr)), UnExpr(-, BooleanLit(False))))
	VarDecl(Nm, AutoType, BinExpr(::, BinExpr(||, BinExpr(+, UnExpr(-, Id(ocR)), StringLit()), BinExpr(-, UnExpr(!, Id(Mm)), Id(A))), BinExpr(-, BinExpr(-, BinExpr(*, Id(c), Id(Bec)), BinExpr(%, BinExpr(%, Id(H), Id(c)), UnExpr(!, Id(erX)))), StringLit())))
])"""
		self.assertTrue(TestAST.test(input, expect, 736))

	def test_737(self):
		input = """k9  : integer   = - z   - i    % mA   - GP      >= y ( )    - ! - M         ;   """
		expect = """Program([
	VarDecl(k9, IntegerType, BinExpr(>=, BinExpr(-, BinExpr(-, UnExpr(-, Id(z)), BinExpr(%, Id(i), Id(mA))), Id(GP)), BinExpr(-, FuncCall(y, []), UnExpr(!, UnExpr(-, Id(M))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 737))

	def test_738(self):
		input = """z , BZ  : auto  ;   """
		expect = """Program([
	VarDecl(z, AutoType)
	VarDecl(BZ, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 738))

	def test_739(self):
		input = """Y : function void ( _UT : auto    ) { Mg , j , UH  : array [ 0 ] of string    = i   / OQ      , - j     :: u   && cj    < - lwc3      , PHVc   || s       ;  vM , t0 , fdw , iF  : auto  ;  }    """
		expect = """Program([
	FuncDecl(Y, VoidType, [Param(_UT, AutoType)], None, BlockStmt([VarDecl(Mg, ArrayType([0], StringType), BinExpr(/, Id(i), Id(OQ))), VarDecl(j, ArrayType([0], StringType), BinExpr(::, UnExpr(-, Id(j)), BinExpr(<, BinExpr(&&, Id(u), Id(cj)), UnExpr(-, Id(lwc3))))), VarDecl(UH, ArrayType([0], StringType), BinExpr(||, Id(PHVc), Id(s))), VarDecl(vM, AutoType), VarDecl(t0, AutoType), VarDecl(fdw, AutoType), VarDecl(iF, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 739))

	def test_740(self):
		input = """gc4 , vf , s , b , Aj_ , VV  : float   ;   T  : float   ;   """
		expect = """Program([
	VarDecl(gc4, FloatType)
	VarDecl(vf, FloatType)
	VarDecl(s, FloatType)
	VarDecl(b, FloatType)
	VarDecl(Aj_, FloatType)
	VarDecl(VV, FloatType)
	VarDecl(T, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 740))

	def test_741(self):
		input = """m : function array [ 0 ] of integer    ( out u : auto   , v : array [ 9 ] of string      ) inherit a { }    """
		expect = """Program([
	FuncDecl(m, ArrayType([0], IntegerType), [OutParam(u, AutoType), Param(v, ArrayType([9], StringType))], a, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 741))

	def test_742(self):
		input = """T : function void ( ) { }    MtsP , I  : auto  ;   """
		expect = """Program([
	FuncDecl(T, VoidType, [], None, BlockStmt([]))
	VarDecl(MtsP, AutoType)
	VarDecl(I, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 742))

	def test_743(self):
		input = """k , d  : array [ 7_4 ] of string    = - AS4HS   - p    % dMSa8   || K09       :: ROh   * i    * G   - j     * wE3qbC   || i    - ! Lw        , Ki   + ""    * ! Y      == kU   || ! eZ    || - T         ;   """
		expect = """Program([
	VarDecl(k, ArrayType([74], StringType), BinExpr(::, BinExpr(||, BinExpr(-, UnExpr(-, Id(AS4HS)), BinExpr(%, Id(p), Id(dMSa8))), Id(K09)), BinExpr(||, BinExpr(-, BinExpr(*, BinExpr(*, Id(ROh), Id(i)), Id(G)), BinExpr(*, Id(j), Id(wE3qbC))), BinExpr(-, Id(i), UnExpr(!, Id(Lw))))))
	VarDecl(d, ArrayType([74], StringType), BinExpr(==, BinExpr(+, Id(Ki), BinExpr(*, StringLit(), UnExpr(!, Id(Y)))), BinExpr(||, BinExpr(||, Id(kU), UnExpr(!, Id(eZ))), UnExpr(-, Id(T)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 743))

	def test_744(self):
		input = """u1V , EDY , Cw , N , HlW  : string   ;   na : function void ( ) { }    M65fB : function void ( inherit Cs : array [ 0 , 0 ] of integer      ) inherit u { k3  : array [ 5_00 ] of float    = F   && QO    <= ""     :: jcN   - e26l6       ;  }    g : function array [ 0 ] of boolean    ( ) inherit P { }    """
		expect = """Program([
	VarDecl(u1V, StringType)
	VarDecl(EDY, StringType)
	VarDecl(Cw, StringType)
	VarDecl(N, StringType)
	VarDecl(HlW, StringType)
	FuncDecl(na, VoidType, [], None, BlockStmt([]))
	FuncDecl(M65fB, VoidType, [InheritParam(Cs, ArrayType([0, 0], IntegerType))], u, BlockStmt([VarDecl(k3, ArrayType([500], FloatType), BinExpr(::, BinExpr(<=, BinExpr(&&, Id(F), Id(QO)), StringLit()), BinExpr(-, Id(jcN), Id(e26l6))))]))
	FuncDecl(g, ArrayType([0], BooleanType), [], P, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 744))

	def test_745(self):
		input = """ejYX  : string   = j   || w    * r   + I     + t7   % d1    / f   % Lxi      != ! lfIR   && lS     || O ( )      :: - W   && wD    && ! ig         ;   Js : function void ( E : auto   , out s : auto    ) { }    W : function array [ 0 ] of string    ( ) inherit ROs { G  : auto  ;  { return ;   xF , LS , T  : boolean   ;  break ;   D ( )  ;   }   F  : array [ 1 ] of float    ;  }    YPZ : function void ( ) { X  : auto  ;  }    """
		expect = """Program([
	VarDecl(ejYX, StringType, BinExpr(::, BinExpr(!=, BinExpr(||, Id(j), BinExpr(+, BinExpr(+, BinExpr(*, Id(w), Id(r)), Id(I)), BinExpr(%, BinExpr(/, BinExpr(%, Id(t7), Id(d1)), Id(f)), Id(Lxi)))), BinExpr(||, BinExpr(&&, UnExpr(!, Id(lfIR)), Id(lS)), FuncCall(O, []))), BinExpr(&&, BinExpr(&&, UnExpr(-, Id(W)), Id(wD)), UnExpr(!, Id(ig)))))
	FuncDecl(Js, VoidType, [Param(E, AutoType), OutParam(s, AutoType)], None, BlockStmt([]))
	FuncDecl(W, ArrayType([0], StringType), [], ROs, BlockStmt([VarDecl(G, AutoType), BlockStmt([ReturnStmt(), VarDecl(xF, BooleanType), VarDecl(LS, BooleanType), VarDecl(T, BooleanType), BreakStmt(), CallStmt(D, )]), VarDecl(F, ArrayType([1], FloatType))]))
	FuncDecl(YPZ, VoidType, [], None, BlockStmt([VarDecl(X, AutoType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 745))

	def test_746(self):
		input = """S : function auto  ( inherit tEB : array [ 653476_56_6 , 4 , 0 ] of string      ) inherit v { }    kZ , Z , VmTHAE , Gx  : array [ 4 , 89 , 9 ] of float    = c   + Y    + QM   - dhd     % ! - yR      >= ! ! u     && 2    || ""       :: - y ( )       , 0     :: - ! F     && y_      , ! T   && I    && ! t      <= u5     , ! F3    || pc7   * jC     * - ! zP4      == Js   * oO    + mK   && Rm     - - rM        ;   """
		expect = """Program([
	FuncDecl(S, AutoType, [InheritParam(tEB, ArrayType([653476566, 4, 0], StringType))], v, BlockStmt([]))
	VarDecl(kZ, ArrayType([4, 89, 9], FloatType), BinExpr(::, BinExpr(>=, BinExpr(-, BinExpr(+, BinExpr(+, Id(c), Id(Y)), Id(QM)), BinExpr(%, Id(dhd), UnExpr(!, UnExpr(-, Id(yR))))), BinExpr(||, BinExpr(&&, UnExpr(!, UnExpr(!, Id(u))), IntegerLit(2)), StringLit())), UnExpr(-, FuncCall(y, []))))
	VarDecl(Z, ArrayType([4, 89, 9], FloatType), BinExpr(::, IntegerLit(0), BinExpr(&&, UnExpr(-, UnExpr(!, Id(F))), Id(y_))))
	VarDecl(VmTHAE, ArrayType([4, 89, 9], FloatType), BinExpr(<=, BinExpr(&&, BinExpr(&&, UnExpr(!, Id(T)), Id(I)), UnExpr(!, Id(t))), Id(u5)))
	VarDecl(Gx, ArrayType([4, 89, 9], FloatType), BinExpr(==, BinExpr(||, UnExpr(!, Id(F3)), BinExpr(*, BinExpr(*, Id(pc7), Id(jC)), UnExpr(-, UnExpr(!, Id(zP4))))), BinExpr(&&, BinExpr(+, BinExpr(*, Id(Js), Id(oO)), Id(mK)), BinExpr(-, Id(Rm), UnExpr(-, Id(rM))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 746))

	def test_747(self):
		input = """Y : function void ( ) { }    """
		expect = """Program([
	FuncDecl(Y, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 747))

	def test_748(self):
		input = """b_ , ir , N , Su  : array [ 0 ] of string    ;   """
		expect = """Program([
	VarDecl(b_, ArrayType([0], StringType))
	VarDecl(ir, ArrayType([0], StringType))
	VarDecl(N, ArrayType([0], StringType))
	VarDecl(Su, ArrayType([0], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 748))

	def test_749(self):
		input = """W : function array [ 36 , 37 , 0 ] of boolean    ( out Qcz7D4Rsb : array [ 76_3_0 , 0 ] of boolean     , inherit m : float     ) inherit _ { continue ;   WP  : auto  = G   || z    > - OE       ;  }    m , Y , W  : array [ 13_87 , 0 ] of float    = MjQI   - r1    || - lznHOA     % BUY   / HRvVJ    - - so       :: ! P ( )     / Qza   / V    || - Ckr0M        , 0    >= U3H     , - K   % V    + vR   + x       :: ox14      ;   wV , D2  : float   = ! ! k   * O3Q      > EP   / UaIm2Mi    / ! TJ     + G ( )       , - ! jR    % q   % ac6       :: ! - kH     - vE3       ;   ey , us  : array [ 83 , 1_1 ] of float    = - S1   % f     || - mEM    && Cj0nM   - bJ3      > - DW    / z   || P8     - n     :: - ! W    || ""        , - ! L     - 36      :: - ! Ko    * v   * f         ;   J : function void ( inherit Wo : auto    ) { Hf , VdC5  : boolean   ;  }    """
		expect = """Program([
	FuncDecl(W, ArrayType([36, 37, 0], BooleanType), [OutParam(Qcz7D4Rsb, ArrayType([7630, 0], BooleanType)), InheritParam(m, FloatType)], _, BlockStmt([ContinueStmt(), VarDecl(WP, AutoType, BinExpr(>, BinExpr(||, Id(G), Id(z)), UnExpr(-, Id(OE))))]))
	VarDecl(m, ArrayType([1387, 0], FloatType), BinExpr(::, BinExpr(||, BinExpr(-, Id(MjQI), Id(r1)), BinExpr(-, BinExpr(/, BinExpr(%, UnExpr(-, Id(lznHOA)), Id(BUY)), Id(HRvVJ)), UnExpr(-, Id(so)))), BinExpr(||, BinExpr(/, BinExpr(/, UnExpr(!, FuncCall(P, [])), Id(Qza)), Id(V)), UnExpr(-, Id(Ckr0M)))))
	VarDecl(Y, ArrayType([1387, 0], FloatType), BinExpr(>=, IntegerLit(0), Id(U3H)))
	VarDecl(W, ArrayType([1387, 0], FloatType), BinExpr(::, BinExpr(+, BinExpr(+, BinExpr(%, UnExpr(-, Id(K)), Id(V)), Id(vR)), Id(x)), Id(ox14)))
	VarDecl(wV, FloatType, BinExpr(>, BinExpr(*, UnExpr(!, UnExpr(!, Id(k))), Id(O3Q)), BinExpr(+, BinExpr(/, BinExpr(/, Id(EP), Id(UaIm2Mi)), UnExpr(!, Id(TJ))), FuncCall(G, []))))
	VarDecl(D2, FloatType, BinExpr(::, BinExpr(%, BinExpr(%, UnExpr(-, UnExpr(!, Id(jR))), Id(q)), Id(ac6)), BinExpr(-, UnExpr(!, UnExpr(-, Id(kH))), Id(vE3))))
	VarDecl(ey, ArrayType([83, 11], FloatType), BinExpr(::, BinExpr(>, BinExpr(&&, BinExpr(||, BinExpr(%, UnExpr(-, Id(S1)), Id(f)), UnExpr(-, Id(mEM))), BinExpr(-, Id(Cj0nM), Id(bJ3))), BinExpr(||, BinExpr(/, UnExpr(-, Id(DW)), Id(z)), BinExpr(-, Id(P8), Id(n)))), BinExpr(||, UnExpr(-, UnExpr(!, Id(W))), StringLit())))
	VarDecl(us, ArrayType([83, 11], FloatType), BinExpr(::, BinExpr(-, UnExpr(-, UnExpr(!, Id(L))), IntegerLit(36)), BinExpr(*, BinExpr(*, UnExpr(-, UnExpr(!, Id(Ko))), Id(v)), Id(f))))
	FuncDecl(J, VoidType, [InheritParam(Wo, AutoType)], None, BlockStmt([VarDecl(Hf, BooleanType), VarDecl(VdC5, BooleanType)]))
])"""
		self.assertTrue(TestAST.test(input, expect, 749))

	def test_750(self):
		input = """t  : float   = - u   && t1     && ! - g       :: 0       ;   """
		expect = """Program([
	VarDecl(t, FloatType, BinExpr(::, BinExpr(&&, BinExpr(&&, UnExpr(-, Id(u)), Id(t1)), UnExpr(!, UnExpr(-, Id(g)))), IntegerLit(0)))
])"""
		self.assertTrue(TestAST.test(input, expect, 750))

	def test_751(self):
		input = """z , u  : boolean   ;   """
		expect = """Program([
	VarDecl(z, BooleanType)
	VarDecl(u, BooleanType)
])"""
		self.assertTrue(TestAST.test(input, expect, 751))

	def test_752(self):
		input = """n  : array [ 0 , 40 , 2_1_935_1_207 ] of float    = - - - a      < ! MNmav   - O     * true        ;   """
		expect = """Program([
	VarDecl(n, ArrayType([0, 40, 219351207], FloatType), BinExpr(<, UnExpr(-, UnExpr(-, UnExpr(-, Id(a)))), BinExpr(-, UnExpr(!, Id(MNmav)), BinExpr(*, Id(O), BooleanLit(True)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 752))

	def test_753(self):
		input = """Et  : array [ 7 , 0 ] of string    = - ! gf     * Yo_   * Zj    || GW   && T         ;   """
		expect = """Program([
	VarDecl(Et, ArrayType([7, 0], StringType), BinExpr(&&, BinExpr(||, BinExpr(*, BinExpr(*, UnExpr(-, UnExpr(!, Id(gf))), Id(Yo_)), Id(Zj)), Id(GW)), Id(T)))
])"""
		self.assertTrue(TestAST.test(input, expect, 753))

	def test_754(self):
		input = """j , _  : boolean   ;   Sj , Z , u  : float   = - - q   || Dq        , - - B    / _U   / Rxx      != ! Ihm    - IX   % Ggc     && ! LHP   / PgMTzk       :: - f   || Sd     && O ( )     <= ! g ( )       , yL   / g    % n0   * YQ     + ""    - k   * n      < ! n    || Mr   * e     * uf   + - RrZ       :: ! - T    && K   * H         ;   """
		expect = """Program([
	VarDecl(j, BooleanType)
	VarDecl(_, BooleanType)
	VarDecl(Sj, FloatType, BinExpr(||, UnExpr(-, UnExpr(-, Id(q))), Id(Dq)))
	VarDecl(Z, FloatType, BinExpr(::, BinExpr(!=, BinExpr(/, BinExpr(/, UnExpr(-, UnExpr(-, Id(B))), Id(_U)), Id(Rxx)), BinExpr(&&, BinExpr(-, UnExpr(!, Id(Ihm)), BinExpr(%, Id(IX), Id(Ggc))), BinExpr(/, UnExpr(!, Id(LHP)), Id(PgMTzk)))), BinExpr(<=, BinExpr(&&, BinExpr(||, UnExpr(-, Id(f)), Id(Sd)), FuncCall(O, [])), UnExpr(!, FuncCall(g, [])))))
	VarDecl(u, FloatType, BinExpr(::, BinExpr(<, BinExpr(-, BinExpr(+, BinExpr(*, BinExpr(%, BinExpr(/, Id(yL), Id(g)), Id(n0)), Id(YQ)), StringLit()), BinExpr(*, Id(k), Id(n))), BinExpr(||, UnExpr(!, Id(n)), BinExpr(+, BinExpr(*, BinExpr(*, Id(Mr), Id(e)), Id(uf)), UnExpr(-, Id(RrZ))))), BinExpr(&&, UnExpr(!, UnExpr(-, Id(T))), BinExpr(*, Id(K), Id(H)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 754))

	def test_755(self):
		input = """O : function float   ( out k1 : auto    ) inherit o { }    s : function array [ 43_903_5_60 ] of string    ( out w : array [ 82_7 ] of string      ) { { }   continue ;   }    N , wn  : float   = - d    + S   || Qmn9IAV     && - ! QF2       :: z ( )      , MwA   && ! h     && ! JwTln        ;   """
		expect = """Program([
	FuncDecl(O, FloatType, [OutParam(k1, AutoType)], o, BlockStmt([]))
	FuncDecl(s, ArrayType([43903560], StringType), [OutParam(w, ArrayType([827], StringType))], None, BlockStmt([BlockStmt([]), ContinueStmt()]))
	VarDecl(N, FloatType, BinExpr(::, BinExpr(&&, BinExpr(||, BinExpr(+, UnExpr(-, Id(d)), Id(S)), Id(Qmn9IAV)), UnExpr(-, UnExpr(!, Id(QF2)))), FuncCall(z, [])))
	VarDecl(wn, FloatType, BinExpr(&&, BinExpr(&&, Id(MwA), UnExpr(!, Id(h))), UnExpr(!, Id(JwTln))))
])"""
		self.assertTrue(TestAST.test(input, expect, 755))

	def test_756(self):
		input = """knc : function void ( ) inherit N { qy  : float   = ! a    <= - U       ;  while ( ! Jb      ) break ;     }    """
		expect = """Program([
	FuncDecl(knc, VoidType, [], N, BlockStmt([VarDecl(qy, FloatType, BinExpr(<=, UnExpr(!, Id(a)), UnExpr(-, Id(U)))), WhileStmt(UnExpr(!, Id(Jb)), BreakStmt())]))
])"""
		self.assertTrue(TestAST.test(input, expect, 756))

	def test_757(self):
		input = """Ro2e , kT7 , L  : array [ 0 , 6_04299_7661 , 1 , 0 , 3466_633_5_86 , 52 , 0 , 593431 ] of integer    = true     :: - Hn    / b ( )     - G   && G    + Y   && VOX        , { }     + 53     <= - ! M8    + ""        , ! ""    + OS   && t      == ! hN7   && K     || lK ( )        ;   b , xXD  : auto  ;   Q , cIt , Auu  : array [ 0 ] of float    = ! - V    % IsB   && eo       :: - x    / - rj     / HZ   / - f        , f0jj_j   % ! SZBz    || ! Y      >= ""      , ! A    && F ( )     - ! _3U     >= ! Rf    % mG   || OP7G    || K   % hStRVMbcML       :: 1    % _   + G     + G8   + o    * wgHt   * n      <= S   || O    * B3qUL47A   || G     - ! - qJ         ;   """
		expect = """Program([
	VarDecl(Ro2e, ArrayType([0, 6042997661, 1, 0, 3466633586, 52, 0, 593431], IntegerType), BinExpr(::, BooleanLit(True), BinExpr(&&, BinExpr(&&, BinExpr(-, BinExpr(/, UnExpr(-, Id(Hn)), FuncCall(b, [])), Id(G)), BinExpr(+, Id(G), Id(Y))), Id(VOX))))
	VarDecl(kT7, ArrayType([0, 6042997661, 1, 0, 3466633586, 52, 0, 593431], IntegerType), BinExpr(<=, BinExpr(+, ArrayLit([]), IntegerLit(53)), BinExpr(+, UnExpr(-, UnExpr(!, Id(M8))), StringLit())))
	VarDecl(L, ArrayType([0, 6042997661, 1, 0, 3466633586, 52, 0, 593431], IntegerType), BinExpr(==, BinExpr(&&, BinExpr(+, UnExpr(!, StringLit()), Id(OS)), Id(t)), BinExpr(||, BinExpr(&&, UnExpr(!, Id(hN7)), Id(K)), FuncCall(lK, []))))
	VarDecl(b, AutoType)
	VarDecl(xXD, AutoType)
	VarDecl(Q, ArrayType([0], FloatType), BinExpr(::, BinExpr(&&, BinExpr(%, UnExpr(!, UnExpr(-, Id(V))), Id(IsB)), Id(eo)), BinExpr(/, BinExpr(/, BinExpr(/, UnExpr(-, Id(x)), UnExpr(-, Id(rj))), Id(HZ)), UnExpr(-, Id(f)))))
	VarDecl(cIt, ArrayType([0], FloatType), BinExpr(>=, BinExpr(||, BinExpr(%, Id(f0jj_j), UnExpr(!, Id(SZBz))), UnExpr(!, Id(Y))), StringLit()))
	VarDecl(Auu, ArrayType([0], FloatType), BinExpr(::, BinExpr(>=, BinExpr(&&, UnExpr(!, Id(A)), BinExpr(-, FuncCall(F, []), UnExpr(!, Id(_3U)))), BinExpr(||, BinExpr(||, BinExpr(%, UnExpr(!, Id(Rf)), Id(mG)), Id(OP7G)), BinExpr(%, Id(K), Id(hStRVMbcML)))), BinExpr(<=, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(%, IntegerLit(1), Id(_)), Id(G)), Id(G8)), BinExpr(*, BinExpr(*, Id(o), Id(wgHt)), Id(n))), BinExpr(||, BinExpr(||, Id(S), BinExpr(*, Id(O), Id(B3qUL47A))), BinExpr(-, Id(G), UnExpr(!, UnExpr(-, Id(qJ))))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 757))

	def test_758(self):
		input = """T : function void ( ) { }    mX : function void ( inherit v : auto    ) inherit Nh { v  : auto  = oI   + iw    != y   || C       ;  }    L7x2 , e , e  : auto  ;   FVW8TP3  : array [ 0 , 0 ] of string    ;   """
		expect = """Program([
	FuncDecl(T, VoidType, [], None, BlockStmt([]))
	FuncDecl(mX, VoidType, [InheritParam(v, AutoType)], Nh, BlockStmt([VarDecl(v, AutoType, BinExpr(!=, BinExpr(+, Id(oI), Id(iw)), BinExpr(||, Id(y), Id(C))))]))
	VarDecl(L7x2, AutoType)
	VarDecl(e, AutoType)
	VarDecl(e, AutoType)
	VarDecl(FVW8TP3, ArrayType([0, 0], StringType))
])"""
		self.assertTrue(TestAST.test(input, expect, 758))

	def test_759(self):
		input = """rPX , p , aZ  : auto  ;   """
		expect = """Program([
	VarDecl(rPX, AutoType)
	VarDecl(p, AutoType)
	VarDecl(aZ, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 759))

	def test_760(self):
		input = """AnbD , RO , A4D  : boolean   ;   """
		expect = """Program([
	VarDecl(AnbD, BooleanType)
	VarDecl(RO, BooleanType)
	VarDecl(A4D, BooleanType)
])"""
		self.assertTrue(TestAST.test(input, expect, 760))

	def test_761(self):
		input = """U , gb  : string   ;   t  : array [ 28_33 ] of string    = ! q8   || s    || g   * M         ;   C : function void ( N : array [ 3_2_419 , 7_0002_526 , 0 , 0 , 8 ] of boolean     , out v : auto    ) inherit Po { Gh , Ty , A9  : array [ 3 , 0 ] of float    ;  o  : string   ;  break ;   }    i : function string   ( rDJ : string     ) inherit w { }    """
		expect = """Program([
	VarDecl(U, StringType)
	VarDecl(gb, StringType)
	VarDecl(t, ArrayType([2833], StringType), BinExpr(||, BinExpr(||, UnExpr(!, Id(q8)), Id(s)), BinExpr(*, Id(g), Id(M))))
	FuncDecl(C, VoidType, [Param(N, ArrayType([32419, 70002526, 0, 0, 8], BooleanType)), OutParam(v, AutoType)], Po, BlockStmt([VarDecl(Gh, ArrayType([3, 0], FloatType)), VarDecl(Ty, ArrayType([3, 0], FloatType)), VarDecl(A9, ArrayType([3, 0], FloatType)), VarDecl(o, StringType), BreakStmt()]))
	FuncDecl(i, StringType, [Param(rDJ, StringType)], w, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 761))

	def test_762(self):
		input = """i  : integer   ;   """
		expect = """Program([
	VarDecl(i, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 762))

	def test_763(self):
		input = """z : function auto  ( le : auto    ) inherit iE2 { }    """
		expect = """Program([
	FuncDecl(z, AutoType, [Param(le, AutoType)], iE2, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 763))

	def test_764(self):
		input = """q  : array [ 0 , 0 ] of integer    = - K ( )      :: ! h48    + - ASe     || ! GT    || F   + Lazw8f      == MR   && Lf    % ""     + - o    && A   || nfT         ;   """
		expect = """Program([
	VarDecl(q, ArrayType([0, 0], IntegerType), BinExpr(::, UnExpr(-, FuncCall(K, [])), BinExpr(==, BinExpr(||, BinExpr(||, BinExpr(+, UnExpr(!, Id(h48)), UnExpr(-, Id(ASe))), UnExpr(!, Id(GT))), BinExpr(+, Id(F), Id(Lazw8f))), BinExpr(||, BinExpr(&&, BinExpr(&&, Id(MR), BinExpr(+, BinExpr(%, Id(Lf), StringLit()), UnExpr(-, Id(o)))), Id(A)), Id(nfT)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 764))

	def test_765(self):
		input = """U : function void ( inherit out rFs : float     ) inherit x { return ;   L , z , P , qTR  : auto  = GD6   || _    < sk4   % tbd      , I   - q     :: a   * R    == - p      , F    :: QHq   % f    == otd   - CB      , Wtd   * _eIEI       ;  { continue ;   }   continue ;   do { { break ;   }   break ;   cT3d ( )  ;   }  while ( BYcy   - c7F4R0H      ) ;   I5 , P  : auto  = 4     :: - e    != - T9NQ      , CAOM ( )       ;  zU0rO2cm , X , v  : auto  = gW   && e      , B   - GSx    <= Q   % F     :: ! hOST      , xL ( )    <= B7qb   % K     :: bH   && FY    != d   && fr       ;  }    t , F  : array [ 60_8 , 882_0 , 7 , 4 ] of integer    ;   """
		expect = """Program([
	FuncDecl(U, VoidType, [InheritOutParam(rFs, FloatType)], x, BlockStmt([ReturnStmt(), VarDecl(L, AutoType, BinExpr(<, BinExpr(||, Id(GD6), Id(_)), BinExpr(%, Id(sk4), Id(tbd)))), VarDecl(z, AutoType, BinExpr(::, BinExpr(-, Id(I), Id(q)), BinExpr(==, BinExpr(*, Id(a), Id(R)), UnExpr(-, Id(p))))), VarDecl(P, AutoType, BinExpr(::, Id(F), BinExpr(==, BinExpr(%, Id(QHq), Id(f)), BinExpr(-, Id(otd), Id(CB))))), VarDecl(qTR, AutoType, BinExpr(*, Id(Wtd), Id(_eIEI))), BlockStmt([ContinueStmt()]), ContinueStmt(), DoWhileStmt(BinExpr(-, Id(BYcy), Id(c7F4R0H)), BlockStmt([BlockStmt([BreakStmt()]), BreakStmt(), CallStmt(cT3d, )])), VarDecl(I5, AutoType, BinExpr(::, IntegerLit(4), BinExpr(!=, UnExpr(-, Id(e)), UnExpr(-, Id(T9NQ))))), VarDecl(P, AutoType, FuncCall(CAOM, [])), VarDecl(zU0rO2cm, AutoType, BinExpr(&&, Id(gW), Id(e))), VarDecl(X, AutoType, BinExpr(::, BinExpr(<=, BinExpr(-, Id(B), Id(GSx)), BinExpr(%, Id(Q), Id(F))), UnExpr(!, Id(hOST)))), VarDecl(v, AutoType, BinExpr(::, BinExpr(<=, FuncCall(xL, []), BinExpr(%, Id(B7qb), Id(K))), BinExpr(!=, BinExpr(&&, Id(bH), Id(FY)), BinExpr(&&, Id(d), Id(fr)))))]))
	VarDecl(t, ArrayType([608, 8820, 7, 4], IntegerType))
	VarDecl(F, ArrayType([608, 8820, 7, 4], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 765))

	def test_766(self):
		input = """CB  : boolean   = ! a6T   * w   || ZgY       :: tJO   * E8    + S   && zN     / Jzjm ( )     <= ! - d    - dri   / z         ;   c , y9G , u  : float   = ! 0    / QM   && A        , - Fi   + W    && ! S7Si       :: - ! - h      <= PTNh ( )      , - A0B6   + xY     + D ( )      :: ! - Kq    + x   || mAhu      > true       ;   """
		expect = """Program([
	VarDecl(CB, BooleanType, BinExpr(::, BinExpr(||, BinExpr(*, UnExpr(!, Id(a6T)), Id(w)), Id(ZgY)), BinExpr(<=, BinExpr(&&, BinExpr(+, BinExpr(*, Id(tJO), Id(E8)), Id(S)), BinExpr(/, Id(zN), FuncCall(Jzjm, []))), BinExpr(-, UnExpr(!, UnExpr(-, Id(d))), BinExpr(/, Id(dri), Id(z))))))
	VarDecl(c, FloatType, BinExpr(&&, BinExpr(/, UnExpr(!, IntegerLit(0)), Id(QM)), Id(A)))
	VarDecl(y9G, FloatType, BinExpr(::, BinExpr(&&, BinExpr(+, UnExpr(-, Id(Fi)), Id(W)), UnExpr(!, Id(S7Si))), BinExpr(<=, UnExpr(-, UnExpr(!, UnExpr(-, Id(h)))), FuncCall(PTNh, []))))
	VarDecl(u, FloatType, BinExpr(::, BinExpr(+, BinExpr(+, UnExpr(-, Id(A0B6)), Id(xY)), FuncCall(D, [])), BinExpr(>, BinExpr(||, BinExpr(+, UnExpr(!, UnExpr(-, Id(Kq))), Id(x)), Id(mAhu)), BooleanLit(True))))
])"""
		self.assertTrue(TestAST.test(input, expect, 766))

	def test_767(self):
		input = """B : function void ( I : array [ 0 ] of boolean     , O : auto   , AuQr : array [ 0 , 3845 , 2_51 , 0 ] of boolean     , f : boolean    , inherit yx : float    , inherit E : auto    ) { }    EB : function void ( ) { }    n : function string   ( ) { }    """
		expect = """Program([
	FuncDecl(B, VoidType, [Param(I, ArrayType([0], BooleanType)), Param(O, AutoType), Param(AuQr, ArrayType([0, 3845, 251, 0], BooleanType)), Param(f, BooleanType), InheritParam(yx, FloatType), InheritParam(E, AutoType)], None, BlockStmt([]))
	FuncDecl(EB, VoidType, [], None, BlockStmt([]))
	FuncDecl(n, StringType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 767))

	def test_768(self):
		input = """o : function float   ( ) inherit Hm { x  : array [ 9_5_51 ] of string    ;  DP , Q_l  : array [ 0 ] of integer    ;  do { }  while ( Y   || qL      ) ;   }    """
		expect = """Program([
	FuncDecl(o, FloatType, [], Hm, BlockStmt([VarDecl(x, ArrayType([9551], StringType)), VarDecl(DP, ArrayType([0], IntegerType)), VarDecl(Q_l, ArrayType([0], IntegerType)), DoWhileStmt(BinExpr(||, Id(Y), Id(qL)), BlockStmt([]))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 768))

	def test_769(self):
		input = """JN : function void ( out W : array [ 0 , 6 ] of integer     , inherit z : auto    ) { A  : array [ 2_5 ] of string    ;  }    """
		expect = """Program([
	FuncDecl(JN, VoidType, [OutParam(W, ArrayType([0, 6], IntegerType)), InheritParam(z, AutoType)], None, BlockStmt([VarDecl(A, ArrayType([25], StringType))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 769))

	def test_770(self):
		input = """h  : array [ 0 ] of integer    = .E-904    != l   || pj    && ""     * ""      :: ! ! K3B     + d   || I    + KX   && d         ;   """
		expect = """Program([
	VarDecl(h, ArrayType([0], IntegerType), BinExpr(::, BinExpr(!=, FloatLit(0.0), BinExpr(&&, BinExpr(||, Id(l), Id(pj)), BinExpr(*, StringLit(), StringLit()))), BinExpr(&&, BinExpr(||, BinExpr(+, UnExpr(!, UnExpr(!, Id(K3B))), Id(d)), BinExpr(+, Id(I), Id(KX))), Id(d))))
])"""
		self.assertTrue(TestAST.test(input, expect, 770))

	def test_771(self):
		input = """N_o : function void ( ) inherit H5eJg { }    k2  : array [ 1 , 0 ] of boolean    ;   JH9 : function void ( ) { }    """
		expect = """Program([
	FuncDecl(N_o, VoidType, [], H5eJg, BlockStmt([]))
	VarDecl(k2, ArrayType([1, 0], BooleanType))
	FuncDecl(JH9, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 771))

	def test_772(self):
		input = """T : function array [ 0 ] of float    ( ) { }    LJ : function void ( ) { gKCP , k  : array [ 0 ] of string    ;  jZCLqR  : auto  ;  }    e : function boolean   ( inherit uR2 : array [ 6_9_0 , 704 ] of string      ) { e  = ! d    < M_voaS   || f     :: de   || G      ;   }    O  : integer   ;   W : function array [ 123_15_5_8_6736_4_46_694_1749 , 0 ] of boolean    ( out q : array [ 6_82 , 0 , 197 , 5 , 0 ] of integer      ) { }    Rd , K , Ff  : array [ 0 , 0 , 0 ] of string    ;   O : function float   ( Fjm : auto   , px : auto    ) { }    ltF : function void ( inherit out G : auto    ) inherit T { o  : auto  = R   && F    != - h       ;  }    """
		expect = """Program([
	FuncDecl(T, ArrayType([0], FloatType), [], None, BlockStmt([]))
	FuncDecl(LJ, VoidType, [], None, BlockStmt([VarDecl(gKCP, ArrayType([0], StringType)), VarDecl(k, ArrayType([0], StringType)), VarDecl(jZCLqR, AutoType)]))
	FuncDecl(e, BooleanType, [InheritParam(uR2, ArrayType([690, 704], StringType))], None, BlockStmt([AssignStmt(Id(e), BinExpr(::, BinExpr(<, UnExpr(!, Id(d)), BinExpr(||, Id(M_voaS), Id(f))), BinExpr(||, Id(de), Id(G))))]))
	VarDecl(O, IntegerType)
	FuncDecl(W, ArrayType([123155867364466941749, 0], BooleanType), [OutParam(q, ArrayType([682, 0, 197, 5, 0], IntegerType))], None, BlockStmt([]))
	VarDecl(Rd, ArrayType([0, 0, 0], StringType))
	VarDecl(K, ArrayType([0, 0, 0], StringType))
	VarDecl(Ff, ArrayType([0, 0, 0], StringType))
	FuncDecl(O, FloatType, [Param(Fjm, AutoType), Param(px, AutoType)], None, BlockStmt([]))
	FuncDecl(ltF, VoidType, [InheritOutParam(G, AutoType)], T, BlockStmt([VarDecl(o, AutoType, BinExpr(!=, BinExpr(&&, Id(R), Id(F)), UnExpr(-, Id(h))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 772))

	def test_773(self):
		input = """g3 : function auto  ( inherit P : auto    ) { for ( q  = ZX0e   / Cl3x    <= ! S      , - F      , ""      ) continue ;     yTz , Y  : auto  = Ex9   || Q      , w0 ( )    > W   || FFWfzt     :: TqI   + D    == - I       ;  Pa , ff8  : auto  ;  }    H : function void ( inherit M : array [ 97 , 89_8 ] of boolean     , inherit out C : array [ 0 , 9_75 ] of string      ) { T , _ , No  : array [ 0 ] of boolean    = t     , g   / e    <= - lm      , KCx   - Cx     :: K3J   + o    > PXd ( )       ;  Gw  : auto  = V_   || a       ;  break ;   }    """
		expect = """Program([
	FuncDecl(g3, AutoType, [InheritParam(P, AutoType)], None, BlockStmt([ForStmt(AssignStmt(Id(q), BinExpr(<=, BinExpr(/, Id(ZX0e), Id(Cl3x)), UnExpr(!, Id(S)))), UnExpr(-, Id(F)), StringLit(), ContinueStmt()), VarDecl(yTz, AutoType, BinExpr(||, Id(Ex9), Id(Q))), VarDecl(Y, AutoType, BinExpr(::, BinExpr(>, FuncCall(w0, []), BinExpr(||, Id(W), Id(FFWfzt))), BinExpr(==, BinExpr(+, Id(TqI), Id(D)), UnExpr(-, Id(I))))), VarDecl(Pa, AutoType), VarDecl(ff8, AutoType)]))
	FuncDecl(H, VoidType, [InheritParam(M, ArrayType([97, 898], BooleanType)), InheritOutParam(C, ArrayType([0, 975], StringType))], None, BlockStmt([VarDecl(T, ArrayType([0], BooleanType), Id(t)), VarDecl(_, ArrayType([0], BooleanType), BinExpr(<=, BinExpr(/, Id(g), Id(e)), UnExpr(-, Id(lm)))), VarDecl(No, ArrayType([0], BooleanType), BinExpr(::, BinExpr(-, Id(KCx), Id(Cx)), BinExpr(>, BinExpr(+, Id(K3J), Id(o)), FuncCall(PXd, [])))), VarDecl(Gw, AutoType, BinExpr(||, Id(V_), Id(a))), BreakStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 773))

	def test_774(self):
		input = """M : function void ( inherit y2a : auto   , h : float     ) { }    """
		expect = """Program([
	FuncDecl(M, VoidType, [InheritParam(y2a, AutoType), Param(h, FloatType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 774))

	def test_775(self):
		input = """LQuj  : array [ 0 ] of integer    ;   """
		expect = """Program([
	VarDecl(LQuj, ArrayType([0], IntegerType))
])"""
		self.assertTrue(TestAST.test(input, expect, 775))

	def test_776(self):
		input = """KCRP : function auto  ( ) { }    i : function void ( ) { }    """
		expect = """Program([
	FuncDecl(KCRP, AutoType, [], None, BlockStmt([]))
	FuncDecl(i, VoidType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 776))

	def test_777(self):
		input = """F : function auto  ( inherit D5 : array [ 0 , 0 , 6_095 ] of integer     , out qP : auto    ) inherit ZG { fqb  = w   && E    >= - pd     :: pzR   - WYJVA    < xV   && DvQ      ;   j  : auto  = ""    > - x     :: Q   && h9    < ""       ;  QLAX  = v9   > QEV9l   - sU     :: XwgWmP   + i    >= s03   / D      ;   }    """
		expect = """Program([
	FuncDecl(F, AutoType, [InheritParam(D5, ArrayType([0, 0, 6095], IntegerType)), OutParam(qP, AutoType)], ZG, BlockStmt([AssignStmt(Id(fqb), BinExpr(::, BinExpr(>=, BinExpr(&&, Id(w), Id(E)), UnExpr(-, Id(pd))), BinExpr(<, BinExpr(-, Id(pzR), Id(WYJVA)), BinExpr(&&, Id(xV), Id(DvQ))))), VarDecl(j, AutoType, BinExpr(::, BinExpr(>, StringLit(), UnExpr(-, Id(x))), BinExpr(<, BinExpr(&&, Id(Q), Id(h9)), StringLit()))), AssignStmt(Id(QLAX), BinExpr(::, BinExpr(>, Id(v9), BinExpr(-, Id(QEV9l), Id(sU))), BinExpr(>=, BinExpr(+, Id(XwgWmP), Id(i)), BinExpr(/, Id(s03), Id(D)))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 777))

	def test_778(self):
		input = """N , M , e1  : string   = R   + I    - ! xHDO     + - oX ( )      <= - ! M    % ! z       :: - l    * Qd      , V   * ! Gs   - WFVK      >= ! QfT      , ! y   && TmXIXh    + qc   % Z      > Ln   && E6In   || eHM_     && cgg   || ZU    + F   || k       :: W   && Y    % n   % gP     + V ( )     > - K   - Gqt2D    && I_   + w         ;   """
		expect = """Program([
	VarDecl(N, StringType, BinExpr(::, BinExpr(<=, BinExpr(+, BinExpr(-, BinExpr(+, Id(R), Id(I)), UnExpr(!, Id(xHDO))), UnExpr(-, FuncCall(oX, []))), BinExpr(%, UnExpr(-, UnExpr(!, Id(M))), UnExpr(!, Id(z)))), BinExpr(*, UnExpr(-, Id(l)), Id(Qd))))
	VarDecl(M, StringType, BinExpr(>=, BinExpr(-, BinExpr(*, Id(V), UnExpr(!, Id(Gs))), Id(WFVK)), UnExpr(!, Id(QfT))))
	VarDecl(e1, StringType, BinExpr(::, BinExpr(>, BinExpr(&&, UnExpr(!, Id(y)), BinExpr(+, Id(TmXIXh), BinExpr(%, Id(qc), Id(Z)))), BinExpr(||, BinExpr(||, BinExpr(&&, BinExpr(||, BinExpr(&&, Id(Ln), Id(E6In)), Id(eHM_)), Id(cgg)), BinExpr(+, Id(ZU), Id(F))), Id(k))), BinExpr(>, BinExpr(&&, Id(W), BinExpr(+, BinExpr(%, BinExpr(%, Id(Y), Id(n)), Id(gP)), FuncCall(V, []))), BinExpr(&&, BinExpr(-, UnExpr(-, Id(K)), Id(Gqt2D)), BinExpr(+, Id(I_), Id(w))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 778))

	def test_779(self):
		input = """R : function void ( ) inherit H { Z , W , H , GS , r , QGf6p , yOiaAM , pKdtLvHmD3xV  : string   ;  return - g     :: q   || E      ;   }    """
		expect = """Program([
	FuncDecl(R, VoidType, [], H, BlockStmt([VarDecl(Z, StringType), VarDecl(W, StringType), VarDecl(H, StringType), VarDecl(GS, StringType), VarDecl(r, StringType), VarDecl(QGf6p, StringType), VarDecl(yOiaAM, StringType), VarDecl(pKdtLvHmD3xV, StringType), ReturnStmt(BinExpr(::, UnExpr(-, Id(g)), BinExpr(||, Id(q), Id(E))))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 779))

	def test_780(self):
		input = """fU , Ex6aL , U , _ , Uj7 , Fzf  : auto  ;   """
		expect = """Program([
	VarDecl(fU, AutoType)
	VarDecl(Ex6aL, AutoType)
	VarDecl(U, AutoType)
	VarDecl(_, AutoType)
	VarDecl(Uj7, AutoType)
	VarDecl(Fzf, AutoType)
])"""
		self.assertTrue(TestAST.test(input, expect, 780))

	def test_781(self):
		input = """x : function auto  ( ) { }    """
		expect = """Program([
	FuncDecl(x, AutoType, [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 781))

	def test_782(self):
		input = """Pk7ew : function void ( ) { f  : boolean   = - bZ     :: t ( )       ;  }    Ln : function void ( ) { GdTAd  : array [ 0 , 6513 ] of boolean    = s   - e    > f   || nnbU8r     :: - G9D       ;  }    d : function void ( inherit R3G : auto   , out F : auto    ) inherit S { }    OYh , py , K  : auto  = ! C   || g408     * ! - R      >= - I      , - U   / g4    && - I      != Q    :: I   - lm   || ic    && e   - o      > ! GIH   || o     && ! ob   + axU        , ! M2p   + - N      == hzJ3V   + H    + a   || n     && Gyk ( )    * PH   + Gy       :: plg ( )    < XP ( )       ;   w : function float   ( TiE : auto   , G : integer    , out Z : integer    , P : string     ) { J6  : boolean   = - Vu       ;  }    """
		expect = """Program([
	FuncDecl(Pk7ew, VoidType, [], None, BlockStmt([VarDecl(f, BooleanType, BinExpr(::, UnExpr(-, Id(bZ)), FuncCall(t, [])))]))
	FuncDecl(Ln, VoidType, [], None, BlockStmt([VarDecl(GdTAd, ArrayType([0, 6513], BooleanType), BinExpr(::, BinExpr(>, BinExpr(-, Id(s), Id(e)), BinExpr(||, Id(f), Id(nnbU8r))), UnExpr(-, Id(G9D))))]))
	FuncDecl(d, VoidType, [InheritParam(R3G, AutoType), OutParam(F, AutoType)], S, BlockStmt([]))
	VarDecl(OYh, AutoType, BinExpr(>=, BinExpr(||, UnExpr(!, Id(C)), BinExpr(*, Id(g408), UnExpr(!, UnExpr(-, Id(R))))), UnExpr(-, Id(I))))
	VarDecl(py, AutoType, BinExpr(::, BinExpr(!=, BinExpr(&&, BinExpr(/, UnExpr(-, Id(U)), Id(g4)), UnExpr(-, Id(I))), Id(Q)), BinExpr(>, BinExpr(&&, BinExpr(||, BinExpr(-, Id(I), Id(lm)), Id(ic)), BinExpr(-, Id(e), Id(o))), BinExpr(&&, BinExpr(||, UnExpr(!, Id(GIH)), Id(o)), BinExpr(+, UnExpr(!, Id(ob)), Id(axU))))))
	VarDecl(K, AutoType, BinExpr(::, BinExpr(==, BinExpr(+, UnExpr(!, Id(M2p)), UnExpr(-, Id(N))), BinExpr(&&, BinExpr(||, BinExpr(+, BinExpr(+, Id(hzJ3V), Id(H)), Id(a)), Id(n)), BinExpr(+, BinExpr(*, FuncCall(Gyk, []), Id(PH)), Id(Gy)))), BinExpr(<, FuncCall(plg, []), FuncCall(XP, []))))
	FuncDecl(w, FloatType, [Param(TiE, AutoType), Param(G, IntegerType), OutParam(Z, IntegerType), Param(P, StringType)], None, BlockStmt([VarDecl(J6, BooleanType, UnExpr(-, Id(Vu)))]))
])"""
		self.assertTrue(TestAST.test(input, expect, 782))

	def test_783(self):
		input = """f0zah1 : function void ( ) inherit mDB0S { { ufDPz  : array [ 98_54_3 ] of boolean    ;  }   for ( XTl  = ! o     :: tni   + d    == - i      , e   && UuzX    == qBOfCp   || J      , - e     :: ok   % s      ) return ;     }    Fx : function string   ( ) inherit F0a { while ( fz   % cO      ) break ;     }    Y : function void ( inherit eb : array [ 4 , 0 ] of float      ) inherit SB4v { }    """
		expect = """Program([
	FuncDecl(f0zah1, VoidType, [], mDB0S, BlockStmt([BlockStmt([VarDecl(ufDPz, ArrayType([98543], BooleanType))]), ForStmt(AssignStmt(Id(XTl), BinExpr(::, UnExpr(!, Id(o)), BinExpr(==, BinExpr(+, Id(tni), Id(d)), UnExpr(-, Id(i))))), BinExpr(==, BinExpr(&&, Id(e), Id(UuzX)), BinExpr(||, Id(qBOfCp), Id(J))), BinExpr(::, UnExpr(-, Id(e)), BinExpr(%, Id(ok), Id(s))), ReturnStmt())]))
	FuncDecl(Fx, StringType, [], F0a, BlockStmt([WhileStmt(BinExpr(%, Id(fz), Id(cO)), BreakStmt())]))
	FuncDecl(Y, VoidType, [InheritParam(eb, ArrayType([4, 0], FloatType))], SB4v, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 783))

	def test_784(self):
		input = """r : function void ( inherit out O : array [ 4 ] of boolean      ) { }    """
		expect = """Program([
	FuncDecl(r, VoidType, [InheritOutParam(O, ArrayType([4], BooleanType))], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 784))

	def test_785(self):
		input = """o  : float   = ! b   && W     - "\\\'"     == s   % Pt    % - Q     / - M    + B   || e       :: EvuT6Vr   && F   * fK   && V         ;   """
		expect = """Program([
	VarDecl(o, FloatType, BinExpr(::, BinExpr(==, BinExpr(&&, UnExpr(!, Id(b)), BinExpr(-, Id(W), StringLit(\\'))), BinExpr(||, BinExpr(+, BinExpr(/, BinExpr(%, BinExpr(%, Id(s), Id(Pt)), UnExpr(-, Id(Q))), UnExpr(-, Id(M))), Id(B)), Id(e))), BinExpr(&&, BinExpr(&&, Id(EvuT6Vr), BinExpr(*, Id(F), Id(fK))), Id(V))))
])"""
		self.assertTrue(TestAST.test(input, expect, 785))

	def test_786(self):
		input = """h : function void ( inherit g : float     ) inherit Tbf { lp  : auto  = j   % D    >= ! ZrM     :: N6   + n    < S4   / g6FYbb3       ;  { }   }    """
		expect = """Program([
	FuncDecl(h, VoidType, [InheritParam(g, FloatType)], Tbf, BlockStmt([VarDecl(lp, AutoType, BinExpr(::, BinExpr(>=, BinExpr(%, Id(j), Id(D)), UnExpr(!, Id(ZrM))), BinExpr(<, BinExpr(+, Id(N6), Id(n)), BinExpr(/, Id(S4), Id(g6FYbb3))))), BlockStmt([])]))
])"""
		self.assertTrue(TestAST.test(input, expect, 786))

	def test_787(self):
		input = """O , tg  : auto  = ! f   % brY    - KSB   - M97u       :: { }     - Bn   % ktsF   * e      > F     , ! Ak   - myNi    || X_   && e      >= - f   && uk    / - t       :: ! - c ( )      <= nOTj ( )    - - IRyA     || - N        ;   """
		expect = """Program([
	VarDecl(O, AutoType, BinExpr(::, BinExpr(-, BinExpr(-, BinExpr(%, UnExpr(!, Id(f)), Id(brY)), Id(KSB)), Id(M97u)), BinExpr(>, BinExpr(-, ArrayLit([]), BinExpr(*, BinExpr(%, Id(Bn), Id(ktsF)), Id(e))), Id(F))))
	VarDecl(tg, AutoType, BinExpr(::, BinExpr(>=, BinExpr(&&, BinExpr(||, BinExpr(-, UnExpr(!, Id(Ak)), Id(myNi)), Id(X_)), Id(e)), BinExpr(&&, UnExpr(-, Id(f)), BinExpr(/, Id(uk), UnExpr(-, Id(t))))), BinExpr(<=, UnExpr(!, UnExpr(-, FuncCall(c, []))), BinExpr(||, BinExpr(-, FuncCall(nOTj, []), UnExpr(-, Id(IRyA))), UnExpr(-, Id(N))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 787))

	def test_788(self):
		input = """P : function array [ 7_71_8_67 ] of boolean    ( ) { }    """
		expect = """Program([
	FuncDecl(P, ArrayType([771867], BooleanType), [], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 788))

	def test_789(self):
		input = """L8  : auto  = ! eL   / k   && e9      == hNg ( )     :: ! ! ufl        ;   """
		expect = """Program([
	VarDecl(L8, AutoType, BinExpr(::, BinExpr(==, BinExpr(&&, BinExpr(/, UnExpr(!, Id(eL)), Id(k)), Id(e9)), FuncCall(hNg, [])), UnExpr(!, UnExpr(!, Id(ufl)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 789))

	def test_790(self):
		input = """Dc  : array [ 5 ] of string    = C   - pTd    || - T     * - xSB   + Am         ;   o , q , a  : float   = xd ( )     :: NgXY     , BevuX ( )     :: ! RljGcK   + Fsl     + ! ! c      <= N   && Bg    + - G     * - th       , - ! e     - a   - f    && b ( )         ;   mopa , D , boS  : boolean   = ""    + frm4Fc   - P    + SVE3   % J       :: ! ! kTsyN     / EydJX   / Jh    && - I      <= - ! w    || L   || xBeGVl        , Pd ( )    && ! y2r   - c      > ! NA   * Vn     + SIa   || Vt    || 8       :: - R   % Z6cH3Q    - JT   || ffF__      > - pd   - g     || - rh    + fA   && z        , - Q   + C     * l7     :: ! G ( )        ;   t : function void ( inherit out w : string     ) { }    ExssD : function array [ 0 , 5_656 ] of boolean    ( inherit Uyn : auto   , out JJh : auto    ) inherit t { mhL  : array [ 4_5 , 4_68_2 ] of integer    ;  f , A , y  : integer   = q ( )     :: ""    <= ! tB      , i   || fKAOR    >= ! GKXM     :: h   || VX      , k   - gT       ;  }    VJ , C  : array [ 0 ] of string    = iiQg   % - yBG   / BLbNm      <= - ! Z   && rTh        , jdo8 ( )    >= KIeoMd   + pps    % ! DF     || ! eYv    || C   * r         ;   """
		expect = """Program([
	VarDecl(Dc, ArrayType([5], StringType), BinExpr(||, BinExpr(-, Id(C), Id(pTd)), BinExpr(+, BinExpr(*, UnExpr(-, Id(T)), UnExpr(-, Id(xSB))), Id(Am))))
	VarDecl(o, FloatType, BinExpr(::, FuncCall(xd, []), Id(NgXY)))
	VarDecl(q, FloatType, BinExpr(::, FuncCall(BevuX, []), BinExpr(<=, BinExpr(+, BinExpr(+, UnExpr(!, Id(RljGcK)), Id(Fsl)), UnExpr(!, UnExpr(!, Id(c)))), BinExpr(&&, Id(N), BinExpr(+, Id(Bg), BinExpr(*, UnExpr(-, Id(G)), UnExpr(-, Id(th))))))))
	VarDecl(a, FloatType, BinExpr(&&, BinExpr(-, BinExpr(-, UnExpr(-, UnExpr(!, Id(e))), Id(a)), Id(f)), FuncCall(b, [])))
	VarDecl(mopa, BooleanType, BinExpr(::, BinExpr(+, BinExpr(-, BinExpr(+, StringLit(), Id(frm4Fc)), Id(P)), BinExpr(%, Id(SVE3), Id(J))), BinExpr(<=, BinExpr(&&, BinExpr(/, BinExpr(/, UnExpr(!, UnExpr(!, Id(kTsyN))), Id(EydJX)), Id(Jh)), UnExpr(-, Id(I))), BinExpr(||, BinExpr(||, UnExpr(-, UnExpr(!, Id(w))), Id(L)), Id(xBeGVl)))))
	VarDecl(D, BooleanType, BinExpr(::, BinExpr(>, BinExpr(&&, FuncCall(Pd, []), BinExpr(-, UnExpr(!, Id(y2r)), Id(c))), BinExpr(||, BinExpr(||, BinExpr(+, BinExpr(*, UnExpr(!, Id(NA)), Id(Vn)), Id(SIa)), Id(Vt)), IntegerLit(8))), BinExpr(>, BinExpr(||, BinExpr(-, BinExpr(%, UnExpr(-, Id(R)), Id(Z6cH3Q)), Id(JT)), Id(ffF__)), BinExpr(&&, BinExpr(||, BinExpr(-, UnExpr(-, Id(pd)), Id(g)), BinExpr(+, UnExpr(-, Id(rh)), Id(fA))), Id(z)))))
	VarDecl(boS, BooleanType, BinExpr(::, BinExpr(+, UnExpr(-, Id(Q)), BinExpr(*, Id(C), Id(l7))), UnExpr(!, FuncCall(G, []))))
	FuncDecl(t, VoidType, [InheritOutParam(w, StringType)], None, BlockStmt([]))
	FuncDecl(ExssD, ArrayType([0, 5656], BooleanType), [InheritParam(Uyn, AutoType), OutParam(JJh, AutoType)], t, BlockStmt([VarDecl(mhL, ArrayType([45, 4682], IntegerType)), VarDecl(f, IntegerType, BinExpr(::, FuncCall(q, []), BinExpr(<=, StringLit(), UnExpr(!, Id(tB))))), VarDecl(A, IntegerType, BinExpr(::, BinExpr(>=, BinExpr(||, Id(i), Id(fKAOR)), UnExpr(!, Id(GKXM))), BinExpr(||, Id(h), Id(VX)))), VarDecl(y, IntegerType, BinExpr(-, Id(k), Id(gT)))]))
	VarDecl(VJ, ArrayType([0], StringType), BinExpr(<=, BinExpr(/, BinExpr(%, Id(iiQg), UnExpr(-, Id(yBG))), Id(BLbNm)), BinExpr(&&, UnExpr(-, UnExpr(!, Id(Z))), Id(rTh))))
	VarDecl(C, ArrayType([0], StringType), BinExpr(>=, FuncCall(jdo8, []), BinExpr(||, BinExpr(||, BinExpr(+, Id(KIeoMd), BinExpr(%, Id(pps), UnExpr(!, Id(DF)))), UnExpr(!, Id(eYv))), BinExpr(*, Id(C), Id(r)))))
])"""
		self.assertTrue(TestAST.test(input, expect, 790))

	def test_791(self):
		input = """mP  : array [ 5 , 0 ] of float    ;   oA : function void ( inherit P1d : auto   , out T : integer    , inherit out U : integer     ) { }    m , iN , i  : auto  = - a    - u   && JA     && - v   || C        , - ! c59    + R     >= A0sns     , ""    - - SgL    - Ni   - t      < - 985      :: ! kEzEn   + T     && 5    * SIF   % Dv      > ya   || k    % LK   / q     && - ! X         ;   """
		expect = """Program([
	VarDecl(mP, ArrayType([5, 0], FloatType))
	FuncDecl(oA, VoidType, [InheritParam(P1d, AutoType), OutParam(T, IntegerType), InheritOutParam(U, IntegerType)], None, BlockStmt([]))
	VarDecl(m, AutoType, BinExpr(||, BinExpr(&&, BinExpr(&&, BinExpr(-, UnExpr(-, Id(a)), Id(u)), Id(JA)), UnExpr(-, Id(v))), Id(C)))
	VarDecl(iN, AutoType, BinExpr(>=, BinExpr(+, UnExpr(-, UnExpr(!, Id(c59))), Id(R)), Id(A0sns)))
	VarDecl(i, AutoType, BinExpr(::, BinExpr(<, BinExpr(-, BinExpr(-, BinExpr(-, StringLit(), UnExpr(-, Id(SgL))), Id(Ni)), Id(t)), UnExpr(-, IntegerLit(985))), BinExpr(>, BinExpr(&&, BinExpr(+, UnExpr(!, Id(kEzEn)), Id(T)), BinExpr(%, BinExpr(*, IntegerLit(5), Id(SIF)), Id(Dv))), BinExpr(&&, BinExpr(||, Id(ya), BinExpr(/, BinExpr(%, Id(k), Id(LK)), Id(q))), UnExpr(-, UnExpr(!, Id(X)))))))
])"""
		self.assertTrue(TestAST.test(input, expect, 791))

	def test_792(self):
		input = """s : function void ( inherit out Ls : auto    ) { }    """
		expect = """Program([
	FuncDecl(s, VoidType, [InheritOutParam(Ls, AutoType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 792))

	def test_793(self):
		input = """O5PnoE  : float   = Y2o   && L    || YEd   % K     - ! K7    * O   || C      >= { }     + CA0n ( )        ;   """
		expect = """Program([
	VarDecl(O5PnoE, FloatType, BinExpr(>=, BinExpr(||, BinExpr(||, BinExpr(&&, Id(Y2o), Id(L)), BinExpr(-, BinExpr(%, Id(YEd), Id(K)), BinExpr(*, UnExpr(!, Id(K7)), Id(O)))), Id(C)), BinExpr(+, ArrayLit([]), FuncCall(CA0n, []))))
])"""
		self.assertTrue(TestAST.test(input, expect, 793))

	def test_794(self):
		input = """H : function boolean   ( ) { break ;   }    j3Gu  : auto  ;   t  : array [ 7_75 , 72_6644116_6_0_47_05_0 , 2_2_50_863 , 171 ] of string    = ! D    != { }        ;   """
		expect = """Program([
	FuncDecl(H, BooleanType, [], None, BlockStmt([BreakStmt()]))
	VarDecl(j3Gu, AutoType)
	VarDecl(t, ArrayType([775, 7266441166047050, 2250863, 171], StringType), BinExpr(!=, UnExpr(!, Id(D)), ArrayLit([])))
])"""
		self.assertTrue(TestAST.test(input, expect, 794))

	def test_795(self):
		input = """b : function auto  ( inherit C : auto   , inherit out c : array [ 94_77_195_22 , 1 ] of float     , g : array [ 0 , 9957 ] of float     , lnR : array [ 47_0 ] of integer      ) inherit r { LC4z  : array [ 25 , 6 ] of integer    = gD   - V       ;  i  : auto  = - Y    >= J   / p       ;  continue ;   }    Up : function void ( ) { }    f : function void ( ) inherit Rr8semSD_ { V  : array [ 7 ] of boolean    = NzU   < M5A   - Q5oIfos       ;  H , lU , If  : float   = - OQSx    >= ! l      , - Fut      , Z   % uTja       ;  }    a : function void ( inherit r : integer    , out a : float     ) { }    """
		expect = """Program([
	FuncDecl(b, AutoType, [InheritParam(C, AutoType), InheritOutParam(c, ArrayType([947719522, 1], FloatType)), Param(g, ArrayType([0, 9957], FloatType)), Param(lnR, ArrayType([470], IntegerType))], r, BlockStmt([VarDecl(LC4z, ArrayType([25, 6], IntegerType), BinExpr(-, Id(gD), Id(V))), VarDecl(i, AutoType, BinExpr(>=, UnExpr(-, Id(Y)), BinExpr(/, Id(J), Id(p)))), ContinueStmt()]))
	FuncDecl(Up, VoidType, [], None, BlockStmt([]))
	FuncDecl(f, VoidType, [], Rr8semSD_, BlockStmt([VarDecl(V, ArrayType([7], BooleanType), BinExpr(<, Id(NzU), BinExpr(-, Id(M5A), Id(Q5oIfos)))), VarDecl(H, FloatType, BinExpr(>=, UnExpr(-, Id(OQSx)), UnExpr(!, Id(l)))), VarDecl(lU, FloatType, UnExpr(-, Id(Fut))), VarDecl(If, FloatType, BinExpr(%, Id(Z), Id(uTja)))]))
	FuncDecl(a, VoidType, [InheritParam(r, IntegerType), OutParam(a, FloatType)], None, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 795))

	def test_796(self):
		input = """tb  : auto  = ! - xi    || - n         ;   """
		expect = """Program([
	VarDecl(tb, AutoType, BinExpr(||, UnExpr(!, UnExpr(-, Id(xi))), UnExpr(-, Id(n))))
])"""
		self.assertTrue(TestAST.test(input, expect, 796))

	def test_797(self):
		input = """bK  : array [ 8946_2 ] of integer    = - ""    / - mMi      >= 0.38E959109     :: ! - d     * ! e   * h      != - Sv ( )     % Se   || GeR    || ! VRfU         ;   _ : function void ( out O : array [ 5_9 ] of boolean      ) inherit ce { }    k : function boolean   ( inherit out c5w : array [ 49_0 ] of float      ) { }    j : function void ( inherit H : auto    ) { }    g : function void ( inherit jWX : boolean     ) inherit Mw { }    """
		expect = """Program([
	VarDecl(bK, ArrayType([89462], IntegerType), BinExpr(::, BinExpr(>=, BinExpr(/, UnExpr(-, StringLit()), UnExpr(-, Id(mMi))), FloatLit(inf)), BinExpr(!=, BinExpr(*, BinExpr(*, UnExpr(!, UnExpr(-, Id(d))), UnExpr(!, Id(e))), Id(h)), BinExpr(||, BinExpr(||, BinExpr(%, UnExpr(-, FuncCall(Sv, [])), Id(Se)), Id(GeR)), UnExpr(!, Id(VRfU))))))
	FuncDecl(_, VoidType, [OutParam(O, ArrayType([59], BooleanType))], ce, BlockStmt([]))
	FuncDecl(k, BooleanType, [InheritOutParam(c5w, ArrayType([490], FloatType))], None, BlockStmt([]))
	FuncDecl(j, VoidType, [InheritParam(H, AutoType)], None, BlockStmt([]))
	FuncDecl(g, VoidType, [InheritParam(jWX, BooleanType)], Mw, BlockStmt([]))
])"""
		self.assertTrue(TestAST.test(input, expect, 797))

	def test_798(self):
		input = """r : function array [ 9_97_554 ] of boolean    ( ) { d  : array [ 4 , 0 , 40 , 0 , 167 , 2 , 0 , 3_1_7 , 9 ] of string    = B_U   || krmz6    <= - H6t       ;  break ;   return ;   }    """
		expect = """Program([
	FuncDecl(r, ArrayType([997554], BooleanType), [], None, BlockStmt([VarDecl(d, ArrayType([4, 0, 40, 0, 167, 2, 0, 317, 9], StringType), BinExpr(<=, BinExpr(||, Id(B_U), Id(krmz6)), UnExpr(-, Id(H6t)))), BreakStmt(), ReturnStmt()]))
])"""
		self.assertTrue(TestAST.test(input, expect, 798))

	def test_799(self):
		input = """M : function string   ( jOQ : array [ 0 ] of boolean      ) { _V  : auto  = 9    > aVhx   * cO     :: d   / yZWx    != rawV5   && G1V7O       ;  l  : auto  = ! u       ;  if ( XD   * E     :: ""      ) return ;   else return ;     break ;   dhF9QKlp , Uaa  : array [ 3575_701 , 0 ] of string    ;  c1 , wt  : auto  = xz28   == ! v     :: aah   * q    > - j9      , ! GWpJ    <= - j     :: ! yr1f    <= - UmZ       ;  }    c , MD  : float   ;   """
		expect = """Program([
	FuncDecl(M, StringType, [Param(jOQ, ArrayType([0], BooleanType))], None, BlockStmt([VarDecl(_V, AutoType, BinExpr(::, BinExpr(>, IntegerLit(9), BinExpr(*, Id(aVhx), Id(cO))), BinExpr(!=, BinExpr(/, Id(d), Id(yZWx)), BinExpr(&&, Id(rawV5), Id(G1V7O))))), VarDecl(l, AutoType, UnExpr(!, Id(u))), IfStmt(BinExpr(::, BinExpr(*, Id(XD), Id(E)), StringLit()), ReturnStmt(), ReturnStmt()), BreakStmt(), VarDecl(dhF9QKlp, ArrayType([3575701, 0], StringType)), VarDecl(Uaa, ArrayType([3575701, 0], StringType)), VarDecl(c1, AutoType, BinExpr(::, BinExpr(==, Id(xz28), UnExpr(!, Id(v))), BinExpr(>, BinExpr(*, Id(aah), Id(q)), UnExpr(-, Id(j9))))), VarDecl(wt, AutoType, BinExpr(::, BinExpr(<=, UnExpr(!, Id(GWpJ)), UnExpr(-, Id(j))), BinExpr(<=, UnExpr(!, Id(yr1f)), UnExpr(-, Id(UmZ)))))]))
	VarDecl(c, FloatType)
	VarDecl(MD, FloatType)
])"""
		self.assertTrue(TestAST.test(input, expect, 799))

	def test_800(self):
		input = """cH : function auto  ( ) inherit cLo6 { }    llP  : integer   ;   """
		expect = """Program([
	FuncDecl(cH, AutoType, [], cLo6, BlockStmt([]))
	VarDecl(llP, IntegerType)
])"""
		self.assertTrue(TestAST.test(input, expect, 800))

